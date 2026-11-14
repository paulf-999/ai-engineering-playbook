"""Tests for the context cost report, which tables each src/claude/ file's tokens and when it loads."""

import subprocess

from _git_repo import isolated_git_repo
from _paths import SCRIPTS_DIR

SCRIPT = SCRIPTS_DIR / "claude_report_context_cost.sh"
REPORT = "maintenance/context_cost.md"
# 400 characters is an estimated 100 tokens
HUNDRED_TOKENS = "x" * 399 + "\n"


def config_repo(tmp_path):
    """Make a git repo holding one always-on, one path-scoped and three on-demand files, and return its env."""
    env = isolated_git_repo(tmp_path)
    files = {
        # HTML comments are stripped before Claude loads a file, so this still counts as 100 tokens
        "src/claude/CLAUDE.md": "<!-- created: 2026-11-13 -->\n" + HUNDRED_TOKENS,
        "src/claude/rules/scoped.md": '---\npaths:\n  - "**/*.py"\n  - "**/*.sh"\n---\n' + HUNDRED_TOKENS,
        "src/claude/rules/on_demand/guide.md": HUNDRED_TOKENS,
        "src/claude/_templates/README.md": HUNDRED_TOKENS,
        # a README is for people browsing the repo, so Claude never loads it on its own
        "src/claude/README.md": HUNDRED_TOKENS,
    }
    for path, text in files.items():
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_text(text)
    (tmp_path / "maintenance").mkdir(parents=True)
    subprocess.run(["git", "add", "."], cwd=tmp_path, env=env, check=True)
    return env


# the fixture's three on-demand files, numbered in byte order, which puts README.md before _templates/ and rules/
ON_DEMAND_ROWS = (
    "| 1 | `README.md` | ~100 |",
    "| 2 | `_templates/README.md` | ~100 |",
    "| 3 | `rules/on_demand/guide.md` | ~100 |",
)


def run_report(tmp_path, env, *args):
    """Run the report script from the test repo's root and return the result."""
    command = ["bash", str(SCRIPT), *args]
    return subprocess.run(command, cwd=tmp_path, env=env, capture_output=True, text=True, check=False)


def write_report(tmp_path, env):
    """Write the report, failing with the script's output if that doesn't work, and return its text."""
    result = run_report(tmp_path, env)
    assert result.returncode == 0, f"writing the report should succeed:\n{result.stdout}{result.stderr}"
    return (tmp_path / REPORT).read_text()


# MoSCoW: Must — every-session files are listed one by one, and the rest are totalled by load type
def test_report_lists_every_session_files_and_totals_the_rest(tmp_path):
    """The report lists each every-session file, and gives one rounded row each for path-scoped and on-demand files."""
    report = write_report(tmp_path, config_repo(tmp_path))
    every, _, rest = report.partition("## 💤 Only when needed")
    assert "| 1 | `CLAUDE.md` | ~100 |" in every and "| | **Subtotal** | **~100** |" in every, (
        "CLAUDE.md loads every session"
    )
    assert all(name not in report for name in ("guide.md", "scoped.md", "`README.md`")), (
        "only every-session files are listed by name"
    )
    assert "| 📂 Path-scoped rules, with matching files | 1 | ~100 |" in rest, "the path-scoped file is totalled"
    assert "| 💤 On demand, via a pointer | 3 | ~300 |" in rest, (
        "the README, templates and lazy rules are totalled as on demand"
    )


# MoSCoW: Must — the terminal output still shows every file, with its load type and globs
def test_terminal_lists_every_file_by_load_type(tmp_path):
    """Writing the report prints every file's tokens, with path-scoped globs, grouped by load type."""
    result = run_report(tmp_path, config_repo(tmp_path))
    scoped, _, lazy = result.stdout.partition("## 💤 On demand")
    assert "| 1 | `rules/scoped.md` | `**/*.py`, `**/*.sh` | ~" in scoped, "a path-scoped file should list every glob"
    assert all(row in lazy for row in ON_DEMAND_ROWS), "each on-demand file should be listed in the terminal"


# MoSCoW: Must — the check must fail when the table no longer matches the files
def test_check_fails_once_a_file_changes(tmp_path):
    """--check passes straight after writing, then fails once a file grows, without rewriting the report."""
    env = config_repo(tmp_path)
    write_report(tmp_path, env)
    assert run_report(tmp_path, env, "--check").returncode == 0, "a freshly written report should pass the check"

    (tmp_path / "src" / "claude" / "CLAUDE.md").write_text(HUNDRED_TOKENS * 2)
    before = (tmp_path / REPORT).read_text()
    result = run_report(tmp_path, env, "--check")

    assert result.returncode == 1, f"a stale report should fail the check:\n{result.stdout}"
    assert "make context_cost" in result.stdout, "the failure should say how to fix it"
    assert (tmp_path / REPORT).read_text() == before, "--check must not rewrite the report"
