"""Tests for the kaizen reminder hook, which suggests /claude-kaizen once 5 feedback notes are new since a run."""

import json
import os
import subprocess
import time

import pytest
from _paths import REPO_ROOT

HOOK = REPO_ROOT / "src" / "claude" / "hooks" / "claude_kaizen" / "hook_reminder_kaizen_due.sh"


def project(tmp_path, notes):
    """Return a project folder holding a transcript and a memory folder with that many feedback notes."""
    memory = tmp_path / "project" / "memory"
    memory.mkdir(parents=True)
    for number in range(notes):
        (memory / f"feedback_{number}.md").write_text("note\n")
    return tmp_path / "project"


def kaizen_dir(project_dir):
    """Return the kaizen folder in that project's test config directory."""
    return project_dir.parent / "config" / "_claude_kaizen"


def run_hook(project_dir, source="startup", cwd=REPO_ROOT):
    """Run the hook as Claude Code would at session start, returning its stdout."""
    payload = json.dumps(
        {
            "hook_event_name": "SessionStart",
            "source": source,
            "cwd": str(cwd),
            "transcript_path": str(project_dir / "s1.jsonl"),
        }
    )
    env = {**os.environ, "CLAUDE_CONFIG_DIR": str(project_dir.parent / "config")}
    result = subprocess.run(["bash", str(HOOK)], input=payload, capture_output=True, text=True, check=True, env=env)
    return result.stdout


def test_silent_below_the_threshold(tmp_path):
    """Four new notes add nothing to the session and log no nudge."""
    project_dir = project(tmp_path, 4)
    assert run_hook(project_dir) == ""
    assert not (kaizen_dir(project_dir) / "nudges.log").exists()


def test_nudges_and_logs_at_the_threshold(tmp_path):
    """Five new notes add one suggestion to the session and log the nudge for the trial's review."""
    project_dir = project(tmp_path, 5)
    stdout = run_hook(project_dir)
    assert "5 feedback notes have been saved since the last /claude-kaizen run" in stdout
    assert "skills/claude-kaizen/reference/_draft.md" in stdout
    assert "new_notes=5" in (kaizen_dir(project_dir) / "nudges.log").read_text()


def test_the_draft_page_it_names_exists():
    """The page the nudge sends Claude to ships with the skill."""
    assert (REPO_ROOT / "src/claude/skills/_claude_skills/claude-kaizen/reference/_draft.md").is_file()


def test_nudges_once_a_day(tmp_path):
    """A second fresh session on the same day stays silent and logs nothing more."""
    project_dir = project(tmp_path, 5)
    assert run_hook(project_dir) != ""
    assert run_hook(project_dir) == ""
    assert len((kaizen_dir(project_dir) / "nudges.log").read_text().splitlines()) == 1


def test_nudges_again_on_a_later_day(tmp_path):
    """A nudge from an earlier day doesn't silence today's."""
    project_dir = project(tmp_path, 5)
    kaizen_dir(project_dir).mkdir(parents=True)
    (kaizen_dir(project_dir) / "nudges.log").write_text("2020-01-01 new_notes=5\n")
    assert run_hook(project_dir) != ""


@pytest.mark.parametrize("source", ["resume", "compact", "fork"])
def test_silent_when_a_session_carries_on(tmp_path, source):
    """A resumed, compacted or forked session isn't nudged."""
    project_dir = project(tmp_path, 5)
    assert run_hook(project_dir, source=source) == ""


def test_nudges_after_clear(tmp_path):
    """A cleared session starts fresh, so it's nudged."""
    assert run_hook(project(tmp_path, 5), source="clear") != ""


def test_silent_outside_a_repo_with_rule_evals(tmp_path):
    """A project the skill can't run in isn't nudged."""
    project_dir = project(tmp_path, 5)
    assert run_hook(project_dir, cwd=tmp_path) == ""


def test_counts_only_notes_newer_than_the_last_run(tmp_path):
    """Notes saved before the last kaizen run don't count towards the next nudge."""
    project_dir = project(tmp_path, 6)
    kaizen_dir(project_dir).mkdir(parents=True)
    runs_log = kaizen_dir(project_dir) / "runs.log"
    runs_log.write_text("2026-11-19 notes=6 proposed=2 kept=1\n")
    later = time.time() + 60
    os.utime(runs_log, (later, later))
    assert run_hook(project_dir) == ""


def test_silent_without_a_memory_folder(tmp_path):
    """A project with no auto-memory folder adds nothing."""
    (tmp_path / "project").mkdir()
    assert run_hook(tmp_path / "project") == ""
