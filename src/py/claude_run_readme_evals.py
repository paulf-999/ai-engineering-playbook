"""Score the README's front page with cold readers who play a new and an experienced Claude Code user.

Each reader is a `claude -p --safe-mode` run, so it sees only its persona and the README text, with none of this
repo's config. It scores how well the page says what the repo is, whether it's for them and what it would do for
them, and lists anything too complex for a front page. `RUNS` sets how many readers each persona gets.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

README = Path(__file__).resolve().parents[2] / "README.md"
PERSONAS = {
    "new": "You are a data engineer who has heard of Claude Code but never used it.",
    "experienced": "You are a software engineer who uses Claude Code every day and has written your own CLAUDE.md "
    "and hooks.",
}
QUESTIONS = ("what_it_is", "for_me", "what_it_does")
# A persona passes when its readers average at least BAR, with no single score below FLOOR
BAR = 7
FLOOR = 6
# Readers at once, kept low so parallel claude -p calls stay within plan rate limits
MAX_WORKERS = 4
MODEL = "sonnet"
TIMEOUT_SECONDS = 300
SCHEMA = {
    "type": "object",
    "properties": {
        **{question: {"type": "integer", "minimum": 1, "maximum": 10} for question in QUESTIONS},
        "too_complex": {"type": "array", "items": {"type": "string"}, "maxItems": 5},
    },
    "required": [*QUESTIONS, "too_complex"],
}
BRIEF = """{persona}

Below is the README of a GitHub repo, as you'd see it on the repo's front page. Score it 1-10 on how well it tells
you what the repo is (what_it_is), whether it's for you (for_me) and what it would do for you (what_it_does). List
up to 5 words or phrases you found too complex or vague for a front page, quoted exactly as they appear.

--- README ---
{readme}"""


def build_prompt(persona, readme):
    """Return the brief one reader gets: its persona, the questions and the README text."""
    return BRIEF.format(persona=persona, readme=readme)


def read_once(prompt, scratch):
    """Run one safe-mode reader in scratch and return its scores and flagged terms."""
    command = ["claude", "-p", prompt, "--safe-mode", "--strict-mcp-config", "--no-session-persistence"]
    command += ["--model", MODEL, "--max-turns", "3", "--output-format", "json", "--json-schema", json.dumps(SCHEMA)]
    result = subprocess.run(command, cwd=scratch, capture_output=True, text=True, timeout=TIMEOUT_SECONDS)
    return json.loads(result.stdout)["structured_output"]


def collect(readme, runs, scratch, read=read_once):
    """Run runs readers per persona in parallel, returning each persona's list of reader results."""
    jobs = [name for name in PERSONAS for _ in range(runs)]

    def run_job(name):
        return name, read(build_prompt(PERSONAS[name], readme), scratch)

    scores = {name: [] for name in PERSONAS}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for name, result in pool.map(run_job, jobs):
            scores[name].append(result)
    return scores


def verdict(readers):
    """Return a persona's mean score, rounded to 1 place, and whether it meets BAR with no score below FLOOR."""
    values = [reader[question] for reader in readers for question in QUESTIONS]
    mean = sum(values) / len(values)
    return round(mean, 1), mean >= BAR and min(values) >= FLOOR


def main():
    """Score the README for each persona, print each mean, verdict and flagged term, and exit 1 if any persona fails."""
    if shutil.which("claude") is None:
        sys.exit("claude isn't on PATH - install Claude Code and log in first.")
    runs = int(os.environ.get("RUNS", "4"))
    with tempfile.TemporaryDirectory(prefix="readme_evals_") as scratch:
        scores = collect(README.read_text(), runs, Path(scratch))
    failed = False
    for name, readers in scores.items():
        mean, passed = verdict(readers)
        failed |= not passed
        print(f"{name}: mean {mean}/10 over {len(readers)} readers, {'pass' if passed else 'fail'}")
        # readers quote the same phrase in different cases, so list each phrase once
        terms = {term.lower(): term for reader in readers for term in reader["too_complex"]}
        for key in sorted(terms):
            print(f"  - {terms[key]}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
