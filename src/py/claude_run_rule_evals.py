"""Run each rule eval case with and without its rule, grade both, and report whether the rule changes the result.

Each run gets its own scratch git repo, built from the case's `setup:`, with no skills or agents, so the only
difference between the two conditions is the rule, copied into `.claude/rules/`. The grader isn't told which
condition it's grading. `RUNS` sets how many runs each condition gets.
"""

import os
import shutil
import sys
import tempfile
from pathlib import Path

import yaml
from claude_run_behaviour_evals import build_repo, git, grade, repo_state, run_claude, transcript
from claude_run_trigger_evals import SOURCE_DIR, project_folder

CASES_FILE = SOURCE_DIR / "rules" / "evals.yaml"
# A rule helps, or hurts, when one condition passes at least this many more runs than the other
MARGIN = 2


def load_cases(cases_file):
    """Return the cases in the rule evals file."""
    return yaml.safe_load(cases_file.read_text())["evals"]


def prepare_repo(repo_dir, case, with_rule):
    """Build the case's scratch repo, commit its files, and copy in its rule when with_rule is set."""
    setup = dict(case.get("setup", {}))
    files = setup.pop("files", {})
    build_repo(repo_dir, setup)
    for name, content in files.items():
        (repo_dir / name).parent.mkdir(parents=True, exist_ok=True)
        (repo_dir / name).write_text(content)
    if files:
        git(repo_dir, "add", "-A")
        git(repo_dir, "commit", "-q", "-m", "chore: add case files")
    if with_rule:
        rule = SOURCE_DIR / "rules" / case["rule"]
        (repo_dir / ".claude/rules").mkdir(parents=True)
        shutil.copy(rule, repo_dir / ".claude/rules" / rule.name)


def run_once(case, with_rule, run_dir):
    """Run the case once in run_dir and return True if the grader passes every assertion."""
    run_dir.mkdir()
    prepare_repo(run_dir, case, with_rule)
    events = run_claude(case["prompt"], run_dir)
    folder = project_folder(events, run_dir.resolve())
    if folder:
        shutil.rmtree(folder, ignore_errors=True)
    results = grade(case["assertions"], transcript([(case["prompt"], events)]), repo_state(run_dir), run_dir.parent)
    return all(result["pass"] for result in results)


def verdict(passes_without, passes_with):
    """Return whether the rule helps, hurts or has no effect, from each condition's passing run count."""
    if passes_with - passes_without >= MARGIN:
        return "helps"
    if passes_without - passes_with >= MARGIN:
        return "hurts"
    return "no effect"


def main():
    """Run every case in both conditions, print each one's pass counts and verdict."""
    if shutil.which("claude") is None:
        sys.exit("claude isn't on PATH - install Claude Code and log in first.")
    runs = int(os.environ.get("RUNS", "3"))
    with tempfile.TemporaryDirectory(prefix="rule_evals_") as scratch:
        for case in load_cases(CASES_FILE):
            passes = {}
            for with_rule in (False, True):
                label = "with" if with_rule else "without"
                passes[with_rule] = sum(
                    run_once(case, with_rule, Path(scratch).resolve() / f"{case['name']}_{label}_{run}")
                    for run in range(runs)
                )
            counts = f"without {passes[False]}/{runs}, with {passes[True]}/{runs}"
            print(f"{case['name']} ({case['rule']}): {counts}, {verdict(passes[False], passes[True])}")


if __name__ == "__main__":
    main()
