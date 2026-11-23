"""Checks every rule file under src/claude/rules/ meets the rule template's structural gates."""

import re

import pytest
import yaml
from _config_files import tracked_config_files
from _paths import REPO_ROOT

CONFIG_DIR = REPO_ROOT / "src" / "claude"

RULES_DIR = CONFIG_DIR / "rules"
# a README under rules/ explains a folder to people browsing the repo, and never installs, so it isn't a rule
RULE_FILES = sorted(path for path in RULES_DIR.rglob("*.md") if path.name != "README.md")
MAX_LINES = 110
# a child shorter than this saves too little context to be worth its own file and pointer
MIN_CHILD_LINES = 40
# a pointer is a Read on demand line, bulleted when there are several, that opens with its target in backticks,
# such as `_templates/README.md`, which a rule wraps in a link to the target's place in the repo
POINTER = re.compile(r"^(?:- )?\[?`((?:on_demand|_templates)/[^`]+|README\.md)`", re.MULTILINE)
LINKED_POINTER = re.compile(r"^(?:- )?\[`([^`]+)`\]\(([^)]+)\)")


# an on-demand rule's last section lists the files that load it, for readers tracing it back
CALLED_BY = "## 📞 Called by"


def without_called_by(lines):
    """Return the lines before a Called by section, which the line limits leave out since it's never followed."""
    return lines[: lines.index(CALLED_BY)] if CALLED_BY in lines else lines


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
    """Return a problem if the file is over the line limit."""
    problems = []
    _, body = split_frontmatter(text.split("\n"))
    counted = [line for line in without_called_by(body) if not line.startswith("<!--")]
    if len(counted) > MAX_LINES + 1:  # the last element is the empty string after the final newline
        problems.append(f"{len(counted) - 1} lines, over the {MAX_LINES}-line limit, so split it into children")
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
def test_rule_size(path):
    """Each rule is 110 lines or fewer, not counting comments or frontmatter."""
    problems = size_problems(path.read_text())
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
    # so on_demand/01_standards/writing_style/ belongs to always_on/01_standards/writing_style.md
    if beside.is_relative_to(on_demand):
        rest = beside.relative_to(on_demand)
        candidates += [rules_dir / "always_on" / rest, rules_dir / "path_scoped" / rest]
    return next((candidate for candidate in candidates if candidate.exists()), beside)


def body_lines(text):
    """Return a rule's line count, leaving out frontmatter and comment lines, as the size limit counts them."""
    _, body = split_frontmatter(text.rstrip("\n").split("\n"))
    return len([line for line in without_called_by(body) if not line.startswith("<!--")])


TEAM_SUFFIX = "_team_conventions"


def is_split_by_kind(parent):
    """Return whether a parent's rules are split between a guide and its team conventions, so children may be short."""
    return parent.with_name(parent.stem + TEAM_SUFFIX + ".md").exists()


def child_problems(path, rules_dir=RULES_DIR):
    """Return problems with a child rule: no parent folder, no sibling, too short, or not named by the parent."""
    parent = find_parent(path, rules_dir)
    if not parent.exists():
        return ["a child must sit in a folder named after a parent rule"]
    problems = []
    if len(list(path.parent.glob("_*.md"))) < 2:
        problems.append("a folder needs 2 or more children, so flatten a lone child")
    # a team child shares its guide's folder, but the guide's team conventions file points to it
    namer = parent.with_name(parent.stem + TEAM_SUFFIX + ".md") if path.stem.endswith(TEAM_SUFFIX) else parent
    if not namer.exists() or path.name not in namer.read_text():
        problems.append("the parent must name this child in a pointer")
    # an always-on parent splits to keep every session cheap, and a split by kind leaves what's left on each side,
    # so the children of either may be short
    is_always_on = parent.is_relative_to(rules_dir / "always_on")
    if not is_always_on and not is_split_by_kind(parent) and body_lines(path.read_text()) < MIN_CHILD_LINES:
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


ON_DEMAND_MENTION = re.compile(r"on_demand/[\w/.-]+?\.md")
CALLER_BULLET = re.compile(r"^(- |This rule is invoked by )\[`([^`]+)`\]\(([^)]+)\), (.+)$")
CALLER_LEAD_IN = "This rule is invoked by:"
# a pointer's trigger follows its path and the install-location phrase, such as "in your Claude config directory"
POINTER_TRIGGER = re.compile(
    r"^- \[?`(on_demand/[^`]+)`(?:\]\([^)]+\))?, (?:in your Claude config directory(?: \([^)]*\))?, )?(.+)$"
)


