"""Tests for the behaviour evals runner's scenario selection, scratch repo setup and transcript, without a live run."""

import importlib
import json
import subprocess
import sys

import pytest
from _paths import REPO_ROOT

# The runner imports its sibling trigger runner by name, as it does when run as a script
sys.path.insert(0, str(REPO_ROOT / "src" / "py"))
runner = importlib.import_module("claude_run_behaviour_evals")


def git_status(repo_dir):
    """Return the repo's short status lines."""
    return subprocess.run(["git", "status", "--short"], cwd=repo_dir, capture_output=True, text=True).stdout.split("\n")


def test_load_scenarios_keeps_only_behaviour_ones(tmp_path):
    """Only scenarios with behaviour: true are run."""
    evals = {"evals": [{"name": "tagged", "behaviour": True}, {"name": "untagged"}]}
    (tmp_path / "evals.yaml").write_text(json.dumps(evals))
    assert [s["name"] for s in runner.load_scenarios(tmp_path)] == ["tagged"]


def test_build_repo_makes_the_described_state(tmp_path):
    """The template is committed, the branch is set, and each changed file is left uncommitted."""
    setup = {
        "current_branch": "feature/x",
        "changed_files": [".env"],
        "changed_file_count": 2,
        "pr_template_exists": True,
    }
    runner.build_repo(tmp_path, setup)
    (tmp_path / ".claude").mkdir()
    (tmp_path / ".claude/skill.md").write_text("copied skill")
    assert (tmp_path / ".github/pull_request_template.md").exists()
    assert "feature/x" in runner.repo_state(tmp_path)
    assert sorted(line for line in git_status(tmp_path) if line) == ["?? .env", "?? src/"]


def test_build_repo_without_template_or_changes_is_clean(tmp_path):
    """A setup with no template and no changes leaves a clean tree on main."""
    runner.build_repo(tmp_path, {"pr_template_exists": False})
    assert not (tmp_path / ".github").exists()
    assert "branch: main\nstatus:\n(clean)" in runner.repo_state(tmp_path)


def test_build_repo_rejects_unknown_setup(tmp_path):
    """A setup key the runner can't build fails the scenario instead of being guessed."""
    with pytest.raises(ValueError, match="unsupported setup: open_pr"):
        runner.build_repo(tmp_path, {"open_pr": True})


def test_transcript_shows_text_tools_and_refusals():
    """The grader sees each prompt, Claude's text, its tool calls and which results were refused."""
    events = [
        {"type": "system", "subtype": "init", "session_id": "abc"},
        {"type": "assistant", "message": {"content": [{"type": "text", "text": "Checking"}]}},
        {
            "type": "assistant",
            "message": {"content": [{"type": "tool_use", "name": "Bash", "input": {"command": "gh"}}]},
        },
        {"type": "user", "message": {"content": [{"type": "tool_result", "is_error": True, "content": "denied"}]}},
    ]
    text = runner.transcript([("/git-create-pr", events)])
    assert text.splitlines() == [
        "USER: /git-create-pr",
        "CLAUDE: Checking",
        'TOOL Bash: {"command": "gh"}',
        "REFUSED OR FAILED: denied",
    ]
    assert runner.session_id_of(events) == "abc"


def test_load_scenarios_records_the_file_agent(tmp_path):
    """A scenario from an agent's evals.yaml carries that agent's name, so its run: block goes to the agent."""
    evals = {"agent_name": "code-reviewer", "evals": [{"name": "tagged", "behaviour": True}]}
    (tmp_path / "evals.yaml").write_text(json.dumps(evals))
    assert runner.load_scenarios(tmp_path)[0]["agent"] == "code-reviewer"


def test_patterns_match_every_line_of_claude_text():
    """must_match patterns see all of Claude's multi-line text, not just each block's first line."""
    reply = {"type": "assistant", "message": {"content": [{"type": "text", "text": "Verdict\n\n## Fix\nrange(n)"}]}}
    text = runner.claude_text([("Review this diff", [reply])])
    results = runner.pattern_results([r"(?s)Verdict.*## Fix", "absent"], text)
    assert [result["pass"] for result in results] == [True, False]
