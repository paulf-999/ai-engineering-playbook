# version: 1.1.0
# created: 2026-11-04
# updated: 2026-11-04
"""Tests for the install script, which copies src/claude/ into a Claude config directory after a typed 'install'."""

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
    return source.removeprefix("rules/") if source.startswith("rules/_rules_lazy_load/") else source


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
    """Files in src/claude/rules/_rules_lazy_load/ install to _rules_lazy_load/, and none of them land in rules/."""
    result = run_install(tmp_path, answer="install")
    assert result.returncode == 0, f"install should succeed:\n{result.stdout}{result.stderr}"
    assert (tmp_path / "_rules_lazy_load" / "guiding_principles.md").is_file(), (
        "on-demand files should sit beside rules/"
    )
    assert not (tmp_path / "rules" / "_rules_lazy_load").exists(), "no on-demand file should install under rules/"


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
