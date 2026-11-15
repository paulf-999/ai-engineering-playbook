"""Tests for the install script, which copies src/claude/ into a Claude config directory after a typed 'install'."""

import json
import os
import pty
import subprocess

import pytest
from _git_repo import isolated_git_repo
from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "claude_install_config.sh"
SOURCE = REPO_ROOT / "src" / "claude"
# ignore the user's git config, so their settings can't change which files git lists
GIT_ENV = {"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}


def run_install(target, answer=None, cwd=REPO_ROOT, **extra_env):
    """Run the script from cwd against a target, typing answer at a pseudo-terminal, or with no terminal if None."""
    env = {**os.environ, **GIT_ENV, "CLAUDE_CONFIG_DIR": str(target), **extra_env}
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
            timeout=30,
        )
    finally:
        os.close(terminal)
        os.close(controller)


def tracked_config_files():
    """Return the files git tracks under src/claude/, as paths relative to it."""
    command = ["git", "ls-files", "--", "src/claude"]
    output = subprocess.run(
        command, cwd=REPO_ROOT, env={**os.environ, **GIT_ENV}, capture_output=True, text=True, check=True
    )
    return {path.removeprefix("src/claude/") for path in output.stdout.splitlines()}


def installed_path(source):
    """Return where a src/claude/ file should install, with on-demand files moved out of rules/."""
    return source.removeprefix("rules/") if source.startswith("rules/on_demand/") else source


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


def test_install_copies_every_tracked_file(tmp_path):
    """Typing 'install' copies each tracked file in src/claude/ to the same relative path in the target."""
    result = run_install(tmp_path, answer="install")
    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    sources = tracked_config_files()
    assert sources, "git should list at least one file under src/claude/"
    installed = {installed_path(path): path for path in sources}
    assert set(installed) <= installed_files(tmp_path), f"missing: {set(installed) - installed_files(tmp_path)}"
    for target, source in installed.items():
        assert (tmp_path / target).read_bytes() == (SOURCE / source).read_bytes(), f"{target} should match {source}"


def test_on_demand_files_install_beside_rules(tmp_path):
    """Files in src/claude/rules/on_demand/ install to on_demand/, and none of them land in rules/."""
    result = run_install(tmp_path, answer="install")
    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    assert (tmp_path / "on_demand" / "claude_config" / "guiding_principles.md").is_file(), (
        "on-demand files should sit beside rules/"
    )
    assert not (tmp_path / "rules" / "on_demand").exists(), "no on-demand file should install under rules/"


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


def test_reinstalling_unchanged_files_makes_no_backup(tmp_path):
    """A second install over identical files copies and backs up nothing."""
    first = run_install(tmp_path, answer="install")
    assert first.returncode == 0, f"the first install should succeed:\n{first.stdout}{first.stderr}"
    result = run_install(tmp_path, answer="install")
    assert result.returncode == 0, f"the second install should succeed:\n{result.stdout}{result.stderr}"
    assert not (tmp_path / "backups").exists(), "no backup folder should be made when nothing is overwritten"


