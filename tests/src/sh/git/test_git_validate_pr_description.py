# version: 1.2.0
# created: 2026-11-02
# updated: 2026-11-05
"""Tests for the PR description check, which keeps PR descriptions short and their links working."""

import os
import subprocess

import pytest
from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "git" / "git_validate_pr_description.sh"
DETAILS = "## :mag: (Optional) Additional Details\n\n"
NEXT_SECTION = "\n## :hammer_and_wrench: Type of PR Change\n\n- [x] Documentation\n"


def run_check(description, changed_files=""):
    """Run the PR description check from the repo root and return the full result."""
    return subprocess.run(
        [str(SCRIPT), description, changed_files], cwd=REPO_ROOT, capture_output=True, text=True, check=False
    )


def bullets(count):
    """Return a list of top-level markdown bullets."""
    return "".join(f"- **Point {n}:** detail.\n" for n in range(1, count + 1))


# MoSCoW: Must — good PR descriptions must not be blocked
@pytest.mark.parametrize(
    "description",
    [
        # exactly 5 bullets, the most allowed
        DETAILS + bullets(5) + NEXT_SECTION,
        # child bullets and other sections' bullets don't count
        DETAILS + bullets(5) + "  - **Child:** detail.\n" + NEXT_SECTION + bullets(3),
        # no details section at all, such as a Dependabot PR
        "Bumps a dependency.",
        "",
        # full links, in-page anchors and links shown as code are fine
        DETAILS + "- See [#7](https://github.com/o/r/issues/7) and [scores](#-scores).\n- Never `[x](docs/a.md)`.\n",
        # bullets and links inside a fenced code block are an example, not content
        DETAILS + "- **Example:** a bad description.\n\n```markdown\n" + bullets(6) + "[x](docs/a.md)\n```\n",
    ],
)
def test_valid_descriptions_pass(description):
    """A description with 5 or fewer detail bullets and only full links exits 0."""
    result = run_check(description)
    assert result.returncode == 0, result.stdout


# MoSCoW: Must — bad PR descriptions must be blocked with a reason
@pytest.mark.parametrize(
    ("description", "expected_error"),
    [
        (DETAILS + bullets(6) + NEXT_SECTION, "5 top-level bullets or fewer (it has 6)"),
        (DETAILS + "- See [the page](docs/a.md).\n", "relative links don't work in a PR description: docs/a.md"),
        # links are checked in every section, not just the details
        ("Fixes [the script](../src/sh/x.sh).", "../src/sh/x.sh"),
    ],
)
def test_invalid_descriptions_fail_with_a_reason(description, expected_error):
    """Too many detail bullets, or a relative link anywhere, exits 1 and says what to fix."""
    result = run_check(description)
    assert result.returncode == 1, f"{description!r} should be blocked"
    assert expected_error in result.stdout, f"expected '{expected_error}' in the reason: {result.stdout}"


# MoSCoW: Must — security: a PR description must never run as code
def test_description_with_shell_characters_is_not_executed(tmp_path):
    """The description is treated as text, so shell syntax in it is never run."""
    marker = tmp_path / "should_not_exist"
    description = DETAILS + "- **Run:** $(touch $MARKER) and `touch $MARKER`.\n"
    env = {**os.environ, "MARKER": str(marker)}
    result = subprocess.run(
        [str(SCRIPT), description], cwd=REPO_ROOT, env=env, capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, f"the description is valid once its shell syntax is read as text: {result.stdout}"
    assert not marker.exists(), "shell syntax in the description was run as a command"


CONFIG_FILE = "src/claude/rules/example.md\ndocs/other.md"
CRITERIA = "\n## :scales: Evaluation criteria\n\n- **Cost:** none.\n- **Red flags:** none.\n"
PLACEHOLDER = "\n## :scales: Evaluation criteria\n\n[One bullet per check.]\n"


# MoSCoW: Must — a PR changing the installed Claude config must answer the evaluation criteria
@pytest.mark.parametrize(
    ("description", "changed_files", "expected_code"),
    [
        # a config change with answered criteria passes, and its bullets don't count towards the details limit
        (DETAILS + bullets(5) + CRITERIA + NEXT_SECTION, CONFIG_FILE, 0),
        # a config change without the section fails
        (DETAILS + bullets(4) + NEXT_SECTION, CONFIG_FILE, 1),
        # the section must hold a top-level bullet, not just the template's placeholder or child bullets
        (DETAILS + bullets(1) + PLACEHOLDER + NEXT_SECTION, CONFIG_FILE, 1),
        (DETAILS + bullets(1) + PLACEHOLDER + "  - **Cost:** none.\n" + NEXT_SECTION, CONFIG_FILE, 1),
        # the old bullet inside Additional Details no longer counts
        (DETAILS + "- **Evaluation criteria:**\n  - **Red flags:** none.\n" + NEXT_SECTION, CONFIG_FILE, 1),
        # a PR that doesn't touch src/claude/ needs no section, and nor does a run without a file list
        (DETAILS + bullets(4) + NEXT_SECTION, "docs/other.md\nsrc/sh/x.sh", 0),
        (DETAILS + bullets(4) + NEXT_SECTION, "", 0),
    ],
)
def test_config_changes_require_evaluation_criteria(description, changed_files, expected_code):
    """Only a PR that changes src/claude/ must answer the Evaluation criteria section with a bullet."""
    result = run_check(description, changed_files)
    assert result.returncode == expected_code, result.stdout
    if expected_code == 1:
        assert "Evaluation criteria" in result.stdout, f"the reason should name the missing section: {result.stdout}"
