# version: 1.0.0
# created: 2026-11-05
# updated: 2026-11-05
"""Checks every rule file under src/claude/rules/ meets the rule template's structural gates.

Also checks that each gate can fail, using small broken examples.
"""

import re

import pytest
from _paths import REPO_ROOT

CONFIG_DIR = REPO_ROOT / "src" / "claude"
RULES_DIR = CONFIG_DIR / "rules"
RULE_FILES = sorted(RULES_DIR.rglob("*.md"))
MAX_LINES = 110
MAX_BULLETS = 5
# emoji blocks: pictographs and symbols, misc symbols and dingbats, arrows and technical symbols
EMOJI = re.compile("[\U0001f300-\U0001faff☀-➿⬀-⯿⌀-⏿←-⇿]")
HEADER_FIELDS = ("version", "created", "updated")
MISS_COSTS = ("low", "medium", "high")
# a pointer line names its target in backticks, such as **Read on demand:** `_templates/README.md`
POINTER = re.compile(r"\*\*Read on demand:\*\* `([^`]+)`")


def relative(path):
    """Return a rule's path relative to src/claude/rules/, as used in messages and loading checks."""
    return path.relative_to(RULES_DIR).as_posix()


def split_frontmatter(lines):
    """Return the lines inside an opening YAML '---' block, and the lines after it."""
    if lines and lines[0] == "---":
        end = lines.index("---", 1)
        return lines[1:end], lines[end + 1 :]
    return [], lines


def header_block(lines):
    """Return the comment lines that open the file: the metadata header and any usage lines after it."""
    frontmatter, body = split_frontmatter(lines)
    # this repo puts a path-scoped rule's header inside its '---' block, as the file-header test expects
    source = frontmatter if frontmatter else body
    # the 3 header lines, then up to 3 usage lines: applies_to, miss_cost and loading
    return [line for line in source if line.startswith("<!--")][: len(HEADER_FIELDS) + 3]


def prose_lines(lines):
    """Return the lines outside fenced code blocks, so examples in code aren't checked."""
    kept, fenced = [], False
    for line in lines:
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            kept.append(line)
    return kept


def opening_problems(text):
    """Return problems with the header, H1 and Purpose line."""
    lines = text.split("\n")
    problems = []
    header = header_block(lines)
    for line, field in zip(header, HEADER_FIELDS):
        if not line.startswith(f"<!-- {field}: "):
            problems.append(f"expected the '{field}' header line, got {line!r}")
    if len(header) < len(HEADER_FIELDS):
        problems.append("the header needs version, created and updated lines")
    h1 = [line for line in prose_lines(lines) if line.startswith("# ")]
    if len(h1) != 1:
        problems.append(f"needs exactly one H1, found {len(h1)}")
    elif not EMOJI.search(h1[0]):
        problems.append(f"the H1 needs an emoji: {h1[0]!r}")
    else:
        after_h1 = lines[lines.index(h1[0]) + 1 :]
        first = next((line for line in after_h1 if line.strip()), "")
        if not first.startswith("**Purpose:**"):
            problems.append("the line after the H1 must be a one-line **Purpose:** statement")
    return problems


def size_problems(text):
    """Return problems with the file's length or its trailing newline."""
    problems = []
    _, body = split_frontmatter(text.split("\n"))
    counted = [line for line in body if not line.startswith("<!--")]
    if len(counted) > MAX_LINES + 1:  # the last element is the empty string after the final newline
        problems.append(f"{len(counted) - 1} lines, over the {MAX_LINES}-line limit, so split it into children")
    if not text.endswith("\n") or text.endswith("\n\n"):
        problems.append("must end with exactly one newline")
    return problems


