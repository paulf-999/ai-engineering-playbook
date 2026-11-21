"""Tests for the README evals runner's reader brief, tally and pass bar, without a live claude run."""

import importlib
import sys

import pytest
from _paths import REPO_ROOT

# The runner is imported by name, as it is when run as a script
sys.path.insert(0, str(REPO_ROOT / "src" / "py"))
runner = importlib.import_module("claude_run_readme_evals")


def reader(score, terms=()):
    """Return one reader result that gives every question the same score."""
    return {**{question: score for question in runner.QUESTIONS}, "too_complex": list(terms)}


def test_build_prompt_gives_the_persona_and_the_readme():
    """Each reader's brief opens with its persona and ends with the README text."""
    prompt = runner.build_prompt(runner.PERSONAS["new"], "# My README\n")
    assert prompt.startswith(runner.PERSONAS["new"])
    assert prompt.endswith("# My README\n")


def test_collect_runs_each_persona_runs_times(tmp_path):
    """Parallel readers still land under their own persona, runs per persona, each briefed with that persona."""

    def fake_read(prompt, scratch):
        return reader(8, [prompt.split("\n")[0]])

    scores = runner.collect("readme", 3, tmp_path, read=fake_read)
    assert set(scores) == set(runner.PERSONAS)
    for name, readers in scores.items():
        assert len(readers) == 3
        assert all(result["too_complex"] == [runner.PERSONAS[name]] for result in readers)


@pytest.mark.parametrize(
    ("scores", "expected"),
    [([7, 7], (7.0, True)), ([8, 6], (7.0, True)), ([9, 5], (7.0, False)), ([7, 6], (6.5, False))],
)
def test_verdict_needs_the_bar_and_the_floor(scores, expected):
    """A persona passes at a mean of exactly 7 with no score under 6, and fails one point under either."""
    assert runner.verdict([reader(score) for score in scores]) == expected
