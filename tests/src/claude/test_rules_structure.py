# version: 1.5.1
# created: 2026-11-05
# updated: 2026-11-11
"""Checks every rule file under src/claude/rules/ meets the rule template's structural gates."""

import re

import pytest
import yaml
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
    # a path-scoped rule's header follows its '---' block, so YAML never reads the comments as keys
    _, body = split_frontmatter(lines)
    # the 3 header lines, then up to 2 usage lines: applies_to and miss_cost
    return [line for line in body if line.startswith("<!--")][: len(HEADER_FIELDS) + 2]


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


# bullets the 5-item cap skips: checklist items, Contents links and Read on demand pointers
UNCOUNTED_BULLET = re.compile(r"[-*] (\[[ x]\] |\[[^]]*\]\(#|\*\*Read on demand:\*\*)")


def list_problems(text):
    """Return each list over 5 counted top-level bullets, where blank lines and child bullets don't end it."""
    problems, count = [], 0
    for line in prose_lines(text.split("\n")) + ["end"]:
        if line.startswith(("- ", "* ")):
            count += 0 if UNCOUNTED_BULLET.match(line) else 1
        elif line.strip() and not line.startswith(" "):
            if count > MAX_BULLETS:
                problems.append(f"a list has {count} top-level bullets, over {MAX_BULLETS}, so split it")
            count = 0
    return problems


def usage_problems(text):
    """Return problems with an entry-point rule's applies_to and miss_cost lines."""
    lines = text.split("\n")
    header = header_block(lines)
    # each usage line reads <!-- field: value -->, so collect them as a field-to-value mapping
    values = dict(re.findall(r"<!-- (applies_to|miss_cost): (.+?) -->", "\n".join(header)))
    problems = [
        f"an entry-point rule needs a '{field}' line after its header"
        for field in ("applies_to", "miss_cost")
        if field not in values
    ]
    # a value is the allowed word, then an em-dash and a reason, such as "low — style drift"
    if "miss_cost" in values and not re.fullmatch(rf"({'|'.join(MISS_COSTS)}) — .+", values["miss_cost"]):
        problems.append(f"miss_cost must be low, medium or high, then ' — ' and a reason: {values['miss_cost']!r}")
    return problems


def frontmatter_problems(text):
    """Return problems with a path-scoped rule's '---' block: YAML that won't parse, or no 'paths' list."""
    frontmatter, _ = split_frontmatter(text.split("\n"))
    if not frontmatter:
        return ["a path-scoped rule needs a '---' frontmatter block"]
    try:
        data = yaml.safe_load("\n".join(frontmatter))
    except yaml.YAMLError as error:
        # Claude Code can't read 'paths' from YAML that won't parse, so it loads the rule in every session
        return [f"the frontmatter isn't valid YAML, so the rule loads everywhere: {error}"]
    paths = data.get("paths") if isinstance(data, dict) else None
    if not isinstance(paths, list) or not paths:
        return ["the frontmatter needs a non-empty 'paths' list"]
    return []


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


# MoSCoW: Must — every entry-point rule must say what it applies to and what missing it costs
@pytest.mark.parametrize(
    "path",
    [path for path in RULE_FILES if is_entry_point(path)],
    ids=relative,
)
def test_entry_point_has_usage_lines(path):
    """Each entry-point rule has applies_to and miss_cost lines, with miss_cost giving a level and a reason."""
    problems = usage_problems(path.read_text())
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


# MoSCoW: Must — frontmatter that won't parse makes a path-scoped rule load in every session
@pytest.mark.parametrize(
    "path",
    [path for path in RULE_FILES if relative(path).startswith("_path_scoped_rules/")],
    ids=relative,
)
def test_path_scoped_frontmatter_parses(path):
    """Each path-scoped rule's '---' block is valid YAML with a non-empty 'paths' list."""
    problems = frontmatter_problems(path.read_text())
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


def find_parent(path, rules_dir=RULES_DIR):
    """Return a child's parent rule: beside its folder, or at the same path in the loaded tree."""
    beside = path.parent.with_suffix(".md")
    candidates = [beside]
    on_demand = rules_dir / "_rules_on_demand"
    # a loaded parent, such as 02_conduct/writing_style.md, keeps its bulky children on demand
    if beside.is_relative_to(on_demand):
        rest = beside.relative_to(on_demand)
        candidates += [rules_dir / rest, rules_dir / "_path_scoped_rules" / rest]
    return next((candidate for candidate in candidates if candidate.exists()), beside)


def child_problems(path, rules_dir=RULES_DIR):
    """Return problems with a child rule: no parent for its folder, no sibling, or not named by the parent."""
    parent = find_parent(path, rules_dir)
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


# MoSCoW: Must — a child no parent points to is never read
@pytest.mark.parametrize(
    "path",
    [path for path in RULE_FILES if not is_entry_point(path)],
    ids=relative,
)
def test_child_is_named_by_its_parent(path):
    """Each child sits in a folder named after its parent, has a sibling, and is named in the parent's text."""
    problems = child_problems(path)
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


# MoSCoW: Must — an on-demand rule nothing points to is never read
@pytest.mark.parametrize(
    "path",
    [path for path in RULE_FILES if is_entry_point(path) and relative(path).startswith("_rules_on_demand/")],
    ids=relative,
)
def test_on_demand_rule_has_an_inbound_pointer(path):
    """Each on-demand entry-point rule is named in a pointer elsewhere in the config, or in a hook's block message."""
    names_it = [source for target, source in pointer_targets() if target == relative(path) and source != path]
    names_it += [hook for hook in (CONFIG_DIR / "hooks").glob("*.sh") if relative(path) in hook.read_text()]
    assert names_it, f"{relative(path)}: add a **Read on demand:** pointer to it from another config file"


def loose_pointers(text):
    """Return each 'Read on demand' line that sits outside a ## Read on demand section."""
    heading, loose = "", []
    for line in text.splitlines():
        if line.startswith("## "):
            heading = line
        elif line.startswith("- **Read on demand:**") and "read on demand" not in heading.lower():
            loose.append(line)
    return loose


# MoSCoW: Should — keeping every pointer in one section lets a reader see what a file links to at a glance
@pytest.mark.parametrize(
    "path", [*RULE_FILES, CONFIG_DIR / "CLAUDE.md"], ids=lambda path: path.relative_to(CONFIG_DIR).as_posix()
)
def test_pointers_sit_in_read_on_demand_section(path):
    """Each 'Read on demand' pointer sits under a ## Read on demand section, so pointers aren't scattered."""
    loose = loose_pointers(path.read_text())
    assert not loose, f"{path.name}: move these pointers under a '## 📚 Read on demand' section: {loose}"


# MoSCoW: Must — a pointer to a missing file sends Claude nowhere
def test_every_pointer_target_exists():
    """Every path named in a 'Read on demand' line in the config exists."""
    missing = [
        f"{source.relative_to(CONFIG_DIR)} -> {target}"
        for target, source in pointer_targets()
        if not resolve(target).exists()
    ]
    assert not missing, "fix these pointers to missing files: " + ", ".join(missing)
