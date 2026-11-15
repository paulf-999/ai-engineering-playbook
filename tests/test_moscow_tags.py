"""Checks every test function carries one '# MoSCoW:' priority, and that none is a Could."""

import re

from _paths import REPO_ROOT


# MoSCoW: Must — an unscored test can't be counted by the grep in test_maintenance.md
def test_every_test_has_one_moscow_score():
    """Each test file has one '# MoSCoW:' comment per test function."""
    for path in (REPO_ROOT / "tests").rglob("test_*.py"):
        text = path.read_text()
        scores = len(re.findall(r"^# MoSCoW: (Must|Should|Could|Won't) ", text, flags=re.MULTILINE))
        functions = len(re.findall(r"^def test_", text, flags=re.MULTILINE))
        name = path.relative_to(REPO_ROOT)
        assert scores == functions, f"{name}: {functions} test functions but {scores} '# MoSCoW:' comments"


# MoSCoW: Must — a Could test guards a rare case, so it costs more upkeep than it saves
def test_no_test_is_a_could():
    """No test carries a '# MoSCoW: Could' priority."""
    could = [
        str(path.relative_to(REPO_ROOT))
        for path in (REPO_ROOT / "tests").rglob("test_*.py")
        if re.search(r"^# MoSCoW: Could ", path.read_text(), flags=re.MULTILINE)
    ]
    assert not could, f"delete these Could tests, or re-rate them if they guard a core path: {could}"
