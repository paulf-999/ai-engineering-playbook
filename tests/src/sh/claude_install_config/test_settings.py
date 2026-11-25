"""Tests for the install library that merges the config's hooks and deny rules into settings.json."""

import json
import shlex
import subprocess

import pytest
from _paths import SCRIPTS_DIR

LIBRARIES = SCRIPTS_DIR / "claude_install_config"
PATH = "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin"


def run_library(target, command, settings=""):
    """Source the library in a strict bash, run the command on settings held as SETTINGS_JSON, and return the result."""
    sources = [SCRIPTS_DIR / "shell_utils.sh", LIBRARIES / "_settings.sh"]
    script = "set -euo pipefail\n" + "".join(f'source "{path}"\n' for path in sources)
    script += f'SETTINGS_JSON="${{GIVEN}}"\n{command}'
    env = {
        "PATH": PATH,
        "GIVEN": settings if isinstance(settings, str) else json.dumps(settings),
        "PROJECT": "",
        "TARGET_DIR": str(target),
        "SETTINGS": str(target / "settings.json"),
        "DENY_MANIFEST": str(target / "deny"),
    }
    return subprocess.run(["bash", "-c", script], env=env, capture_output=True, text=True, check=False)


def merged(target, command, settings):
    """Run a merge on settings and return what it makes of them."""
    result = run_library(target, f'{command}\nprintf "%s" "${{SETTINGS_JSON}}"', settings)
    assert result.returncode == 0, result.stdout + result.stderr
    return json.loads(result.stdout)


def command_hook(command):
    """Return a hook that runs a command."""
    return {"type": "command", "command": command}


def rendered(hooks=None, deny=()):
    """Return a shell line that sets RENDERED_SETTINGS to the hooks and deny rules."""
    return f"RENDERED_SETTINGS={shlex.quote(json.dumps({'hooks': hooks or {}, 'permissions': {'deny': list(deny)}}))}\n"


def test_merge_hooks_replaces_its_own_copy_and_keeps_hooks_beside_it(tmp_path):
    """A hook at an old path goes, while the user's hook in the same entry stays and the current one is added last."""
    mine = command_hook("bash /mine.sh")
    old = {"matcher": "Bash", "hooks": [command_hook('bash "/old/hook_x.sh"'), mine]}
    new = {"matcher": "Bash", "hooks": [{**command_hook('bash "/new/hook_x.sh"'), "statusMessage": "Checking"}]}
    command = rendered({"PreToolUse": [new]}) + "merge_hooks"
    settings = merged(tmp_path, command, {"hooks": {"PreToolUse": [old]}})
    assert settings["hooks"]["PreToolUse"] == [{"matcher": "Bash", "hooks": [mine]}, new]


@pytest.mark.parametrize("hooks_dir", ["{target}/hooks", "$CLAUDE_PROJECT_DIR/.claude/hooks"])
def test_strip_dead_hooks_removes_only_hooks_whose_file_is_gone(tmp_path, hooks_dir):
    """An entry for a missing hook_*.sh under hooks/ goes, and one whose file exists or that sits elsewhere stays."""
    target = tmp_path / "configé"
    (target / "hooks" / "git").mkdir(parents=True)
    (target / "hooks" / "git" / "hook_live.sh").write_text("live\n")
    hooks_dir = hooks_dir.format(target=target)
    kept = [
        command_hook(f'bash "{hooks_dir}/git/hook_live.sh"'),
        # not a name the config uses, and not in this hooks folder
        command_hook(f'bash "{hooks_dir}/git/mine.sh"'),
        command_hook('bash "/elsewhere/hooks/git/hook_gone.sh"'),
        {"type": "prompt", "prompt": "no command"},
    ]
    dead = [command_hook(f'bash "{hooks_dir}/git/hook_gone.sh"'), command_hook(f"bash {hooks_dir}/hook_old.sh --flag")]
    given = {"hooks": {"Stop": [{"hooks": [dead[0], *kept]}, {"hooks": [dead[1]]}], "SessionStart": "not a list"}}
    settings = merged(target, f"HOOKS_DIR={shlex.quote(hooks_dir)}\nstrip_dead_hooks", given)
    assert settings["hooks"] == {"Stop": [{"hooks": kept}], "SessionStart": "not a list"}


def test_merge_deny_rules_moves_its_own_rules_last_and_drops_old_ones(tmp_path):
    """The config's rules end up last, in order, whatever was there, and a dropped rule goes."""
    (tmp_path / "deny").write_text('["Read(dropped)"]')
    deny = ["Read(b)", "Read(mine)", "Read(dropped)", "Read(a)"]
    command = rendered(deny=["Read(a)", "Read(b)"]) + "merge_deny_rules"
    settings = merged(tmp_path, command, {"permissions": {"deny": deny}})
    assert settings["permissions"]["deny"] == ["Read(mine)", "Read(a)", "Read(b)"]


def test_merge_deny_rules_treats_an_unreadable_record_as_empty(tmp_path):
    """A corrupt record of the last install's deny rules doesn't stop the current ones being added."""
    (tmp_path / "deny").write_text("{not json")
    settings = merged(tmp_path, rendered(deny=["Read(a)"]) + "merge_deny_rules", {})
    assert settings["permissions"]["deny"] == ["Read(a)"]


def test_write_settings_replaces_a_read_only_file_and_leaves_no_temporary_one(tmp_path):
    """A read-only settings.json is replaced and stays read-only, with no temporary file left behind."""
    path = tmp_path / "settings.json"
    path.write_text("{}")
    path.chmod(0o444)
    result = run_library(tmp_path, "write_settings", '{"model": "opus"}')
    assert result.returncode == 0, result.stderr
    assert path.read_text() == '{"model": "opus"}\n' and path.stat().st_mode & 0o777 == 0o444
    assert list(tmp_path.iterdir()) == [path], "no temporary file should stay"