def heading_problems(text):
    """Return problems with ## headings: a missing emoji, an unearned Contents section or a Related section."""
    h2 = [line for line in prose_lines(text.split("\n")) if line.startswith("## ")]
    problems = [f"this heading needs an emoji: {line!r}" for line in h2 if not EMOJI.search(line)]
    real = [line for line in h2 if "Contents" not in line]
    if len(real) < len(h2) and len(real) < 3:
        problems.append(f"a Contents section needs 3 or more other ## headings, found {len(real)}")
    problems += [f"link other files by pointer, not a Related section: {line!r}" for line in h2 if "Related" in line]
    return problems


def list_problems(text):
    """Return each list with more than 5 top-level bullets, where blank lines and child bullets don't end a list."""
    problems, count = [], 0
    for line in prose_lines(text.split("\n")) + ["end"]:
        if line.startswith(("- ", "* ")):
            count += 1
        elif line.strip() and not line.startswith(" "):
            if count > MAX_BULLETS:
                problems.append(f"a list has {count} top-level bullets, over {MAX_BULLETS}, so split it")
            count = 0
    return problems


def expected_loading(rule_path):
    """Return the loading value a rule's folder implies."""
    if rule_path.startswith("_rules_on_demand/"):
        return "lazy"
    if rule_path.startswith("_path_scoped_rules/"):
        return "path-scoped"
    return "always-on"


def usage_problems(text, rule_path):
    """Return problems with an entry-point rule's applies_to, miss_cost and loading lines."""
    lines = text.split("\n")
    header = header_block(lines)
    # each usage line reads <!-- field: value -->, so collect them as a field-to-value mapping
    values = dict(re.findall(r"<!-- (applies_to|miss_cost|loading): (.+?) -->", "\n".join(header)))
    problems = [
        f"an entry-point rule needs a '{field}' line after its header"
        for field in ("applies_to", "miss_cost", "loading")
        if field not in values
    ]
    # a value is the allowed word, then an em-dash and a reason, such as "low — style drift"
    if "miss_cost" in values and not re.fullmatch(rf"({'|'.join(MISS_COSTS)}) — .+", values["miss_cost"]):
        problems.append(f"miss_cost must be low, medium or high, then ' — ' and a reason: {values['miss_cost']!r}")
    if "loading" in values:
        expected = expected_loading(rule_path)
        if not re.fullmatch(rf"{expected} — .+", values["loading"]):
            problems.append(f"loading must be '{expected}', then ' — ' and a reason, for a rule in this folder")
    return problems


def is_entry_point(path):
    """Succeed for a rule that isn't a child, since children start with '_' and inherit their parent's fields."""
    return not path.name.startswith("_")


# MoSCoW: Must — every rule must open with the header, an emoji H1 and a Purpose line
@pytest.mark.parametrize("path", RULE_FILES, ids=relative)
def test_rule_opens_with_header_h1_and_purpose(path):
    """Each rule has the 3-line header, exactly one H1 with an emoji, and a Purpose line straight after it."""
    problems = opening_problems(path.read_text())
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


# MoSCoW: Must — rules over the line limit cost context and must be split
@pytest.mark.parametrize("path", RULE_FILES, ids=relative)
def test_rule_size_and_ending(path):
    """Each rule is 110 lines or fewer, not counting comments or frontmatter, and ends with one newline."""
    problems = size_problems(path.read_text())
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


# MoSCoW: Should — headings keep rules scannable and link only through pointers
@pytest.mark.parametrize("path", RULE_FILES, ids=relative)
def test_rule_headings(path):
    """Each ## heading has an emoji, Contents appears only with 3 or more headings, and there's no Related section."""
    problems = heading_problems(path.read_text())
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


# MoSCoW: Should — long lists are hard to scan, so the layout rule caps them at 5
@pytest.mark.parametrize("path", RULE_FILES, ids=relative)
def test_rule_lists_are_short(path):
    """No list in a rule has more than 5 top-level bullets."""
    problems = list_problems(path.read_text())
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


