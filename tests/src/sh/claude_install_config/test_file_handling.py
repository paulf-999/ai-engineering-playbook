"""Tests for the install libraries that pick, render, copy, back up and remove files."""

import subprocess

import pytest
from _paths import SCRIPTS_DIR

LIBRARIES = SCRIPTS_DIR / "claude_install_config"


def run_library(command, **variables):
    """Source the file libraries in a strict bash with the variables set, run the command, and return the result."""
    values = {
        "PROJECT": "",
        "WITH_HOOKS": "",
        "PREFERENCES": "1",
        **{name: str(value) for name, value in variables.items()},
    }
    sources = [SCRIPTS_DIR / "shell_utils.sh", LIBRARIES / "_file_selection.sh", LIBRARIES / "_file_changes.sh"]
    script = "set -euo pipefail\n" + "".join(f'source "{path}"\n' for path in sources) + command
    return subprocess.run(
        ["bash", "-c", script], env={"PATH": "/usr/bin:/bin", **values}, capture_output=True, text=True
    )


def succeeds(command, **variables):
    """Return whether a library check succeeds, failing the test on any other error."""
    result = run_library(f"if {command}; then echo yes; else echo no; fi", **variables)
    assert result.stdout in ("yes\n", "no\n"), f"the check should run:\n{result.stdout}{result.stderr}"
    return result.stdout == "yes\n"


# --- file selection tests ---


@pytest.mark.parametrize(
    ("source", "target"),
    [
        ("rules/on_demand/style_guides/jira.md", "on_demand/style_guides/jira.md"),
        ("skills/_git_skills/git-create-pr/SKILL.md", "skills/git-create-pr/SKILL.md"),
        ("rules/always_on/rule.md", "rules/always_on/rule.md"),
    ],
)
def test_target_path_moves_on_demand_files_and_flattens_skill_groups(source, target):
    """On-demand files move out of rules/, a grouped skill loses its group folder, and other files stay put."""
    assert run_library(f'target_path "{source}"; echo "${{TARGET_PATH}}"').stdout == f"{target}\n"


@pytest.mark.parametrize(
    ("path", "variables", "expected"),
    [
        ("rules/always_on/rule.md", {}, True),
        ("rules/always_on/02_preferences/style.md", {}, True),
        ("rules/always_on/02_preferences/style.md", {"PREFERENCES": "0"}, False),
        ("_templates/rule.md.template", {}, False),
        ("hooks/README.md", {}, False),
        ("skills/_git_skills/notes.md", {}, False),
        ("rules/deleted.md", {}, False),
    ],
)
def test_is_installable_leaves_out_what_never_installs(tmp_path, path, variables, expected):
    """Templates, READMEs, skill groups' own files, deleted files and unwanted preferences are left out."""
    if path != "rules/deleted.md":
        (tmp_path / path).parent.mkdir(parents=True)
        (tmp_path / path).write_text("x\n")
    assert succeeds(f'is_installable "{path}"', SOURCE_DIR=tmp_path, **variables) is expected


# --- rendering tests ---


@pytest.mark.parametrize(
    ("link", "installed"),
    [
        # an on-demand rule sits one folder higher once installed
        ("../../always_on/a.md", "../../rules/always_on/a.md"),
        ("../other/b.md", "../other/b.md"),
        ("../../../skills/_git_skills/x/SKILL.md", "../../skills/x/SKILL.md"),
        # a link out of the config has nowhere to move to
        ("../../../../docs/c.md", "../../../../docs/c.md"),
    ],
)
def test_relink_points_at_where_targets_install(link, installed):
    """A link from an on-demand rule leads to where its target installs, keeping any #fragment."""
    source = "rules/on_demand/guides/from.md"
    text = run_library(f'printf "see [x]({link}#top) now" | relink {source} on_demand/guides/from.md').stdout
    assert text == f"see [x]({installed}#top) now\n"


@pytest.mark.parametrize(
    ("project", "pointer"), [("", "in your Claude config directory"), ("/repo", "in this project's `.claude/` folder")]
)
def test_render_text_names_the_project_folder_only_in_a_project(project, pointer):
    """A pointer to your Claude config directory names the project's .claude/ folder in a project install only."""
    assert run_library('echo "in your Claude config directory" | render_text', PROJECT=project).stdout == f"{pointer}\n"


# --- file change tests ---


def test_is_up_to_date_compares_the_rendered_file(tmp_path):
    """A project's copy is compared as rendered, so an unchanged one counts as up to date and the raw source doesn't."""
    (tmp_path / "a.md").write_text("in your Claude config directory\n")
    (tmp_path / "raw.md").write_text("in your Claude config directory\n")
    (tmp_path / "rendered.md").write_text("in this project's `.claude/` folder\n")
    for copy, expected in (("rendered.md", True), ("raw.md", False), ("missing.md", False)):
        check = f'is_up_to_date a.md "{tmp_path / copy}"'
        assert succeeds(check, SOURCE_DIR=tmp_path, PROJECT="/repo") is expected, f"wrong answer for {copy}"


def test_back_up_and_remove_moves_a_file_with_its_mode(tmp_path):
    """The file leaves the target and its backup keeps its text and mode."""
    target, backup = tmp_path / "target", tmp_path / "backup"
    (target / "hooks").mkdir(parents=True)
    (target / "hooks" / "a.sh").write_text("mine\n")
    (target / "hooks" / "a.sh").chmod(0o750)
    result = run_library(f'back_up_and_remove "{backup}" hooks/a.sh', TARGET_DIR=target)
    assert result.returncode == 0, result.stderr
    assert not (target / "hooks" / "a.sh").exists(), "the file should be removed"
    copy = backup / "hooks" / "a.sh"
    assert (copy.read_text(), copy.stat().st_mode & 0o777) == ("mine\n", 0o750), "the backup should match the file"


def test_backup_dir_for_matches_whole_manifest_paths(tmp_path):
    """Only a path the manifest lists in full goes to the upgrade folder."""
    (tmp_path / "manifest").write_text("rules/a.md\n")
    folders = {"MANIFEST": tmp_path / "manifest", "BACKUP_DIR": "usual", "UPGRADE_BACKUP_DIR": "upgrade"}
    assert run_library("backup_dir_for rules/a.md; backup_dir_for a.md", **folders).stdout == "upgrade\nusual\n"
