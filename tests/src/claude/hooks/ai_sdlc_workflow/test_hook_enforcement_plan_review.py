"""Tests for the plan review hook, which blocks a long plan until a cold reviewer scores it 10/10, for two rounds."""

import json
import os
import shutil
import subprocess

import pytest
from _paths import REPO_ROOT
from test_hook_enforcement_plan_sections import MIN_PLAN_LINES, exit_plan_input, steps

HOOK = REPO_ROOT / "src" / "claude" / "hooks" / "ai_sdlc_workflow" / "hook_enforcement_plan_review.sh"
RULES = REPO_ROOT / "src" / "claude" / "rules"
WORKFLOW_RULE = RULES / "always_on" / "01_standards" / "ai_sdlc_workflow.md"
SAVING_RULE = RULES / "on_demand" / "02_preferences" / "claude_saved_plans.md"
INTENT_SECTIONS = (
    "Problem",
    "Proposed outcome",
    "Success",
    "Affected users and systems",
    "Constraints",
    "Open questions",
)
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
# a stub perl that saves the seconds the hook gives the reviewer, then runs the real perl
STUB_PERL = """#!/bin/bash
echo "$3" > "${STUB_DIR}/limit.txt"
exec "${REAL_PERL}" "$@"
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
            "REAL_PERL": shutil.which("perl"),
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
            timeout=60,
        )

    run.prompt = tmp_path / "prompt.txt"
    run.log = tmp_path / "memory" / "plan_reviews.log"
    return run


def context(result):
    """Return the additionalContext the hook printed for Claude on stdout."""
    return json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]


def user_message(result):
    """Return the systemMessage the hook printed for the user, checking it exited 0."""
    assert result.returncode == 0, f"the hook should exit 0:\n{result.stderr}"
    return json.loads(result.stdout)["systemMessage"]


def denied(result):
    """Return whether the hook denied the plan."""
    assert result.returncode == 0, f"the hook should exit 0:\n{result.stderr}"
    return json.loads(result.stdout).get("hookSpecificOutput", {}).get("permissionDecision") == "deny"


def deny_reason(result):
    """Return the reason the hook gave Claude for denying the plan."""
    assert denied(result), f"the plan should be denied:\n{result.stdout}"
    return json.loads(result.stdout)["hookSpecificOutput"]["permissionDecisionReason"]


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
    """An all-10 verdict allows the plan and tells the user its scores, and the reviewer saw the plan and style rule."""
    stub = _make_stub(tmp_path)
    result = stub(LONG_PLAN, {"scores": ALL_TENS, "findings": []})
    assert not denied(result), f"the plan should be allowed:\n{result.stdout}"
    assert "passed" in user_message(result) and "intent 10/10" in user_message(result)
    assert "hookSpecificOutput" not in json.loads(result.stdout), "a pass should leave the user's approval in place"
    prompt = stub.prompt.read_text()
    assert LONG_PLAN.strip() in prompt, "the reviewer should see the plan"
    assert "British spelling" in prompt, "the reviewer should see the writing style rule"


def test_a_plan_scored_under_10_is_blocked_with_the_findings(tmp_path):
    """Any theme under 10 denies the plan with the scores and findings, and tells the user the scores and round."""
    stub = _make_stub(tmp_path)
    verdict = {"scores": ALL_TENS | {"spec": 8}, "findings": ["Spec has no Out of scope bullet."]}
    result = stub(LONG_PLAN, verdict)
    assert "spec 8/10" in deny_reason(result), "the reason should give the scores"
    assert "Spec has no Out of scope bullet." in deny_reason(result), "the reason should list the findings"
    assert "spec 8/10" in user_message(result) and "round 1 of 2" in user_message(result)


def test_a_decisions_score_under_10_is_blocked_and_sent_to_the_user(tmp_path):
    """A decisions score under 10 denies the plan, and tells Claude to ask the user about those findings."""
    stub = _make_stub(tmp_path)
    verdict = {"scores": ALL_TENS | {"decisions": 6}, "findings": ["decisions: the database choice isn't agreed."]}
    result = stub(LONG_PLAN, verdict)
    assert "decisions 6/10" in deny_reason(result), "the reason should give the score"
    assert "ask the user" in deny_reason(result).lower(), "the reason should send Claude to the user"


def test_findings_nested_in_the_scores_are_read_as_findings(tmp_path):
    """A reply with findings inside scores passes when every theme is 10, and otherwise lists them as findings."""
    stub = _make_stub(tmp_path)
    result = stub(LONG_PLAN, {"scores": ALL_TENS | {"findings": []}})
    assert not denied(result), f"an all-10 plan should be allowed:\n{result.stdout}"
    result = stub(LONG_PLAN, {"scores": ALL_TENS | {"spec": 8, "findings": ["spec: no Out of scope bullet."]}})
    assert "\n- spec: no Out of scope bullet." in deny_reason(result), "the findings should be listed"


def test_the_third_submission_passes_with_the_findings_for_the_user(tmp_path):
    """After two blocks, the next submission passes with the findings for Claude and the scores for the user."""
    stub = _make_stub(tmp_path)
    verdict = {"scores": ALL_TENS | {"plan": 9}, "findings": ["Step 3 has no check."]}
    assert all(denied(stub(LONG_PLAN, verdict)) for _ in range(2)), "the first two submissions should be denied"
    result = stub(LONG_PLAN, verdict)
    assert not denied(result), f"the third submission should pass:\n{result.stdout}"
    assert "Step 3 has no check." in context(result), "the findings should reach Claude"
    assert "plan 9/10" in user_message(result) and "after 2 rounds" in user_message(result)
    assert denied(stub(LONG_PLAN, verdict, session="s2")), "another session gets its own rounds"


@pytest.mark.parametrize("ending", ["passed", "capped"])
def test_the_next_plan_in_a_session_gets_its_own_two_rounds(tmp_path, ending):
    """Once a plan passes or is capped, the next plan in the session is denied twice before it goes through."""
    stub = _make_stub(tmp_path)
    weak = {"scores": ALL_TENS | {"plan": 9}, "findings": ["Step 3 has no check."]}
    clean = {"scores": ALL_TENS, "findings": []}
    first_plan = [weak, weak, clean if ending == "passed" else weak]
    assert [denied(stub(LONG_PLAN, verdict)) for verdict in first_plan] == [True, True, False]
    second_plan = [denied(stub(LONG_PLAN, weak)) for _ in range(3)]
    assert second_plan == [True, True, False], f"the second plan should get two rounds: {second_plan}"


def test_the_reviewer_is_given_60_seconds(tmp_path):
    """The hook limits the reviewer to 60 seconds."""
    stub = _make_stub(tmp_path)
    perl = tmp_path / "bin" / "perl"
    perl.write_text(STUB_PERL)
    perl.chmod(0o755)
    stub(LONG_PLAN, {"scores": ALL_TENS, "findings": []})
    assert (tmp_path / "limit.txt").read_text().strip() == "60"


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
    assert "wasn't reviewed" in user_message(result), "the user should hear the review didn't run"


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


def test_the_hook_prompt_and_both_rules_name_the_six_intent_sections(tmp_path):
    """The reviewer's intent criterion, the workflow rule and the saving template name the same sections."""
    stub = _make_stub(tmp_path)
    stub(LONG_PLAN, {"scores": ALL_TENS, "findings": []})
    criterion = stub.prompt.read_text().split("- intent:")[1].split("- spec:")[0]
    # the prompt wraps its lines, so a section's name can span two of them
    criterion = " ".join(criterion.split())
    row = next(line for line in WORKFLOW_RULE.read_text().splitlines() if line.startswith("| `1. Intent`"))
    template = SAVING_RULE.read_text()
    for section in INTENT_SECTIONS:
        assert section in criterion, f"the hook's intent criterion should name {section}"
        assert f"**{section}**" in row, f"the workflow rule's Intent row should name {section}"
        assert f"\n## {section}\n" in template, f"the saving rule's template should have a {section} section"


def test_the_saving_rule_records_what_the_measures_need():
    """The saving rule names the four recorded fields, both decisions and the folder for a closed intent."""
    rule = SAVING_RULE.read_text()
    fields = ("**Started:**", "**Saved:**", "**Decision:** accepted", "**Edits after spec:**")
    for text in (*fields, "**Decision:** closed", "_plans/dropped/"):
        assert text in rule, f"the saving rule should give {text}"
