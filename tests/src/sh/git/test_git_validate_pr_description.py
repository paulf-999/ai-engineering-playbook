# version: 1.6.0
# created: 2026-11-02
# updated: 2026-11-13
"""Tests for the PR description check: a src/claude/ PR carries its spec, and an always-on one the criteria."""

import os
import subprocess

import pytest
from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "git" / "git_validate_pr_description.sh"
DETAILS = "## :mag: (Optional) Additional Details\n\n"
NEXT_SECTION = "\n## :hammer_and_wrench: Type of PR Change\n\n- [x] Documentation\n"
# the section names the script's reasons quote, kept here so renaming a section changes one line
CRITERIA_NAME = "Evaluation Criteria"
SPEC_NAME = "Plan Spec"


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


# an always-on rule, which needs the spec and the evaluation criteria
CONFIG_FILE = "src/claude/rules/02_conduct/example.md\ndocs/other.md"
# an on-demand rule, which needs the spec but not the criteria
ON_DEMAND_FILE = "src/claude/rules/_rules_on_demand/example.md"
CRITERIA = (
    "\n## :balance_scale: Evaluation criteria\n\n- :triangular_flag_on_post: **Red flags:** none.\n"
    "- :toolbox: **Shape:** on demand.\n- :test_tube: **Working:** trial at the next review.\n"
)
PLACEHOLDER = "\n## :balance_scale: Evaluation criteria\n\n[Three bullets, one per stage.]\n"
# the Spec section's heading, and a filled Spec section, which a config PR also needs
SPEC_HEADING = "\n## :robot: Claude: Plan Spec (spec.md) - Requirements and Design\n\n"
SPEC = SPEC_HEADING + "- **Hook:** blocks a stop once after files change.\n"


# MoSCoW: Must — a PR changing an always-on or enforcing file must answer the evaluation criteria
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
        # CLAUDE.md and hooks count as always-on or enforcing, so they need the section too
        (DETAILS + bullets(4) + SPEC + NEXT_SECTION, "src/claude/CLAUDE.md", 1),
        (DETAILS + bullets(4) + SPEC + NEXT_SECTION, "src/claude/hooks/example.sh", 1),
        # an on-demand or path-scoped change needs only the spec
        (DETAILS + bullets(4) + SPEC + NEXT_SECTION, ON_DEMAND_FILE, 0),
        (DETAILS + bullets(4) + SPEC + NEXT_SECTION, "src/claude/rules/_path_scoped_rules/x.md", 0),
        # a PR that doesn't touch src/claude/ needs no section, and nor does a run without a file list
        (DETAILS + bullets(4) + NEXT_SECTION, "docs/other.md\nsrc/sh/x.sh", 0),
        (DETAILS + bullets(4) + NEXT_SECTION, "", 0),
    ],
)
def test_always_on_changes_require_evaluation_criteria(description, changed_files, expected_code):
    """Only a PR that changes an always-on or enforcing file must answer the Evaluation criteria with a bullet."""
    result = run_check(description, changed_files)
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"
    if expected_code == 1:
        assert CRITERIA_NAME in result.stdout, f"the reason should name the missing section: {result.stdout}"


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
        # a PR that doesn't touch an always-on or enforcing file isn't checked for criteria placeholders
        (DETAILS + bullets(1) + TEMPLATE_CRITERIA + NEXT_SECTION, "docs/other.md", 0),
        (DETAILS + bullets(1) + SPEC + TEMPLATE_CRITERIA + NEXT_SECTION, ON_DEMAND_FILE, 0),
    ],
)
def test_config_changes_reject_unfilled_criteria(description, changed_files, expected_code):
    """A config PR whose Evaluation criteria still holds the template's placeholders, or no answer, exits 1."""
    result = run_check(description, changed_files)
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"
    if expected_code == 1:
        assert CRITERIA_NAME in result.stdout, f"the reason should name the section: {result.stdout}"


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
        # an example inside a fenced code block isn't an answer
        (SPEC_HEADING + "```markdown\n- **Hook:** an example.\n```\n", CONFIG_FILE, 1),
        # an on-demand change still needs a spec, but a PR that doesn't touch src/claude/ doesn't
        ("", ON_DEMAND_FILE, 1),
        ("", "docs/other.md", 0),
    ],
)
def test_config_changes_require_a_spec(spec, changed_files, expected_code):
    """A PR that changes src/claude/ must fill the Spec section, so the reviewer can check the diff against it."""
    result = run_check(DETAILS + bullets(1) + spec + CRITERIA + NEXT_SECTION, changed_files)
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"
    if expected_code == 1:
        assert SPEC_NAME in result.stdout, f"the reason should name the spec section: {result.stdout}"


# MoSCoW: Must — the reason must name each placeholder left in, so the author knows what to fill
@pytest.mark.parametrize(
    ("description", "placeholders"),
    [
        (SPEC + TEMPLATE_CRITERIA, ("[one sentence saying why.]", "[✅ Aligned or ❌ Misaligned]", "[why]")),
        (SPEC_PLACEHOLDER + CRITERIA, ("[Paste the change's spec.md.]",)),
    ],
)
def test_unfilled_reason_lists_each_placeholder(description, placeholders):
    """The failure reason quotes every square-bracket placeholder left in the Plan Spec or Evaluation Criteria."""
    result = run_check(DETAILS + bullets(1) + description + NEXT_SECTION, CONFIG_FILE)
    assert result.returncode == 1, f"a section with placeholders left in should fail: {result.stdout}"
    for placeholder in placeholders:
        assert placeholder in result.stdout, f"the reason should list {placeholder}: {result.stdout}"
