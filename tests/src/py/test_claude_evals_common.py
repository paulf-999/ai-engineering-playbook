"""Tests for the shared eval helpers: the config copy, scratch repos, transcripts, grading and projects/ cleanup."""

import importlib
import subprocess
import sys

import pytest
from _paths import REPO_ROOT

# The runners import the shared helpers by name, as they do when run as scripts
sys.path.insert(0, str(REPO_ROOT / "src" / "py"))
common = importlib.import_module("claude_evals_common")


def git_status(repo_dir):
    """Return the repo's short status lines."""
    return subprocess.run(["git", "status", "--short"], cwd=repo_dir, capture_output=True, text=True).stdout.split("\n")


def test_copy_components_flattens_grouped_skills(tmp_path):
    """Grouped skills install flat, and agents keep their folders."""
    source = tmp_path / "src"
    (source / "skills/_git_skills/git-create-pr").mkdir(parents=True)
    (source / "skills/_git_skills/git-create-pr/SKILL.md").write_text("skill")
    (source / "agents/core/code-reviewer").mkdir(parents=True)
    (source / "agents/core/code-reviewer/AGENT.md").write_text("agent")
    common.copy_components(source, tmp_path)
    assert (tmp_path / ".claude/skills/git-create-pr/SKILL.md").exists()
    assert (tmp_path / ".claude/agents/core/code-reviewer/AGENT.md").exists()


def test_build_repo_makes_the_described_state(tmp_path):
    """The template is committed, the branch is set, and each changed file is left uncommitted."""
    setup = {
        "current_branch": "feature/x",
        "changed_files": [".env"],
        "changed_file_count": 2,
        "pr_template_exists": True,
    }
    common.build_repo(tmp_path, setup)
    (tmp_path / ".claude").mkdir()
    (tmp_path / ".claude/skill.md").write_text("copied skill")
    assert (tmp_path / ".github/pull_request_template.md").exists()
    assert "feature/x" in common.repo_state(tmp_path)
    assert sorted(line for line in git_status(tmp_path) if line) == ["?? .env", "?? src/"]


def test_build_repo_without_template_or_changes_is_clean(tmp_path):
    """A setup with no template and no changes leaves a clean tree on main."""
    common.build_repo(tmp_path, {"pr_template_exists": False})
    assert not (tmp_path / ".github").exists()
    assert "branch: main\nstatus:\n(clean)" in common.repo_state(tmp_path)


def test_build_repo_rejects_unknown_setup(tmp_path):
    """A setup key the runner can't build fails the scenario instead of being guessed."""
    with pytest.raises(ValueError, match="unsupported setup: open_pr"):
        common.build_repo(tmp_path, {"open_pr": True})


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
    text = common.transcript([("/git-create-pr", events)])
    assert text.splitlines() == [
        "USER: /git-create-pr",
        "CLAUDE: Checking",
        'TOOL Bash: {"command": "gh"}',
        "REFUSED OR FAILED: denied",
    ]


def test_graded_results_pass_only_a_pass_verdict():
    """Only a pass verdict passes, and an unknown one says so in its reason."""
    results = [{"assertion": v, "reason": "why", "verdict": v} for v in ("pass", "fail", "unknown")]
    graded = common.graded_results(["pass", "fail", "unknown"], results)
    assert [result["pass"] for result in graded] == [True, False, False]
    assert [result["reason"] for result in graded] == ["why", "why", "unknown: why"]


def test_graded_results_rejects_missing_results():
    """A grader that skips an assertion stops the run instead of counting as a pass."""
    with pytest.raises(ValueError, match="0 results for 1 assertions"):
        common.graded_results(["The branch is main"], [])


def test_project_folder_only_matches_the_scratch_repo(tmp_path):
    """Only the projects/ folder named after the scratch repo is picked for deletion."""
    repo_dir = tmp_path / "trigger_evals_ab12"
    init = {
        "type": "system",
        "subtype": "init",
        "memory_paths": {"auto": "/cfg/projects/-tmp-trigger-evals-ab12/memory/"},
    }
    assert str(common.project_folder([init], repo_dir)) == "/cfg/projects/-tmp-trigger-evals-ab12"
    init["memory_paths"]["auto"] = "/cfg/projects/-Users-me-real-repo/memory/"
    assert common.project_folder([init], repo_dir) is None


def test_repo_changes_shows_commits_edits_and_new_files(tmp_path):
    """The diff covers a commit, an edit and a new file made since the base commit, and leaves out .claude/."""
    common.build_repo(tmp_path, {})
    base = common.git(tmp_path, "rev-parse", "HEAD").strip()
    (tmp_path / "committed.md").write_text("committed line\n")
    common.git(tmp_path, "add", "-A")
    common.git(tmp_path, "commit", "-q", "-m", "docs: add a file")
    (tmp_path / "README.md").write_text("edited line\n")
    (tmp_path / "new.md").write_text("new line\n")
    (tmp_path / ".claude").mkdir()
    (tmp_path / ".claude/rule.md").write_text("hidden rule\n")
    changes = common.repo_changes(tmp_path, base)
    assert all(f"+{name} line" in changes for name in ("committed", "edited", "new")), changes
    assert "hidden rule" not in changes


@pytest.mark.parametrize(("over", "cut"), [(0, False), (1, True)])
def test_repo_changes_cuts_only_diffs_over_the_cap(tmp_path, monkeypatch, over, cut):
    """A diff at the cap is whole, and one over it is cut and says so."""
    diff = "x" * (common.MAX_DIFF_CHARS + over)
    monkeypatch.setattr(common, "git", lambda repo_dir, *args: diff if args[0] == "diff" else "")
    changes = common.repo_changes(tmp_path, "base")
    assert changes == "x" * common.MAX_DIFF_CHARS + ("\n(cut: the rest of the diff isn't shown)" if cut else "")


@pytest.mark.parametrize(("options", "expected"), [({}, False), ({"permission_mode": "acceptEdits"}, True)])
def test_run_claude_sets_a_permission_mode_only_when_asked(tmp_path, monkeypatch, options, expected):
    """Other evals keep their command, and a runner that asks for a permission mode gets the flag."""
    commands = []

    def fake_run(command, **kwargs):
        commands.append(command)
        return subprocess.CompletedProcess(command, 0, stdout="")

    monkeypatch.setattr(common.subprocess, "run", fake_run)
    common.run_claude("hello", tmp_path, **options)
    assert ("--permission-mode" in commands[0]) is expected
    if expected:
        assert commands[0][commands[0].index("--permission-mode") + 1] == "acceptEdits"


def test_select_cases_runs_only_the_named_case():
    """CASE picks one case by name, an empty name keeps them all, and an unknown name stops the run."""
    cases = [{"name": "a"}, {"name": "b"}]
    assert common.select_cases(cases, "b") == [{"name": "b"}]
    assert common.select_cases(cases, "") == cases
    with pytest.raises(SystemExit, match="No eval case is named c"):
        common.select_cases(cases, "c")
