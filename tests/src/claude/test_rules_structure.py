"""Checks every rule file under src/claude/rules/ meets the rule template's structural gates."""

import re
from pathlib import Path

import pytest
import yaml
from _config_files import tracked_config_files
from _paths import REPO_ROOT

CONFIG_DIR = REPO_ROOT / "src" / "claude"

RULES_DIR = CONFIG_DIR / "rules"
RULE_FILES = sorted(RULES_DIR.rglob("*.md"))
MAX_LINES = 110
# a child shorter than this saves too little context to be worth its own file and pointer
MIN_CHILD_LINES = 40
# a pointer is a Read on demand bullet that opens with its target in backticks, such as `_templates/README.md`
POINTER = re.compile(r"^- `((?:on_demand|_templates)/[^`]+|README\.md)`", re.MULTILINE)


def relative(path):
    """Return a rule's path relative to src/claude/rules/, as used in messages and loading checks."""
    return path.relative_to(RULES_DIR).as_posix()


def split_frontmatter(lines):
    """Return the lines inside an opening YAML '---' block, and the lines after it."""
    if lines and lines[0] == "---":
        end = lines.index("---", 1)
        return lines[1:end], lines[end + 1 :]
    return [], lines


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
    """Return problems with the H1 and Purpose line."""
    lines = text.split("\n")
    problems = []
    h1 = [line for line in prose_lines(lines) if line.startswith("# ")]
    if len(h1) != 1:
        problems.append(f"needs exactly one H1, found {len(h1)}")
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
    """Return problems with ## headings: a Related section."""
    h2 = [line for line in prose_lines(text.split("\n")) if line.startswith("## ")]
    problems = [f"link other files by pointer, not a Related section: {line!r}" for line in h2 if "Related" in line]
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


@pytest.mark.parametrize("path", RULE_FILES, ids=relative)
def test_rule_opens_with_h1_and_purpose(path):
    """Each rule has exactly one H1, and a Purpose line straight after it."""
    problems = opening_problems(path.read_text())
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


@pytest.mark.parametrize("path", RULE_FILES, ids=relative)
def test_rule_size_and_ending(path):
    """Each rule is 110 lines or fewer, not counting comments or frontmatter, and ends with one newline."""
    problems = size_problems(path.read_text())
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


@pytest.mark.parametrize("path", RULE_FILES, ids=relative)
def test_rule_headings(path):
    """No ## heading is a Related section."""
    problems = heading_problems(path.read_text())
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


