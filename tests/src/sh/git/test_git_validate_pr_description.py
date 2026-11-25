"""Tests for the PR description check: config PRs need a plan, any plan is complete, and always-on PRs need criteria."""

import os
import subprocess

import pytest
from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "git" / "git_validate_pr_description.sh"
DETAILS = "## :mag: (Optional) Additional Details\n\n"
NEXT_SECTION = "\n## :hammer_and_wrench: Type of PR Change\n\n- [x] Documentation\n"
# the section names the script's reasons quote, kept here so renaming a section changes one line
CRITERIA_NAME = "Evaluation Criteria"
PLAN_NAME = "Claude: Plan"
TEMPLATE = (REPO_ROOT / ".github" / "pull_request_template.md").read_text()


def template_heading(section):
    """Return the quoted "## " heading for a section, as the template's comment names it."""
    return next(part for part in TEMPLATE.split('"') if part.startswith("## ") and section in part)


def run_check(description, changed_files=""):
    """Run the PR description check from the repo root and return the full result."""
    return subprocess.run(
        [str(SCRIPT), description, changed_files], cwd=REPO_ROOT, capture_output=True, text=True, check=False
    )


def bullets(count):
    """Return a list of top-level markdown bullets."""
    return "".join(f"- **Point {n}:** detail.\n" for n in range(1, count + 1))


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


# an always-on rule, which needs the plan and the evaluation criteria
CONFIG_FILE = "src/claude/rules/always_on/conduct/example.md\ndocs/other.md"
# an on-demand rule, which needs the plan but not the criteria
ON_DEMAND_FILE = "src/claude/rules/on_demand/example.md"
CRITERIA = (
    "\n## :balance_scale: Evaluation criteria\n\n- :triangular_flag_on_post: **Red flags:** none.\n"
    "- :toolbox: **Shape:** on demand.\n- :test_tube: **Working:** trial at the next review.\n"
)
# the Plan section's heading, and a filled Plan section, which a config PR also needs
PLAN_HEADING = "\n## :robot: Claude: Plan\n\n"
MENUS = ("intent.md", "spec.md", "plan.md", "measures", "governance")


def menu(name):
    """Return a collapsible menu, as the template's comment lays it out."""
    return f"<details>\n<summary>Show {name}</summary>\n\n- **Hook:** blocks a stop once.\n\n</details>\n\n"


PLAN = PLAN_HEADING + "".join(menu(name) for name in MENUS)
NO_PLAN = PLAN_HEADING + "No saved plan: a typo fix.\n"