# MoSCoW: Must — the loading line must match where the rule lives, so it can't drift
@pytest.mark.parametrize("path", [path for path in RULE_FILES if is_entry_point(path)], ids=relative)
def test_entry_point_has_usage_lines(path):
    """Each entry-point rule has applies_to, miss_cost and loading lines, with loading matching its folder."""
    problems = usage_problems(path.read_text(), relative(path))
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


def child_problems(path):
    """Return problems with a child rule: no parent beside its folder, no sibling, or not named by the parent."""
    parent = path.parent.with_suffix(".md")
    if not parent.exists():
        return ["a child must sit in a folder named after a parent rule"]
    problems = []
    if len(list(path.parent.glob("_*.md"))) < 2:
        problems.append("a folder needs 2 or more children, so flatten a lone child")
    if path.name not in parent.read_text():
        problems.append("the parent must name this child in a pointer")
    return problems


def pointer_targets():
    """Return every path named in a 'Read on demand' line anywhere in the config, with the file that names it."""
    return [(match, source) for source in CONFIG_DIR.rglob("*.md") for match in POINTER.findall(source.read_text())]


def resolve(target):
    """Return where a pointer's target lives in the repo, since on-demand files install beside rules/."""
    return RULES_DIR / target if target.startswith("_rules_on_demand/") else CONFIG_DIR / target


# entry-point rules nothing in src/claude/ points to yet, until the always-on rules that name them are ported
AWAITING_POINTERS = {"_rules_on_demand/style_guides/jira.md", "_rules_on_demand/style_guides/utilities/datetime.md"}


def inbound_params():
    """Return one case per on-demand entry point, marking those still awaiting a pointer as strict expected failures."""
    mark = pytest.mark.xfail(reason="TODO: gains a pointer when the always-on rules are ported", strict=True)
    paths = [path for path in RULE_FILES if is_entry_point(path) and relative(path).startswith("_rules_on_demand/")]
    return [pytest.param(path, marks=mark if relative(path) in AWAITING_POINTERS else ()) for path in paths]


# MoSCoW: Must — a child no parent points to is never read
@pytest.mark.parametrize("path", [path for path in RULE_FILES if not is_entry_point(path)], ids=relative)
def test_child_is_named_by_its_parent(path):
    """Each child sits in a folder named after its parent, has a sibling, and is named in the parent's text."""
    problems = child_problems(path)
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


# MoSCoW: Must — an on-demand rule nothing points to is never read
@pytest.mark.parametrize("path", inbound_params(), ids=relative)
def test_on_demand_rule_has_an_inbound_pointer(path):
    """Each on-demand entry-point rule is named in a pointer somewhere else in the config."""
    names_it = [source for target, source in pointer_targets() if target == relative(path) and source != path]
    assert names_it, f"{relative(path)}: add a **Read on demand:** pointer to it from another config file"


# MoSCoW: Must — a pointer to a missing file sends Claude nowhere
def test_every_pointer_target_exists():
    """Every path named in a 'Read on demand' line in the config exists."""
    missing = [
        f"{source.relative_to(CONFIG_DIR)} -> {target}"
        for target, source in pointer_targets()
        if not resolve(target).exists()
    ]
    assert not missing, "fix these pointers to missing files: " + ", ".join(missing)


GOOD_RULE = (
    "<!-- version: 1.0.0 -->\n<!-- created: 2026-11-05 -->\n<!-- updated: 2026-11-05 -->\n"
    "<!-- applies_to: * -->\n<!-- miss_cost: low — style drift -->\n<!-- loading: lazy — read on demand -->\n"
    "# 🧪 Example\n\n**Purpose:** an example rule.\n\n## 🔢 Points\n\n- **One:** a point.\n"
)


