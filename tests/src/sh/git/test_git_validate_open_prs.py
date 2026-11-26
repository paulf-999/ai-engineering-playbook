"""Tests for the open PR check, which fails a PR whose author has too many open."""

import os
import subprocess

import pytest
from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "git" / "git_validate_open_prs.sh"


def run_check(tmp_path, author, open_prs, pr_number=100, gh_exit=0):
    """Run the check with a stub gh that lists each open PR's author and number, and return the full result."""
    (tmp_path / "authors").write_text("".join(f"{name} {number}\n" for name, number in open_prs))
    stub = tmp_path / "gh"
    stub.write_text(f'#!/bin/bash\ncat "{tmp_path}/authors"\nexit {gh_exit}\n')
    stub.chmod(0o755)
    env = {**os.environ, "PATH": f"{tmp_path}:{os.environ['PATH']}"}
    return subprocess.run(
        [str(SCRIPT), author, "org/repo", str(pr_number)],
        cwd=REPO_ROOT,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


def prs(author, count, first=1):
    """Return count open PRs by the author, numbered from first."""
    return [(author, number) for number in range(first, first + count)]


@pytest.mark.parametrize(
    ("author", "open_prs", "expected_code"),
    [
        pytest.param("dev1", prs("dev1", 6), 0, id="at_the_limit"),
        pytest.param("dev1", prs("dev1", 7), 1, id="over_the_limit"),
        pytest.param(
            "dev1", prs("dev1", 6) + prs("dev2", 3, 50) + prs("dev12", 1, 60), 0, id="other_authors_dont_count"
        ),
        pytest.param("dependabot[bot]", prs("dependabot[bot]", 7), 0, id="dependabot_is_left_out"),
    ],
)
def test_an_author_is_limited_to_six_open_prs(tmp_path, author, open_prs, expected_code):
    """Six open PRs pass and a seventh fails, counting only the author's own."""
    result = run_check(tmp_path, author, open_prs)
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"


@pytest.mark.parametrize(
    ("pr_number", "expected_code"),
    [
        pytest.param(6, 0, id="sixth_oldest_passes"),
        pytest.param(7, 1, id="seventh_oldest_fails"),
    ],
)
def test_newer_prs_dont_block_older_ones(tmp_path, pr_number, expected_code):
    """A PR counts only itself and older open PRs, so the oldest can merge however many newer ones are open."""
    result = run_check(tmp_path, "dev1", prs("dev1", 10), pr_number=pr_number)
    assert result.returncode == expected_code, f"expected exit {expected_code} for PR {pr_number}: {result.stdout}"


def test_a_failed_lookup_fails_the_check(tmp_path):
    """When GitHub can't be read the check fails, rather than passing uncounted."""
    result = run_check(tmp_path, "dev1", [], gh_exit=1)
    assert result.returncode == 1, f"a failed lookup should fail: {result.stdout}"
    assert "couldn't list" in result.stdout, f"the reason should say the lookup failed: {result.stdout}"
