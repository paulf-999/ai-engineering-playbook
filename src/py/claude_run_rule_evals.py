"""Run each rule eval case with and without its rule, grade both, and report whether the rule changes the result.

Each run gets its own scratch git repo, built from the case's `setup:`, with no skills or agents, so the only
difference between the two conditions is the rule, copied into `.claude/rules/`. The runs go in parallel, and the
grader, on Haiku, isn't told which condition it's grading. Claude may edit files in the scratch repo, the grader sees
the diff, and each failed assertion's reason is printed.

The test is staged. Stage 1 runs `RUNS` runs per condition, 5 by default, and stops when its counts already settle the
case. Otherwise stage 2 runs as many again, and a one-sided Fisher exact test on the combined counts decides. `CASE`
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
    repo_changes,
    repo_state,
    run_claude,
    select_cases,
    transcript,
)

CASES_FILE = SOURCE_DIR / "rules" / "evals.yaml"
# A rule helps, or hurts, when the one-sided Fisher exact p of its lead is below this
P_THRESHOLD = 0.01
# Runs at once, kept low so parallel claude -p calls stay within plan rate limits
MAX_WORKERS = 6
# Haiku grades faster, and agreed with the default grader on all 16 runs of the first four cases
GRADER_MODEL = "haiku"


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
    base = git(run_dir, "rev-parse", "HEAD").strip()
    events = run_claude(case["prompt"], run_dir, permission_mode="acceptEdits")
    remove_project_folder(events, run_dir.resolve())
    # repo_changes runs git add -N, which changes the status, so read the state first
    state = repo_state(run_dir)
    state += f"changes:\n{repo_changes(run_dir, base)}"
    results = grade(case["assertions"], transcript([(case["prompt"], events)]), state, run_dir.parent, GRADER_MODEL)
    for result in results:
        if not result["pass"]:
            print(f"{run_dir.name}: {result['reason']}")
    return all(result["pass"] for result in results)


def count_passes(cases, runs, scratch, run=run_once, start=0):
    """Run every case's runs in both conditions in parallel, returning passing counts keyed by (name, with_rule).

    Run folders are numbered from start, so a second stage's folders don't clash with the first's.
    """
    jobs = [(case, with_rule, n) for case in cases for with_rule in (False, True) for n in range(start, start + runs)]

    def run_job(job):
        case, with_rule, n = job
        label = "with" if with_rule else "without"
        return (case["name"], with_rule), run(case, with_rule, scratch / f"{case['name']}_{label}_{n}")

    passes = {(case["name"], with_rule): 0 for case in cases for with_rule in (False, True)}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for key, passed in pool.map(run_job, jobs):
            passes[key] += passed
    return passes


def fisher_p(passes_a, passes_b, runs):
    """Return the one-sided Fisher exact p that condition a passes more often than b, with runs runs in each."""
    total = passes_a + passes_b
    tail = range(passes_a, min(total, runs) + 1)
    return sum(math.comb(total, x) * math.comb(2 * runs - total, runs - x) for x in tail) / math.comb(2 * runs, runs)


def stage_one_verdict(passes_without, passes_with, runs):
    """Return (verdict, p) when stage 1's counts settle the case, or None when stage 2 should run.

    The rule helps if its lead is already significant, and has no effect if the without-rule runs all pass or the
    with-rule runs don't lead.
    """
    p = fisher_p(passes_with, passes_without, runs)
    if p < P_THRESHOLD:
        return "helps", p
    if passes_without == runs or passes_with <= passes_without:
        return "no effect", p
    return None


def verdict(passes_without, passes_with, runs):
    """Return (verdict, p) from both stages' combined counts: helps or hurts when significant, else inconclusive."""
    helps_p = fisher_p(passes_with, passes_without, runs)
    if helps_p < P_THRESHOLD:
        return "helps", helps_p
    hurts_p = fisher_p(passes_without, passes_with, runs)
    if hurts_p < P_THRESHOLD:
        return "hurts", hurts_p
    return "inconclusive", helps_p


def main():
    """Run stage 1 of every case, stage 2 of those it doesn't settle, and print each one's counts and verdict."""
    if shutil.which("claude") is None:
        sys.exit("claude isn't on PATH - install Claude Code and log in first.")
    runs = int(os.environ.get("RUNS", "5"))
    cases = select_cases(load_cases(CASES_FILE), os.environ.get("CASE", ""))
    with tempfile.TemporaryDirectory(prefix="rule_evals_") as scratch:
        scratch = Path(scratch).resolve()
        passes = count_passes(cases, runs, scratch)
        settled = {
            case["name"]: stage_one_verdict(passes[(case["name"], False)], passes[(case["name"], True)], runs)
            for case in cases
        }
        unsettled = [case for case in cases if settled[case["name"]] is None]
        if unsettled:
            for key, more in count_passes(unsettled, runs, scratch, start=runs).items():
                passes[key] += more
    for case in cases:
        without, with_ = passes[(case["name"], False)], passes[(case["name"], True)]
        total = runs if settled[case["name"]] else 2 * runs
        result, p = settled[case["name"]] or verdict(without, with_, total)
        print(
            f"{case['name']} ({case['rule']}): without {without}/{total}, with {with_}/{total}, {result} (p = {p:.3f})"
        )


if __name__ == "__main__":
    main()