# MoSCoW: Must — a check that can never fail gives false confidence
@pytest.mark.parametrize(
    ("check", "text", "expected"),
    [
        (opening_problems, GOOD_RULE.replace("<!-- created: 2026-11-05 -->\n", ""), "'created' header line"),
        (opening_problems, GOOD_RULE.replace("# 🧪 Example", "# Example"), "H1 needs an emoji"),
        (opening_problems, GOOD_RULE.replace("**Purpose:** an example rule.", "Some text."), "Purpose"),
        (size_problems, GOOD_RULE + "line\n" * MAX_LINES, "over the 110-line limit"),
        (size_problems, GOOD_RULE + "\n", "exactly one newline"),
        (heading_problems, GOOD_RULE.replace("## 🔢 Points", "## Points"), "heading needs an emoji"),
        (heading_problems, GOOD_RULE + "\n## 📋 Contents\n", "Contents section needs 3"),
        (heading_problems, GOOD_RULE + "\n## 🔗 Related\n", "Related section"),
        (list_problems, GOOD_RULE + "\n".join(f"- **P{n}:** x." for n in range(6)) + "\n", "over 5"),
        (list_problems, GOOD_RULE + "- **P:** x.\n\n" * 6, "over 5"),
    ],
)
def test_each_check_can_fail(check, text, expected):
    """Each structural check reports a problem for a broken example, and none for the good one."""
    assert not check(GOOD_RULE), f"{check.__name__} should pass the good example"
    problems = check(text)
    assert any(expected in problem for problem in problems), f"{check.__name__} missed it: {problems}"


# MoSCoW: Must — usage lines must fail when missing or when loading disagrees with the folder
@pytest.mark.parametrize(
    ("text", "rule_path", "expected"),
    [
        (GOOD_RULE.replace("<!-- loading: lazy — read on demand -->\n", ""), "_rules_on_demand/x.md", "'loading' line"),
        (GOOD_RULE, "01_standards/x.md", "loading must be 'always-on'"),
        (GOOD_RULE.replace("low — style drift", "tiny"), "_rules_on_demand/x.md", "miss_cost must be"),
    ],
)
def test_usage_check_can_fail(text, rule_path, expected):
    """The usage-line check passes a correct on-demand rule and flags each broken example."""
    assert not usage_problems(GOOD_RULE, "_rules_on_demand/x.md"), "a correct on-demand rule should pass"
    problems = usage_problems(text, rule_path)
    assert any(expected in problem for problem in problems), f"missed it: {problems}"


PATH_SCOPED_RULE = "---\n" + GOOD_RULE.replace("# 🧪", "paths:\n  - '*.sql'\n---\n# 🧪").replace(
    "lazy — read on demand", "path-scoped — loads with SQL files"
)


# MoSCoW: Should — path-scoped rules keep their header inside the '---' block, and must still pass
def test_path_scoped_rule_passes_the_checks():
    """A rule with a 'paths:' block, header and usage lines inside it, passes the opening and usage checks."""
    assert not opening_problems(PATH_SCOPED_RULE), opening_problems(PATH_SCOPED_RULE)
    assert not usage_problems(PATH_SCOPED_RULE, "_path_scoped_rules/x.md"), "a correct path-scoped rule should pass"
    problems = usage_problems(PATH_SCOPED_RULE, "_rules_on_demand/x.md")
    assert any("loading must be 'lazy'" in problem for problem in problems), f"missed it: {problems}"


# MoSCoW: Must — the child check must fail for a lone or unnamed child
def test_child_check_can_fail(tmp_path):
    """A lone child its parent never names is flagged twice, and a child with no parent once."""
    (tmp_path / "parent.md").write_text("# 🧪 Parent\n")
    (tmp_path / "parent").mkdir()
    lone = tmp_path / "parent" / "_lone.md"
    lone.write_text("x\n")
    problems = child_problems(lone)
    assert any("2 or more children" in problem for problem in problems), problems
    assert any("must name this child" in problem for problem in problems), problems
    (tmp_path / "orphan").mkdir()
    orphan = tmp_path / "orphan" / "_child.md"
    orphan.write_text("x\n")
    assert child_problems(orphan) == ["a child must sit in a folder named after a parent rule"]
