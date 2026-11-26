"""Tests for the human author check, which fails a bot's PR with no person assigned."""

import subprocess

import pytest
from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "git" / "git_validate_human_author.sh"


@pytest.mark.parametrize(
    ("author_type", "assignee_types", "author", "expected_code"),
    [
        pytest.param("User", "", "dev1", 0, id="person"),
        pytest.param("Bot", "", "some-agent[bot]", 1, id="bot_unassigned"),
        pytest.param("Bot", "Bot", "some-agent[bot]", 1, id="bot_assigned_to_a_bot"),
        pytest.param("Bot", "Bot User", "some-agent[bot]", 0, id="bot_assigned_to_a_person"),
        pytest.param("Bot", "", "dependabot[bot]", 0, id="dependabot_unassigned"),
    ],
)
def test_a_person_must_be_named(author_type, assignee_types, author, expected_code):
    """A person's PR passes, a bot's passes only once a person is assigned, and Dependabot's always passes."""
    result = subprocess.run(
        [str(SCRIPT), author_type, assignee_types, author], cwd=REPO_ROOT, capture_output=True, text=True, check=False
    )
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"
