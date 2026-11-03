# version: 1.0.0
# created: 2026-11-03
# updated: 2026-11-03
"""Tests for the always-on budget check, which caps the Claude context loaded into every session."""

import os
import subprocess

import pytest
from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "claude_validate_always_on_budget.sh"
# 400 characters is an estimated 100 tokens
HUNDRED_TOKENS = "x" * 399 + "\n"


def run_check(directory, budget="150"):
    """Run the check from the repo root against a test directory, with a small token budget."""
    env = {**os.environ, "ALWAYS_ON_TOKEN_BUDGET": budget}
    return subprocess.run(
        [str(SCRIPT), str(directory)], cwd=REPO_ROOT, env=env, capture_output=True, text=True, check=False
    )


def write(directory, path, text):
    """Write a file under the test directory, creating its folders."""
    target = directory / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text)


# MoSCoW: Must — context within the budget must not be blocked
@pytest.mark.parametrize(
    ("text", "tokens"),
    [
        (HUNDRED_TOKENS, 100),
        # exactly at the budget still passes, since only going over fails
        ("x" * 599 + "\n", 150),
    ],
)
def test_context_within_the_budget_passes(tmp_path, text, tokens):
    """A CLAUDE.md at or under a 150-token budget exits 0 and reports its estimate."""
    write(tmp_path, "CLAUDE.md", text)
    result = run_check(tmp_path)
    assert result.returncode == 0, f"~{tokens} tokens should pass a 150-token budget:\n{result.stdout}"
    assert f"~{tokens} tokens, within the 150-token budget" in result.stdout, "the estimate should be reported"


# MoSCoW: Must — every kind of always-on context counts towards the budget
@pytest.mark.parametrize(
    ("path", "text"),
    [
        ("src/templates/global_claude.md", HUNDRED_TOKENS),
        # a file CLAUDE.md pulls in with an @-import loads in full
        ("docs/imported.md", HUNDRED_TOKENS),
        # a rule with no paths: setting loads in every session
        (".claude/rules/always.md", HUNDRED_TOKENS),
        # Claude sees every skill's description, even when the skill isn't used
        (".claude/skills/example/SKILL.md", "---\ndescription: " + "x" * 400 + "\n---\n"),
        # agent descriptions count the same way
        (".claude/agents/example.md", "---\ndescription: " + "x" * 400 + "\n---\n"),
    ],
)
def test_each_kind_of_always_on_context_is_counted(tmp_path, path, text):
    """Adding 100 tokens of any always-on kind to a 100-token CLAUDE.md breaks a 150-token budget."""
    write(tmp_path, "CLAUDE.md", HUNDRED_TOKENS + "@docs/imported.md\n")
    write(tmp_path, path, text)
    result = run_check(tmp_path)
    assert result.returncode == 1, f"{path} should push the total over the budget:\n{result.stdout}"
    assert "over the 150-token budget" in result.stdout, "the failure should say the budget was exceeded"


# MoSCoW: Must — rules that load only for certain files mustn't count against the budget
def test_a_path_scoped_rule_is_not_counted(tmp_path):
    """A rule whose opening block sets paths: loads only with matching files, so it isn't counted."""
    write(tmp_path, "CLAUDE.md", HUNDRED_TOKENS)
    write(tmp_path, ".claude/rules/scoped.md", "---\npaths:\n  - '*.sql'\n---\n" + HUNDRED_TOKENS)
    result = run_check(tmp_path)
    assert result.returncode == 0, f"a paths: rule shouldn't count towards the budget:\n{result.stdout}"


# MoSCoW: Should — a bad budget value must fail clearly rather than be compared as text
def test_a_budget_that_is_not_a_whole_number_fails(tmp_path):
    """An ALWAYS_ON_TOKEN_BUDGET like '3k' exits 1 and says what's wrong."""
    write(tmp_path, "CLAUDE.md", HUNDRED_TOKENS)
    result = run_check(tmp_path, budget="3k")
    assert result.returncode == 1, "a budget of '3k' should be rejected"
    assert "must be a whole number" in result.stdout, "the error should say the budget must be a whole number"