@pytest.mark.parametrize(
    "path",
    [path for path in RULE_FILES if relative(path).startswith("path_scoped/")],
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
    on_demand = rules_dir / "on_demand"
    # a loaded parent keeps its bulky children on demand, at the same path under always_on/ or path_scoped/,
    # so on_demand/conduct/writing_style/ belongs to always_on/conduct/writing_style.md
    if beside.is_relative_to(on_demand):
        rest = beside.relative_to(on_demand)
        candidates += [rules_dir / "always_on" / rest, rules_dir / "path_scoped" / rest]
    return next((candidate for candidate in candidates if candidate.exists()), beside)


def body_lines(text):
    """Return a rule's line count, leaving out frontmatter and comment lines, as the size limit counts them."""
    _, body = split_frontmatter(text.rstrip("\n").split("\n"))
    return len([line for line in body if not line.startswith("<!--")])


def is_split_by_kind(parent, rules_dir=RULES_DIR):
    """Return whether a parent's rules are split between a guide and its team conventions, so children may be short."""
    parts = parent.relative_to(rules_dir).parts
    if "team_conventions" in parts:
        return True
    is_guide = parts[:2] == ("path_scoped", "style_guides")
    return is_guide and (rules_dir / "path_scoped" / "team_conventions" / Path(*parts[2:])).exists()


def child_problems(path, rules_dir=RULES_DIR):
    """Return problems with a child rule: no parent folder, no sibling, too short, or not named by the parent."""
    parent = find_parent(path, rules_dir)
    if not parent.exists():
        return ["a child must sit in a folder named after a parent rule"]
    problems = []
    if len(list(path.parent.glob("_*.md"))) < 2:
        problems.append("a folder needs 2 or more children, so flatten a lone child")
    if path.name not in parent.read_text():
        problems.append("the parent must name this child in a pointer")
    # an always-on parent splits to keep every session cheap, and a split by kind leaves what's left on each side,
    # so the children of either may be short
    is_always_on = parent.is_relative_to(rules_dir / "always_on")
    if not is_always_on and not is_split_by_kind(parent, rules_dir) and body_lines(path.read_text()) < MIN_CHILD_LINES:
        problems.append(f"a child needs {MIN_CHILD_LINES} or more lines, so fold it into its parent or a sibling")
    return problems


def pointer_targets():
    """Return every path named in a 'Read on demand' line anywhere in the config, with the file that names it."""
    return [(match, source) for source in CONFIG_DIR.rglob("*.md") for match in POINTER.findall(source.read_text())]


def resolve(target):
    """Return where a pointer's target lives in the repo, since on-demand files install beside rules/."""
    return RULES_DIR / target if target.startswith("on_demand/") else CONFIG_DIR / target


@pytest.mark.parametrize(
    "path",
    [path for path in RULE_FILES if not is_entry_point(path)],
    ids=relative,
)
def test_child_is_named_by_its_parent(path):
    """Each child sits in a folder named after its parent, has a sibling, is long enough, and is named by the parent."""
    problems = child_problems(path)
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


def test_a_short_child_is_reported_unless_its_parent_is_always_on(tmp_path):
    """A child under the line floor fails beside an on-demand parent, and passes beside an always-on one."""
    names = "parent.md\n- `_short.md`\n- `_other.md`\n"
    for tier in ("on_demand", "always_on"):
        (tmp_path / tier / "parent").mkdir(parents=True)
        (tmp_path / tier / "parent.md").write_text(names)
        for child in ("_short.md", "_other.md"):
            (tmp_path / tier / "parent" / child).write_text("x\n" * 5)
    floor = f"a child needs {MIN_CHILD_LINES} or more lines"
    assert any(
        floor in problem for problem in child_problems(tmp_path / "on_demand" / "parent" / "_short.md", tmp_path)
    )
    assert not child_problems(tmp_path / "always_on" / "parent" / "_short.md", tmp_path)


@pytest.mark.parametrize(
    "path",
    [path for path in RULE_FILES if is_entry_point(path) and relative(path).startswith("on_demand/")],
    ids=relative,
)
def test_on_demand_rule_has_an_inbound_pointer(path):
    """Each on-demand entry-point rule is named in a pointer elsewhere in the config, or in a hook's block message."""
    names_it = [source for target, source in pointer_targets() if target == relative(path) and source != path]
    names_it += [hook for hook in (CONFIG_DIR / "hooks").glob("*.sh") if relative(path) in hook.read_text()]
    assert names_it, f"{relative(path)}: point to it from another config file's '## 📚 Read on demand' section"


def loose_pointers(text):
    """Return each 'Read on demand' line that sits outside a ## Read on demand section."""
    heading, loose = "", []
    for line in text.splitlines():
        if line.startswith("## "):
            heading = line
        elif POINTER.match(line) and "read on demand" not in heading.lower():
            loose.append(line)
    return loose


@pytest.mark.parametrize(
    "path", [*RULE_FILES, CONFIG_DIR / "CLAUDE.md"], ids=lambda path: path.relative_to(CONFIG_DIR).as_posix()
)
def test_pointers_sit_in_read_on_demand_section(path):
    """Each 'Read on demand' pointer sits under a ## Read on demand section, so pointers aren't scattered."""
    loose = loose_pointers(path.read_text())
    assert not loose, f"{path.name}: move these pointers under a '## 📚 Read on demand' section: {loose}"


def test_every_pointer_target_exists():
    """Every path named in a 'Read on demand' line in the config exists."""
    missing = [
        f"{source.relative_to(CONFIG_DIR)} -> {target}"
        for target, source in pointer_targets()
        if not resolve(target).exists()
    ]
    assert not missing, "fix these pointers to missing files: " + ", ".join(missing)


# a backticked path into a preferences/ folder, which a default install leaves out
PREFERENCE_PATH = re.compile(r"`[^`\n]*preferences/[^`\n]*`")


def preference_paths(text):
    """Return each backticked path into a preferences/ folder that the text names."""
    return PREFERENCE_PATH.findall(text)


def test_preference_paths_are_found_in_any_backticks():
    """A pointer bullet, a table cell or prose naming a preferences/ path is caught, and other paths aren't."""
    text = "- `on_demand/preferences/x.md`, when\n| `_templates/preferences/y` |\nsee `rules/always_on/z.md`"
    assert preference_paths(text) == ["`on_demand/preferences/x.md`", "`_templates/preferences/y`"]


def test_no_default_install_file_names_a_preference():
    """Nothing a default install ships points into a preferences/ folder, which only PREFERENCES=1 installs."""
    problems = [
        f"{path}: {found}"
        for path in sorted(tracked_config_files())
        if not path.endswith("README.md")
        for found in preference_paths((CONFIG_DIR / path).read_text())
    ]
    assert not problems, "default files name preferences they may not have:\n" + "\n".join(problems)


# working-file folders that only the working-files preference names, since a default install never writes there
WORKING_FILE_FOLDERS = re.compile(r"\.claude_work/|~/_drafts/|~/_errors/")


def test_no_default_install_file_names_a_working_file_folder():
    """Only preferences say where Claude keeps a user's plans, drafts, errors and session notes."""
    problems = [
        f"{path}: {found}"
        for path in sorted(tracked_config_files())
        if not path.endswith("README.md")
        for found in WORKING_FILE_FOLDERS.findall((CONFIG_DIR / path).read_text())
    ]
    assert not problems, "default files name working-file folders:\n" + "\n".join(problems)


def test_a_short_child_passes_once_its_guide_is_split_by_kind(tmp_path):
    """A guide whose team conventions moved out may leave short children, on both the guide's side and the team's."""
    for parent in ("path_scoped/style_guides/tool", "path_scoped/team_conventions/tool"):
        (tmp_path / parent).with_suffix(".md").parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / parent).with_suffix(".md").write_text("- `_short.md`\n- `_other.md`\n")
        folder = tmp_path / parent.replace("path_scoped", "on_demand")
        folder.mkdir(parents=True)
        for child in ("_short.md", "_other.md"):
            (folder / child).write_text("x\n" * 5)
    for side in ("style_guides", "team_conventions"):
        assert not child_problems(tmp_path / "on_demand" / side / "tool" / "_short.md", tmp_path), side
    # without a team conventions file, the guide isn't split, so its short child still fails the floor
    (tmp_path / "path_scoped" / "team_conventions" / "tool.md").unlink()
    problems = child_problems(tmp_path / "on_demand" / "style_guides" / "tool" / "_short.md", tmp_path)
    assert any(f"{MIN_CHILD_LINES} or more lines" in problem for problem in problems)


