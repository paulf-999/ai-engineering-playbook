"""Checks that every '# MoSCoW:' tag is a Must, since only Must tests are tagged."""

import re

from _paths import REPO_ROOT


# MoSCoW: Must — the Must count in test_maintenance.md only works if every tag is a Must
def test_every_moscow_tag_is_a_must():
    """No test file carries a '# MoSCoW:' tag other than Must."""
    others = [
        f"{path.relative_to(REPO_ROOT)}: {line}"
        for path in (REPO_ROOT / "tests").rglob("test_*.py")
        for line in path.read_text().splitlines()
        if re.match(r"# MoSCoW: (?!Must )", line)
    ]
    assert not others, f"tag only Must tests, and delete any Could or Won't test: {others}"
