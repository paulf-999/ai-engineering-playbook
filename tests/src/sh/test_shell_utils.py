"""Tests for the shared shell helper functions."""

import subprocess

import pytest
from _paths import SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "shell_utils.sh"


def run_with_utils(command):
    """Source shell_utils.sh in a fresh bash, run the command, and return the result."""
    return subprocess.run(
        ["bash", "-c", f'source "{SCRIPT}" && {command}'],
        capture_output=True,
        text=True,
        check=False,
    )


def test_handle_interruption_logs_and_exits():
    """handle_interruption prints its abort message and exits 1, with no missing-command error."""
    result = run_with_utils("handle_interruption")
    assert result.returncode == 1, "handle_interruption should exit 1"
    assert "Script execution aborted by the user." in result.stdout, f"expected the abort message: {result.stdout}"
    assert "command not found" not in result.stderr, f"a command it calls is missing: {result.stderr}"


@pytest.mark.parametrize(
    ("frontmatter", "expected"),
    [
        ("---\npaths:\n  - \"*.sql\"\n  - '*.py'\n---\n", "*.sql\n*.py"),
        ("---\nname: x\n---\npaths:\n  - a\n", ""),
        ("# no block\n", ""),
    ],
)
def test_rule_path_globs_reads_only_the_opening_block(tmp_path, frontmatter, expected):
    """rule_path_globs prints each paths: glob without quotes, and nothing for globs outside the opening --- block."""
    rule = tmp_path / "rule.md"
    rule.write_text(frontmatter)
    result = run_with_utils(f'rule_path_globs "{rule}"')
    assert result.stdout.strip() == expected, f"expected globs {expected!r}, got {result.stdout!r}"


@pytest.mark.parametrize(
    ("frontmatter", "expected"),
    [
        ("---\nname: x\ndescription: Do a thing\n---\n", "Do a thing"),
        ("---\nname: x\ndescription: >\n  Do a\n  thing\n---\n", "Do a\n  thing"),
        ("---\nname: x\ndescription: Do a thing\ndisable-model-invocation: true\n---\n", ""),
    ],
)
def test_description_text_skips_slash_only_skills(tmp_path, frontmatter, expected):
    """description_text prints a description, folded or not, and nothing for a slash-only skill Claude never sees."""
    skill = tmp_path / "SKILL.md"
    skill.write_text(frontmatter)
    result = run_with_utils(f'description_text "{skill}"')
    assert result.stdout.strip() == expected, f"expected {expected!r}, got {result.stdout!r}"


@pytest.mark.parametrize(("value", "expected"), [("7", "7"), ("010", "10"), ("08", "8"), ("123456789", "123456789")])
def test_to_whole_number_reads_base_ten(value, expected):
    """to_whole_number prints the base-10 value, so a leading zero isn't read as octal."""
    result = run_with_utils(f'to_whole_number "{value}"')
    assert result.returncode == 0, f"to_whole_number should accept {value!r}: {result.stderr}"
    assert result.stdout.strip() == expected, f"{value!r} should read as {expected}"


@pytest.mark.parametrize("value", ["", "abc", "-5", "1.5", "1234567890"])
def test_to_whole_number_rejects_non_numbers(value):
    """to_whole_number fails on anything that isn't 1 to 9 digits, which keeps it clear of 64-bit overflow."""
    assert run_with_utils(f'to_whole_number "{value}"').returncode == 1, f"to_whole_number should reject {value!r}"