@pytest.mark.parametrize(
    ("description", "changed_files", "expected_code"),
    [
        # a config change with answered criteria passes
        (DETAILS + bullets(5) + PLAN + CRITERIA + NEXT_SECTION, CONFIG_FILE, 0),
        # headings match whatever their case, so a Title Case heading passes
        (DETAILS + bullets(1) + PLAN + CRITERIA.replace("criteria", "Criteria", 1) + NEXT_SECTION, CONFIG_FILE, 0),
        # a config change without the section fails
        (DETAILS + bullets(4) + NEXT_SECTION, CONFIG_FILE, 1),
        # CLAUDE.md and hooks count as always-on or enforcing, so they need the section too
        (DETAILS + bullets(4) + PLAN + NEXT_SECTION, "src/claude/CLAUDE.md", 1),
        (DETAILS + bullets(4) + PLAN + NEXT_SECTION, "src/claude/hooks/example.sh", 1),
        # an on-demand or path-scoped change needs only the plan
        (DETAILS + bullets(4) + PLAN + NEXT_SECTION, ON_DEMAND_FILE, 0),
        (DETAILS + bullets(4) + PLAN + NEXT_SECTION, "src/claude/rules/path_scoped/x.md", 0),
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


@pytest.mark.parametrize(
    ("plan", "changed_files", "expected_code"),
    [
        # a filled plan or a stated "No saved plan" passes
        (PLAN, CONFIG_FILE, 0),
        (NO_PLAN, CONFIG_FILE, 0),
        # a missing plan fails a config PR
        ("", CONFIG_FILE, 1),
        # an on-demand change still needs a plan, but a PR that doesn't touch src/claude/ doesn't
        ("", ON_DEMAND_FILE, 1),
        ("", "docs/other.md", 0),
    ],
)
def test_config_changes_require_a_plan(plan, changed_files, expected_code):
    """A PR that changes src/claude/ must have a Plan section, for the reviewer."""
    result = run_check(DETAILS + bullets(1) + plan + CRITERIA + NEXT_SECTION, changed_files)
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"
    if expected_code == 1:
        assert PLAN_NAME in result.stdout, f"the reason should name the plan section: {result.stdout}"


@pytest.mark.parametrize("missing", MENUS)
def test_each_plan_menu_is_required_and_named(missing):
    """A Plan section missing one menu fails, and the message names only that menu."""
    plan = PLAN_HEADING + "".join(menu(name) for name in MENUS if name != missing)
    result = run_check(plan, ON_DEMAND_FILE)
    assert result.returncode == 1, f"a plan without its {missing} menu should fail: {result.stdout}"
    named = [name for name in MENUS if f"'Show {name}'" in result.stdout]
    assert named == [missing], f"the reason should name only the missing menu: {result.stdout}"


@pytest.mark.parametrize(
    ("plan", "expected_code"),
    [
        pytest.param(PLAN_HEADING + "No saved plan:\n", 1, id="no_reason"),
        pytest.param(PLAN_HEADING + "No saved plan:  \r\n", 1, id="blank_reason"),
        pytest.param(PLAN_HEADING + "There is No saved plan: typo.\n", 1, id="reason_mid_line"),
        pytest.param(f"{PLAN_HEADING}<!--\n{''.join(map(menu, MENUS))}-->\n", 1, id="menus_in_a_comment"),
        pytest.param(PLAN_HEADING + "<!-- \nNo saved plan: typo.\n-->\n", 1, id="reason_in_a_comment"),
        pytest.param(f"<!--{PLAN_HEADING}-->\n{''.join(map(menu, MENUS))}", 1, id="heading_in_a_comment"),
        pytest.param(PLAN.replace("<summary>", "See <summary>"), 1, id="summary_mid_line"),
        pytest.param(PLAN.replace("\n", "\r\n"), 0, id="windows_line_endings"),
        pytest.param(NO_PLAN.replace("\n", "\r\n"), 0, id="reason_with_windows_line_endings"),
        pytest.param(PLAN.replace("<details>\n", "<details>"), 0, id="details_on_the_same_line"),
        pytest.param("<!-- one --> <!--\ntwo -->\n" + PLAN, 0, id="menus_after_comments"),
        # bigger than a pipe's buffer, so an early match mustn't break the read
        pytest.param(PLAN + "a line of a long plan\n" * 2700, 0, id="long_description"),
    ],
)
def test_plan_menus_or_reason_must_be_visible_lines(plan, expected_code):
    """The menus or the reason count only as whole, visible lines, whatever their line endings."""
    result = run_check(plan, ON_DEMAND_FILE)
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"


@pytest.mark.parametrize(
    ("plan", "expected_code"),
    [
        pytest.param(PLAN, 0, id="all_menus"),
        pytest.param(NO_PLAN, 0, id="reason"),
        pytest.param(PLAN_HEADING + menu("intent.md"), 1, id="missing_menus"),
    ],
)
def test_a_plan_outside_the_config_is_checked_when_present(plan, expected_code):
    """A PR that doesn't touch src/claude/ may leave the Plan section out, but one it has must be complete."""
    result = run_check(DETAILS + bullets(1) + plan + NEXT_SECTION, "docs/other.md")
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"
    assert ("'Show spec.md'" in result.stdout) is bool(expected_code), f"unexpected reason: {result.stdout}"


def test_the_template_names_every_menu():
    """The template's comment names each menu and the opt-out line that the check looks for."""
    unnamed = [name for name in MENUS if f"<summary>Show {name}</summary>" not in TEMPLATE]
    assert not unnamed, f"the template's comment should name the menus: {unnamed}"
    assert '"No saved plan: ' in TEMPLATE, "the template's comment should name the opt-out line"


@pytest.mark.parametrize(
    ("changed_files", "expected_code", "reason"),
    [
        pytest.param("docs/other.md", 0, None, id="docs_pr_passes_as_is"),
        pytest.param(ON_DEMAND_FILE, 1, f"Add the '{PLAN_NAME}' section", id="config_needs_plan"),
        pytest.param(CONFIG_FILE, 1, f"Add the '{CRITERIA_NAME}' section", id="always_on_needs_criteria"),
    ],
)
def test_the_unedited_template_passes_only_when_no_section_is_needed(changed_files, expected_code, reason):
    """The template, unedited, passes a docs-only PR, since its comment's headings don't count as sections."""
    result = run_check(TEMPLATE, changed_files)
    assert result.returncode == expected_code, f"unexpected result for {changed_files!r}:\n{result.stdout}"
    assert reason is None or reason in result.stdout, f"the reason should name the missing section:\n{result.stdout}"


def test_the_headings_the_template_names_pass():
    """Adding the headings exactly as the template's comment names them satisfies the check."""
    menus = "".join(menu(name) for name in MENUS)
    description = (
        TEMPLATE + f"\n{template_heading(PLAN_NAME)}\n\n{menus}{template_heading(CRITERIA_NAME)}\n\nNo red flags.\n"
    )
    result = run_check(description, CONFIG_FILE)
    assert result.returncode == 0, f"the template's own headings should pass:\n{result.stdout}"
