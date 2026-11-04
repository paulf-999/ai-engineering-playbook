# version: 1.0.0
# created: 2026-11-04
# updated: 2026-11-04
"""Tests for the context cost report, which tables each src/claude/ file's tokens and when it loads."""

import subprocess

from _git_repo import isolated_git_repo
from _paths import SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "claude_report_context_cost.sh"
REPORT = "docs/maintenance/context_cost.md"
# 400 characters is an estimated 100 tokens
HUNDRED_TOKENS = "x" * 399 + "\n"


def config_repo(tmp_path):
    """Make a git repo holding one always-on, one path-scoped and one on-demand file, and return its env."""
    env = isolated_git_repo(tmp_path)
    files = {
        # HTML comments are stripped before Claude loads a file, so this still counts as 100 tokens
        "src/claude/CLAUDE.md": "<!-- version: 1.0.0 -->\n" + HUNDRED_TOKENS,
        "src/claude/rules/scoped.md": '---\npaths:\n  - "**/*.py"\n---\n' + HUNDRED_TOKENS,
        "src/claude/rules/_rules_lazy_load/guide.md": HUNDRED_TOKENS,
    }
    for path, text in files.items():
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_text(text)
    (tmp_path / "docs" / "maintenance").mkdir(parents=True)
    subprocess.run(["git", "add", "."], cwd=tmp_path, env=env, check=True)
    return env


def run_report(tmp_path, env, *args):
    """Run the report script from the test repo's root and return the result."""
    command = ["bash", str(SCRIPT), *args]
    return subprocess.run(command, cwd=tmp_path, env=env, capture_output=True, text=True, check=False)


# MoSCoW: Must — each file's row must say when it loads, and only every-session files count in the total
def test_report_lists_each_file_with_when_it_loads(tmp_path):
    """The table gives each tracked file its load condition and tokens, and totals only every-session files."""
    env = config_repo(tmp_path)
    result = run_report(tmp_path, env)
    assert result.returncode == 0, f"writing the report should succeed:\n{result.stdout}{result.stderr}"
    report = (tmp_path / REPORT).read_text()
    assert "| `CLAUDE.md` | Every session | ~100 |" in report, "CLAUDE.md should load every session"
    assert "| `rules/scoped.md` | With matching files: `**/*.py` | ~" in report, "paths: globs should be listed"
    assert "| `rules/_rules_lazy_load/guide.md` | On demand, via a pointer | ~100 |" in report, (
        "lazy files are on demand"
    )
    assert "**~100**" in report, "only the every-session file should count in the total"


# MoSCoW: Must — the check must fail when the table no longer matches the files
def test_check_fails_once_a_file_changes(tmp_path):
    """--check passes straight after writing, then fails once a file grows, without rewriting the report."""
    env = config_repo(tmp_path)
    run_report(tmp_path, env)
    assert run_report(tmp_path, env, "--check").returncode == 0, "a freshly written report should pass the check"

    (tmp_path / "src" / "claude" / "CLAUDE.md").write_text(HUNDRED_TOKENS * 2)
    before = (tmp_path / REPORT).read_text()
    result = run_report(tmp_path, env, "--check")

    assert result.returncode == 1, f"a stale report should fail the check:\n{result.stdout}"
    assert "make context_cost" in result.stdout, "the failure should say how to fix it"
    assert (tmp_path / REPORT).read_text() == before, "--check must not rewrite the report"


# MoSCoW: Should — a header bump alone mustn't make the report look stale
def test_check_ignores_the_version_header(tmp_path):
    """Changing only the report's version header still passes the check."""
    env = config_repo(tmp_path)
    run_report(tmp_path, env)
    report = tmp_path / REPORT
    report.write_text(report.read_text().replace("version: 1.0.0", "version: 1.0.7", 1))
    assert run_report(tmp_path, env, "--check").returncode == 0, "a header-only change should pass the check"
