"""Run each eval scenario tagged `behaviour: true` end to end, then have a separate grader judge its assertions.

Each scenario gets its own scratch git repo, built from its `setup:` keys, with no remote and only this repo's
skills and agents. Push, gh and web tools are blocked and MCP servers are dropped, so nothing leaves the machine.
A `confirm_reply` is sent by resuming the session. An agent's scenario with a `run:` block sends its self-contained
prompt straight to that agent in a bare repo, since its `setup:` only describes the prompt, and checks each
`must_match` pattern against Claude's text. The grader is a `claude -p --safe-mode` run that sees only the
assertions, the transcript and the repo's final state.
"""

import re
import shutil
import sys
import tempfile
from pathlib import Path

import yaml
from claude_evals_common import (
    SOURCE_DIR,
    build_repo,
    copy_components,
    grade,
    remove_project_folder,
    repo_state,
    run_claude,
    transcript,
)


def load_scenarios(source_dir):
    """Return every scenario tagged `behaviour: true`, from each evals.yaml under source_dir."""
    scenarios = []
    for path in sorted(source_dir.rglob("evals.yaml")):
        evals = yaml.safe_load(path.read_text())
        for scenario in evals["evals"]:
            if scenario.get("behaviour") is True:
                scenarios.append({**scenario, "agent": evals.get("agent_name")})
    return scenarios


def session_id_of(events):
    """Return the session ID from a run's events, or None."""
    return next((event["session_id"] for event in events if event.get("session_id")), None)


def claude_text(turns):
    """Return all of Claude's text blocks across the turns, joined by newlines."""
    blocks = []
    for _, events in turns:
        for event in events:
            if event.get("type") == "assistant":
                blocks += [b["text"] for b in event["message"].get("content", []) if b.get("type") == "text"]
    return "\n".join(blocks)


def pattern_results(patterns, text):
    """Check each must_match pattern against Claude's text, in the grader's result format."""
    return [
        {"assertion": f"Claude's reply matches {pattern}", "pass": bool(re.search(pattern, text)), "reason": ""}
        for pattern in patterns
    ]


def run_scenario(scenario, scratch_dir):
    """Build, run and grade one scenario, returning (results, error), and delete its projects/ folder."""
    repo_dir = scratch_dir / scenario["name"]
    repo_dir.mkdir()
    direct = scenario.get("run") if scenario["agent"] else None
    try:
        build_repo(repo_dir, {} if direct else scenario.get("setup", {}))
    except ValueError as error:
        return [], str(error)
    copy_components(SOURCE_DIR, repo_dir)
    prompt = direct["prompt"] if direct else scenario["input"]["prompt"]
    turns = [(prompt, run_claude(prompt, repo_dir, agent=scenario["agent"] if direct else None))]
    reply = scenario["input"].get("confirm_reply")
    if reply:
        turns.append((reply, run_claude(reply, repo_dir, session_id_of(turns[0][1]))))
    remove_project_folder(turns[0][1], repo_dir.resolve())
    patterns = pattern_results(direct.get("must_match", []) if direct else [], claude_text(turns))
    return patterns + grade(scenario["assertions"], transcript(turns), repo_state(repo_dir), scratch_dir), None


def main():
    """Run every tagged scenario, print each assertion's verdict, and exit 1 if any failed."""
    if shutil.which("claude") is None:
        sys.exit("claude isn't on PATH - install Claude Code and log in first.")
    scenarios = load_scenarios(SOURCE_DIR)
    failed = 0
    with tempfile.TemporaryDirectory(prefix="behaviour_evals_") as scratch:
        for scenario in scenarios:
            results, error = run_scenario(scenario, Path(scratch).resolve())
            passed = not error and all(result["pass"] for result in results)
            failed += not passed
            print(f"{'PASS' if passed else 'FAIL'}  {scenario['name']}" + (f": {error}" if error else ""))
            for result in results:
                print(f"    {'ok ' if result['pass'] else 'NO '} {result['assertion']} - {result['reason']}")
    print(f"\n{len(scenarios) - failed} of {len(scenarios)} scenarios passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
