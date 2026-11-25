"""Tests for the install script, which copies src/claude/ into a Claude config directory after a typed 'install'."""

import json
import os
import pty
import re
import shutil
import subprocess
import tempfile
from functools import cache
from pathlib import Path

import pytest
from _config_files import AUTHORING_TEMPLATES, GIT_ENV, is_preference, tracked_config_files
from _git_repo import isolated_git_repo
from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "claude_install_config.sh"
SOURCE = REPO_ROOT / "src" / "claude"


# a preference that PREFERENCES=0 leaves out
OUTPUT_FORMAT = "rules/always_on/02_preferences/claude_output_format.md"


@cache
def _make_small_repo():
    """Return a temporary repo with the real CLAUDE.md and hooks and one preference, deleted when the tests exit."""
    # an install's time grows with its file count, so only tests about the full config install all of it
    # those pass cwd=REPO_ROOT, as they check every tracked file, rewritten pointer or preference
    repo = tempfile.TemporaryDirectory()
    root = Path(repo.name)
    env = isolated_git_repo(root)
    for path in ("CLAUDE.md", OUTPUT_FORMAT):
        (root / "src" / "claude" / path).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(SOURCE / path, root / "src" / "claude" / path)
    shutil.copytree(SOURCE / "hooks", root / "src" / "claude" / "hooks")
    subprocess.run(["git", "add", "src/claude"], cwd=root, env=env, check=True)
    return repo


def run_install(target, answer=None, cwd=None, **extra_env):
    """Run the script from cwd, default a small repo, typing answer at a pseudo-terminal, or with none if it is None."""
    cwd = cwd or _make_small_repo().name
    # a temporary home, outside the target, so an install never touches the real saved plans
    with tempfile.TemporaryDirectory() as home:
        env = {**os.environ, **GIT_ENV, "HOME": home, "CLAUDE_CONFIG_DIR": str(target), **extra_env}
        if answer is None:
            return subprocess.run(
                [str(SCRIPT)], cwd=cwd, env=env, stdin=subprocess.DEVNULL, capture_output=True, text=True, check=False
            )
        # a pseudo-terminal makes [[ -t 0 ]] true, as it is when a person runs make install
        controller, terminal = pty.openpty()
        try:
            os.write(controller, f"{answer}\n".encode())
            return subprocess.run(
                [str(SCRIPT)],
                cwd=cwd,
                env=env,
                stdin=terminal,
                capture_output=True,
                text=True,
                check=False,
                timeout=120,
            )
        finally:
            os.close(terminal)
            os.close(controller)


def installed_path(source):
    """Return where a src/claude/ file should install, with on-demand files moved out of rules/ and skills flattened."""
    if source.startswith("rules/on_demand/"):
        return source.removeprefix("rules/")
    return re.sub(r"^skills/_[^/]+/", "skills/", source)


def installed_files(target):
    """Return every file under the target, as paths relative to it, ignoring backups."""
    return {
        str(path.relative_to(target)) for path in target.rglob("*") if path.is_file() and "backups" not in path.parts
    }


def test_without_a_terminal_nothing_is_installed(tmp_path):
    """With no terminal attached, the script exits 1, says to run it yourself and writes nothing."""
    result = run_install(tmp_path)
    assert result.returncode == 1, f"install should refuse without a terminal:\n{result.stdout}"
    assert "from your own terminal" in result.stdout, "the refusal should say how to run it"
    assert not any(tmp_path.iterdir()), "nothing should be written without a terminal"


def test_a_wrong_answer_cancels(tmp_path):
    """Typing anything other than 'install' cancels with exit 1 and writes nothing."""
    result = run_install(tmp_path, answer="yes")
    assert result.returncode == 1, f"a wrong answer should cancel:\n{result.stdout}"
    assert "nothing changed" in result.stdout, "the cancellation should be reported"
    assert not any(tmp_path.iterdir()), "nothing should be written after cancelling"


@pytest.fixture(scope="module")
def default_install(tmp_path_factory):
    """Install once into a fresh config directory, shared by the tests that only read a plain install."""
    target = tmp_path_factory.mktemp("default_install")
    result = run_install(target, answer="install", cwd=REPO_ROOT)
    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    return target


