# version: 1.1.6
# created: 2026-11-04
# updated: 2026-11-10
"""Tests for the install script, which copies src/claude/ into a Claude config directory after a typed 'install'."""

import json
import os
import pty
import subprocess

from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "claude_install_config.sh"
SOURCE = REPO_ROOT / "src" / "claude"
# ignore the user's git config, so their settings can't change which files git lists
GIT_ENV = {"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}


def run_install(target, answer=None):
    """Run the script against a test target, typing answer at a pseudo-terminal, or with no terminal if it's None."""
    env = {**os.environ, **GIT_ENV, "CLAUDE_CONFIG_DIR": str(target)}
    if answer is None:
        return subprocess.run(
            [str(SCRIPT)], cwd=REPO_ROOT, env=env, stdin=subprocess.DEVNULL, capture_output=True, text=True, check=False
        )
    # a pseudo-terminal makes [[ -t 0 ]] true, as it is when a person runs make install
    controller, terminal = pty.openpty()
    try:
        os.write(controller, f"{answer}\n".encode())
        return subprocess.run(
            [str(SCRIPT)],
            cwd=REPO_ROOT,
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
    return source.removeprefix("rules/") if source.startswith("rules/_rules_on_demand/") else source


def installed_files(target):
    """Return every file under the target, as paths relative to it, ignoring backups."""
    return {
        str(path.relative_to(target)) for path in target.rglob("*") if path.is_file() and "backups" not in path.parts
    }


# MoSCoW: Must — Claude's Bash tool has no terminal, so it must never be able to install
def test_without_a_terminal_nothing_is_installed(tmp_path):
    """With no terminal attached, the script exits 1, says to run it yourself and writes nothing."""
    result = run_install(tmp_path)
    assert result.returncode == 1, f"install should refuse without a terminal:\n{result.stdout}"
    assert "from your own terminal" in result.stdout, "the refusal should say how to run it"
    assert not any(tmp_path.iterdir()), "nothing should be written without a terminal"


# MoSCoW: Must — anything but the typed word cancels
def test_a_wrong_answer_cancels(tmp_path):
    """Typing anything other than 'install' cancels with exit 1 and writes nothing."""
    result = run_install(tmp_path, answer="yes")
    assert result.returncode == 1, f"a wrong answer should cancel:\n{result.stdout}"
    assert "nothing changed" in result.stdout, "the cancellation should be reported"
    assert not any(tmp_path.iterdir()), "nothing should be written after cancelling"


# MoSCoW: Must — install mirrors src/claude/ into the target, byte for byte
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


# MoSCoW: Must — on-demand files must never install under rules/, where Claude Code would load them every session
def test_on_demand_files_install_beside_rules(tmp_path):
    """Files in src/claude/rules/_rules_on_demand/ install to _rules_on_demand/, and none of them land in rules/."""
    result = run_install(tmp_path, answer="install")
    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    assert (tmp_path / "_rules_on_demand" / "claude_config" / "guiding_principles.md").is_file(), (
        "on-demand files should sit beside rules/"
    )
    assert not (tmp_path / "rules" / "_rules_on_demand").exists(), "no on-demand file should install under rules/"


# MoSCoW: Must — install never loses what's already in your config
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


# MoSCoW: Should — rerunning an install with nothing changed backs nothing up
def test_reinstalling_unchanged_files_makes_no_backup(tmp_path):
    """A second install over identical files copies and backs up nothing."""
    first = run_install(tmp_path, answer="install")
    assert first.returncode == 0, f"the first install should succeed:\n{first.stdout}{first.stderr}"
    result = run_install(tmp_path, answer="install")
    assert result.returncode == 0, f"the second install should succeed:\n{result.stdout}{result.stderr}"
    assert not (tmp_path / "backups").exists(), "no backup folder should be made when nothing is overwritten"


# MoSCoW: Must — a file an earlier install added, and the repo has since removed, must not linger
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


# MoSCoW: Must — a tampered manifest must never remove a file outside the config directory
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


# MoSCoW: Must — a hook does nothing until settings.json lists it, so install must register it
def test_install_registers_the_plan_hook_and_keeps_existing_settings(tmp_path):
    """Install adds the ExitPlanMode hook by its absolute path, keeps other settings and backs up the old file."""
    (tmp_path / "settings.json").write_text(json.dumps({"model": "opus", "permissions": {"allow": ["Bash(ls)"]}}))

    result = run_install(tmp_path, answer="install")

    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    settings = json.loads((tmp_path / "settings.json").read_text())
    assert settings["model"] == "opus" and settings["permissions"] == {"allow": ["Bash(ls)"]}, "settings must be kept"
    assert plan_hook_commands(tmp_path) == [f'bash "{tmp_path}/hooks/hook_enforcement_plan_sections.sh"']
    assert list((tmp_path / "backups").glob("install_*/settings.json")), "the old settings.json should be backed up"


# MoSCoW: Should — rerunning install must not stack duplicate hooks
def test_reinstalling_registers_the_plan_hook_once(tmp_path):
    """A second install leaves exactly one plan sections hook, and makes no backup of settings.json."""
    run_install(tmp_path, answer="install")
    result = run_install(tmp_path, answer="install")
    assert result.returncode == 0, f"the second install should succeed:\n{result.stdout}{result.stderr}"
    assert len(plan_hook_commands(tmp_path)) == 1, "the hook should be registered once"
    assert not (tmp_path / "backups").exists(), "an unchanged settings.json should not be backed up"


# MoSCoW: Should — a settings.json the merge can't safely change must be left as it was
def test_unmergeable_settings_are_left_alone(tmp_path):
    """A settings.json whose hooks.PreToolUse isn't a list is kept unchanged, and the install still succeeds."""
    original = json.dumps({"hooks": {"PreToolUse": "not a list"}})
    (tmp_path / "settings.json").write_text(original)

    result = run_install(tmp_path, answer="install")

    assert result.returncode == 0, f"install should still succeed:\n{result.stdout}{result.stderr}"
    assert (tmp_path / "settings.json").read_text() == original, "an unmergeable settings.json must be unchanged"
    assert "wasn't added" in result.stdout, "the install should say the hook wasn't added"
