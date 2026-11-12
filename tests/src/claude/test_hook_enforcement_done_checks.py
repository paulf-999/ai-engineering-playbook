# version: 1.0.0
# created: 2026-11-12
# updated: 2026-11-12
"""Tests for the done checks hook, which stops Claude once to run the repo's checks after files change."""

import json
import os
import subprocess

import pytest
from _paths import REPO_ROOT

HOOK = REPO_ROOT / "src" / "claude" / "hooks" / "hook_enforcement_done_checks.sh"
# exit code 2 is how a Stop hook tells Claude Code to keep going and show stderr to Claude
BLOCKED = 2
GIT_ENV = {
    "GIT_CONFIG_GLOBAL": os.devnull,
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_AUTHOR_NAME": "Test",
    "GIT_AUTHOR_EMAIL": "test@example.com",
    "GIT_COMMITTER_NAME": "Test",
    "GIT_COMMITTER_EMAIL": "test@example.com",
}


@pytest.fixture
def repo(tmp_path):
    """Return a git repo with one committed file."""
    path = tmp_path / "repo"
    path.mkdir()
    env = {**os.environ, **GIT_ENV}
    subprocess.run(["git", "init", "-q"], cwd=path, env=env, check=True)
    (path / "app.py").write_text("print('hi')\n")
    subprocess.run(["git", "add", "app.py"], cwd=path, env=env, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=path, env=env, check=True)
    return path


def run_hook(tmp_path, cwd, active=False, session="s1"):
    """Run the hook as Claude Code would at a Stop, keeping its state under tmp_path."""
    payload = json.dumps(
        {"hook_event_name": "Stop", "session_id": session, "cwd": str(cwd), "stop_hook_active": active}
    )
    env = {**os.environ, **GIT_ENV, "TMPDIR": str(tmp_path / "state")}
    return subprocess.run(
        ["bash", str(HOOK)], input=payload, env=env, capture_output=True, text=True, check=False, timeout=10
    )


# MoSCoW: Must — the point of the hook: changed files send Claude back to run the checks
def test_a_stop_after_changes_is_blocked_with_the_reason(tmp_path, repo):
    """A stop with uncommitted changes to tracked files exits 2 and points Claude to the repo's done checks."""
    (repo / "app.py").write_text("print('changed')\n")
    result = run_hook(tmp_path, repo)
    assert result.returncode == BLOCKED, f"the stop should be blocked:\n{result.stderr}"
    assert "CLAUDE.md" in result.stderr, "the reason should point to the checks CLAUDE.md names"


# MoSCoW: Must — the hook blocks once per change, so a read-only turn after it isn't blocked again
def test_a_second_stop_with_the_same_changes_is_allowed(tmp_path, repo):
    """Once blocked, a later stop with no further change exits 0."""
    (repo / "app.py").write_text("print('changed')\n")
    run_hook(tmp_path, repo)
    result = run_hook(tmp_path, repo)
    assert result.returncode == 0, f"an unchanged stop should be allowed:\n{result.stderr}"


# MoSCoW: Should — a new change after the nudge needs the checks run again
def test_a_further_change_is_blocked_again(tmp_path, repo):
    """A stop after another edit to the same file is blocked again."""
    (repo / "app.py").write_text("print('changed')\n")
    run_hook(tmp_path, repo)
    (repo / "app.py").write_text("print('changed again')\n")
    result = run_hook(tmp_path, repo)
    assert result.returncode == BLOCKED, f"a further change should be blocked:\n{result.stderr}"


# MoSCoW: Must — Claude Code sets stop_hook_active while a stop hook keeps it going, so blocking then would loop
def test_a_stop_while_the_hook_is_active_is_allowed(tmp_path, repo):
    """A stop with stop_hook_active set exits 0, even with changes."""
    (repo / "app.py").write_text("print('changed')\n")
    result = run_hook(tmp_path, repo, active=True)
    assert result.returncode == 0, f"an active stop hook should never block:\n{result.stderr}"


# MoSCoW: Should — nothing to check means nothing to block
@pytest.mark.parametrize("where", ["clean_repo", "not_a_repo"])
def test_a_stop_with_nothing_changed_is_allowed(tmp_path, repo, where):
    """A clean repo, or a folder outside git, exits 0 and prints nothing."""
    cwd = repo if where == "clean_repo" else tmp_path
    result = run_hook(tmp_path, cwd)
    assert result.returncode == 0 and result.stderr == "", f"nothing changed, so the stop should pass:\n{result.stderr}"


# MoSCoW: Should — the hook must fail open, so malformed input never blocks every stop
@pytest.mark.parametrize("payload", ["", "not json", json.dumps({"hook_event_name": "Stop"})])
def test_input_with_no_session_is_allowed(payload):
    """Empty input, input that isn't JSON, or input with no session or folder exits 0."""
    result = subprocess.run(["bash", str(HOOK)], input=payload, capture_output=True, text=True, check=False, timeout=10)
    assert result.returncode == 0, f"malformed input should be allowed:\n{result.stderr}"