def test_install_copies_every_tracked_file(default_install):
    """Each tracked file installs to its relative path, with on-demand files beside rules/ and grouped skills flat."""
    sources = tracked_config_files()
    assert sources, "git should list at least one file under src/claude/"
    installed = {installed_path(path): path for path in sources}
    on_disk = installed_files(default_install)
    assert set(installed) <= on_disk, f"missing: {set(installed) - on_disk}"
    for target, source in installed.items():
        copied, original = (default_install / target).read_bytes(), (SOURCE / source).read_bytes()
        if target.endswith(".md"):
            # install corrects the paths of relative links, which their own test checks
            copied, original = (re.sub(rb"\]\(\.\./[^)#\s]+", b"](", text) for text in (copied, original))
        assert copied == original, f"{target} should match {source}"
    assert (default_install / "on_demand" / "01_standards" / "claude_config" / "guiding_principles.md").is_file(), (
        "on-demand files should sit beside rules/"
    )
    assert not (default_install / "rules" / "on_demand").exists(), "no on-demand file should install under rules/"
    assert (SOURCE / "skills" / "_git_skills" / "git-create-pr" / "SKILL.md").is_file(), "the repo should group it"
    assert (default_install / "skills" / "git-create-pr" / "SKILL.md").is_file(), "the skill should install flat"
    assert not (default_install / "skills" / "_git_skills").exists(), "no group folder, nor its README, should install"


def test_relative_links_open_once_installed(default_install):
    """Each link that climbs out of its folder opens its target where it installs, whether either file moved or not."""
    # the install test shows every link's target is installed, so a broken link here means its path is wrong
    links = {
        (path, link)
        for path in (default_install / installed for installed in installed_files(default_install))
        if path.suffix == ".md"
        for link in re.findall(r"\]\((\.\./[^)#\s]+)", path.read_text())
    }
    assert links, "the config should hold links between folders"
    broken = {
        f"{path.relative_to(default_install)}: {link}" for path, link in links if not (path.parent / link).exists()
    }
    assert not broken, f"{len(broken)} broken: {sorted(broken)}"


def test_install_backs_up_overwrites_and_keeps_other_files(tmp_path):
    """An existing CLAUDE.md that differs is backed up before it's replaced, and files the repo lacks are left alone."""
    (tmp_path / "CLAUDE.md").write_text("my old config\n")
    (tmp_path / "memory").mkdir()
    (tmp_path / "memory" / "note.md").write_text("keep me\n")

    result = run_install(tmp_path, answer="install")

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    backups = list((tmp_path / "backups").glob("install_*/CLAUDE.md"))
    assert len(backups) == 1 and backups[0].read_text() == "my old config\n", "the old CLAUDE.md should be backed up"
    assert (tmp_path / "memory" / "note.md").read_text() == "keep me\n", "files the repo doesn't have must be untouched"


def test_files_the_repo_removed_are_backed_up_then_removed(tmp_path):
    """A manifest path the repo no longer has is backed up, removed and dropped, along with the folders it empties."""
    (tmp_path / "rules" / "gone").mkdir(parents=True)
    (tmp_path / "rules" / "gone" / "old.md").write_text("old rule\n")
    (tmp_path / "rules" / "mine").mkdir()
    (tmp_path / ".playbook_install_manifest").write_text("rules/gone/old.md\n")

    result = run_install(tmp_path, answer="install", cwd=REPO_ROOT)

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    assert not (tmp_path / "rules" / "gone").exists(), "the file and the folder it emptied should be removed"
    assert (tmp_path / "rules" / "mine").is_dir(), "an empty folder the install didn't empty should stay"
    backups = list((tmp_path / "backups").glob("install_*/rules/gone/old.md"))
    assert len(backups) == 1 and backups[0].read_text() == "old rule\n", "the removed file should be backed up first"
    manifest = (tmp_path / ".playbook_install_manifest").read_text().splitlines()
    assert set(manifest) == {installed_path(path) for path in tracked_config_files(include_preferences=True)}, (
        "the manifest should list this install"
    )


def test_manifest_paths_outside_the_target_are_ignored(tmp_path):
    """A manifest path containing '..' is skipped, so the file it points at is left alone."""
    target = tmp_path / "config"
    target.mkdir()
    outside = tmp_path / "outside.md"
    outside.write_text("keep me\n")
    (target / ".playbook_install_manifest").write_text("../outside.md\n")

    result = run_install(target, answer="install")

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    assert outside.read_text() == "keep me\n", "a file outside the config directory must never be removed"


