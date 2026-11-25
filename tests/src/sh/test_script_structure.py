"""Checks every script and library in src/sh/ and the bash script template follow the template's structure."""

import re

import pytest
from _paths import REPO_ROOT, SCRIPTS_DIR

# the copy make install puts in the Claude config, for repos with no template of their own
TEMPLATE = REPO_ROOT / "src" / "claude" / "_templates" / "utils" / "template_bash_script.sh"
# shell_utils.sh and the files whose names start with _ are libraries other scripts source, not scripts that run alone
LIBRARY_PATHS = sorted([SCRIPTS_DIR / "shell_utils.sh", *SCRIPTS_DIR.rglob("_*.sh")])
SCRIPTS = sorted(path for path in SCRIPTS_DIR.rglob("*.sh") if path not in LIBRARY_PATHS)

# the parts of the bash script template every script must keep, in this order
REQUIRED_PARTS = [
    ("shebang", r"#!/bin/bash"),
    ("strict mode", r"set -euo pipefail\b.*"),
    ("description line", r"# Description: .+"),
    ("usage line", r"# Usage: .+"),
    # sourced by a path built from the script's own folder, so it works from any working directory
    ("shell_utils.sh source", r'source "\$\(dirname "\$\{BASH_SOURCE\[0\]\}"\)/(\.\./)?shell_utils\.sh"'),
    ("Ctrl+C trap", r"trap handle_interruption SIGINT"),
    ("Variables section", r"# Variables"),
    ("Functions section", r"# Functions"),
    ("Main script logic section", r"# Main script logic"),
    ("start message", r'print_section_header "\$\{DEBUG\}" "Script execution started\."'),
    ("completed message", r'print_section_header "\$\{DEBUG\}" "Script execution completed\."( && echo)?'),
]
# a sourced library skips strict mode, the trap and the start/end messages, so it doesn't change its caller's shell
LIBRARY_PARTS = [
    part
    for part in REQUIRED_PARTS
    if part[0] in {"shebang", "description line", "usage line", "Variables section", "Functions section"}
]


def problems_with(path, parts=REQUIRED_PARTS):
    """Return each required part that's missing or out of order in the script, as readable messages."""
    lines = path.read_text().splitlines()
    problems, last_found = [], -1
    for name, pattern in parts:
        found = next((n for n, line in enumerate(lines) if re.fullmatch(pattern, line)), None)
        if found is None:
            problems.append(f"missing the {name}")
        # each part must come after the one before it, so a part found above the last one is out of order
        elif found < last_found:
            problems.append(f"the {name} (line {found + 1}) is out of order")
        else:
            last_found = found
    return problems


def test_scripts_are_found():
    """The scan finds the scripts, so an empty glob can't make every other test pass by default."""
    assert len(SCRIPTS) >= 5, f"expected at least 5 scripts in src/sh/, found {[p.name for p in SCRIPTS]}"


@pytest.mark.parametrize(
    ("path", "parts"),
    [(path, REQUIRED_PARTS) for path in [TEMPLATE, *SCRIPTS]] + [(path, LIBRARY_PARTS) for path in LIBRARY_PATHS],
    ids=lambda value: value.name if hasattr(value, "name") else None,
)
def test_script_follows_the_template(path, parts):
    """Each script keeps every template part, and each library the parts it can, in the template's order."""
    problems = problems_with(path, parts)
    assert not problems, f"{path.relative_to(REPO_ROOT)} doesn't follow {TEMPLATE.relative_to(REPO_ROOT)}: {problems}"


def test_a_missing_part_is_reported(tmp_path):
    """A script with no completed message is caught, so the check can't silently pass everything."""
    script = tmp_path / "broken.sh"
    script.write_text(TEMPLATE.read_text().replace('"Script execution completed."', '"Done."'))
    assert problems_with(script) == ["missing the completed message"], "only the completed message should be missing"