def caller_files(config_dir=CONFIG_DIR):
    """Return every config file that can name an on-demand rule: markdown other than READMEs, and hook scripts."""
    files = [path for path in config_dir.rglob("*.md") if path.name != "README.md"]
    return sorted(files + list((config_dir / "hooks").glob("*.sh")))


def expected_callers(path, config_dir=CONFIG_DIR):
    """Return each file naming an on-demand rule outside a Called by section, with its pointer's trigger or None."""
    target = path.relative_to(config_dir / "rules").as_posix()
    callers = {}
    for source in caller_files(config_dir):
        lines = without_called_by(source.read_text().splitlines())
        if source == path or target not in ON_DEMAND_MENTION.findall("\n".join(lines)):
            continue
        triggers = [match[2] for match in map(POINTER_TRIGGER.match, lines) if match and match[1] == target]
        callers[source.relative_to(config_dir).as_posix()] = triggers[0] if triggers else None
    return callers


def called_by_problems(path, config_dir=CONFIG_DIR):
    """Return problems with an on-demand rule's Called by section: missing, or out of step with its callers."""
    lines = path.read_text().splitlines()
    if CALLED_BY not in lines:
        return [f"end it with a '{CALLED_BY}' section listing each file that names it"]
    section = lines[lines.index(CALLED_BY) + 1 :]
    listed, shapes, problems = {}, set(), []
    for bullet in map(CALLER_BULLET.match, section):
        if not bullet:
            continue
        shape, caller, link, trigger = bullet.groups()
        listed[caller] = trigger
        shapes.add(shape)
        if (path.parent / link).resolve() != (config_dir / caller).resolve():
            problems.append(f"{caller}: link it to its repo path")
    if len(listed) == 1 and shapes != {"This rule is invoked by "}:
        problems.append("word its one caller as 'This rule is invoked by [`<caller>`](<link>), <trigger>'")
    if len(listed) > 1 and (shapes != {"- "} or CALLER_LEAD_IN not in section):
        problems.append(f"open its callers with '{CALLER_LEAD_IN}', then one bullet per caller")
    if list(listed) != sorted(listed, key=lambda caller: not caller.startswith("rules/")):
        problems.append("list rule callers before other callers")
    expected = expected_callers(path, config_dir)
    if set(listed) != set(expected):
        problems.append(f"list exactly these callers: {sorted(expected)}, not {sorted(listed)}")
    problems += [
        f"{caller}: copy its trigger, '{trigger}'"
        for caller, trigger in expected.items()
        if trigger and caller in listed and listed[caller] != trigger
    ]
    return problems


@pytest.mark.parametrize("path", [path for path in RULE_FILES if relative(path).startswith("on_demand/")], ids=relative)
def test_on_demand_rule_lists_its_callers(path):
    """Each on-demand rule ends with a Called by section listing every file that names it, with each trigger."""
    problems = called_by_problems(path)
    assert not problems, f"{relative(path)}: " + "; ".join(problems)


def test_a_missing_caller_or_stale_trigger_is_reported(tmp_path):
    """A Called by section that leaves out a caller, rewords a trigger, or lists a rule caller last, is reported."""
    (tmp_path / "rules" / "on_demand").mkdir(parents=True)
    (tmp_path / "hooks").mkdir()
    rule = tmp_path / "rules" / "on_demand" / "guide.md"
    (tmp_path / "rules" / "caller.md").write_text(
        "- [`on_demand/guide.md`](on_demand/guide.md), in your Claude config directory, before acting.\n"
    )
    (tmp_path / "hooks" / "block.sh").write_text("echo 'read on_demand/guide.md first'\n")
    caller = "- [`rules/caller.md`](../caller.md), before acting.\n"
    hook = "- [`hooks/block.sh`](../../hooks/block.sh), when it blocks.\n"
    rule.write_text(f"{CALLED_BY}\n\n{CALLER_LEAD_IN}\n\n{caller}{hook}")
    assert not called_by_problems(rule, tmp_path)
    rule.write_text(f"{CALLED_BY}\n\n{caller}{hook}")
    assert any(CALLER_LEAD_IN in problem for problem in called_by_problems(rule, tmp_path))
    rule.write_text(f"{CALLED_BY}\n\n{caller}")
    assert any("list exactly these callers" in problem for problem in called_by_problems(rule, tmp_path))
    rule.write_text(f"{CALLED_BY}\n\n{CALLER_LEAD_IN}\n\n{caller.replace('acting', 'work')}{hook}")
    assert called_by_problems(rule, tmp_path) == ["rules/caller.md: copy its trigger, 'before acting.'"]
    rule.write_text(f"{CALLED_BY}\n\n{CALLER_LEAD_IN}\n\n{hook}{caller}")
    assert called_by_problems(rule, tmp_path) == ["list rule callers before other callers"]


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


