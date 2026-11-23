"""Tests for the done checks hook, which stops Claude once to run the repo's checks after files change."""

import json
import os
import subprocess

import pytest
from _paths import REPO_ROOT

HOOK = REPO_ROOT / "src" / "claude" / "hooks" / "ai_sdlc_workflow" / "hook_enforcement_done_checks.sh"
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
    """Return a git repo with one committed file, and a CLAUDE.md naming its done checks."""
    path = tmp_path / "repo"
    path.mkdir()
    env = {**os.environ, **GIT_ENV}
    subprocess.run(["git", "init", "-q"], cwd=path, env=env, check=True)
    (path / "app.py").write_text("print('hi')\n")
    (path / "CLAUDE.md").write_text("Done means `make test` passes.\n")
    subprocess.run(["git", "add", "app.py", "CLAUDE.md"], cwd=path, env=env, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=path, env=env, check=True)
    return path


def write_transcript(tmp_path, *calls):
    """Write a session transcript of Edit calls, one per path, and Bash calls, one per string, and return its path."""
    path = tmp_path / "transcript.jsonl"
    lines = [{"type": "user", "message": {"content": "change the app"}}]
    for call_for in calls:
        if isinstance(call_for, str):
            call = {"type": "tool_use", "name": "Bash", "input": {"command": call_for}}
        else:
            call = {"type": "tool_use", "name": "Edit", "input": {"file_path": str(call_for)}}
        lines.append({"type": "assistant", "message": {"content": [call]}})
    path.write_text("".join(json.dumps(line) + "\n" for line in lines))
    return path


def run_hook(tmp_path, cwd, active=False, session="s1", transcript=None):
    """Run the hook as Claude Code would at a Stop, keeping its state under tmp_path."""
    fields = {"hook_event_name": "Stop", "session_id": session, "cwd": str(cwd), "stop_hook_active": active}
    if transcript:
        fields["transcript_path"] = str(transcript)
    payload = json.dumps(fields)
    env = {**os.environ, **GIT_ENV, "TMPDIR": str(tmp_path / "state")}
    return subprocess.run(
        ["bash", str(HOOK)], input=payload, env=env, capture_output=True, text=True, check=False, timeout=10
    )


def test_a_stop_after_changes_is_blocked_with_the_reason(tmp_path, repo):
    """A stop with uncommitted changes to tracked files exits 2 and points Claude to the repo's done checks."""
    (repo / "app.py").write_text("print('changed')\n")
    result = run_hook(tmp_path, repo)
    assert result.returncode == BLOCKED, f"the stop should be blocked:\n{result.stderr}"
    assert "CLAUDE.md" in result.stderr, "the reason should point to the checks CLAUDE.md names"


@pytest.mark.parametrize("where", ["root", ".claude"])
def test_a_repo_without_a_claude_md_is_left_alone_unless_one_is_added(tmp_path, repo, where):
    """With CLAUDE.md removed, a stop after changes is allowed, and one in .claude/ counts like one at the root."""
    (repo / "CLAUDE.md").unlink()
    (repo / "app.py").write_text("print('changed')\n")
    assert run_hook(tmp_path, repo).returncode == 0, "a repo with no CLAUDE.md shouldn't be blocked"
    placed = repo / "CLAUDE.md" if where == "root" else repo / ".claude" / "CLAUDE.md"
    placed.parent.mkdir(exist_ok=True)
    placed.write_text("Done means `make test` passes.\n")
    assert run_hook(tmp_path, repo).returncode == BLOCKED, f"a CLAUDE.md in {where} should turn the hook on"


def test_a_second_stop_with_the_same_changes_is_allowed(tmp_path, repo):
    """Once blocked, a later stop with no further change exits 0."""
    (repo / "app.py").write_text("print('changed')\n")
    run_hook(tmp_path, repo)
    result = run_hook(tmp_path, repo)
    assert result.returncode == 0, f"an unchanged stop should be allowed:\n{result.stderr}"


