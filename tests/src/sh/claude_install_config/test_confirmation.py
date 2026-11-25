"""Tests for the install library that shows what will change and requires a typed confirmation."""

import subprocess

import pytest
from _paths import SCRIPTS_DIR

LIBRARIES = SCRIPTS_DIR / "claude_install_config"


def run_library(command, answer="", **variables):
    """Source the library in a strict bash with the variables set, and run the command with answer on stdin."""
    sources = [SCRIPTS_DIR / "shell_utils.sh", LIBRARIES / "_file_selection.sh", LIBRARIES / "_confirmation.sh"]
    script = "set -euo pipefail\n" + "".join(f'source "{path}"\n' for path in sources) + command
    env = {"PATH": "/usr/bin:/bin", "PROJECT": "", "PREFERENCES": "1", **variables}
    return subprocess.run(["bash", "-c", script], env=env, input=answer, capture_output=True, text=True, check=False)


@pytest.mark.parametrize(("answer", "code"), [("install\n", 0), ("install", 0), ("Install\n", 1), ("\n", 1), ("", 1)])
def test_require_typed_accepts_only_the_exact_word(answer, code):
    """Only the exact word continues, and a wrong answer or end of input cancels."""
    result = run_library('require_typed install "? " Install; echo continued', answer)
    assert result.returncode == code, result.stderr
    assert ("continued" in result.stdout) is (code == 0), "it should continue only on the exact word"
    assert ("Install cancelled - nothing changed." in result.stdout) is (code == 1), "a cancellation should be reported"


def test_require_terminal_names_the_make_target():
    """With no terminal, it stops and says which make target to run yourself."""
    result = run_library("require_terminal uninstall; echo continued")
    assert result.returncode == 1 and "continued" not in result.stdout, "it should stop without a terminal"
    assert "Run make uninstall from your own terminal" in result.stdout


@pytest.mark.parametrize(
    ("variables", "reason", "note"),
    [
        ({"PREFERENCES": "1"}, "no longer in the repo", None),
        ({"PREFERENCES": "0"}, "holds preferences, left out", "rerun with a plain make install"),
        ({"PREFERENCES": "0", "PROJECT": "/repo"}, "holds preferences, left out", "don't install into a project"),
    ],
)
def test_print_removals_says_why_and_how_to_keep_preferences(variables, reason, note):
    """Each removed preference gets its reason, and a note that fits the kind of install."""
    path = "rules/always_on/02_preferences/style.md"
    result = run_library(f"REMOVED_FILES=({path}); print_removals", **variables)
    assert f"  {path} ({reason})" in result.stdout, result.stdout + result.stderr
    notes = [
        text for text in ("rerun with a plain make install", "don't install into a project") if text in result.stdout
    ]
    assert notes == ([note] if note else []), "only the fitting note should print"


def test_print_removals_is_silent_with_nothing_to_remove():
    """An install that removes nothing prints nothing, even on bash 3.2, where an empty list can count as unset."""
    result = run_library("print_removals")
    assert (result.returncode, result.stdout, result.stderr) == (0, "", "")
