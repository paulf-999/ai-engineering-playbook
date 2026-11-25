"""Test that hooks keep their logs out of the auto-memory folder, where people don't look for them."""

import re

from _paths import REPO_ROOT

HOOKS_DIR = REPO_ROOT / "src" / "claude" / "hooks"
# plan_reviews.log is trial evidence until 2026-12-07, so it stays where it is until then
EXEMPT = {"hook_enforcement_plan_review.sh"}
LOG_IN_MEMORY = re.compile(r"(memory|MEMORY_DIR\}?)/[\w.]+\.log")


def test_the_pattern_spots_both_ways_of_writing_to_memory():
    """A log path is caught whether it's spelled out or built from the memory folder's variable."""
    assert LOG_IN_MEMORY.search('LOG="$(dirname "${TRANSCRIPT}")/memory/a.log"')
    assert LOG_IN_MEMORY.search('LOG="${MEMORY_DIR}/a.log"')
    assert not LOG_IN_MEMORY.search('LOG="${KAIZEN_DIR}/a.log"')


def test_hooks_write_no_logs_to_memory():
    """Each hook logs to its own folder in the Claude config directory instead."""
    offenders = [
        hook.name
        for hook in HOOKS_DIR.rglob("*.sh")
        if hook.name not in EXEMPT and LOG_IN_MEMORY.search(hook.read_text())
    ]
    assert not offenders, f"these hooks write a log to memory/: {offenders}"
