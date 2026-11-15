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


# MoSCoW: Must — shared number parsing used by three scripts
@pytest.mark.parametrize(("value", "expected"), [("7", "7"), ("010", "10"), ("08", "8"), ("123456789", "123456789")])
def test_to_whole_number_reads_base_ten(value, expected):
    """to_whole_number prints the base-10 value, so a leading zero isn't read as octal."""
    result = run_with_utils(f'to_whole_number "{value}"')
    assert result.returncode == 0, f"to_whole_number should accept {value!r}: {result.stderr}"
    assert result.stdout.strip() == expected, f"{value!r} should read as {expected}"


# MoSCoW: Must — shared input validation used by three scripts
@pytest.mark.parametrize("value", ["", "abc", "-5", "1.5", "1234567890"])
def test_to_whole_number_rejects_non_numbers(value):
    """to_whole_number fails on anything that isn't 1 to 9 digits, which keeps it clear of 64-bit overflow."""
    assert run_with_utils(f'to_whole_number "{value}"').returncode == 1, f"to_whole_number should reject {value!r}"