def plan_hook_commands(target, hook_file="hook_enforcement_plan_sections.sh"):
    """Return the ExitPlanMode hook commands in the target's settings.json that run hook_file, default plan sections."""
    settings = json.loads((target / "settings.json").read_text())
    return [
        hook["command"]
        for entry in settings.get("hooks", {}).get("PreToolUse", [])
        if entry.get("matcher") == "ExitPlanMode"
        for hook in entry.get("hooks", [])
        if hook_file in hook.get("command", "")
    ]


def edit_hook_commands(target):
    """Return the PreToolUse hook commands in the target's settings.json that run the worktree edits hook."""
    settings = json.loads((target / "settings.json").read_text())
    return [
        hook["command"]
        for entry in settings.get("hooks", {}).get("PreToolUse", [])
        if entry.get("matcher") == "Edit|Write|NotebookEdit"
        for hook in entry.get("hooks", [])
        if "hook_enforcement_worktree_edits.sh" in hook.get("command", "")
    ]


def stop_hook_commands(target):
    """Return the Stop hook commands in the target's settings.json that run the done checks hook."""
    settings = json.loads((target / "settings.json").read_text())
    return [
        hook["command"]
        for entry in settings.get("hooks", {}).get("Stop", [])
        if "matcher" not in entry
        for hook in entry.get("hooks", [])
        if "hook_enforcement_done_checks.sh" in hook.get("command", "")
    ]


def test_install_registers_the_hooks_and_keeps_existing_settings(tmp_path):
    """Install adds every shipped hook by absolute path, keeps other settings and backs up the old file."""
    (tmp_path / "settings.json").write_text(json.dumps({"model": "opus", "permissions": {"allow": ["Bash(ls)"]}}))

    result = run_install(tmp_path, answer="install")

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    settings = json.loads((tmp_path / "settings.json").read_text())
    assert settings["model"] == "opus" and settings["permissions"]["allow"] == ["Bash(ls)"], "settings must be kept"
    sdlc = f"{tmp_path}/hooks/ai_sdlc_workflow"
    assert plan_hook_commands(tmp_path) == [f'bash "{sdlc}/hook_enforcement_plan_sections.sh"']
    review = "hook_enforcement_plan_review.sh"
    assert plan_hook_commands(tmp_path, review) == [f'bash "{sdlc}/{review}"']
    assert edit_hook_commands(tmp_path) == [f'bash "{tmp_path}/hooks/git/hook_enforcement_worktree_edits.sh"']
    assert stop_hook_commands(tmp_path) == [f'bash "{sdlc}/hook_enforcement_done_checks.sh"']
    assert list((tmp_path / "backups").glob("install_*/settings.json")), "the old settings.json should be backed up"
    shipped = [hook for entries in settings["hooks"].values() for entry in entries for hook in entry["hooks"]]
    statuses = {hook["command"]: hook["statusMessage"] for hook in shipped if "statusMessage" in hook}
    expected = {f'bash "{sdlc}/{review}"': "Reviewing plan against quality gates"}
    assert statuses == expected, "only the plan review hook should show a status message"


# the deny rules install keeps last in permissions.deny, in order, so the carve-out follows the rules it narrows
ENV_DENY_RULES = ["Read(.env)", "Read(.env.*)", "Read(!.env.example)"]


def test_install_adds_the_env_deny_rules_after_existing_ones(tmp_path):
    """Install appends the .env deny rules to permissions.deny and keeps the rules already there."""
    (tmp_path / "settings.json").write_text(json.dumps({"permissions": {"deny": ["Bash(rm:*)"]}}))

    result = run_install(tmp_path, answer="install")

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    deny = json.loads((tmp_path / "settings.json").read_text())["permissions"]["deny"]
    assert deny == ["Bash(rm:*)", *ENV_DENY_RULES], "existing rules come first, then the .env rules in order"


def test_install_removes_a_deny_rule_it_no_longer_ships(tmp_path):
    """A deny rule the last install added but the config dropped is removed, and the user's own rules are kept."""
    (tmp_path / ".playbook_install_deny_rules").write_text(json.dumps(["Read(old)"]))
    (tmp_path / "settings.json").write_text(json.dumps({"permissions": {"deny": ["Bash(rm:*)", "Read(old)"]}}))

    result = run_install(tmp_path, answer="install")

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    deny = json.loads((tmp_path / "settings.json").read_text())["permissions"]["deny"]
    assert deny == ["Bash(rm:*)", *ENV_DENY_RULES], "the dropped rule should go and the user's rule stay"


