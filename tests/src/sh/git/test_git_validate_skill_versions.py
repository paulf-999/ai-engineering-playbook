"""Tests for the skill version check, which fails a PR that changes a skill without bumping its contract version."""

import os
import subprocess

import pytest
from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "git" / "git_validate_skill_versions.sh"
SKILL = "src/claude/skills/_git_skills/demo-skill"
CONTRACT = f"{SKILL}/skill.contract.yaml"
# a stub gh that answers the compare call with the merge base, and each contents call from files under commits/
STUB_GH = """#!/bin/bash
case "$2" in
    */compare/*) echo merge_base ;;
    */contents/*)
        [[ -f "{root}/fail" ]] && {{ echo "HTTP 500" >&2; exit 1; }}
        path="${{2#*/contents/}}"
        file="{root}/commits/${{path#*ref=}}/${{path%%\\?ref=*}}"
        [[ -f "${{file}}" ]] || {{ echo "gh: Not Found (HTTP 404)" >&2; exit 1; }}
        cat "${{file}}" ;;
esac
"""


def _make_contract(tmp_path, commit, version):
    """Write the demo skill's contract at the given version into a commit the stub gh serves."""
    contract = tmp_path / "commits" / commit / CONTRACT
    contract.parent.mkdir(parents=True, exist_ok=True)
    contract.write_text(f"name: demo-skill\nversion: {version}\n")


def run_check(tmp_path, changed_files):
    """Run the version check with the stub gh on the PR's changed files, and return the full result."""
    stub = tmp_path / "gh"
    stub.write_text(STUB_GH.format(root=tmp_path))
    stub.chmod(0o755)
    env = {**os.environ, "PATH": f"{tmp_path}:{os.environ['PATH']}"}
    return subprocess.run(
        ["bash", str(SCRIPT), "org/repo", "base_sha", "head_sha", changed_files],
        cwd=REPO_ROOT,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


@pytest.mark.parametrize(("head_version", "expected"), [("1.0.0", 1), ("1.1.0", 0)])
def test_a_changed_skill_needs_a_version_bump(tmp_path, head_version, expected):
    """Changing a skill's files fails until its contract version changes too, and names the skill."""
    _make_contract(tmp_path, "merge_base", "1.0.0")
    _make_contract(tmp_path, "head_sha", head_version)
    result = run_check(tmp_path, f"{SKILL}/SKILL.md\n")
    assert result.returncode == expected, f"head version {head_version} should exit {expected}:\n{result.stdout}"
    if expected == 1:
        assert "demo-skill" in result.stdout, "the failure should name the skill to bump"


@pytest.mark.parametrize(
    "changed_files", ["README.md\n", "src/claude/skills/_git_skills/new-skill/skill.contract.yaml\n"]
)
def test_changes_with_no_existing_skill_pass(tmp_path, changed_files):
    """A PR that changes no skill, or adds a new one with no earlier contract, passes."""
    result = run_check(tmp_path, changed_files)
    assert result.returncode == 0, f"{changed_files!r} should pass:\n{result.stdout}"


def test_a_failed_lookup_fails_the_check(tmp_path):
    """When GitHub can't be read the check fails, rather than treating the skill as new."""
    (tmp_path / "fail").touch()
    result = run_check(tmp_path, f"{SKILL}/SKILL.md\n")
    assert result.returncode == 1, f"a failed lookup should fail: {result.stdout}"
    assert "couldn't read" in result.stdout, f"the reason should say the lookup failed: {result.stdout}"
