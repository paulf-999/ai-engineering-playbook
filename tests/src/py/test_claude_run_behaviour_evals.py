"""Tests for the behaviour evals runner's scenario selection, scratch repo setup and transcript, without a live run."""

import importlib
import json
import sys

from _paths import REPO_ROOT

# The runner imports the shared eval helpers by name, as it does when run as a script
sys.path.insert(0, str(REPO_ROOT / "src" / "py"))
runner = importlib.import_module("claude_run_behaviour_evals")


def test_load_scenarios_keeps_only_behaviour_ones(tmp_path):
    """Only scenarios with behaviour: true are run."""
    evals = {"evals": [{"name": "tagged", "behaviour": True}, {"name": "untagged"}]}
    (tmp_path / "evals.yaml").write_text(json.dumps(evals))
    assert [s["name"] for s in runner.load_scenarios(tmp_path)] == ["tagged"]


def test_session_id_of_reads_the_init_event():
    """A confirm_reply resumes the session named by the first event that carries an ID."""
    events = [{"type": "system", "subtype": "init", "session_id": "abc"}, {"type": "assistant"}]
    assert runner.session_id_of(events) == "abc"


def test_load_scenarios_records_the_file_agent(tmp_path):
    """A scenario from an agent's evals.yaml carries that agent's name, so its run: block goes to the agent."""
    evals = {"agent_name": "code-reviewer", "evals": [{"name": "tagged", "behaviour": True}]}
    (tmp_path / "evals.yaml").write_text(json.dumps(evals))
    assert runner.load_scenarios(tmp_path)[0]["agent"] == "code-reviewer"


def test_patterns_match_every_line_of_claude_text():
    """Patterns see all of Claude's multi-line text, and a must_not_match pattern fails when it matches."""
    reply = {"type": "assistant", "message": {"content": [{"type": "text", "text": "Verdict\n\n## Fix\nrange(n)"}]}}
    text = runner.claude_text([("Review this diff", [reply])])
    results = runner.pattern_results([r"(?s)Verdict.*## Fix", "absent"], text)
    assert [result["pass"] for result in results] == [True, False]
    results = runner.pattern_results(["range", "absent"], text, must_match=False)
    assert [result["pass"] for result in results] == [False, True]