def unlinked_pointers(text, folder):
    """Return each pointer in text that isn't a link, relative to folder, to its target's place in the repo."""
    problems = []
    for line in text.splitlines():
        if not POINTER.match(line):
            continue
        link = LINKED_POINTER.match(line)
        if not link or (folder / link.group(2)).resolve() != resolve(link.group(1)).resolve():
            problems.append(line)
    return problems


@pytest.mark.parametrize("path", RULE_FILES, ids=relative)
def test_rule_pointers_link_to_their_target(path):
    """Each pointer in a rule links to its target's place in the repo, so a reader browsing the repo can open it."""
    problems = unlinked_pointers(path.read_text(), path.parent)
    assert not problems, f"{relative(path)}: link each pointer to its target's repo path: {problems}"


def test_an_unlinked_or_misdirected_pointer_is_reported():
    """A pointer in backticks only, or linked to the wrong file, is reported, and a correct link isn't."""
    target = "on_demand/01_standards/git.md"
    good = f"- [`{target}`](../../{target}), before git."
    bare = f"- `{target}`, before git."
    wrong = f"- [`{target}`](../{target}), before git."
    folder = RULES_DIR / "always_on" / "01_standards"
    assert unlinked_pointers("\n".join([good, bare, wrong]), folder) == [bare, wrong]


# a backticked path into a 02_preferences/ folder, which a default install leaves out
PREFERENCE_PATH = re.compile(r"`[^`\n]*preferences/[^`\n]*`")


def preference_paths(text):
    """Return each backticked path into a 02_preferences/ folder that the text names."""
    return PREFERENCE_PATH.findall(text)


def test_preference_paths_are_found_in_any_backticks():
    """A pointer bullet, a table cell or prose naming a 02_preferences/ path is caught, and other paths aren't."""
    text = "- `on_demand/02_preferences/x.md`, when\n| `_templates/preferences/y` |\nsee `rules/always_on/z.md`"
    assert preference_paths(text) == ["`on_demand/02_preferences/x.md`", "`_templates/preferences/y`"]


# working-file folders that only the working-files preference names, since an install without it never writes there
WORKING_FILE_FOLDERS = re.compile(r"\.claude_work/|~/_drafts/|~/_errors/")


@pytest.mark.parametrize(
    "find", [preference_paths, WORKING_FILE_FOLDERS.findall], ids=["preference", "working_file_folder"]
)
def test_no_standard_file_names_what_only_preferences_hold(find):
    """Only preferences name a 02_preferences/ path or a working-file folder, which PREFERENCES=0 leaves out."""
    problems = [
        f"{path}: {found}"
        for path in sorted(tracked_config_files())
        if not path.endswith("README.md")
        for found in find((CONFIG_DIR / path).read_text())
    ]
    assert not problems, "standard files name what only preferences hold:\n" + "\n".join(problems)