def test_files_the_repo_removed_are_backed_up_then_removed(tmp_path):
    """A path in the last install's manifest that the repo no longer has is backed up, removed and dropped."""
    (tmp_path / "rules").mkdir()
    (tmp_path / "rules" / "old.md").write_text("old rule\n")
    (tmp_path / ".playbook_install_manifest").write_text("rules/old.md\n")

    result = run_install(tmp_path, answer="install")

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    assert not (tmp_path / "rules" / "old.md").exists(), "a file the repo removed should be removed"
    backups = list((tmp_path / "backups").glob("install_*/rules/old.md"))
    assert len(backups) == 1 and backups[0].read_text() == "old rule\n", "the removed file should be backed up first"
    manifest = (tmp_path / ".playbook_install_manifest").read_text().splitlines()
    assert set(manifest) == {installed_path(path) for path in tracked_config_files()}, (
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


def plan_hook_commands(target):
    """Return the PreToolUse hook commands in the target's settings.json that run the plan sections hook."""
    settings = json.loads((target / "settings.json").read_text())
    return [
        hook["command"]
        for entry in settings.get("hooks", {}).get("PreToolUse", [])
        if entry.get("matcher") == "ExitPlanMode"
        for hook in entry.get("hooks", [])
        if "hook_enforcement_plan_sections.sh" in hook.get("command", "")
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
    """Install adds the ExitPlanMode and Stop hooks by absolute path, keeps other settings and backs up the old file."""
    (tmp_path / "settings.json").write_text(json.dumps({"model": "opus", "permissions": {"allow": ["Bash(ls)"]}}))

    result = run_install(tmp_path, answer="install")

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    settings = json.loads((tmp_path / "settings.json").read_text())
    assert settings["model"] == "opus" and settings["permissions"]["allow"] == ["Bash(ls)"], "settings must be kept"
    assert plan_hook_commands(tmp_path) == [f'bash "{tmp_path}/hooks/hook_enforcement_plan_sections.sh"']
    assert stop_hook_commands(tmp_path) == [f'bash "{tmp_path}/hooks/hook_enforcement_done_checks.sh"']
    assert list((tmp_path / "backups").glob("install_*/settings.json")), "the old settings.json should be backed up"


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
    """Write a settings.json holding the plan sections hook installed under plan_hook_dir, plus OTHER_HOOK."""
    plan_hook = {"type": "command", "command": f'bash "{plan_hook_dir}/hooks/hook_enforcement_plan_sections.sh"'}
    settings = {"hooks": {"PreToolUse": [{"matcher": "ExitPlanMode", "hooks": [plan_hook]}, OTHER_HOOK]}}
    (target / "settings.json").write_text(json.dumps(settings))


def pre_tool_use(target):
    """Return the PreToolUse list in the target's settings.json."""
    return json.loads((target / "settings.json").read_text())["hooks"]["PreToolUse"]


def test_install_replaces_the_plan_hook_from_an_old_path(tmp_path):
    """A plan sections hook registered under another path is replaced by the current one, and other hooks are kept."""
    seed_settings(tmp_path, "/old/path")

    result = run_install(tmp_path, answer="install")

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    assert plan_hook_commands(tmp_path) == [f'bash "{tmp_path}/hooks/hook_enforcement_plan_sections.sh"']
    assert OTHER_HOOK in pre_tool_use(tmp_path), "an unrelated hook must be kept"


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


def project_install(tmp_path, **extra_env):
    """Install into a fresh repo folder with its own config directory, returning both and the result."""
    config, project = tmp_path / "config", tmp_path / "repo"
    config.mkdir(parents=True)
    project.mkdir(parents=True)
    result = run_install(config, answer="install", PROJECT=str(project), **extra_env)
    assert result.returncode == 0, f"a project install should succeed:\n{result.stdout}{result.stderr}"
    return config, project / ".claude"


def test_project_install_writes_only_into_the_repo(tmp_path):
    """With PROJECT set, the config lands in the repo's .claude/ folder, and your config directory gets nothing."""
    config, target = project_install(tmp_path)
    assert (target / "CLAUDE.md").is_file(), "CLAUDE.md should install into the repo's .claude/ folder"
    assert (target / "on_demand" / "claude_config" / "guiding_principles.md").is_file(), "on-demand files should too"
    assert installed_files(config) == set(), "nothing but backups should land in your own config directory"


def test_project_install_points_rules_at_the_project_folder(tmp_path):
    """Every 'in your Claude config directory' pointer reads 'in this project's .claude/ folder' instead."""
    _, target = project_install(tmp_path)
    texts = [path.read_text() for path in target.rglob("*.md")]
    assert not [text for text in texts if "in your Claude config directory" in text], "no pointer should name it"
    assert "in this project's `.claude/` folder" in (target / "CLAUDE.md").read_text(), "CLAUDE.md should name it"


def test_project_install_ships_the_plan_hook_and_the_done_checks_only_when_asked(tmp_path):
    """A project install always registers the plan hook, and the done checks hook only with HOOKS=1."""
    plan = 'bash "$CLAUDE_PROJECT_DIR/.claude/hooks/hook_enforcement_plan_sections.sh"'
    _, target = project_install(tmp_path / "without")
    assert plan_hook_commands(target) == [plan], "the plan hook should be registered through CLAUDE_PROJECT_DIR"
    assert not (target / "hooks" / "hook_enforcement_done_checks.sh").exists(), "no done checks hook by default"
    assert not stop_hook_commands(target), "no done checks hook should be registered by default"

    _, target = project_install(tmp_path / "with", HOOKS="1")
    done = 'bash "$CLAUDE_PROJECT_DIR/.claude/hooks/hook_enforcement_done_checks.sh"'
    assert stop_hook_commands(target) == [done], "HOOKS=1 should register the done checks hook"


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
