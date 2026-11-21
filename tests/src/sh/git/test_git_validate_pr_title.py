"""Tests for the PR title check, with a fake npx standing in for commitlint so no network is needed."""

import os
import re
import subprocess

from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "git" / "git_validate_pr_title.sh"
CONFIG = (REPO_ROOT / ".pre-commit-config.yaml").read_text()

# Records its arguments and stdin, then fails when the title doesn't start with a type, as commitlint would
FAKE_NPX = """#!/bin/bash
echo "$@" > "${NPX_LOG}"
title="$(cat)"
echo "${title}" >> "${NPX_LOG}"
[[ "${title}" =~ ^[a-z]+(\\(.+\\))?:\\  ]]
"""


def run_check(tmp_path, title, config=CONFIG):
    """Run the script in a folder holding the given hook config, and return the result and the fake npx's log."""
    (tmp_path / ".pre-commit-config.yaml").write_text(config)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (bin_dir / "npx").write_text(FAKE_NPX)
    (bin_dir / "npx").chmod(0o755)
    log = tmp_path / "npx.log"
    env = {**os.environ, "PATH": f"{bin_dir}:{os.environ['PATH']}", "NPX_LOG": str(log)}
    result = subprocess.run([str(SCRIPT), title], cwd=tmp_path, env=env, capture_output=True, text=True, check=False)
    return result, log.read_text() if log.exists() else ""


def test_passes_the_title_to_the_pinned_commitlint(tmp_path):
    """A valid title passes, and commitlint runs at the version the hook config pins, reading the title on stdin."""
    result, log = run_check(tmp_path, "feat(rules): add a thing")
    version = re.search(r"@commitlint/config-conventional@([0-9.]+)", CONFIG).group(1)
    assert result.returncode == 0, result.stdout + result.stderr
    assert f"@commitlint/cli@{version}" in log, log
    assert log.splitlines()[-1] == "feat(rules): add a thing"


def test_fails_when_commitlint_rejects_the_title(tmp_path):
    """A title commitlint rejects exits non-zero."""
    result, _ = run_check(tmp_path, "Add a thing")
    assert result.returncode != 0


def test_fails_without_a_pinned_version(tmp_path):
    """A hook config with no commitlint pin fails before commitlint runs."""
    result, log = run_check(tmp_path, "feat: x", config="repos: []\n")
    assert result.returncode == 1
    assert log == ""
