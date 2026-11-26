"""Tests for the claude-kaizen plugin: its copies match the repo's, its manifests agree, and its setup hook is quiet."""

import json
import os
import shutil
import subprocess

import pytest
import yaml
from _paths import REPO_ROOT

PLUGIN = REPO_ROOT / "plugins" / "claude-kaizen"
SKILL = REPO_ROOT / "src" / "claude" / "skills" / "_claude_skills" / "claude-kaizen"
HOOK = PLUGIN / "hooks" / "hook_setup_kaizen_venv.sh"
# A plugin can use only files inside its own folder, so it ships copies, which must match the repo's
COPIES = {
    "skills/claude-kaizen/SKILL.md": SKILL / "SKILL.md",
    "skills/claude-kaizen/reference/_implementation.md": SKILL / "reference" / "_implementation.md",
    "skills/claude-kaizen/reference/_draft.md": SKILL / "reference" / "_draft.md",
    "scripts/claude_run_rule_evals.py": REPO_ROOT / "src" / "py" / "claude_run_rule_evals.py",
    "scripts/claude_evals_common.py": REPO_ROOT / "src" / "py" / "claude_evals_common.py",
}


@pytest.mark.parametrize("copy", COPIES)
def test_plugin_copies_match_the_repo(copy):
    """Each file the plugin ships is identical to the repo's, so both installs behave the same."""
    assert (PLUGIN / copy).read_text() == COPIES[copy].read_text(), f"run: cp {COPIES[copy]} {PLUGIN / copy}"


def test_manifests_agree_with_the_skill():
    """The marketplace lists the plugin at its folder, and the plugin's version follows the skill contract's."""
    marketplace = json.loads((REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text())
    manifest = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text())
    contract = yaml.safe_load((SKILL / "skill.contract.yaml").read_text())
    [entry] = [plugin for plugin in marketplace["plugins"] if plugin["name"] == "claude-kaizen"]
    assert (REPO_ROOT / entry["source"]).resolve() == PLUGIN
    assert manifest["name"] == entry["name"]
    assert manifest["version"] == contract["version"], "bump plugin.json with the skill contract, or users won't update"


def make_python(stub_dir, log):
    """Write a python3 stub that fakes venv creation and pip, logging each call to log."""
    stub_dir.mkdir()
    # python3 -m venv <dir> makes a venv python that only logs, so pip never reaches the network
    script = f"""#!/bin/bash
echo "python3 $*" >> "{log}"
mkdir -p "$3/bin"
printf '#!/bin/bash\\necho "venv python $*" >> "{log}"\\n' > "$3/bin/python"
chmod +x "$3/bin/python"
"""
    (stub_dir / "python3").write_text(script)
    (stub_dir / "python3").chmod(0o755)


def run_hook(tmp_path, path):
    """Run the setup hook as Claude Code would, returning its stdout."""
    env = {
        **os.environ,
        "PATH": path,
        "CLAUDE_PLUGIN_ROOT": str(tmp_path / "root"),
        "CLAUDE_PLUGIN_DATA": str(tmp_path / "data"),
    }
    return subprocess.run(["/bin/bash", str(HOOK)], capture_output=True, text=True, check=True, env=env).stdout


def test_setup_hook_builds_once_and_rebuilds_on_new_requirements(tmp_path):
    """The hook builds the virtualenv on the first session, skips it after, and rebuilds when requirements change."""
    (tmp_path / "root").mkdir()
    (tmp_path / "root" / "requirements.txt").write_text("pyyaml==1\n")
    log = tmp_path / "calls.log"
    make_python(tmp_path / "bin", log)
    path = f"{tmp_path / 'bin'}:/usr/bin:/bin"
    assert run_hook(tmp_path, path) == "", "Claude Code adds the hook's stdout to the session"
    assert log.read_text().count("-m venv") == 1
    assert "pip install" in log.read_text()
    run_hook(tmp_path, path)
    assert log.read_text().count("-m venv") == 1, "a second session shouldn't rebuild"
    (tmp_path / "root" / "requirements.txt").write_text("pyyaml==2\n")
    run_hook(tmp_path, path)
    assert log.read_text().count("-m venv") == 2, "new requirements should rebuild"


def test_setup_hook_is_silent_without_python(tmp_path):
    """With no python3 on PATH, the hook exits cleanly with no output, and builds nothing."""
    (tmp_path / "root").mkdir()
    (tmp_path / "root" / "requirements.txt").write_text("pyyaml==1\n")
    tools = tmp_path / "tools"
    tools.mkdir()
    for tool in ("cmp", "mkdir", "cp"):
        (tools / tool).symlink_to(shutil.which(tool))
    assert run_hook(tmp_path, str(tools)) == ""
    assert not (tmp_path / "data").exists()
