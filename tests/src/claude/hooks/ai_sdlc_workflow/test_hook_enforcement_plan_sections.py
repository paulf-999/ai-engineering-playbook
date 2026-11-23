"""Tests for the plan sections hook, which blocks a plan that has no Intent or Spec heading."""

import json
import subprocess

import pytest
from _paths import REPO_ROOT

HOOK = REPO_ROOT / "src" / "claude" / "hooks" / "ai_sdlc_workflow" / "hook_enforcement_plan_sections.sh"
# exit code 2 is how a PreToolUse hook tells Claude Code to block the call
BLOCKED = 2
# the hook checks only plans of this many non-blank lines or more
MIN_PLAN_LINES = 15


def steps(count):
    """Return count numbered step lines, to pad a plan to a given length."""
    return "".join(f"{n}. Step {n}.\n" for n in range(1, count + 1))


def run_hook(payload):
    """Run the hook with payload as its stdin, as Claude Code would."""
    return subprocess.run(["bash", str(HOOK)], input=payload, capture_output=True, text=True, check=False, timeout=10)


def exit_plan_input(plan):
    """Return the JSON Claude Code sends a PreToolUse hook for ExitPlanMode with this plan."""
    return json.dumps({"hook_event_name": "PreToolUse", "tool_name": "ExitPlanMode", "tool_input": {"plan": plan}})


@pytest.mark.parametrize(
    "plan",
    [
        "# Plan\n\n## Intent\n\nWhy.\n\n## Spec\n\nWhat.\n\n## Steps\n",
        "## 📝 **Intent**\n\nWhy.\n\n### spec and checks\n\nWhat.\n",
        "## 1. Intent\n\nWhy.\n\n## 2. Spec\n\nWhat.\n",
    ],
)
def test_a_plan_with_intent_and_spec_is_allowed(plan):
    """A plan with an Intent heading and a Spec heading, in any case or level, exits 0 and prints nothing."""
    result = run_hook(exit_plan_input(plan))
    assert result.returncode == 0, f"the plan should be allowed:\n{result.stderr}"
    assert result.stdout == "" and result.stderr == "", "an allowed plan should print nothing"


@pytest.mark.parametrize(
    ("plan", "missing"),
    [
        ("## Spec\n\nWhat.\n" + steps(MIN_PLAN_LINES), "Intent"),
        ("## Intent\n\nWhy.\n" + steps(MIN_PLAN_LINES), "Spec"),
        ("# Plan\n\nIntent and spec are mentioned in prose only.\n" + steps(MIN_PLAN_LINES), "Intent/Spec"),
    ],
)
def test_a_plan_missing_a_section_is_blocked(plan, missing):
    """A plan without an Intent or Spec heading exits 2, names what's missing and points to the SDLC rule."""
    result = run_hook(exit_plan_input(plan))
    assert result.returncode == BLOCKED, f"the plan should be blocked:\n{result.stderr}"
    assert f"no {missing} heading" in result.stderr, f"the reason should name {missing}:\n{result.stderr}"
    assert "rules/always_on/01_standards/ai_sdlc_workflow.md" in result.stderr, "the reason should point to the rule"
    assert (REPO_ROOT / "src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md").is_file(), (
        "that rule should exist"
    )


@pytest.mark.parametrize(("lines", "blocked"), [(MIN_PLAN_LINES - 1, False), (MIN_PLAN_LINES, True)])
def test_only_a_plan_at_the_line_limit_needs_the_sections(lines, blocked):
    """A plan of 14 non-blank lines with no headings passes, and one of 15 is blocked, with blank lines not counted."""
    result = run_hook(exit_plan_input("\n\n".join(steps(lines).splitlines())))
    assert (result.returncode == BLOCKED) is blocked, (
        f"a {lines}-line plan should {'' if blocked else 'not '}be blocked"
    )


@pytest.mark.parametrize("payload", ["", "not json", json.dumps({"tool_input": {}})])
def test_input_with_no_plan_is_allowed(payload):
    """Empty input, input that isn't JSON, or input with no plan text exits 0."""
    result = run_hook(payload)
    assert result.returncode == 0, f"input with no plan should be allowed:\n{result.stderr}"


def test_a_plan_is_blocked_when_jq_is_missing(tmp_path):
    """With no jq on PATH, the hook exits 2 and says to install jq."""
    result = subprocess.run(
        ["/bin/bash", str(HOOK)],
        input=exit_plan_input("## Intent\n\nWhy.\n\n## Spec\n\nWhat.\n"),
        env={"PATH": str(tmp_path)},
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )
    assert result.returncode == BLOCKED, f"the plan should be blocked without jq:\n{result.stderr}"
    assert "install jq" in result.stderr, "the reason should say to install jq"
