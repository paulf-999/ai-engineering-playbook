"""Tests for the missed rules script, on made-up rules and transcripts."""

import importlib
import json
import sys

import pytest
from _paths import REPO_ROOT

sys.path.insert(0, str(REPO_ROOT / "src" / "py"))
script = importlib.import_module("find_missed_rules")

START = "2026-11-19"


def write_rule(home):
    """Write one path-based rule for Python files, and return its path."""
    rule = home / "rules" / "python.md"
    rule.parent.mkdir()
    rule.write_text('---\npaths:\n  - "**/*.py"\n---\n# Python\n')
    return str(rule)


def write_session(home, *entries, started="2026-11-20T09:00", instructed=True):
    """Write one transcript that starts at the given time, then holds the given entries."""
    attachment = {"type": "instructions"} if instructed else {}
    log = home / "projects" / "repo" / "session.jsonl"
    log.parent.mkdir(parents=True)
    lines = [json.dumps(entry) for entry in [{"timestamp": started, "attachment": attachment}, *entries]]
    log.write_text("\n".join(lines) + '\n{"cut off')


def edit(path):
    """Return a transcript entry that edits a file."""
    content = [{"type": "tool_use", "name": "Edit", "input": {"file_path": path}}]
    return {"message": {"content": content}}


@pytest.mark.parametrize(("loads", "expected"), [(True, 0), (False, 1)])
def test_counts_a_miss_only_when_the_rule_never_loaded(tmp_path, loads, expected):
    """A session that edits a matching file is a miss unless the rule loaded."""
    rule = write_rule(tmp_path)
    load = [{"attachment": {"type": "nested_memory", "path": rule}}] if loads else []
    write_session(tmp_path, edit("/repo/src/app.py"), *load)
    applied, missed = script.count_misses(tmp_path, START)
    assert (applied[rule], missed[rule]) == (1, expected)


@pytest.mark.parametrize(
    ("path", "session"),
    [
        ("/repo/notes.md", {}),
        ("/repo/app.py", {"started": "2026-11-18T09:00"}),
        ("/repo/app.py", {"instructed": False}),
    ],
    ids=["no matching file", "before the start date", "ran without rules"],
)
def test_ignores_sessions_the_rule_does_not_apply_to(tmp_path, path, session):
    """Sessions with no matching file, from before the start date or without rules aren't counted."""
    write_rule(tmp_path)
    write_session(tmp_path, edit(path), **session)
    assert not script.count_misses(tmp_path, START)[0]