def test_reinstalling_registers_each_hook_once(tmp_path):
    """A second install leaves exactly one of each hook, and makes no backup of settings.json."""
    run_install(tmp_path, answer="install")
    result = run_install(tmp_path, answer="install")
    assert result.returncode == 0, f"the second install should succeed:\n{result.stdout}{result.stderr}"
    assert len(plan_hook_commands(tmp_path)) == 1, "the plan hook should be registered once"
    assert len(stop_hook_commands(tmp_path)) == 1, "the stop hook should be registered once"
    deny = json.loads((tmp_path / "settings.json").read_text())["permissions"]["deny"]
    assert deny == ENV_DENY_RULES, "each .env deny rule should be added once"
    assert not (tmp_path / "backups").exists(), "an unchanged settings.json should not be backed up"


@pytest.mark.parametrize("settings", [{"hooks": {"PreToolUse": "not a list"}}, {"permissions": {"deny": "not a list"}}])
def test_unmergeable_settings_are_left_alone(tmp_path, settings):
    """A settings.json whose hooks.PreToolUse or permissions.deny isn't a list is kept, and the install succeeds."""
    original = json.dumps(settings)
    (tmp_path / "settings.json").write_text(original)

    result = run_install(tmp_path, answer="install")

    assert result.returncode == 0, f"install should still succeed:\n{result.stdout}{result.stderr}"
    assert (tmp_path / "settings.json").read_text() == original, "an unmergeable settings.json must be unchanged"
    assert "weren't added" in result.stdout, "the install should say the settings weren't added"


# an unrelated PreToolUse hook, which install must keep whatever it does to the plan sections hook
OTHER_HOOK = {"matcher": "Bash", "hooks": [{"type": "command", "command": "bash /my/own/hook.sh"}]}


def seed_settings(target, plan_hook_dir):
    """Write a settings.json holding the plan sections hook at its old flat path in plan_hook_dir, and OTHER_HOOK."""
    plan_hook = {"type": "command", "command": f'bash "{plan_hook_dir}/hooks/hook_enforcement_plan_sections.sh"'}
    settings = {"hooks": {"PreToolUse": [{"matcher": "ExitPlanMode", "hooks": [plan_hook]}, OTHER_HOOK]}}
    (target / "settings.json").write_text(json.dumps(settings))


def pre_tool_use(target):
    """Return the PreToolUse list in the target's settings.json."""
    return json.loads((target / "settings.json").read_text())["hooks"]["PreToolUse"]


def test_install_removes_the_plan_hook_when_it_isnt_shipped(tmp_path):
    """From a repo that doesn't ship the hook, install removes its entry, keeps other hooks and backs up settings."""
    repo = tmp_path / "repo"
    repo.mkdir()
    env = isolated_git_repo(repo)
    (repo / "src" / "claude").mkdir()
    (repo / "src" / "claude" / "CLAUDE.md").write_text("config\n")
    subprocess.run(["git", "add", "src/claude/CLAUDE.md"], cwd=repo, env=env, check=True)
    target = tmp_path / "config"
    target.mkdir()
    seed_settings(target, target)

    result = run_install(target, answer="install", cwd=repo)

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    assert plan_hook_commands(target) == [], "an unshipped hook should be removed"
    assert pre_tool_use(target) == [OTHER_HOOK], "an unrelated hook must be kept"
    assert list((target / "backups").glob("install_*/settings.json")), "the old settings.json should be backed up"


def test_install_moves_a_hook_registered_at_an_old_path(tmp_path):
    """A hook registered at its old flat path is replaced by its current path, keeping other hooks."""
    seed_settings(tmp_path, tmp_path)

    result = run_install(tmp_path, answer="install")

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    current = f'bash "{tmp_path}/hooks/ai_sdlc_workflow/hook_enforcement_plan_sections.sh"'
    assert plan_hook_commands(tmp_path) == [current], "only the current path should be registered"
    assert OTHER_HOOK in pre_tool_use(tmp_path), "an unrelated hook must be kept"


def project_install(tmp_path, **extra_env):
    """Install into a fresh repo folder with its own config directory, returning both and the result."""
    config, project = tmp_path / "config", tmp_path / "repo"
    config.mkdir(parents=True)
    project.mkdir(parents=True)
    result = run_install(config, answer="install", PROJECT=str(project), **extra_env)
    assert result.returncode == 0, f"a project install should succeed:\n{result.stdout}{result.stderr}"
    return config, project / ".claude"


