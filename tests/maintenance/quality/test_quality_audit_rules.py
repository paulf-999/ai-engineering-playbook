"""Checks the rules quality audit has one row per entry-point rule, and that each row's scores add up."""

import pytest
from _audit_tables import assert_links_work, assert_quality_scores, read_table
from _paths import REPO_ROOT

AUDIT = REPO_ROOT / "maintenance" / "quality" / "quality_audit.md"
RULES_DIR = REPO_ROOT / "src" / "claude" / "rules"

# the themes in the Rules section of quality/quality_rubrics.md, as the audit's column headings
THEMES = ("Changes behaviour", "Right place", "No duplicate", "Clarity", "Accuracy")


def entry_point_rules(rules_dir=RULES_DIR, root=REPO_ROOT):
    """Return every entry-point rule's path relative to root, leaving out children, whose names start with '_'."""
    return {
        str(path.relative_to(root))
        for path in rules_dir.rglob("*.md")
        # a child sits in a folder named after its parent, and is scored with it
        if not path.name.startswith("_")
    }


def row_list_problems(rows, rules):
    """Return the rules with no row, the rows for no rule, and the rules with more than one row."""
    links = [row["link"] for row in rows]
    missing, extra = sorted(set(rules) - set(links)), sorted(set(links) - set(rules))
    repeated = sorted({link for link in links if links.count(link) > 1})
    return [
        f"{label}: {paths}"
        for label, paths in (("add rows for", missing), ("remove", extra), ("de-duplicate", repeated))
        if paths
    ]


# MoSCoW: Must — a rule with no row is never checked for whether it earns its place
def test_every_rule_has_a_row():
    """Links work, each entry-point rule has exactly one row, and each row's score and Gaps match its themes."""
    assert_links_work(AUDIT)
    rows = read_table(AUDIT, "⭐ Quality by rule")
    problems = row_list_problems(rows, entry_point_rules())
    assert not problems, "; ".join(problems)
    assert_quality_scores(rows, THEMES)


# MoSCoW: Must — a row check that never fails would let a rule go unscored
@pytest.mark.parametrize(
    ("links", "expected"),
    [
        pytest.param(["a.md"], "add rows for: ['b.md']", id="missing_row"),
        pytest.param(["a.md", "b.md", "c.md"], "remove: ['c.md']", id="extra_row"),
        pytest.param(["a.md", "b.md", "b.md"], "de-duplicate: ['b.md']", id="repeated_row"),
    ],
)
def test_a_wrong_row_list_is_reported(links, expected):
    """A rule with no row, a row for no rule and a repeated row each fail, naming the path."""
    rows = [{"link": link} for link in links]
    assert expected in row_list_problems(rows, {"a.md", "b.md"})


# MoSCoW: Should — children are scored with their parent, so they mustn't need rows of their own
def test_children_need_no_row(tmp_path):
    """A '_'-prefixed child is left out of the rules that need rows, while its parent is kept."""
    (tmp_path / "parent").mkdir()
    (tmp_path / "parent.md").write_text("x\n")
    (tmp_path / "parent" / "_child.md").write_text("x\n")
    assert entry_point_rules(tmp_path, tmp_path) == {"parent.md"}
