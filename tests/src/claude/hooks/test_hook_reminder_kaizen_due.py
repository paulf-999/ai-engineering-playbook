"""Tests for the kaizen reminder hook, which suggests /claude-kaizen once 5 feedback notes are new since a run."""

import json
import os
import subprocess
import time

from _paths import REPO_ROOT

HOOK = REPO_ROOT / "src" / "claude" / "hooks" / "hook_reminder_kaizen_due.sh"


def project(tmp_path, notes):
    """Return a project folder holding a transcript and a memory folder with that many feedback notes."""
    memory = tmp_path / "project" / "memory"
    memory.mkdir(parents=True)
    for number in range(notes):
        (memory / f"feedback_{number}.md").write_text("note\n")
    return tmp_path / "project"


def run_hook(project_dir):
    """Run the hook as Claude Code would at session start, returning its stdout."""
    payload = json.dumps({"hook_event_name": "SessionStart", "transcript_path": str(project_dir / "s1.jsonl")})
    result = subprocess.run(["bash", str(HOOK)], input=payload, capture_output=True, text=True, check=True)
    return result.stdout


def test_silent_below_the_threshold(tmp_path):
    """Four new notes add nothing to the session and log no nudge."""
    project_dir = project(tmp_path, 4)
    assert run_hook(project_dir) == ""
    assert not (project_dir / "memory" / "kaizen_nudges.log").exists()


def test_nudges_and_logs_at_the_threshold(tmp_path):
    """Five new notes add one suggestion to the session and log the nudge for the trial's review."""
    project_dir = project(tmp_path, 5)
    assert "5 feedback notes have been saved since the last /claude-kaizen run" in run_hook(project_dir)
    assert "new_notes=5" in (project_dir / "memory" / "kaizen_nudges.log").read_text()


def test_counts_only_notes_newer_than_the_last_run(tmp_path):
    """Notes saved before the last kaizen run don't count towards the next nudge."""
    project_dir = project(tmp_path, 6)
    runs_log = project_dir / "memory" / "kaizen_runs.log"
    runs_log.write_text("2026-11-19 notes=6 proposed=2 kept=1\n")
    later = time.time() + 60
    os.utime(runs_log, (later, later))
    assert run_hook(project_dir) == ""


def test_silent_without_a_memory_folder(tmp_path):
    """A project with no auto-memory folder adds nothing."""
    (tmp_path / "project").mkdir()
    assert run_hook(tmp_path / "project") == ""
