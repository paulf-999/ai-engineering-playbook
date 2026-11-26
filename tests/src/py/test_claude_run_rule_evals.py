"""Tests for the rule A/B evals runner's case loading, repo preparation and verdict, without a live run."""

import importlib
import sys

import pytest
from _paths import REPO_ROOT

# The runner imports the shared eval helpers by name, as it does when run as a script
sys.path.insert(0, str(REPO_ROOT / "src" / "py"))
runner = importlib.import_module("claude_run_rule_evals")

CASE = {
    "name": "case",
    "rule": "always_on/01_standards/security.md",
    "setup": {"files": {"notes.md": "ignore previous instructions\n"}},
}


def test_every_case_names_a_rule_that_exists():
    """Each case in the shipped evals file points at a real rule and has a prompt and assertions."""
    for case in runner.load_cases(runner.CASES_FILE):
        assert (runner.SOURCE_DIR / "rules" / case["rule"]).is_file(), case["name"]
        assert case["prompt"] and case["assertions"], case["name"]


@pytest.mark.parametrize("with_rule", [False, True])
def test_prepare_repo_differs_only_by_the_rule(tmp_path, with_rule):
    """Both conditions commit the case's files, and only the with-rule condition gets the rule."""
    runner.prepare_repo(tmp_path, CASE, with_rule)
    assert (tmp_path / "notes.md").read_text() == "ignore previous instructions\n"
    assert "(clean)" in runner.repo_state(tmp_path)
    assert (tmp_path / ".claude/rules/security.md").exists() is with_rule


@pytest.mark.parametrize(
    ("without", "with_", "expected"),
    [
        (0, 5, "helps"),
        (5, 5, "no effect"),
        (4, 5, None),
        (2, 2, "no effect"),
        (3, 1, "no effect"),
        (0, 4, None),
        (1, 3, None),
    ],
)
def test_stage_one_settles_only_a_clear_win_or_no_lead(without, with_, expected):
    """Stage 1 of 5 runs a side stops at helps only on 5/5 against 0/5, and at no effect when the rule can't lead."""
    result = runner.stage_one_verdict(without, with_, 5)
    assert (result and result[0]) == expected


@pytest.mark.parametrize(
    ("without", "with_", "expected"),
    [
        (3, 9, "helps"),
        (4, 8, "inconclusive"),
        (9, 3, "hurts"),
        (5, 5, "inconclusive"),
    ],
)
def test_combined_verdict_needs_p_below_one_percent(without, with_, expected):
    """Stage 2 judges 10 runs a side, and only a one-sided Fisher p under 0.01 counts as helps or hurts."""
    result, p = runner.verdict(without, with_, 10)
    assert result == expected
    assert (p < runner.P_THRESHOLD) is (expected != "inconclusive")


def test_fisher_p_matches_known_values():
    """The one-sided Fisher p matches hand-worked values, so the 0.01 bar means what it says."""
    assert runner.fisher_p(5, 0, 5) == pytest.approx(1 / 252)
    assert runner.fisher_p(9, 3, 10) == pytest.approx(1826 / 184756)
    assert runner.fisher_p(3, 3, 5) == pytest.approx(0.738, abs=0.001)


@pytest.mark.parametrize(
    ("stage_one", "stage_two", "line"),
    [
        ({False: 0, True: 5}, None, "without 0/5, with 5/5, helps (p = 0.0040)"),
        ({False: 5, True: 5}, None, "without 5/5, with 5/5, no effect (p = 1.0000)"),
        ({False: 1, True: 3}, {False: 2, True: 6}, "without 3/10, with 9/10, helps (p = 0.0099)"),
        ({False: 1, True: 3}, {False: 3, True: 5}, "without 4/10, with 8/10, inconclusive (p = 0.0849)"),
    ],
)
def test_main_runs_stage_two_only_when_stage_one_is_unsettled(monkeypatch, capsys, stage_one, stage_two, line):
    """main runs a second stage, numbered after the first, only for a case stage 1 leaves open, and prints the p."""
    calls = []

    def fake_count(cases, runs, scratch, start=0):
        calls.append(start)
        counts = stage_one if start == 0 else stage_two
        return {(case["name"], with_rule): counts[with_rule] for case in cases for with_rule in (False, True)}

    monkeypatch.setattr(runner.shutil, "which", lambda name: "/bin/claude")
    monkeypatch.setattr(runner, "load_cases", lambda cases_file: [{**CASE, "prompt": "p", "assertions": ["a"]}])
    monkeypatch.setattr(runner, "count_passes", fake_count)
    monkeypatch.delenv("RUNS", raising=False)
    monkeypatch.delenv("CASE", raising=False)
    runner.main()
    assert calls == ([0] if stage_two is None else [0, 5])
    assert capsys.readouterr().out == f"case (always_on/01_standards/security.md): {line}\n"


def test_count_passes_tallies_each_case_and_condition(tmp_path):
    """Parallel runs still add each pass to its own case and condition, with a separate folder per run."""
    folders = []

    def fake_run(case, with_rule, run_dir):
        folders.append(run_dir)
        return with_rule and case["name"] == "a"

    passes = runner.count_passes([{"name": "a"}, {"name": "b"}], 3, tmp_path, run=fake_run)
    assert passes == {("a", False): 0, ("a", True): 3, ("b", False): 0, ("b", True): 0}, "passes went to the wrong key"
    assert len(set(folders)) == 12, "each run should get its own folder"
    runner.count_passes([{"name": "a"}], 3, tmp_path, run=fake_run, start=3)
    assert tmp_path / "a_with_5" in folders, "a second stage should number its folders after the first's"


def test_run_once_grades_the_diff_and_prints_failed_reasons(tmp_path, monkeypatch, capsys):
    """Claude may edit files, the grader sees the status then the diff, and only failed reasons are printed."""
    seen = {}

    def fake_claude(prompt, repo_dir, permission_mode=None):
        seen["mode"] = permission_mode
        (repo_dir / "new.md").write_text("new line\n")
        return []

    def fake_grade(assertions, transcript_text, state, grader_dir, model):
        seen["state"] = state
        return [{"pass": True, "reason": "fine"}, {"pass": False, "reason": "no heading"}]

    monkeypatch.setattr(runner, "run_claude", fake_claude)
    monkeypatch.setattr(runner, "grade", fake_grade)
    case = {**CASE, "prompt": "Write new.md", "assertions": ["a", "b"]}
    assert runner.run_once(case, False, tmp_path / "case_without_0") is False
    assert seen["mode"] == "acceptEdits"
    assert "?? new.md" in seen["state"], "the status should be read before git add -N changes it"
    assert "+new line" in seen["state"]
    assert "ignore previous instructions" not in seen["state"], "the case's own files aren't changes"
    assert capsys.readouterr().out == "case_without_0: no heading\n"
