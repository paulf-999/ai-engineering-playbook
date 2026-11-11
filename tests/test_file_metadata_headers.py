# version: 1.4.1
# created: 2026-10-30
# updated: 2026-11-11
"""Checks every tracked file opens with a version/created/updated header (see docs/maintenance/file_headers.md)."""

import os
import re
import subprocess
from datetime import date

import pytest
from _paths import REPO_ROOT

HEADER_FIELDS = ("version", "created", "updated")

# no header: copied into every new PR or issue body, or kept verbatim so GitHub detects the licence
EXEMPT = {
    "LICENSE",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
}

# no header either: a .template file is copied into each new file made from it, like the PR template
TEMPLATE_SUFFIX = ".template"


def tracked_files():
    """Return every file git tracks in the repo, minus the exempt ones and any .template file."""
    # ignore the user's git config, so a setting like core.quotePath can't change the paths listed
    env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
    command = ["git", "ls-files"]
    output = subprocess.run(command, cwd=REPO_ROOT, env=env, capture_output=True, text=True, check=True).stdout
    return [path for path in output.splitlines() if path not in EXEMPT and not path.endswith(TEMPLATE_SUFFIX)]


def header_lines(path, root):
    """Return the three lines where the header belongs: line 1, after a shebang or YAML '---', or after frontmatter."""
    lines = (root / path).read_text().splitlines()
    if path.endswith(".md") and lines and lines[0] == "---":
        # a markdown file's frontmatter is YAML, so the header follows its closing '---' to stay out of the YAML
        start = lines.index("---", 1) + 1
    else:
        start = 1 if lines and (lines[0].startswith("#!") or lines[0] == "---") else 0
    return lines[start : start + 3]


def header_pattern(path, field):
    """Return the regex for one header line, using HTML comments in markdown and '#' comments elsewhere."""
    value = r"\d+\.\d+\.\d+" if field == "version" else r"\d{4}-\d{2}-\d{2}"
    if path.endswith(".md"):
        return rf"<!-- {field}: ({value}) -->"
    return rf"# {field}: ({value})"


def header_problem(path, root=REPO_ROOT):
    """Return what's wrong with a file's header, or None if it has version, created and updated lines in order."""
    values = {}
    for line, field in zip(header_lines(path, root), HEADER_FIELDS):
        match = re.fullmatch(header_pattern(path, field), line)
        if not match:
            return f"{path}: expected the '{field}' header line here, got {line!r}"
        values[field] = match.group(1)
    if len(values) < len(HEADER_FIELDS):
        return f"{path}: the header needs version, created and updated lines"
    try:
        created, updated = date.fromisoformat(values["created"]), date.fromisoformat(values["updated"])
    except ValueError as error:  # the regex allows impossible dates like 2026-13-45
        return f"{path}: not a real date: {error}"
    if created > updated:
        return f"{path}: updated ({updated}) is earlier than created ({created})"
    return None


# one case for the whole repo, so adding a file doesn't change the test count
# MoSCoW: Must — every tracked file needs a valid header
def test_every_tracked_file_has_a_metadata_header():
    """Every tracked file has version, created and updated lines in order, with real dates and created <= updated."""
    problems = [problem for path in tracked_files() if (problem := header_problem(path))]
    assert not problems, "fix these file headers:\n" + "\n".join(problems)


# MoSCoW: Must — a check that never reports a problem would pass every file
@pytest.mark.parametrize(
    ("header", "problem"),
    [
        ("# no header at all", "expected the 'version' header line"),
        ("# version: 1.0.0\n# created: 2026-13-45\n# updated: 2026-10-31", "not a real date"),  # month 13
        ("# version: 1.0.0\n# created: 2026-10-31\n# updated: 2026-10-30", "earlier than created"),
    ],
)
def test_a_bad_header_is_reported(tmp_path, header, problem):
    """A missing header, an impossible date, and an updated date before created are each reported as that problem."""
    (tmp_path / "script.sh").write_text(f"#!/bin/bash\n{header}\n")
    assert problem in (header_problem("script.sh", tmp_path) or ""), f"this header should be reported as {problem!r}"


MARKDOWN_HEADER = "<!-- version: 1.0.0 -->\n<!-- created: 2026-11-11 -->\n<!-- updated: 2026-11-11 -->\n"
FRONTMATTER = "---\npaths:\n  - '*.sql'\n---\n"


# MoSCoW: Must — path-scoped rules keep their header after the frontmatter, and must pass
def test_a_markdown_header_after_the_frontmatter_passes(tmp_path):
    """A markdown header straight after the frontmatter's closing '---' is accepted."""
    (tmp_path / "rule.md").write_text(FRONTMATTER + MARKDOWN_HEADER + "# Title\n")
    reported = header_problem("rule.md", tmp_path)
    assert reported is None, f"a header after the frontmatter should pass, got {reported!r}"


# MoSCoW: Must — a header inside the frontmatter is parsed as YAML keys and shown by GitHub
def test_a_markdown_header_inside_the_frontmatter_is_reported(tmp_path):
    """A markdown header inside the '---' block is reported, so it can't land in the YAML."""
    (tmp_path / "rule.md").write_text("---\n" + MARKDOWN_HEADER + "paths:\n  - '*.sql'\n---\n# Title\n")
    reported = header_problem("rule.md", tmp_path) or ""
    assert "expected the 'version' header line" in reported, f"a header in the frontmatter should fail: {reported!r}"
