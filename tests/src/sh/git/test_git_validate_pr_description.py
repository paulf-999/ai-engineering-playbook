# version: 1.5.2
# created: 2026-11-02
# updated: 2026-11-13
"""Tests for the PR description check, which makes a PR that changes src/claude/ answer the evaluation criteria."""

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
CRITERIA = (
    "\n## :balance_scale: Evaluation criteria\n\n- :triangular_flag_on_post: **Red flags:** none.\n"
    "- :toolbox: **Shape:** on demand.\n- :test_tube: **Working:** trial at the next review.\n"
)
PLACEHOLDER = "\n## :balance_scale: Evaluation criteria\n\n[Three bullets, one per stage.]\n"
# the Spec section's heading, and a filled Spec section, which a config PR also needs
SPEC_HEADING = "\n## :robot: Claude: Plan Spec (spec.md) - Requirements and Design\n\n"
SPEC = SPEC_HEADING + "- **Hook:** blocks a stop once after files change.\n"


# MoSCoW: Must — a PR changing the installed Claude config must answer the evaluation criteria
@pytest.mark.parametrize(
    ("description", "changed_files", "expected_code"),
    [
        # a config change with answered criteria passes
        (DETAILS + bullets(5) + SPEC + CRITERIA + NEXT_SECTION, CONFIG_FILE, 0),
        # headings match whatever their case, so a Title Case heading passes
        (DETAILS + bullets(1) + SPEC + CRITERIA.replace("criteria", "Criteria", 1) + NEXT_SECTION, CONFIG_FILE, 0),
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
        assert "Evaluation Criteria" in result.stdout, f"the reason should name the missing section: {result.stdout}"


TABLE_HEADER = "| Review area | Standard | Result | Why |\n|---|---|---|---|\n"
TEMPLATE_CRITERIA = (
    "\n## :balance_scale: Evaluation criteria\n\n> [!TIP]\n> **✅ Safe to approve:** [one sentence saying why.]\n\n"
    + TABLE_HEADER
    + "| :toolbox: Shape | No duplicate | [✅ Aligned or ❌ Misaligned] | [why] |\n"
)
FILLED_CRITERIA = (
    "\n## :balance_scale: Evaluation criteria\n\n> [!TIP]\n> **✅ Safe to approve:** no red flags.\n\n"
    + TABLE_HEADER
    + "| :toolbox: Shape | No duplicate | ✅ Aligned | Unique, per the [rules](https://x.io/r.md). |\n"
    + "| :test_tube: Working | Trial | ⏳ Not yet due | [x] due at the next review, with `[x]` shown as code. |\n"
)
SEPARATOR_ONLY = "\n## :balance_scale: Evaluation criteria\n\n|---|---|\n"


# MoSCoW: Must — a config PR must not pass with the template's example table left unfilled
@pytest.mark.parametrize(
    ("description", "changed_files", "expected_code"),
    [
        # the template's table and callout left as they are fail
        (DETAILS + bullets(1) + TEMPLATE_CRITERIA + NEXT_SECTION, CONFIG_FILE, 1),
        # a filled table passes, with links, inline code, checkboxes and the alert marker allowed
        (DETAILS + bullets(1) + SPEC + FILLED_CRITERIA + NEXT_SECTION, CONFIG_FILE, 0),
        # a table separator alone holds no answer
        (DETAILS + bullets(1) + SEPARATOR_ONLY + NEXT_SECTION, CONFIG_FILE, 1),
        # a PR that doesn't touch src/claude/ isn't checked for placeholders
        (DETAILS + bullets(1) + TEMPLATE_CRITERIA + NEXT_SECTION, "docs/other.md", 0),
    ],
)
def test_config_changes_reject_unfilled_criteria(description, changed_files, expected_code):
    """A config PR whose Evaluation criteria still holds the template's placeholders, or no answer, exits 1."""
    result = run_check(description, changed_files)
    assert result.returncode == expected_code, result.stdout
    if expected_code == 1:
        assert "Evaluation Criteria" in result.stdout, f"the reason should name the section: {result.stdout}"


# MoSCoW: Must — the reason must name each placeholder left in, so the author knows what to fill
def test_unfilled_criteria_reason_lists_each_placeholder():
    """The failure reason quotes every square-bracket placeholder left in the Evaluation criteria table."""
    result = run_check(DETAILS + bullets(1) + TEMPLATE_CRITERIA + NEXT_SECTION, CONFIG_FILE)
    assert result.returncode == 1, result.stdout
    for placeholder in ("[one sentence saying why.]", "[✅ Aligned or ❌ Misaligned]", "[why]"):
        assert placeholder in result.stdout, f"the reason should list {placeholder}: {result.stdout}"


# a heading still in the older sentence case, which matches too
OLD_SPEC = "\n## :robot: Claude plan spec: requirements and design\n\n- **Hook:** blocks a stop once.\n"
# the template's note and show/hide wrapper, which authors keep, so they aren't an answer on their own
SPEC_DETAILS = (
    "> [!NOTE]\n> **What is `spec.md`?** The approved plan's requirements and design.\n\n"
    "<details>\n<summary>Approved plan's spec</summary>\n\n</details>\n"
)
FILLED_DETAILS = SPEC_DETAILS.replace("</details>", "- **Hook:** blocks a stop once.\n\n</details>")
SPEC_PLACEHOLDER = SPEC_HEADING + "[Paste the change's spec.md.]\n"


# MoSCoW: Must — a reviewer can only check a config PR against its spec if the PR carries one
@pytest.mark.parametrize(
    ("spec", "changed_files", "expected_code"),
    [
        # a filled spec, a stated "Not applicable", an older sentence-case heading or a spec in the wrapper passes
        (SPEC, CONFIG_FILE, 0),
        (SPEC_HEADING + "Not applicable: a typo fix.\n", CONFIG_FILE, 0),
        (OLD_SPEC, CONFIG_FILE, 0),
        (SPEC_HEADING + FILLED_DETAILS, CONFIG_FILE, 0),
        # a missing, empty or unfilled spec fails a config PR, as does the wrapper and callout alone
        ("", CONFIG_FILE, 1),
        (SPEC_HEADING, CONFIG_FILE, 1),
        (SPEC_PLACEHOLDER, CONFIG_FILE, 1),
        (SPEC_HEADING + SPEC_DETAILS, CONFIG_FILE, 1),
        # a PR that doesn't touch src/claude/ needs no spec
        ("", "docs/other.md", 0),
    ],
)
def test_config_changes_require_a_spec(spec, changed_files, expected_code):
    """A PR that changes src/claude/ must fill the Spec section, so the reviewer can check the diff against it."""
    result = run_check(DETAILS + bullets(1) + spec + CRITERIA + NEXT_SECTION, changed_files)
    assert result.returncode == expected_code, result.stdout
    if expected_code == 1:
        assert "Plan Spec" in result.stdout, f"the reason should name the spec section: {result.stdout}"
