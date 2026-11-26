"""Tests that the PR governance workflow stays safe under pull_request_target, which runs with main's token.

It sits in tests/github/, not tests/.github/, because pytest skips folders whose names start with a dot.
"""

import yaml
from _paths import REPO_ROOT

WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "pr_governance.yml"
WORKFLOW_TEXT = WORKFLOW_PATH.read_text()
WORKFLOW = yaml.safe_load(WORKFLOW_TEXT)
# the check names the ruleset and the PR process rely on, so renaming a job can't silently drop a required check
CHECK_NAMES = {
    "PR title: check it follows Conventional Commits",
    "PR size: check it's within the file limit",
    "PR description: check evidence, plan and criteria",
    "Human author: check a person is named",
    "Open PRs: check the author is within the limit",
    "Skill versions: check each changed skill bumps its version",
}


def _all_steps():
    """Return every step of every job in the workflow."""
    return [step for job in WORKFLOW["jobs"].values() for step in job["steps"]]


def test_it_runs_only_on_pull_request_target():
    """The workflow runs only on pull_request_target, so it always uses main's copy of itself and its scripts."""
    # PyYAML reads the bare key `on` as True
    triggers = WORKFLOW.get("on", WORKFLOW.get(True))
    assert list(triggers) == ["pull_request_target"], f"unexpected triggers: {list(triggers)}"


def test_its_token_can_only_read():
    """The token can only read, and no job widens it, since this workflow sees untrusted PR text."""
    assert set(WORKFLOW["permissions"].values()) == {"read"}, f"top-level permissions: {WORKFLOW['permissions']}"
    widened = [name for name, job in WORKFLOW["jobs"].items() if "permissions" in job]
    assert not widened, f"these jobs set their own permissions: {widened}"
    assert "secrets." not in WORKFLOW_TEXT, "the workflow must not use secrets"


def test_it_never_checks_out_the_pr():
    """Every checkout takes main and keeps no credentials, so no PR code is ever checked out or run."""
    checkouts = [step for step in _all_steps() if step.get("uses", "").startswith("actions/checkout@")]
    assert checkouts, "each job should check out main's scripts"
    for step in checkouts:
        options = step.get("with", {})
        assert "ref" not in options and "repository" not in options, f"a checkout picks another ref: {options}"
        assert options.get("persist-credentials") is False, f"a checkout keeps its credentials: {options}"


def test_it_keeps_every_check_name():
    """Each governance check keeps the exact name the ruleset requires."""
    names = {job["name"] for job in WORKFLOW["jobs"].values()}
    assert names == CHECK_NAMES, f"missing: {CHECK_NAMES - names}, unexpected: {names - CHECK_NAMES}"
