"""Tests for the plan review hook, which blocks a long plan until a cold reviewer scores it 10/10, for two rounds."""

import json
import os
import subprocess

import pytest
from _paths import REPO_ROOT
from test_hook_enforcement_plan_sections import MIN_PLAN_LINES, exit_plan_input, steps

HOOK = REPO_ROOT / "src" / "claude" / "hooks" / "ai_sdlc_workflow" / "hook_enforcement_plan_review.sh"
# exit code 2 is how a PreToolUse hook tells Claude Code to block the call
BLOCKED = 2
# a plan long enough to review, with the Intent and Spec headings the sections hook requires
LONG_PLAN = "## 1. Intent\n\nWhy.\n\n## 2. Spec\n\nWhat.\n\n## 3. Plan\n\n" + steps(MIN_PLAN_LINES)
ALL_TENS = {"intent": 10, "spec": 10, "plan": 10, "writing_style": 10, "decisions": 10}
# a verdict with no decisions score
NO_DECISIONS = {"scores": {theme: 10 for theme in ALL_TENS if theme != "decisions"}, "findings": []}
# a stub claude that saves its prompt, then prints the reply file and exits with STUB_EXIT
STUB_CLAUDE = """#!/bin/bash
cat > "${STUB_DIR}/prompt.txt"
cat "${STUB_DIR}/reply.json" 2> /dev/null
exit "${STUB_EXIT:-0}"
"""


def _make_stub(tmp_path):
    """Put a stub claude first on PATH, with a memory folder beside the transcript, and return a hook runner."""
    (tmp_path / "bin").mkdir()
    (tmp_path / "memory").mkdir()
    claude = tmp_path / "bin" / "claude"
    claude.write_text(STUB_CLAUDE)
    claude.chmod(0o755)

    def run(plan, verdict=None, raw=None, stub_exit=0, session="s1"):
        """Run the hook on plan, with the stub replying verdict as claude -p JSON, or raw text if given."""
        reply = raw if raw is not None else json.dumps({"result": json.dumps(verdict), "is_error": False})
        (tmp_path / "reply.json").write_text(reply)
        transcript = str(tmp_path / f"{session}.jsonl")
        payload = json.loads(exit_plan_input(plan)) | {"session_id": session, "transcript_path": transcript}
        env = os.environ | {
            "PATH": f"{tmp_path / 'bin'}:{os.environ['PATH']}",
            "STUB_DIR": str(tmp_path),
            "STUB_EXIT": str(stub_exit),
            "TMPDIR": str(tmp_path),
        }
        return subprocess.run(
            ["bash", str(HOOK)],
            input=json.dumps(payload),
            env=env,
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )

    run.prompt = tmp_path / "prompt.txt"
    run.log = tmp_path / "memory" / "plan_reviews.log"
    return run


def context(result):
    """Return the additionalContext the hook printed for Claude on stdout."""
    return json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]


@pytest.mark.parametrize(
    "plan",
    ["## Intent\n\nWhy.\n\n## Spec\n\nWhat.\n", "# Plan\n\nNo sections here.\n" + steps(MIN_PLAN_LINES)],
)
def test_a_short_plan_or_one_without_sections_is_not_reviewed(tmp_path, plan):
    """A plan under 15 lines, or one the sections hook already blocks, exits 0 without calling claude."""
    stub = _make_stub(tmp_path)
    result = stub(plan, {"scores": ALL_TENS, "findings": []})
    assert result.returncode == 0 and result.stdout == "", f"the plan should pass silently:\n{result.stderr}"
    assert not stub.prompt.exists(), "claude should not be called"
    assert not stub.log.exists(), "a plan that isn't reviewed should not be logged"


def test_a_plan_scored_10_on_every_theme_is_allowed(tmp_path):
    """An all-10 verdict exits 0 silently, and the reviewer saw the plan and the writing style rule."""
    stub = _make_stub(tmp_path)
    result = stub(LONG_PLAN, {"scores": ALL_TENS, "findings": []})
    assert result.returncode == 0 and result.stdout == "", f"the plan should be allowed:\n{result.stderr}"
    prompt = stub.prompt.read_text()
    assert LONG_PLAN.strip() in prompt, "the reviewer should see the plan"
    assert "British spelling" in prompt, "the reviewer should see the writing style rule"


