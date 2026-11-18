"""git-review-pr's secret check catches known secret shapes, passes ordinary review text, and never echoes a secret.

The check is a bash block in the skill's reference/_implementation.md, run on the comment before it's saved. Each test
runs the block from the doc itself, so a change to the doc is what gets tested.

Sample secrets are built by joining pieces, so this file holds no literal that secret scanners or the private-key
pre-commit hook would flag.
"""

import re
import subprocess

import pytest
from _paths import REPO_ROOT

IMPLEMENTATION = REPO_ROOT / "src/claude/skills/_git_skills/git-review-pr/reference/_implementation.md"
CHECK_BLOCK = re.compile(r"```bash\n(?P<code>[^`]*?^grep -[^`]*?)```", re.M)

SECRETS = {
    "aws": "AKIA" + "ABCDEFGHIJKLMNOP",
    "pem": "-----BEGIN " + "RSA PRIVATE" + " KEY-----",
    "github": "gh" + "p_" + "a" * 36,
    "github_fine_grained": "github" + "_pat_" + "g" * 30,
    "slack": "xo" + "xb-" + "1234-abcd",
    "anthropic": "sk" + "-ant-" + "api03-" + "b" * 24,
    "openai": "key is sk" + "-proj-" + "c" * 24,
    "google": "AI" + "za" + "d" * 35,
    "stripe": "sk" + "_live_" + "e" * 16,
    "key_value": "password = " + "hunter2hunter2",
    "json_pair": '{"api_key": "' + "f" * 12 + '"}',
    "single_quoted_pair": "{'api_key': '" + "h" * 12 + "'}",
    "upper_case_key": "PASSWORD=" + "hunter2hunter2",
}
SAFE = {
    "prose": "The token is read from an environment variable, never hard-coded.",
    "short_value": "password: abc",
    "hyphenated": "See task-runner-configuration-file-for-the-vm for details.",
    "live_word": "the disk_live_metrics_dashboard_panel is unchanged",
}


def run_check(target):
    """Run the doc's secret-check block against a file, and return the completed process."""
    block = CHECK_BLOCK.search(IMPLEMENTATION.read_text())
    assert block, f"no bash block holding the grep found in {IMPLEMENTATION}"
    script = block["code"].replace("<temp file>", str(target))
    return subprocess.run(["bash", "-c", script], capture_output=True, text=True, check=False)


def comment_with(text, tmp_path):
    """Write a review comment holding this text, and return its path."""
    comment = tmp_path / "comment.md"
    comment.write_text(f"**Claude review — PR #1**\n\n{text}\n")
    return comment


@pytest.mark.parametrize("name", sorted(SECRETS))
def test_secret_is_flagged_by_line_number_only(name, tmp_path):
    """Every secret shape the doc says it catches is flagged, printing only its line number, never the secret."""
    result = run_check(comment_with(SECRETS[name], tmp_path))
    assert result.returncode == 0, f"{name} sample was not flagged: {result.stderr}"
    assert result.stdout.strip() == "3", f"only the line number should print, got {result.stdout!r}"


@pytest.mark.parametrize("name", sorted(SAFE))
def test_safe_text_passes(name, tmp_path):
    """Ordinary review text, including hyphenated words and short values, exits 1, which means no secret."""
    result = run_check(comment_with(SAFE[name], tmp_path))
    assert result.returncode == 1, f"{name} text was wrongly flagged, or grep failed: {result.stderr}"


def test_a_missing_file_is_an_error_not_a_pass(tmp_path):
    """A grep error exits 2, so a failed check is never read as a clean comment."""
    assert run_check(tmp_path / "missing.md").returncode == 2, "a missing file should exit 2, not pass silently"
