"""Run each rule eval case with and without its rule, grade both, and report whether the rule changes the result.

Each run gets its own scratch git repo, built from the case's `setup:`, with no skills or agents, so the only
difference between the two conditions is the rule, copied into `.claude/rules/`. The runs go in parallel, and the
grader, on Haiku, isn't told which condition it's grading. `RUNS` sets how many runs each condition gets, and `CASE`
runs only the case with that name.
"""

import math
import os
import shutil
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml
from claude_evals_common import (
    SOURCE_DIR,
    build_repo,
    git,
    grade,
    remove_project_folder,
    repo_state,
    run_claude,
    transcript,
)

CASES_FILE = SOURCE_DIR / "rules" / "evals.yaml"
# A rule helps, or hurts, when one condition leads by a third of the runs, rounded up, and by at least this many
MIN_MARGIN = 2
# Runs at once, kept low so parallel claude -p calls stay within plan rate limits
MAX_WORKERS = 6
# Haiku grades faster, and agreed with the default grader on all 16 runs of the first four cases
GRADER_MODEL = "haiku"


def load_cases(cases_file):
    """Return the cases in the rule evals file."""
    return yaml.safe_load(cases_file.read_text())["evals"]


def select_cases(cases, name):
    """Return only the case called name, or every case when name is empty, and exit if no case has that name."""
    if not name:
        return cases
    chosen = [case for case in cases if case["name"] == name]
    if not chosen:
        sys.exit(f"No rule eval case is named {name}.")
    return chosen


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
    remove_project_folder(events, run_dir.resolve())
    results = grade(
        case["assertions"], transcript([(case["prompt"], events)]), repo_state(run_dir), run_dir.parent, GRADER_MODEL
    )
    return all(result["pass"] for result in results)


def count_passes(cases, runs, scratch, run=run_once):
    """Run every case's runs in both conditions in parallel, returning passing counts keyed by (name, with_rule)."""
    jobs = [(case, with_rule, n) for case in cases for with_rule in (False, True) for n in range(runs)]

    def run_job(job):
        case, with_rule, n = job
        label = "with" if with_rule else "without"
        return (case["name"], with_rule), run(case, with_rule, scratch / f"{case['name']}_{label}_{n}")

    passes = {(case["name"], with_rule): 0 for case in cases for with_rule in (False, True)}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for key, passed in pool.map(run_job, jobs):
            passes[key] += passed
    return passes


def verdict(passes_without, passes_with, runs):
    """Return whether the rule helps, hurts or has no effect, from each condition's passing run count."""
    margin = max(MIN_MARGIN, math.ceil(runs / 3))
    if passes_with - passes_without >= margin:
        return "helps"
    if passes_without - passes_with >= margin:
        return "hurts"
    return "no effect"


def main():
    """Run every case in both conditions, print each one's pass counts and verdict."""
    if shutil.which("claude") is None:
        sys.exit("claude isn't on PATH - install Claude Code and log in first.")
    runs = int(os.environ.get("RUNS", "3"))
    cases = select_cases(load_cases(CASES_FILE), os.environ.get("CASE", ""))
    with tempfile.TemporaryDirectory(prefix="rule_evals_") as scratch:
        passes = count_passes(cases, runs, Path(scratch).resolve())
    for case in cases:
        without, with_ = passes[(case["name"], False)], passes[(case["name"], True)]
        counts = f"without {without}/{runs}, with {with_}/{runs}"
        print(f"{case['name']} ({case['rule']}): {counts}, {verdict(without, with_, runs)}")


if __name__ == "__main__":
    main()
