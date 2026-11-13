"""Checks each installed file under src/claude/ opens with a created line (see maintenance/file_headers.md)."""

import os
import re
import subprocess
from datetime import date

import pytest
from _paths import REPO_ROOT

# no header: a .template file is copied into each new file made from it
TEMPLATE_SUFFIX = ".template"


def tracked_files():
    """Return every file git tracks under src/claude/, which make install copies, minus any .template file."""
    # ignore the user's git config, so a setting like core.quotePath can't change the paths listed
    env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
    command = ["git", "ls-files", "src/claude"]
    output = subprocess.run(command, cwd=REPO_ROOT, env=env, capture_output=True, text=True, check=True).stdout
    return [path for path in output.splitlines() if not path.endswith(TEMPLATE_SUFFIX)]


def header_line(path, root):
    """Return the line where the header belongs: line 1, after a shebang or YAML '---', or after frontmatter."""
    lines = (root / path).read_text().splitlines()
    if path.endswith(".md") and lines and lines[0] == "---":
        # a markdown file's frontmatter is YAML, so the header follows its closing '---' to stay out of the YAML
        start = lines.index("---", 1) + 1
    else:
        start = 1 if lines and (lines[0].startswith("#!") or lines[0] == "---") else 0
    return lines[start] if start < len(lines) else ""


def header_problem(path, root=REPO_ROOT):
    """Return what's wrong with a file's created line, or None if it holds a real date no later than today."""
    line = header_line(path, root)
    pattern = r"<!-- created: (\d{4}-\d{2}-\d{2}) -->" if path.endswith(".md") else r"# created: (\d{4}-\d{2}-\d{2})"
    match = re.fullmatch(pattern, line)
    if not match:
        return f"{path}: expected the 'created' header line here, got {line!r}"
    try:
        created = date.fromisoformat(match.group(1))
    except ValueError as error:  # the regex allows impossible dates like 2026-13-45
        return f"{path}: not a real date: {error}"
    if created > date.today():
        return f"{path}: created ({created}) is in the future"
    return None


# one case for the whole repo, so adding a file doesn't change the test count
# MoSCoW: Must — every installed file needs a valid created line
def test_every_installed_file_has_a_created_line():
    """Every installed file opens with a created line holding a real date that isn't in the future."""
    problems = [problem for path in tracked_files() if (problem := header_problem(path))]
    assert not problems, "fix these file headers:\n" + "\n".join(problems)


# MoSCoW: Must — a check that never reports a problem would pass every file
@pytest.mark.parametrize(
    ("header", "problem"),
    [
        ("# no header at all", "expected the 'created' header line"),
        ("# created: 2026-13-45", "not a real date"),  # month 13
        ("# created: 2999-01-01", "in the future"),
    ],
)
def test_a_bad_header_is_reported(tmp_path, header, problem):
    """A missing created line, an impossible date and a future date are each reported as that problem."""
    (tmp_path / "script.sh").write_text(f"#!/bin/bash\n{header}\n")
    assert problem in (header_problem("script.sh", tmp_path) or ""), f"this header should be reported as {problem!r}"


MARKDOWN_HEADER = "<!-- created: 2026-11-11 -->\n"
FRONTMATTER = "---\npaths:\n  - '*.sql'\n---\n"


# MoSCoW: Must — path-scoped rules keep their header after the frontmatter, and must pass
def test_a_markdown_header_after_the_frontmatter_passes(tmp_path):
    """A markdown created line straight after the frontmatter's closing '---' is accepted."""
    (tmp_path / "rule.md").write_text(FRONTMATTER + MARKDOWN_HEADER + "# Title\n")
    reported = header_problem("rule.md", tmp_path)
    assert reported is None, f"a header after the frontmatter should pass, got {reported!r}"


# MoSCoW: Must — a header inside the frontmatter is parsed as YAML keys and shown by GitHub
def test_a_markdown_header_inside_the_frontmatter_is_reported(tmp_path):
    """A markdown created line inside the '---' block is reported, so it can't land in the YAML."""
    (tmp_path / "rule.md").write_text("---\n" + MARKDOWN_HEADER + "paths:\n  - '*.sql'\n---\n# Title\n")
    reported = header_problem("rule.md", tmp_path) or ""
    assert "expected the 'created' header line" in reported, f"a header in the frontmatter should fail: {reported!r}"
