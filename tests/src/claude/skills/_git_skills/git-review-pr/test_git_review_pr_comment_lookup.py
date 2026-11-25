"""git-review-pr finds the user's earlier review of a PR, in the current or the older comment format, and no other.

The lookup is a jq filter in the skill's reference/_implementation.md. Each test runs the filter from the doc itself, so
a change to the doc is what gets tested.
"""

import json
import re
import subprocess

import pytest
from _paths import REPO_ROOT

SKILL_REFERENCE = REPO_ROOT / "src/claude/skills/_git_skills/git-review-pr/reference"
LOOKUP_FILTER = re.compile(r"issues/<number>/comments\" --paginate \\\n\s+--jq '(?P<filter>[^']+)'")
TEMPLATE = re.compile(r"```markdown\n(?P<template>.*?)```", re.S)

BOLD_TITLE = "**Claude review — PR #7**\n**Verdict: Approve ✅**"
MARKED = "<!-- claude-review-pr-7 -->\n# 🔴 Requires human review\n\n" + BOLD_TITLE


def found_ids(login, body):
    """Run the doc's filter for user `me` on PR 7 against one comment, and return the IDs it prints."""
    match = LOOKUP_FILTER.search((SKILL_REFERENCE / "_implementation.md").read_text())
    assert match, "no jq filter found for the earlier-review lookup in _implementation.md"
    jq_filter = match["filter"].replace("<login>", "me").replace("<number>", "7")
    comments = json.dumps([{"id": 1, "user": {"login": login}, "body": body}])
    result = subprocess.run(["jq", jq_filter], input=comments, capture_output=True, text=True, check=True)
    return result.stdout.split()


@pytest.mark.parametrize("body", [MARKED, BOLD_TITLE], ids=["marker", "bold_title"])
def test_own_earlier_review_is_found(body):
    """A review by the same user is found, whether it opens with the marker or the older bold title."""
    assert found_ids("me", body) == ["1"], f"earlier review not found: {body!r}"


@pytest.mark.parametrize(
    ("login", "body"),
    [
        ("someone_else", MARKED),
        ("me", MARKED.replace("pr-7 ", "pr-77 ").replace("#7*", "#77*")),
        ("me", "Looks good, see <!-- claude-review-pr-7 -->"),
    ],
    ids=["another_user", "another_pr", "unrelated_comment"],
)
def test_other_comments_are_ignored(login, body):
    """Another user's review, another PR's review and an unrelated comment are never offered for update."""
    assert found_ids(login, body) == [], f"wrongly matched a comment by {login}: {body!r}"


def test_a_comment_from_the_template_is_found():
    """A comment that follows the template in _formats.md is found again on the next run."""
    template = TEMPLATE.search((SKILL_REFERENCE / "_formats.md").read_text())["template"]
    assert found_ids("me", template.replace("<number>", "7")) == ["1"], "the lookup misses the template's own opening"