@pytest.fixture(scope="module")
def default_project_install(tmp_path_factory):
    """Install once into a fresh repo folder, shared by the tests that only read a plain project install."""
    return project_install(tmp_path_factory.mktemp("default_project_install"), cwd=REPO_ROOT)


def test_project_install_writes_only_into_the_repo(default_project_install):
    """With PROJECT set, the config lands in the repo's .claude/ folder, and your config directory gets nothing."""
    config, target = default_project_install
    assert (target / "CLAUDE.md").is_file(), "CLAUDE.md should install into the repo's .claude/ folder"
    assert (target / "on_demand" / "01_standards" / "claude_config" / "guiding_principles.md").is_file(), (
        "on-demand files should too"
    )
    assert installed_files(config) == set(), "nothing but backups should land in your own config directory"


def test_project_install_points_rules_at_the_project_folder(default_project_install):
    """Every 'in your Claude config directory' pointer reads 'in this project's .claude/ folder' instead."""
    _, target = default_project_install
    texts = [path.read_text() for path in target.rglob("*.md")]
    assert not [text for text in texts if "in your Claude config directory" in text], "no pointer should name it"
    assert "in this project's `.claude/` folder" in (target / "CLAUDE.md").read_text(), "CLAUDE.md should name it"


def test_project_install_ships_the_plan_hook_and_the_done_checks_only_when_asked(tmp_path, default_project_install):
    """A project install always registers the plan hook, and the done checks and worktree hooks only with HOOKS=1."""
    plan = 'bash "$CLAUDE_PROJECT_DIR/.claude/hooks/ai_sdlc_workflow/hook_enforcement_plan_sections.sh"'
    _, target = default_project_install
    assert plan_hook_commands(target) == [plan], "the plan hook should be registered through CLAUDE_PROJECT_DIR"
    assert not (target / "hooks" / "ai_sdlc_workflow" / "hook_enforcement_done_checks.sh").exists(), (
        "no done checks hook by default"
    )
    assert not stop_hook_commands(target), "no done checks hook should be registered by default"
    assert not edit_hook_commands(target), "no worktree edits hook should be registered by default"

    _, target = project_install(tmp_path / "with", HOOKS="1")
    done = 'bash "$CLAUDE_PROJECT_DIR/.claude/hooks/ai_sdlc_workflow/hook_enforcement_done_checks.sh"'
    assert stop_hook_commands(target) == [done], "HOOKS=1 should register the done checks hook"
    edits = 'bash "$CLAUDE_PROJECT_DIR/.claude/hooks/git/hook_enforcement_worktree_edits.sh"'
    assert edit_hook_commands(target) == [edits], "HOOKS=1 should register the worktree edits hook"


def test_project_installed_worktree_hook_names_the_project_folder(tmp_path):
    """The project-installed worktree hook prints its rewritten pointer as text, not as a backticked command."""
    _, target = project_install(tmp_path, HOOKS="1")
    env = {**isolated_git_repo(target.parent), "TMPDIR": str(tmp_path / "state")}
    edit = {"file_path": str(target.parent / "app.py")}
    payload = json.dumps({"hook_event_name": "PreToolUse", "session_id": "s1", "tool_name": "Edit", "tool_input": edit})
    hook = target / "hooks" / "git" / "hook_enforcement_worktree_edits.sh"
    result = subprocess.run(["bash", str(hook)], input=payload, env=env, capture_output=True, text=True, check=False)
    assert "in this project's `.claude/` folder" in result.stderr, f"the pointer should print intact:\n{result.stderr}"


def test_project_install_backs_up_into_your_config_directory(tmp_path):
    """A file the project install overwrites is backed up in your config directory, never in the repo."""
    config, project = tmp_path / "config", tmp_path / "repo"
    (project / ".claude").mkdir(parents=True)
    config.mkdir()
    (project / ".claude" / "CLAUDE.md").write_text("the team's own notes\n")
    result = run_install(config, answer="install", PROJECT=str(project))
    assert result.returncode == 0, f"a project install should succeed:\n{result.stdout}{result.stderr}"
    backups = list((config / "backups").glob("project_repo_*/CLAUDE.md"))
    assert backups and backups[0].read_text() == "the team's own notes\n", "the old CLAUDE.md should be backed up"
    assert not (project / ".claude" / "backups").exists(), "no backup should be written inside the repo"


