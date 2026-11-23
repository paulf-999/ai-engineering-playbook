"""Tests for the worktree edits hook, which blocks a session's first edit in a repo's main folder once."""

import json
import os
import subprocess

import pytest
from _paths import REPO_ROOT

HOOK = REPO_ROOT / "src" / "claude" / "hooks" / "git" / "hook_enforcement_worktree_edits.sh"
# exit code 2 is how a PreToolUse hook tells Claude Code to block the tool call and show stderr to Claude
BLOCKED = 2
GIT_ENV = {
    "GIT_CONFIG_GLOBAL": os.devnull,
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_AUTHOR_NAME": "Test",
    "GIT_AUTHOR_EMAIL": "test@example.com",
    "GIT_COMMITTER_NAME": "Test",
    "GIT_COMMITTER_EMAIL": "test@example.com",
}


def git(cwd, *args):
    """Run a git command in cwd with a clean config."""
    subprocess.run(["git", *args], cwd=cwd, env={**os.environ, **GIT_ENV}, check=True, capture_output=True)


@pytest.fixture
def repo(tmp_path):
    """Return a git repo's main folder with one committed file."""
    path = tmp_path / "repo"
    path.mkdir()
    git(path, "init", "-q")
    (path / "app.py").write_text("print('hi')\n")
    git(path, "add", "app.py")
    git(path, "commit", "-q", "-m", "init")
    return path


def run_hook(tmp_path, file_path, session="s1", tool="Edit"):
    """Run the hook as Claude Code would before an edit to file_path, keeping its state under tmp_path."""
    key = "notebook_path" if tool == "NotebookEdit" else "file_path"
    payload = json.dumps(
        {"hook_event_name": "PreToolUse", "session_id": session, "tool_name": tool, "tool_input": {key: str(file_path)}}
    )
    env = {**os.environ, **GIT_ENV, "TMPDIR": str(tmp_path / "state")}
    return subprocess.run(
        ["bash", str(HOOK)], input=payload, env=env, capture_output=True, text=True, check=False, timeout=10
    )


@pytest.mark.parametrize("tool", ["Edit", "Write", "NotebookEdit"])
def test_a_first_edit_in_the_main_folder_is_blocked_once(tmp_path, repo, tool):
    """The first edit in a repo's main folder exits 2 and points to a worktree, and the next edit is allowed."""
    first = run_hook(tmp_path, repo / "app.py", tool=tool)
    assert first.returncode == BLOCKED, f"the first edit should be blocked:\n{first.stderr}"
    assert "worktree" in first.stderr, "the reason should point Claude to a worktree"
    assert "already have changes" not in first.stderr, "a clean folder shouldn't mention another session's changes"
    assert run_hook(tmp_path, repo / "app.py", tool=tool).returncode == 0, "a second edit should be allowed"


def test_changes_from_before_the_first_edit_are_named(tmp_path, repo):
    """With tracked files already changed, the block message says another session is likely working here."""
    (repo / "app.py").write_text("print('changed')\n")
    result = run_hook(tmp_path, repo / "app.py")
    assert result.returncode == BLOCKED and "already have changes" in result.stderr, result.stderr


def test_another_session_is_blocked_on_its_own_first_edit(tmp_path, repo):
    """Each session is warned once, so a second session's first edit is blocked too."""
    run_hook(tmp_path, repo / "app.py", session="s1")
    assert run_hook(tmp_path, repo / "app.py", session="s2").returncode == BLOCKED


def test_a_new_file_in_a_new_folder_is_checked(tmp_path, repo):
    """A Write to a folder that doesn't exist yet is checked against the repo that will hold it."""
    assert run_hook(tmp_path, repo / "new" / "deeper" / "file.md", tool="Write").returncode == BLOCKED


def test_an_edit_in_a_linked_worktree_is_allowed(tmp_path, repo):
    """An edit inside a linked worktree exits 0 and prints nothing."""
    worktree = tmp_path / "worktree"
    git(repo, "worktree", "add", "-q", "-b", "feature/x", str(worktree))
    result = run_hook(tmp_path, worktree / "app.py")
    assert result.returncode == 0 and result.stderr == "", f"a worktree edit should pass:\n{result.stderr}"


def test_an_edit_outside_a_repo_is_allowed(tmp_path):
    """An edit to a file outside any git repo, such as a scratch file, exits 0."""
    folder = tmp_path / "scratch"
    folder.mkdir()
    assert run_hook(tmp_path, folder / "notes.md").returncode == 0


@pytest.mark.parametrize(
    "payload", ["", "not json", json.dumps({"session_id": "s1"}), json.dumps({"tool_input": {"file_path": "/x"}})]
)
def test_input_with_no_session_or_file_is_allowed(payload):
    """Empty input, input that isn't JSON, or input with no session or file path exits 0."""
    result = subprocess.run(["bash", str(HOOK)], input=payload, capture_output=True, text=True, check=False, timeout=10)
    assert result.returncode == 0, f"malformed input should be allowed:\n{result.stderr}"