def test_a_short_child_passes_once_its_guide_is_split_by_kind(tmp_path):
    """A guide whose team conventions moved out may leave short children, on both the guide's side and the team's."""
    (tmp_path / "path_scoped" / "style_guides").mkdir(parents=True)
    (tmp_path / "path_scoped" / "style_guides" / "tool.md").write_text("- `_short.md`\n")
    (tmp_path / "path_scoped" / "style_guides" / "tool_team_conventions.md").write_text(
        "- `_short_team_conventions.md`\n"
    )
    folder = tmp_path / "on_demand" / "style_guides" / "tool"
    folder.mkdir(parents=True)
    for child in ("_short.md", "_short_team_conventions.md"):
        (folder / child).write_text("x\n" * 5)
    for child in ("_short.md", "_short_team_conventions.md"):
        assert not child_problems(folder / child, tmp_path), child
    # a team child is named by the team conventions file, not the guide
    (tmp_path / "path_scoped" / "style_guides" / "tool_team_conventions.md").write_text("no pointers\n")
    assert "the parent must name this child in a pointer" in child_problems(
        folder / "_short_team_conventions.md", tmp_path
    )
    (tmp_path / "path_scoped" / "style_guides" / "tool_team_conventions.md").write_text(
        "- `_short_team_conventions.md`\n"
    )
    # without a team conventions file, the guide isn't split, so its short child still fails the floor
    (tmp_path / "path_scoped" / "style_guides" / "tool_team_conventions.md").unlink()
    problems = child_problems(tmp_path / "on_demand" / "style_guides" / "tool" / "_short.md", tmp_path)
    assert any(f"{MIN_CHILD_LINES} or more lines" in problem for problem in problems)


def team_convention_pairs(rules_dir=RULES_DIR):
    """Return each path-scoped team conventions file with the guide beside it, paired by name."""
    teams = (rules_dir / "path_scoped" / "style_guides").rglob(f"*{TEAM_SUFFIX}.md")
    return [(team, team.with_name(team.name.replace(TEAM_SUFFIX, ""))) for team in teams]


def globs_problem(team, guide):
    """Return why a team conventions file won't load with its guide, or None if their paths: lists match."""
    if not guide.exists():
        return f"{team.name} has no guide beside it named {guide.name}"
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
    for name, glob in (("tool", "**/*.sql"), ("tool_team_conventions", "**/*.py")):
        (tmp_path / f"{name}.md").write_text(f'---\npaths:\n  - "{glob}"\n---\n# Tool\n')
    team, guide = tmp_path / "tool_team_conventions.md", tmp_path / "tool.md"
    assert "different paths" in globs_problem(team, guide)
    # two files with no paths: match each other, but neither would load, so that's caught too
    for path in (team, guide):
        path.write_text("# Tool\n")
    assert "no paths: list" in globs_problem(team, guide)


KINDS = {"01_standards", "02_preferences"}
# style guides sit in one folder per load time, and a team convention shows its kind by a _team_conventions name
STYLE_GUIDE_HOMES = {"path_scoped/style_guides", "on_demand/style_guides"}


def misplaced_rules(rules_dir=RULES_DIR):
    """Return each rule that sits outside a kind folder, or a style guide home, inside its load-time folder."""
    rules = sorted(path for path in rules_dir.rglob("*.md") if path.name != "README.md")
    return [path for path in rules if path.relative_to(rules_dir).parts[1] not in KINDS | {"style_guides"}]


def test_every_rule_sits_in_a_kind_folder():
    """Every rule is under a kind folder or style_guides/, so its kind shows in its path or name."""
    assert not misplaced_rules(), "rules outside a kind folder: " + ", ".join(map(relative, misplaced_rules()))


def stray_style_guide_folders(rules_dir=RULES_DIR):
    """Return each style_guides/ folder that isn't one of the two homes."""
    folders = (path.relative_to(rules_dir).as_posix() for path in rules_dir.rglob("style_guides") if path.is_dir())
    return sorted(folder for folder in folders if folder not in STYLE_GUIDE_HOMES)


def test_style_guides_live_only_in_their_two_homes():
    """Style guides sit only in path_scoped/style_guides/ and on_demand/style_guides/, so a topic has one place."""
    assert not stray_style_guide_folders(), "move these into a style guide home: " + ", ".join(
        stray_style_guide_folders()
    )


def test_a_style_guide_folder_under_a_kind_folder_is_reported(tmp_path):
    """A style_guides/ folder inside a kind folder is caught, and the two homes aren't."""
    for folder in (*STYLE_GUIDE_HOMES, "path_scoped/01_standards/style_guides"):
        (tmp_path / folder).mkdir(parents=True)
    assert stray_style_guide_folders(tmp_path) == ["path_scoped/01_standards/style_guides"]


def test_a_rule_outside_a_kind_folder_is_reported(tmp_path):
    """A rule straight under a load-time folder's topic folder is caught."""
    (tmp_path / "always_on" / "conduct").mkdir(parents=True)
    (tmp_path / "always_on" / "conduct" / "rule.md").write_text("# Rule\n")
    assert misplaced_rules(tmp_path) == [tmp_path / "always_on" / "conduct" / "rule.md"]