def test_uninstall_removes_the_install_and_restores_what_it_replaced(tmp_path):
    """Uninstall removes installed files, restores the pre-install CLAUDE.md and strips only the config's settings."""
    (tmp_path / "CLAUDE.md").write_text("my old config\n")
    (tmp_path / "memory").mkdir()
    (tmp_path / "memory" / "note.md").write_text("keep me\n")
    (tmp_path / "settings.json").write_text(json.dumps({"model": "opus", "permissions": {"deny": ["Bash(rm:*)"]}}))
    assert run_install(tmp_path, answer="install").returncode == 0, "the install should succeed"

    result = run_install(tmp_path, answer="uninstall", UNINSTALL="1")

    assert result.returncode == 0, f"uninstall should succeed:\n{result.stdout}{result.stderr}"
    assert installed_files(tmp_path) == {"CLAUDE.md", "memory/note.md", "settings.json"}, "only the user's files stay"
    assert (tmp_path / "CLAUDE.md").read_text() == "my old config\n", "the replaced CLAUDE.md should be restored"
    settings = json.loads((tmp_path / "settings.json").read_text())
    assert settings["model"] == "opus" and settings["permissions"]["deny"] == ["Bash(rm:*)"], "user settings stay"
    assert plan_hook_commands(tmp_path) == [] and stop_hook_commands(tmp_path) == [], "the hooks should be removed"


def commit_config(repo, env, files):
    """Write config files under src/claude/ in a test repo and commit them, as a playbook release would."""
    for path, text in files.items():
        (repo / "src" / "claude" / path).parent.mkdir(parents=True, exist_ok=True)
        (repo / "src" / "claude" / path).write_text(text)
    subprocess.run(["git", "add", "src/claude"], cwd=repo, env=env, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "release"], cwd=repo, env=env, check=True)


# an always-on rule and an on-demand one, which installs beside rules/, each with a pointer a project install rewrites
RULES = {
    "rules/always_on/rule.md": "rule {}: see it in your Claude config directory\n",
    "rules/on_demand/detail.md": "detail {}: see it in your Claude config directory\n",
}
INSTALLED = ["rules/always_on/rule.md", "on_demand/detail.md"]


def release(version):
    """Return the rule files as a given playbook release has them."""
    return {path: text.format(version) for path, text in RULES.items()}


def test_an_upgrade_backs_up_the_installs_own_copies_where_uninstall_wont_restore_them(tmp_path):
    """An upgrade backs up the previous install's copies, even edited ones, to an upgrade folder uninstall skips."""
    repo, config = tmp_path / "repo", tmp_path / "config"
    repo.mkdir()
    config.mkdir()
    env = isolated_git_repo(repo)
    commit_config(repo, env, release(1))
    assert run_install(config, answer="install", cwd=repo).returncode == 0, "the first install should work"
    (config / INSTALLED[0]).write_text("the user's edit of the installed rule\n")
    commit_config(repo, env, release(2))
    assert run_install(config, answer="install", cwd=repo).returncode == 0, "the upgrade should work"
    assert list((config / "backups").glob(f"install_upgrade_*/{INSTALLED[0]}")), "the edited copy goes to upgrade_"

    result = run_install(config, answer="uninstall", cwd=repo, UNINSTALL="1")

    assert result.returncode == 0, f"uninstall should succeed:\n{result.stdout}{result.stderr}"
    for installed in INSTALLED:
        assert not (config / installed).exists(), f"no copy of {installed} should be restored"


def test_uninstall_without_a_terminal_changes_nothing(tmp_path):
    """With no terminal attached, uninstall exits 1 and leaves the install in place."""
    assert run_install(tmp_path, answer="install").returncode == 0, "the install should succeed"
    before = installed_files(tmp_path)

    result = run_install(tmp_path, UNINSTALL="1")

    assert result.returncode == 1, f"uninstall should refuse without a terminal:\n{result.stdout}"
    assert installed_files(tmp_path) == before, "nothing should change without a terminal"


def test_uninstall_with_no_manifest_removes_nothing(tmp_path):
    """Without an install manifest, uninstall says there's nothing to remove and leaves files alone."""
    (tmp_path / "CLAUDE.md").write_text("my own config\n")

    result = run_install(tmp_path, answer="uninstall", UNINSTALL="1")

    assert result.returncode == 1, f"uninstall should stop:\n{result.stdout}"
    assert "nothing to uninstall" in result.stdout, "it should say there's nothing to uninstall"
    assert (tmp_path / "CLAUDE.md").read_text() == "my own config\n", "the user's file must be untouched"