def test_a_plan_scored_under_10_is_blocked_with_the_findings(tmp_path):
    """Any theme under 10 exits 2, with the scores and findings on stderr."""
    stub = _make_stub(tmp_path)
    verdict = {"scores": ALL_TENS | {"spec": 8}, "findings": ["Spec has no Out of scope bullet."]}
    result = stub(LONG_PLAN, verdict)
    assert result.returncode == BLOCKED, f"the plan should be blocked:\n{result.stderr}"
    assert "spec 8/10" in result.stderr, f"the reason should give the scores:\n{result.stderr}"
    assert "Spec has no Out of scope bullet." in result.stderr, "the reason should list the findings"


def test_a_decisions_score_under_10_is_blocked_and_sent_to_the_user(tmp_path):
    """A decisions score under 10 exits 2, and tells Claude to ask the user about those findings."""
    stub = _make_stub(tmp_path)
    verdict = {"scores": ALL_TENS | {"decisions": 6}, "findings": ["decisions: the database choice isn't agreed."]}
    result = stub(LONG_PLAN, verdict)
    assert result.returncode == BLOCKED, f"the plan should be blocked:\n{result.stderr}"
    assert "decisions 6/10" in result.stderr, f"the reason should give the score:\n{result.stderr}"
    assert "ask the user" in result.stderr.lower(), f"the reason should send Claude to the user:\n{result.stderr}"


def test_findings_nested_in_the_scores_are_read_as_findings(tmp_path):
    """A reply with findings inside scores passes when every theme is 10, and otherwise lists them as findings."""
    stub = _make_stub(tmp_path)
    result = stub(LONG_PLAN, {"scores": ALL_TENS | {"findings": []}})
    assert result.returncode == 0 and result.stdout == "", f"an all-10 plan should be allowed:\n{result.stderr}"
    result = stub(LONG_PLAN, {"scores": ALL_TENS | {"spec": 8, "findings": ["spec: no Out of scope bullet."]}})
    assert result.returncode == BLOCKED, f"the plan should be blocked:\n{result.stderr}"
    assert "\n- spec: no Out of scope bullet." in result.stderr, f"the findings should be listed:\n{result.stderr}"


def test_the_third_submission_passes_with_the_findings_for_the_user(tmp_path):
    """After two blocks in a session, the next plan exits 0 with the findings in additionalContext."""
    stub = _make_stub(tmp_path)
    verdict = {"scores": ALL_TENS | {"plan": 9}, "findings": ["Step 3 has no check."]}
    assert [stub(LONG_PLAN, verdict).returncode for _ in range(2)] == [BLOCKED, BLOCKED]
    result = stub(LONG_PLAN, verdict)
    assert result.returncode == 0, f"the third submission should pass:\n{result.stderr}"
    assert "Step 3 has no check." in context(result), "the findings should reach Claude"
    assert stub(LONG_PLAN, verdict, session="s2").returncode == BLOCKED, "another session gets its own rounds"


@pytest.mark.parametrize(
    ("raw", "stub_exit"),
    [
        ("", 1),
        ("not json", 0),
        (json.dumps({"result": "no verdict"}), 0),
        (json.dumps({"result": json.dumps(NO_DECISIONS)}), 0),
    ],
)
def test_a_failed_review_lets_the_plan_through_with_a_note(tmp_path, raw, stub_exit):
    """When claude fails or returns no verdict, the hook exits 0 and notes that the plan wasn't reviewed."""
    stub = _make_stub(tmp_path)
    result = stub(LONG_PLAN, raw=raw, stub_exit=stub_exit)
    assert result.returncode == 0, f"a failed review should not block:\n{result.stderr}"
    assert "wasn't reviewed" in context(result), "Claude should hear the review didn't run"


def test_each_review_outcome_is_logged_with_its_scores(tmp_path):
    """Each reviewed plan adds one line to plan_reviews.log in the memory folder, giving its outcome and scores."""
    stub = _make_stub(tmp_path)
    weak = {"scores": ALL_TENS | {"plan": 9}, "findings": ["Step 3 has no check."]}
    for verdict in (weak, weak, weak):
        stub(LONG_PLAN, verdict)
    stub(LONG_PLAN, {"scores": ALL_TENS, "findings": []}, session="s2")
    stub(LONG_PLAN, raw="not json", session="s3")
    lines = stub.log.read_text().splitlines()
    outcomes = [line.split(" outcome=")[1].split()[0] for line in lines]
    assert outcomes == ["blocked", "blocked", "capped", "passed", "unreviewed"], f"unexpected log:\n{lines}"
    assert "session=s1" in lines[0] and "plan=9" in lines[0], f"a line should give its session and scores:\n{lines[0]}"
