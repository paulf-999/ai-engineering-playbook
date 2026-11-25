"""Tests for the open PR check, which fails a PR whose author has too many open."""

import os
import subprocess

import pytest
from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "git" / "git_validate_open_prs.sh"


def run_check(tmp_path, author, open_authors, gh_exit=0):
    """Run the check with a stub gh that lists the author of each open PR, and return the full result."""
    (tmp_path / "authors").write_text("".join(f"{name}\n" for name in open_authors))
    stub = tmp_path / "gh"
    stub.write_text(f'#!/bin/bash\ncat "{tmp_path}/authors"\nexit {gh_exit}\n')
    stub.chmod(0o755)
    env = {**os.environ, "PATH": f"{tmp_path}:{os.environ['PATH']}"}
    return subprocess.run(
        [str(SCRIPT), author, "org/repo"], cwd=REPO_ROOT, env=env, capture_output=True, text=True, check=False
    )


@pytest.mark.parametrize(
    ("author", "open_authors", "expected_code"),
    [
        pytest.param("dev1", ["dev1"] * 3, 0, id="at_the_limit"),
        pytest.param("dev1", ["dev1"] * 4, 1, id="over_the_limit"),
        pytest.param("dev1", ["dev1"] * 3 + ["dev2", "dev12"], 0, id="other_authors_dont_count"),
        pytest.param("dependabot[bot]", ["dependabot[bot]"] * 4, 0, id="dependabot_is_left_out"),
    ],
)
def test_an_author_is_limited_to_three_open_prs(tmp_path, author, open_authors, expected_code):
    """Three open PRs pass and a fourth fails, counting only the author's own."""
    result = run_check(tmp_path, author, open_authors)
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"


def test_a_failed_lookup_fails_the_check(tmp_path):
    """When GitHub can't be read the check fails, rather than passing uncounted."""
    result = run_check(tmp_path, "dev1", [], gh_exit=1)
    assert result.returncode == 1, f"a failed lookup should fail: {result.stdout}"
    assert "couldn't list" in result.stdout, f"the reason should say the lookup failed: {result.stdout}"