def test_yes_installs_without_a_terminal(tmp_path, monkeypatch):
    """Outside Claude Code, YES=1 installs with no terminal and no typed answer."""
    monkeypatch.delenv("CLAUDECODE", raising=False)

    result = run_install(tmp_path, YES="1")

    assert result.returncode == 0, f"YES=1 should install without a terminal:\n{result.stdout}{result.stderr}"
    assert (tmp_path / "CLAUDE.md").is_file(), "the config should be installed"


def test_yes_is_refused_inside_claude_code(tmp_path):
    """With CLAUDECODE set, as in Claude's Bash tool, YES=1 exits 1 and writes nothing."""
    result = run_install(tmp_path, YES="1", CLAUDECODE="1")

    assert result.returncode == 1, f"YES=1 should be refused inside Claude Code:\n{result.stdout}"
    assert "can't be used from Claude Code" in result.stdout, "the refusal should say why"
    assert not any(tmp_path.iterdir()), "nothing should be written"


def test_authoring_templates_and_readmes_never_install(default_install):
    """Authoring templates and READMEs, which explain folders to people browsing, stay in the repo, while templates
    that rules point to still install."""
    installed = installed_files(default_install)
    assert not {path for path in installed if path in AUTHORING_TEMPLATES or path.startswith("_templates/skills/")}
    assert "_templates/preferences/TODO.md.template" in installed, "the TODO template a preference points to installs"
    for readme in ("README.md", "hooks/README.md", "rules/always_on/README.md"):
        assert (SOURCE / readme).is_file(), f"the repo should have {readme}"
    readmes = [path for path in installed if path.endswith("README.md")]
    assert readmes == [], f"no README should install: {readmes}"


# files an install writes for its own records, beside the config it copies
BOOKKEEPING = {".playbook_install_manifest", ".playbook_install_deny_rules", "settings.json"}


def preference_files(target):
    """Return the installed files that are preferences."""
    return {path for path in installed_files(target) if is_preference(path)}


def test_a_default_install_includes_every_preference(tmp_path):
    """A plain install, with no PREFERENCES set, installs every preference along with everything else."""
    config = tmp_path / "config"

    result = run_install(config, answer="install", cwd=REPO_ROOT)

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    expected = {installed_path(path) for path in tracked_config_files(include_preferences=True)}
    assert installed_files(config) - BOOKKEEPING == expected, "a default install should install everything"


def test_zero_removes_preferences_until_a_plain_reinstall(tmp_path):
    """PREFERENCES=0 removes the preferences and their empty folders, and a plain reinstall brings them back."""
    config = tmp_path / "config"
    assert run_install(config, answer="install").returncode == 0, "the default install should work"

    result = run_install(config, answer="install", PREFERENCES="0")

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    assert preference_files(config) == set(), "PREFERENCES=0 should remove every preference"
    assert not (config / "rules" / "always_on" / "02_preferences").exists(), "the empty folder should be removed"
    assert "rerun with a plain make install" in result.stdout, "it should say how to keep them"
    assert run_install(config, answer="install").returncode == 0, "the plain reinstall should work"
    assert (config / OUTPUT_FORMAT).exists(), "a plain reinstall should bring the preferences back"


def test_a_project_never_gets_preferences(tmp_path):
    """A project install leaves preferences out."""
    config, project = tmp_path / "config", tmp_path / "repo"
    project.mkdir()

    result = run_install(config, answer="install", cwd=REPO_ROOT, PROJECT=str(project))

    assert result.returncode == 0, f"a project install should succeed:\n{result.stdout}{result.stderr}"
    assert preference_files(project / ".claude") == set(), "a project install should have no preferences"


@pytest.mark.parametrize("value", ["1", "yes"])
def test_a_preferences_value_other_than_0_is_refused(tmp_path, value):
    """PREFERENCES can only be 0, since preferences install by default, and a refused install changes nothing."""
    refused = run_install(tmp_path, answer="install", PREFERENCES=value)

    assert refused.returncode == 1, f"PREFERENCES={value} should be refused:\n{refused.stdout}"
    assert "can only be 0" in refused.stdout + refused.stderr, "it should say which value works"
    assert not (tmp_path / "CLAUDE.md").exists(), "a refused install should change nothing"


