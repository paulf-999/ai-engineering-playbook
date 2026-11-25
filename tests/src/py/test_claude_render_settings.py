"""Tests for the settings renderer, and that its template and the hooks in src/claude/hooks/ stay in step."""

import json
import subprocess
import sys

import pytest
from _git_repo import isolated_git_repo
from _paths import REPO_ROOT

SCRIPT = REPO_ROOT / "src" / "py" / "claude_render_settings.py"
sys.path.insert(0, str(SCRIPT.parent))

import claude_render_settings as renderer  # noqa: E402

PROJECT_ONLY_WHEN_ASKED = {
    "ai_sdlc_workflow/hook_enforcement_done_checks.sh",
    "git/hook_enforcement_worktree_edits.sh",
}


def _make_repo(tmp_path, hooks):
    """Make a repo that tracks the named hooks under src/claude/hooks/."""
    env = isolated_git_repo(tmp_path)
    for hook in hooks:
        path = tmp_path / renderer.HOOKS_SOURCE / hook
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("#!/bin/bash\n")
    subprocess.run(["git", "add", "src"], cwd=tmp_path, env=env, check=True)
    return tmp_path


def run_renderer(repo, *args):
    """Run the renderer from a repo and return the result."""
    command = [sys.executable, str(SCRIPT), *args]
    return subprocess.run(command, cwd=repo, capture_output=True, text=True, check=False)


def test_the_template_lists_exactly_the_shipped_hooks():
    """Every hook file has a template entry, and every template entry names a hook file."""
    shipped = renderer.shipped_hooks(REPO_ROOT)
    assert shipped, "the repo should ship hooks"
    listed = renderer.named_hooks(renderer.render("/hooks", all_hooks=True), "/hooks")
    assert shipped - listed == set(), f"add these hooks to {renderer.TEMPLATE.name}"
    assert listed - shipped == set(), f"{renderer.TEMPLATE.name} names hooks that don't exist"


def test_only_all_hooks_includes_the_ones_a_project_leaves_out():
    """Without --all-hooks, only the done checks and worktree edits hooks are left out."""
    every, default = (renderer.named_hooks(renderer.render("/hooks", flag), "/hooks") for flag in (True, False))
    assert every - default == PROJECT_ONLY_WHEN_ASKED and default < every


@pytest.mark.parametrize("hooks_dir", ["/plain/hooks", '/a "quoted" \\\\ path/hooks', "/café & <co>/hooks"])
def test_the_hooks_folder_survives_json_escaping(hooks_dir):
    """Whatever characters the folder's path has, the command names it exactly."""
    commands = [
        hook["command"]
        for entries in renderer.render(hooks_dir, all_hooks=True)["hooks"].values()
        for entry in entries
        for hook in entry["hooks"]
    ]
    assert all(command.startswith(f'bash "{hooks_dir}/') for command in commands), commands


def test_an_unlisted_hook_stops_it(tmp_path):
    """A tracked hook with no template entry exits 1, names the hook and prints no settings."""
    result = run_renderer(_make_repo(tmp_path, ["git/hook_enforcement_new.sh"]), "/hooks")
    assert result.returncode == 1 and result.stdout == "", "it should stop and print nothing"
    assert "no entry for: git/hook_enforcement_new.sh" in result.stderr, result.stderr


def test_hooks_the_repo_doesnt_ship_are_left_out(tmp_path):
    """Only hooks the repo ships are printed, with the deny rules, and a helper beside them needs no entry."""
    kaizen = "claude_kaizen/hook_reminder_kaizen_due.sh"
    result = run_renderer(_make_repo(tmp_path, [kaizen, "git/helper.sh"]), "/hooks", "--all-hooks")
    assert result.returncode == 0, result.stderr
    settings = json.loads(result.stdout)
    assert renderer.named_hooks(settings, "/hooks") == {kaizen} and list(settings["hooks"]) == ["SessionStart"]
    assert settings["permissions"]["deny"], "the deny rules should be printed"


def test_a_tracked_hook_deleted_from_the_checkout_isnt_shipped(tmp_path):
    """A hook git tracks but the working tree lacks doesn't count as shipped."""
    repo = _make_repo(tmp_path, ["git/hook_enforcement_new.sh"])
    (repo / renderer.HOOKS_SOURCE / "git" / "hook_enforcement_new.sh").unlink()
    assert renderer.shipped_hooks(repo) == set()
