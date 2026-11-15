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
CONFIG_FILE = "src/claude/rules/always_on/conduct/example.md\ndocs/other.md"
# an on-demand rule, which needs the spec but not the criteria
ON_DEMAND_FILE = "src/claude/rules/on_demand/example.md"
CRITERIA = (
    "\n## :balance_scale: Evaluation criteria\n\n- :triangular_flag_on_post: **Red flags:** none.\n"
    "- :toolbox: **Shape:** on demand.\n- :test_tube: **Working:** trial at the next review.\n"
)
DEFAULT_CRITERIA = (
    "\n## :balance_scale: Evaluation criteria\n\nNot applicable: this PR changes no always-on or enforcing file.\n"
)
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
        # the section must replace the template's default line
        (DETAILS + bullets(1) + SPEC + DEFAULT_CRITERIA + NEXT_SECTION, CONFIG_FILE, 1),
        # CLAUDE.md and hooks count as always-on or enforcing, so they need the section too
        (DETAILS + bullets(4) + SPEC + NEXT_SECTION, "src/claude/CLAUDE.md", 1),
        (DETAILS + bullets(4) + SPEC + NEXT_SECTION, "src/claude/hooks/example.sh", 1),
        # an on-demand or path-scoped change needs only the spec
        (DETAILS + bullets(4) + SPEC + NEXT_SECTION, ON_DEMAND_FILE, 0),
        (DETAILS + bullets(4) + SPEC + NEXT_SECTION, "src/claude/rules/path_scoped/x.md", 0),
        # a PR that doesn't touch src/claude/ needs no section, and nor does a run without a file list
        (DETAILS + bullets(4) + NEXT_SECTION, "docs/other.md\nsrc/sh/x.sh", 0),
        (DETAILS + bullets(4) + NEXT_SECTION, "", 0),
    ],
)
def test_always_on_changes_require_evaluation_criteria(description, changed_files, expected_code):
    """Only a PR that changes an always-on or enforcing file must answer the Evaluation criteria."""
    result = run_check(description, changed_files)
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"
    if expected_code == 1:
        assert CRITERIA_NAME in result.stdout, f"the reason should name the missing section: {result.stdout}"


# a heading still in the older sentence case, which matches too
OLD_SPEC = "\n## :robot: Claude plan spec: requirements and design\n\n- **Hook:** blocks a stop once.\n"


# the template's note and show/hide wrapper, which authors keep, so they aren't an answer on their own
# MoSCoW: Must — a reviewer can only check a config PR against its spec if the PR carries one
@pytest.mark.parametrize(
    ("spec", "changed_files", "expected_code"),
    [
        # a filled spec, a stated "Not applicable" or an older sentence-case heading passes
        (SPEC, CONFIG_FILE, 0),
        (SPEC_HEADING + "Not applicable: a typo fix.\n", CONFIG_FILE, 0),
        (OLD_SPEC, CONFIG_FILE, 0),
        # a missing spec, or one still holding the template's default line, fails a config PR
        ("", CONFIG_FILE, 1),
        (SPEC_HEADING + "Not applicable: this PR changes nothing under `src/claude/`.\n", CONFIG_FILE, 1),
        # an on-demand change still needs a spec, but a PR that doesn't touch src/claude/ doesn't
        ("", ON_DEMAND_FILE, 1),
        ("", "docs/other.md", 0),
    ],
)
def test_config_changes_require_a_spec(spec, changed_files, expected_code):
    """A PR that changes src/claude/ must keep the Spec section and replace its default line, for the reviewer."""
    result = run_check(DETAILS + bullets(1) + spec + CRITERIA + NEXT_SECTION, changed_files)
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"
    if expected_code == 1:
        assert SPEC_NAME in result.stdout, f"the reason should name the spec section: {result.stdout}"


TEMPLATE = (REPO_ROOT / ".github" / "pull_request_template.md").read_text()


# MoSCoW: Must — the template's defaults must suit a docs PR, but never let a config PR through unanswered
@pytest.mark.parametrize(
    ("changed_files", "expected_code", "reason"),
    [
        pytest.param("docs/other.md", 0, None, id="docs_pr_passes_as_is"),
        pytest.param(ON_DEMAND_FILE, 1, f"default 'Not applicable' line in '{SPEC_NAME}'", id="config_spec"),
        pytest.param(
            CONFIG_FILE, 1, f"default 'Not applicable' line in '{CRITERIA_NAME}'", id="always_on_keeps_criteria"
        ),
    ],
)
def test_the_template_defaults_pass_only_when_the_section_isnt_needed(changed_files, expected_code, reason):
    """The template, unedited, passes a docs-only PR, and fails a config PR that keeps a default 'Not applicable'."""
    result = run_check(TEMPLATE, changed_files)
    assert result.returncode == expected_code, f"unexpected result for {changed_files!r}:\n{result.stdout}"
    assert reason is None or reason in result.stdout, f"the reason should name the default left in:\n{result.stdout}"