def test_a_further_change_is_blocked_again(tmp_path, repo):
    """A stop after another edit to the same file is blocked again."""
    (repo / "app.py").write_text("print('changed')\n")
    run_hook(tmp_path, repo)
    (repo / "app.py").write_text("print('changed again')\n")
    result = run_hook(tmp_path, repo)
    assert result.returncode == BLOCKED, f"a further change should be blocked:\n{result.stderr}"


def test_changes_this_session_didnt_make_are_left_alone(tmp_path, repo):
    """With a transcript showing no edit to a changed file, such as another session's change, the stop is allowed."""
    (repo / "app.py").write_text("print('changed elsewhere')\n")
    result = run_hook(tmp_path, repo, transcript=write_transcript(tmp_path, tmp_path / "elsewhere.py"))
    assert result.returncode == 0, f"another session's change shouldn't block this one:\n{result.stderr}"


def test_a_change_this_session_made_is_blocked(tmp_path, repo):
    """With a transcript showing an edit to a changed tracked file, the stop is blocked."""
    (repo / "app.py").write_text("print('changed')\n")
    result = run_hook(tmp_path, repo, transcript=write_transcript(tmp_path, repo / "app.py"))
    assert result.returncode == BLOCKED, f"this session's own change should be blocked:\n{result.stderr}"


@pytest.mark.parametrize(("order", "expected"), [("edit_then_check", 0), ("check_then_edit", BLOCKED)])
def test_checks_run_after_the_last_edit_are_not_asked_for_again(tmp_path, repo, order, expected):
    """A CLAUDE.md command run after the session's last edit allows the stop, but one run before an edit doesn't."""
    (repo / "app.py").write_text("print('changed')\n")
    calls = [repo / "app.py", "make test 2>&1 | tail -1"]
    if order == "check_then_edit":
        calls.reverse()
    result = run_hook(tmp_path, repo, transcript=write_transcript(tmp_path, *calls))
    assert result.returncode == expected, f"{order} should exit {expected}:\n{result.stderr}"


def test_only_the_done_means_commands_count_as_checks(tmp_path, repo):
    """Another command CLAUDE.md names, such as its install step, doesn't count as the checks having run."""
    (repo / "CLAUDE.md").write_text("Install with `make deps`.\n\nDone means `make test` passes.\n")
    calls = [repo / "CLAUDE.md", "make deps"]
    result = run_hook(tmp_path, repo, transcript=write_transcript(tmp_path, *calls))
    assert result.returncode == BLOCKED, f"running only make deps shouldn't allow the stop:\n{result.stderr}"


def test_a_stop_while_the_hook_is_active_is_allowed(tmp_path, repo):
    """A stop with stop_hook_active set exits 0, even with changes."""
    (repo / "app.py").write_text("print('changed')\n")
    result = run_hook(tmp_path, repo, active=True)
    assert result.returncode == 0, f"an active stop hook should never block:\n{result.stderr}"


@pytest.mark.parametrize("where", ["clean_repo", "not_a_repo"])
def test_a_stop_with_nothing_changed_is_allowed(tmp_path, repo, where):
    """A clean repo, or a folder outside git, exits 0 and prints nothing."""
    cwd = repo if where == "clean_repo" else tmp_path
    result = run_hook(tmp_path, cwd)
    assert result.returncode == 0 and result.stderr == "", f"nothing changed, so the stop should pass:\n{result.stderr}"


@pytest.mark.parametrize("payload", ["", "not json", json.dumps({"hook_event_name": "Stop"})])
def test_input_with_no_session_is_allowed(payload):
    """Empty input, input that isn't JSON, or input with no session or folder exits 0."""
    result = subprocess.run(["bash", str(HOOK)], input=payload, capture_output=True, text=True, check=False, timeout=10)
    assert result.returncode == 0, f"malformed input should be allowed:\n{result.stderr}"
