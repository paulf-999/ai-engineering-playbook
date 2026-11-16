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


def test_terminal_lists_every_file_by_load_type(tmp_path):
    """Writing the report prints every file's tokens, with path-scoped globs, grouped by load type."""
    result = run_report(tmp_path, config_repo(tmp_path))
    scoped, _, lazy = result.stdout.partition("## 💤 On demand")
    assert "| 1 | `rules/scoped.md` | `**/*.py`, `**/*.sh` | ~" in scoped, "a path-scoped file should list every glob"
    assert all(row in lazy for row in ON_DEMAND_ROWS), "each on-demand file should be listed in the terminal"


def test_stage_rewrites_and_stages_a_stale_report_except_in_ci(tmp_path):
    """--stage rewrites a stale report and stages it, and with CI=true fails, leaving the report alone."""
    env = config_repo(tmp_path)
    write_report(tmp_path, env)
    subprocess.run(["git", "add", REPORT], cwd=tmp_path, env=env, check=True)
    (tmp_path / "src" / "claude" / "CLAUDE.md").write_text(HUNDRED_TOKENS * 2)

    stale = (tmp_path / REPORT).read_text()
    in_ci = run_report(tmp_path, {**env, "CI": "true"}, "--stage")
    assert in_ci.returncode == 1, f"a stale report should fail in CI:\n{in_ci.stdout}"
    assert "make context_cost" in in_ci.stdout, "the CI failure should say how to fix it"
    assert (tmp_path / REPORT).read_text() == stale, "CI must not rewrite the report"

    local = run_report(tmp_path, {k: v for k, v in env.items() if k != "CI"}, "--stage")
    assert local.returncode == 0, f"a stale report should be fixed locally:\n{local.stdout}"
    assert "| 1 | `CLAUDE.md` | ~200 |" in (tmp_path / REPORT).read_text(), "the report should be rewritten"
    staged_files = ["git", "diff", "--cached", "--name-only"]
    staged = subprocess.run(staged_files, cwd=tmp_path, env=env, capture_output=True, text=True, check=True)
    assert REPORT in staged.stdout.split(), "the rewritten report should be staged for the commit"
