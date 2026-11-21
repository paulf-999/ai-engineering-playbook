"""Check that each eval scenario tagged with `trigger:` starts the right skill or agent, or none, in a live run.

Each scenario runs `claude -p` once, on the user's own login, in a scratch git repo holding only this repo's skills
and agents. File-changing, shell and web tools are blocked, so a run can't change anything or reach another service.
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from claude_evals_common import SOURCE_DIR, copy_components, parse_events, remove_project_folder

BLOCKED_TOOLS = ["Bash", "Write", "Edit", "NotebookEdit", "WebFetch", "WebSearch"]
# Enough turns to look around before routing; a run stops early at its first skill or agent call
MAX_TURNS = "5"


def load_scenarios(source_dir):
    """Return every scenario that has a `trigger:` key, from each evals.yaml under source_dir."""
    scenarios = []
    for path in sorted(source_dir.rglob("evals.yaml")):
        for scenario in yaml.safe_load(path.read_text())["evals"]:
            if "trigger" in scenario:
                scenarios.append(
                    {"name": scenario["name"], "prompt": scenario["input"]["prompt"], "trigger": scenario["trigger"]}
                )
    return scenarios


def component_names(source_dir):
    """Return the names of the repo's skills and agents, which are their folder names."""
    folders = [*source_dir.glob("skills/**/SKILL.md"), *source_dir.glob("agents/**/AGENT.md")]
    return {path.parent.name for path in folders}


def first_call(events):
    """Return the skill or agent named by a run's first Skill or Agent call, or None."""
    for event in events:
        if event.get("type") != "assistant":
            continue
        for block in event["message"].get("content", []):
            if block.get("type") == "tool_use":
                called = block["input"].get("skill") or block["input"].get("subagent_type")
                if called:
                    return called
    return None


def first_component(events, names):
    """Return the repo skill or agent a run routes to first, or "none" if it routes elsewhere or nowhere."""
    called = first_call(events)
    return called if called in names else "none"


def run_scenario(prompt, repo_dir):
    """Run one prompt through claude -p in repo_dir, stopping at its first skill or agent call; return its events."""
    command = ["claude", "-p", prompt, "--setting-sources", "project", "--output-format", "stream-json"]
    command += ["--verbose", "--max-turns", MAX_TURNS, "--disallowedTools", *BLOCKED_TOOLS]
    events = []
    with subprocess.Popen(command, cwd=repo_dir, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True) as run:
        for line in run.stdout:
            events += parse_events([line])
            # The first skill or agent call, from the repo or built in, settles the result, so stop it there
            if first_call(events[-1:]):
                # claude -p keeps running after SIGTERM until its turn ends, so SIGKILL it
                run.kill()
                break
    return events


def main():
    """Run every tagged scenario, print a pass or fail line for each, and exit 1 if any failed."""
    if shutil.which("claude") is None:
        sys.exit("claude isn't on PATH - install Claude Code and log in first.")
    scenarios = load_scenarios(SOURCE_DIR)
    names = component_names(SOURCE_DIR)
    failures = 0
    with tempfile.TemporaryDirectory(prefix="trigger_evals_") as scratch:
        repo_dir = Path(scratch).resolve()
        subprocess.run(["git", "init", "-q", str(repo_dir)], check=True)
        copy_components(SOURCE_DIR, repo_dir)
        for scenario in scenarios:
            events = run_scenario(scenario["prompt"], repo_dir)
            called = first_component(events, names)
            passed = called == scenario["trigger"]
            failures += not passed
            print(f"{'PASS' if passed else 'FAIL'}  {scenario['name']}: expected {scenario['trigger']}, got {called}")
            remove_project_folder(events, repo_dir)
    print(f"\n{len(scenarios) - failures} of {len(scenarios)} passed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
