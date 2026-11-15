"""Checks every test function carries one '# MoSCoW:' priority of Must or Should."""

import re

from _paths import REPO_ROOT


# MoSCoW: Must — an unscored test can't be counted by the grep in test_maintenance.md
def test_every_test_has_one_moscow_score():
    """Each test file has one Must or Should '# MoSCoW:' comment per test function."""
    for path in (REPO_ROOT / "tests").rglob("test_*.py"):
        text = path.read_text()
        scores = len(re.findall(r"^# MoSCoW: (Must|Should) ", text, flags=re.MULTILINE))
        functions = len(re.findall(r"^def test_", text, flags=re.MULTILINE))
        name = path.relative_to(REPO_ROOT)
        assert scores == functions, f"{name}: {functions} functions but {scores} Must or Should scores"
