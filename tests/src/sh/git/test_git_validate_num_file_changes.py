"""Tests for the PR file-count check, which takes the PR's changed files and skips release/ branches."""

import os
import subprocess

import pytest
from _paths import REPO_ROOT, SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "git" / "git_validate_num_file_changes.sh"


def run_check(branch, count, extra_env=None):
    """Run the file-count check on a PR that changes the given number of files, and return the full result."""
    env = {key: value for key, value in os.environ.items() if key != "MAX_FILES_ALLOWED"}
    changed_files = "".join(f"file_{index}.txt\n" for index in range(count))
    return subprocess.run(
        ["bash", str(SCRIPT), branch, changed_files],
        cwd=REPO_ROOT,
        env={**env, **(extra_env or {})},
        capture_output=True,
        text=True,
        check=False,
    )


@pytest.mark.parametrize(
    ("branch", "count", "extra_env", "expected_code"),
    [
        pytest.param("feature/at_limit", 20, None, 0, id="at_the_limit"),
        pytest.param("feature/too_big", 21, None, 1, id="over_the_limit"),
        pytest.param("release/bulk_change", 21, None, 0, id="release_branch_skips"),
        pytest.param("feature/custom_limit", 21, {"MAX_FILES_ALLOWED": "25"}, 0, id="override_raises_the_limit"),
    ],
)
def test_a_pr_is_limited_to_twenty_files(branch, count, extra_env, expected_code):
    """Twenty files pass and 21 fail, unless the branch is a release/ one or MAX_FILES_ALLOWED raises the limit."""
    result = run_check(branch, count, extra_env)
    assert result.returncode == expected_code, f"expected exit {expected_code}: {result.stdout}"


@pytest.mark.parametrize("bad_limit", ["abc", "-5", "1.5"])
def test_non_numeric_limit_fails_clearly(bad_limit):
    """A MAX_FILES_ALLOWED that isn't a whole number exits 1 with an explanation."""
    result = run_check("feature/small", 1, {"MAX_FILES_ALLOWED": bad_limit})
    assert result.returncode == 1, f"a limit of {bad_limit!r} should fail"
    assert "must be a whole number" in result.stdout, f"expected the whole-number explanation: {result.stdout}"
