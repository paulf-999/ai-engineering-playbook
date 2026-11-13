"""Checks every test is scored, and maintenance/quality/audits/quality_audit_test_files.md fits the rubric."""

import re
from pathlib import Path

from _audit_tables import assert_links_work, assert_quality_scores, read_table
from _paths import REPO_ROOT

AUDIT = REPO_ROOT / "maintenance" / "quality" / "audits" / "quality_audit_test_files.md"

# this file, which the audit doesn't score, since it can't fairly score its own checker
THIS_FILE = str(Path(__file__).relative_to(REPO_ROOT))

# the themes in quality/themes/quality_themes_test_files.md, as the audit's column headings
THEMES = ("Core coverage", "Leanness", "Clarity", "Simplicity", "Reliability")


def find_test_file(row):
    """Return the test file, relative to the repo root, for a row of the quality table."""
    assert row["link"], f"{row['name']}: link the first cell to its script, or to its test file"
    target = Path(row["link"])

    # a check with no script, like 'Every tracked file's header', links straight to its test file
    if target.name.startswith("test_"):
        return row["link"]

    # a script's tests live in the matching test_<name>.py, e.g. bump_file_headers.sh -> test_bump_file_headers.py
    # (lowercased, so the Makefile maps to test_makefile.py)
    test_name = f"test_{target.stem.lower()}.py"
    matches = list((REPO_ROOT / "tests").rglob(test_name))
    assert len(matches) == 1, f"{target.name}: expected one {test_name} in tests/, found {len(matches)}"
    return str(matches[0].relative_to(REPO_ROOT))


def all_test_files():
    """Return every test file in tests/, keyed by its path from the repo root."""
    return {str(path.relative_to(REPO_ROOT)): path for path in (REPO_ROOT / "tests").rglob("test_*.py")}


# MoSCoW: Must — an unscored test can't be counted by the grep in test_maintenance.md
def test_every_test_has_one_moscow_score():
    """Each test file has one '# MoSCoW:' comment per test function."""
    for name, path in all_test_files().items():
        text = path.read_text()
        scores = len(re.findall(r"^# MoSCoW: (Must|Should|Could|Won't) ", text, flags=re.MULTILINE))
        functions = len(re.findall(r"^def test_", text, flags=re.MULTILINE))
        assert scores == functions, f"{name}: {functions} test functions but {scores} '# MoSCoW:' comments"


# MoSCoW: Should — keeps the quality table in step with the test files and the rubric
def test_quality_table_fits_the_rubric():
    """Links work, every test file bar this checker has one row, and each score and Gaps fit the themes."""
    assert_links_work(AUDIT)
    quality = read_table(AUDIT, "⭐ Quality by script")
    scored = [find_test_file(row) for row in quality]
    assert sorted(scored) == sorted(set(all_test_files()) - {THIS_FILE}), (
        "add or remove quality rows so the table lists every test file but this checker, once each"
    )
    assert_quality_scores(quality, THEMES)
