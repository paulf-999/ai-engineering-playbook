"""Tests for the skill version check, which fails a PR that changes a skill without bumping its contract version."""

import subprocess

import pytest
from _git_repo import isolated_git_repo
from _paths import SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "git" / "git_validate_skill_versions.sh"
SKILL = "src/claude/skills/_git_skills/demo-skill"


def commit(repo, env, message):
    """Stage everything in repo and commit it."""
    subprocess.run(["git", "add", "."], cwd=repo, env=env, check=True)
    subprocess.run(["git", "commit", "-q", "-m", message], cwd=repo, env=env, check=True)


@pytest.fixture
def git_repo(tmp_path):
    """Create a repo whose main holds one skill at version 1.0.0, then switch to a feature branch."""
    env = isolated_git_repo(tmp_path, branch="main")
    skill = tmp_path / SKILL
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("# demo\n")
    (skill / "skill.contract.yaml").write_text("name: demo-skill\nversion: 1.0.0\n")
    commit(tmp_path, env, "base")
    subprocess.run(["git", "switch", "-q", "-c", "feature/change"], cwd=tmp_path, env=env, check=True)
    return tmp_path, env


def run_check(repo, env):
    """Run the version check against main and return the full result."""
    return subprocess.run(["bash", str(SCRIPT), "main"], cwd=repo, env=env, capture_output=True, text=True, check=False)


@pytest.mark.parametrize(("bump", "expected"), [(False, 1), (True, 0)])
def test_a_changed_skill_needs_a_version_bump(git_repo, bump, expected):
    """Changing a skill's files fails until its contract version changes too, and names the skill."""
    repo, env = git_repo
    (repo / SKILL / "SKILL.md").write_text("# demo, changed\n")
    if bump:
        (repo / SKILL / "skill.contract.yaml").write_text("name: demo-skill\nversion: 1.1.0\n")
    commit(repo, env, "change")
    result = run_check(repo, env)
    assert result.returncode == expected, f"bump={bump} should exit {expected}:\n{result.stdout}"
    if not bump:
        assert "demo-skill" in result.stdout, "the failure should name the skill to bump"


@pytest.mark.parametrize("change", ["other_file", "new_skill"])
def test_changes_with_no_existing_skill_pass(git_repo, change):
    """A PR that changes no existing skill, or adds a new one, passes."""
    repo, env = git_repo
    if change == "other_file":
        (repo / "README.md").write_text("hello\n")
    else:
        new = repo / "src/claude/skills/_git_skills/new-skill"
        new.mkdir()
        (new / "skill.contract.yaml").write_text("name: new-skill\nversion: 1.0.0\n")
    commit(repo, env, "change")
    result = run_check(repo, env)
    assert result.returncode == 0, f"{change} should pass:\n{result.stdout}"