def test_opting_in_and_out_then_uninstalling_leaves_only_the_users_files(tmp_path):
    """Install with and without preferences, then uninstall, and only the user's own files remain."""
    config = tmp_path / "config"
    config.mkdir()
    (config / "CLAUDE.md").write_text("my old config\n")
    for flag in ("", "0", "", "0"):
        result = run_install(config, answer="install", **({"PREFERENCES": flag} if flag else {}))
        assert result.returncode == 0, f"install with PREFERENCES={flag!r} should work:\n{result.stdout}"

    result = run_install(config, answer="uninstall", UNINSTALL="1")

    assert result.returncode == 0, f"uninstall should succeed:\n{result.stdout}{result.stderr}"
    assert installed_files(config) - {"settings.json"} == {"CLAUDE.md"}, "only the user's own files should remain"
    assert (config / "CLAUDE.md").read_text() == "my old config\n", "the user's CLAUDE.md should be restored"


def seed_plans(tmp_path):
    """Save a finished plan in active/ and an old scratch plan, returning (home, config, plan, scratch plan)."""
    home, config = tmp_path / "home", tmp_path / "config"
    plan = config / "_plans" / "active" / "x"
    plan.mkdir(parents=True)
    (plan / "plan.md").write_text("# Plan\n\n**Plan status:** ✅ Done · updated 2026-01-01\n", encoding="utf-8")
    scratch = config / "plans" / "x.md"
    scratch.parent.mkdir(parents=True)
    scratch.write_text("scratch\n")
    os.utime(scratch, (0, 0))
    return home, config, plan, scratch


def test_a_global_install_files_plans(tmp_path):
    """A plain install says it files plans, then files saved plans and archives old scratch plans."""
    home, config, plan, scratch = seed_plans(tmp_path)
    result = run_install(config, answer="install", HOME=str(home))
    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    assert "files saved plans" in result.stdout, "the confirmation should mention filing"
    assert not plan.exists() and (config / "_plans" / "done" / "x" / "plan.md").is_file()
    assert not scratch.exists() and (config / "plans" / "archive" / "x.md").is_file()


@pytest.mark.parametrize("skip", ["PROJECT", "PREFERENCES", "UNINSTALL", "cancelled"])
def test_other_runs_leave_plans_alone(tmp_path, skip):
    """A project install, PREFERENCES=0, an uninstall and a cancelled install file nothing."""
    home, config, plan, scratch = seed_plans(tmp_path)
    (tmp_path / "project").mkdir()
    answer, code, extra_env = {
        "PROJECT": ("install", 0, {"PROJECT": str(tmp_path / "project")}),
        "PREFERENCES": ("install", 0, {"PREFERENCES": "0"}),
        "UNINSTALL": ("uninstall", 0, {"UNINSTALL": "1"}),
        "cancelled": ("no", 1, {}),
    }[skip]
    if skip == "UNINSTALL":
        # a manifest and one installed file give the uninstall something to remove
        (config / "CLAUDE.md").write_text("installed\n")
        (config / ".playbook_install_manifest").write_text("CLAUDE.md\n")
    result = run_install(config, answer=answer, HOME=str(home), **extra_env)
    assert result.returncode == code, f"unexpected exit:\n{result.stdout}{result.stderr}"
    assert plan.exists() and scratch.exists(), "no plan should move"
    assert ("files saved plans" in result.stdout) is (skip == "cancelled"), "only a filing install should mention it"


@pytest.mark.parametrize("exit_code", [1, 127])
def test_a_filing_failure_only_warns(tmp_path, exit_code):
    """A script error, or the 127 a shell gives for a missing python3, warns, and the install still succeeds."""
    home, config, plan, _ = seed_plans(tmp_path)
    python = tmp_path / "bin" / "python3"
    python.parent.mkdir()
    python.write_text(f"#!/bin/sh\nexit {exit_code}\n")
    python.chmod(0o755)
    path = f"{python.parent}{os.pathsep}{os.environ['PATH']}"
    result = run_install(config, answer="install", HOME=str(home), PATH=path)
    assert result.returncode == 0, f"install should still succeed:\n{result.stdout}{result.stderr}"
    assert "plans weren't filed" in result.stdout, "the failure should be reported"
    assert (config / "CLAUDE.md").is_file() and plan.exists()
