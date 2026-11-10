# version: 1.0.0
# created: 2026-11-10
# updated: 2026-11-10
"""Tests for the plan sections hook, which blocks a plan that has no Intent or Spec heading."""

import json
import subprocess

import pytest
from _paths import REPO_ROOT

HOOK = REPO_ROOT / "src" / "claude" / "hooks" / "hook_enforcement_plan_sections.sh"
# exit code 2 is how a PreToolUse hook tells Claude Code to block the call
BLOCKED = 2


def run_hook(payload):
    """Run the hook with payload as its stdin, as Claude Code would."""
    return subprocess.run(["bash", str(HOOK)], input=payload, capture_output=True, text=True, check=False, timeout=10)


def exit_plan_input(plan):
    """Return the JSON Claude Code sends a PreToolUse hook for ExitPlanMode with this plan."""
    return json.dumps({"hook_event_name": "PreToolUse", "tool_name": "ExitPlanMode", "tool_input": {"plan": plan}})


# MoSCoW: Must — a plan with both sections must never be blocked
@pytest.mark.parametrize(
    "plan",
    [
        "# Plan\n\n## Intent\n\nWhy.\n\n## Spec\n\nWhat.\n\n## Steps\n",
        "## 📝 **Intent**\n\nWhy.\n\n### spec and checks\n\nWhat.\n",
    ],
)
def test_a_plan_with_intent_and_spec_is_allowed(plan):
    """A plan with an Intent heading and a Spec heading, in any case or level, exits 0 and prints nothing."""
    result = run_hook(exit_plan_input(plan))
    assert result.returncode == 0, f"the plan should be allowed:\n{result.stderr}"
    assert result.stdout == "" and result.stderr == "", "an allowed plan should print nothing"


# MoSCoW: Must — the point of the hook: a plan missing a section is sent back with the reason
@pytest.mark.parametrize(
    ("plan", "missing"),
    [
        ("## Spec\n\nWhat.\n", "Intent"),
        ("## Intent\n\nWhy.\n", "Spec"),
        ("# Plan\n\nIntent and spec are mentioned in prose only.\n", "Intent/Spec"),
    ],
)
def test_a_plan_missing_a_section_is_blocked(plan, missing):
    """A plan without an Intent or Spec heading exits 2, names what's missing and points to the SDLC rule."""
    result = run_hook(exit_plan_input(plan))
    assert result.returncode == BLOCKED, f"the plan should be blocked:\n{result.stderr}"
    assert f"no {missing} heading" in result.stderr, f"the reason should name {missing}:\n{result.stderr}"
    assert "sdlc_workflow.md" in result.stderr, "the reason should point to the SDLC workflow rule"


# MoSCoW: Should — the hook must fail open, so a malformed call never blocks every plan
@pytest.mark.parametrize("payload", ["", "not json", json.dumps({"tool_input": {}})])
def test_input_with_no_plan_is_allowed(payload):
    """Empty input, input that isn't JSON, or input with no plan text exits 0."""
    result = run_hook(payload)
    assert result.returncode == 0, f"input with no plan should be allowed:\n{result.stderr}"