def team_convention_pairs(rules_dir=RULES_DIR):
    """Return each path-scoped team conventions file with the guide it belongs to, paired by relative path."""
    team_dir = rules_dir / "path_scoped" / "team_conventions"
    return [
        (team, rules_dir / "path_scoped" / "style_guides" / team.relative_to(team_dir))
        for team in team_dir.rglob("*.md")
    ]


def globs_problem(team, guide):
    """Return why a team conventions file won't load with its guide, or None if their paths: lists match."""
    if not guide.exists():
        return f"{team.name} has no guide at the same path under style_guides/"
    if not paths_of(guide):
        return f"{guide.name} has no paths: list, so neither file loads on a matching file"
    if paths_of(team) != paths_of(guide):
        return f"{team.name} has different paths: from its guide, so the two won't load together"
    return None


def paths_of(path):
    """Return a rule's paths: globs, or an empty list."""
    frontmatter, _ = split_frontmatter(path.read_text().split("\n"))
    return (yaml.safe_load("\n".join(frontmatter)) or {}).get("paths", []) if frontmatter else []


@pytest.mark.parametrize(("team", "guide"), team_convention_pairs(), ids=lambda path: relative(path))
def test_team_conventions_load_with_their_guide(team, guide):
    """Each guide's team conventions have the same paths: list, so Claude loads both on a matching file."""
    assert globs_problem(team, guide) is None, globs_problem(team, guide)


def test_mismatched_team_convention_globs_are_reported(tmp_path):
    """A team conventions file whose globs differ from its guide's is caught."""
    for side, glob in (("style_guides", "**/*.sql"), ("team_conventions", "**/*.py")):
        (tmp_path / side).mkdir()
        (tmp_path / side / "tool.md").write_text(f'---\npaths:\n  - "{glob}"\n---\n# Tool\n')
    team, guide = tmp_path / "team_conventions" / "tool.md", tmp_path / "style_guides" / "tool.md"
    assert "different paths" in globs_problem(team, guide)
    # two files with no paths: match each other, but neither would load, so that's caught too
    for path in (team, guide):
        path.write_text("# Tool\n")
    assert "no paths: list" in globs_problem(team, guide)
