# version: 1.0.6
# created: 2026-11-03
# updated: 2026-11-04
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


# MoSCoW: Must — context at the budget must pass, and context one token over must fail
@pytest.mark.parametrize(
    ("tokens", "exit_code", "message"),
    [
        (100, 0, "~100 tokens, within the 150-token budget"),
        # exactly at the budget still passes, since only going over fails
        (150, 0, "~150 tokens, within the 150-token budget"),
        (151, 1, "~151 tokens, over the 150-token budget"),
    ],
)
def test_the_budget_boundary(tmp_path, tokens, exit_code, message):
    """A CLAUDE.md at or under a 150-token budget passes, one token over fails, and the estimate is reported."""
    write(tmp_path, "CLAUDE.md", "x" * (tokens * 4 - 1) + "\n")
    result = run_check(tmp_path)
    assert result.returncode == exit_code, f"~{tokens} tokens should exit {exit_code}:\n{result.stdout}"
    assert message in result.stdout, "the estimate and verdict should be reported"


# MoSCoW: Must — every kind of always-on context counts towards the budget
@pytest.mark.parametrize(
    ("path", "text"),
    [
        ("src/claude/CLAUDE.md", HUNDRED_TOKENS),
        # a file CLAUDE.md pulls in with an @-import loads in full
        ("docs/imported.md", HUNDRED_TOKENS),
        # a rule with no paths: setting loads in every session
        (".claude/rules/always.md", HUNDRED_TOKENS),
        # the global config make install copies loads in every session too
        ("src/claude/rules/always.md", HUNDRED_TOKENS),
        ("src/claude/skills/example/SKILL.md", "---\ndescription: " + "x" * 400 + "\n---\n"),
        # Claude sees every skill's description, even when the skill isn't used
        (".claude/skills/example/SKILL.md", "---\ndescription: " + "x" * 400 + "\n---\n"),
        # agent descriptions count the same way
        (".claude/agents/example.md", "---\ndescription: " + "x" * 400 + "\n---\n"),
        # a description folded over several lines with > counts in full
        (".claude/skills/folded/SKILL.md", "---\ndescription: >\n  " + "x" * 200 + "\n  " + "x" * 200 + "\n---\n"),
    ],
)
def test_each_kind_of_always_on_context_is_counted(tmp_path, path, text):
    """Adding 100 tokens of any always-on kind to a 100-token CLAUDE.md breaks a 150-token budget."""
    write(tmp_path, "CLAUDE.md", HUNDRED_TOKENS + "@docs/imported.md\n")
    write(tmp_path, path, text)
    result = run_check(tmp_path)
    assert result.returncode == 1, f"{path} should push the total over the budget:\n{result.stdout}"
    assert "over the 150-token budget" in result.stdout, "the failure should say the budget was exceeded"


# MoSCoW: Must — context that doesn't load in every session mustn't count against the budget
@pytest.mark.parametrize(
    ("path", "text"),
    [
        # a rule whose opening block sets paths: loads only with matching files
        (".claude/rules/scoped.md", "---\npaths:\n  - '*.sql'\n---\n" + HUNDRED_TOKENS),
        ("src/claude/rules/scoped.md", "---\npaths:\n  - '*.sql'\n---\n" + HUNDRED_TOKENS),
        # a file read on demand loads only when Claude follows a pointer to it
        ("src/claude/rules/_rules_on_demand/guide.md", HUNDRED_TOKENS),
        # a skill's or agent's body loads only when it's used, so only its description counts
        (".claude/skills/example/SKILL.md", "---\ndescription: short\n---\n" + HUNDRED_TOKENS),
        (".claude/agents/example.md", "---\ndescription: short\n---\n" + HUNDRED_TOKENS),
    ],
)
def test_context_loaded_only_on_demand_is_not_counted(tmp_path, path, text):
    """Adding 100 tokens that load only on demand to a 100-token CLAUDE.md stays within a 150-token budget."""
    write(tmp_path, "CLAUDE.md", HUNDRED_TOKENS)
    write(tmp_path, path, text)
    result = run_check(tmp_path)
    assert result.returncode == 0, f"{path} shouldn't count towards the budget:\n{result.stdout}"


# MoSCoW: Should — a bad budget value must fail clearly rather than be compared as text
def test_a_budget_that_is_not_a_whole_number_fails(tmp_path):
    """An ALWAYS_ON_TOKEN_BUDGET like '3k' exits 1 and says what's wrong."""
    write(tmp_path, "CLAUDE.md", HUNDRED_TOKENS)
    result = run_check(tmp_path, budget="3k")
    assert result.returncode == 1, "a budget of '3k' should be rejected"
    assert "must be a whole number" in result.stdout, "the error should say the budget must be a whole number"


# MoSCoW: Must — HTML comments don't reach Claude, so they mustn't count towards the budget
def test_html_comments_are_not_counted(tmp_path):
    """A 100-token CLAUDE.md plus 100 tokens of HTML comments, one over several lines, stays within 150 tokens."""
    comments = "<!-- " + "x" * 190 + " -->\n<!--\n" + "x" * 190 + "\n-->\n"
    write(tmp_path, "CLAUDE.md", comments + HUNDRED_TOKENS)
    result = run_check(tmp_path)
    assert result.returncode == 0, f"HTML comments shouldn't count towards the budget:\n{result.stdout}"
