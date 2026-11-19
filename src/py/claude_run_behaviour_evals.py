"""Run each eval scenario tagged `behaviour: true` end to end, then have a separate grader judge its assertions.

Each scenario gets its own scratch git repo, built from its `setup:` keys, with no remote and only this repo's
skills and agents. Push, gh and web tools are blocked and MCP servers are dropped, so nothing leaves the machine.
A `confirm_reply` is sent by resuming the session. An agent's scenario with a `run:` block sends its self-contained
prompt straight to that agent in a bare repo, since its `setup:` only describes the prompt, and checks each
`must_match` pattern against Claude's text. The grader is a `claude -p --safe-mode` run that sees only the
assertions, the transcript and the repo's final state.
"""

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from claude_run_trigger_evals import SOURCE_DIR, copy_components, parse_events, project_folder

# claude -p refuses any tool not allowed here, so every other gh command, such as gh pr create, is refused too
ALLOWED_TOOLS = ["Read", "Glob", "Grep", "Skill", "Bash(ls:*)", "Bash(gh auth status:*)"] + [
    f"Bash(git {command}:*)"
    for command in ["status", "diff", "log", "branch", "rev-parse", "ls-files", "remote", "switch", "checkout"]
    + ["add", "commit"]
]
BLOCKED_TOOLS = ["Bash(git push:*)", "Bash(curl:*)", "WebFetch", "WebSearch"]
SETUP_KEYS = {"current_branch", "changed_files", "changed_file_count", "pr_template_exists"}
MAX_TURNS = "15"
TIMEOUT_SECONDS = 900
GRADER_SCHEMA = {
    "type": "object",
    "properties": {
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "assertion": {"type": "string"},
                    "pass": {"type": "boolean"},
                    "reason": {"type": "string"},
                },
                "required": ["assertion", "pass", "reason"],
            },
        }
    },
    "required": ["results"],
}
GRADER_BRIEF = """Grade each assertion against this Claude Code session. Pass an assertion only if the transcript or the
final repo state shows it holds. Give one short reason for each.

Assertions:
{assertions}

Transcript:
{transcript}

Final repo state:
{state}"""


def load_scenarios(source_dir):
    """Return every scenario tagged `behaviour: true`, from each evals.yaml under source_dir."""
    scenarios = []
    for path in sorted(source_dir.rglob("evals.yaml")):
        evals = yaml.safe_load(path.read_text())
        for scenario in evals["evals"]:
            if scenario.get("behaviour") is True:
                scenarios.append({**scenario, "agent": evals.get("agent_name")})
    return scenarios


def git(repo_dir, *args):
    """Run one git command in repo_dir and return its output."""
    return subprocess.run(["git", *args], cwd=repo_dir, check=True, capture_output=True, text=True).stdout


def build_repo(repo_dir, setup):
    """Make repo_dir a git repo in the state setup describes, or raise ValueError for a setup key it can't build."""
    unknown = set(setup) - SETUP_KEYS
    if unknown:
        raise ValueError(f"unsupported setup: {', '.join(sorted(unknown))}")
    git(repo_dir, "init", "-q", "-b", "main")
    git(repo_dir, "config", "user.email", "evals@example.invalid")
    git(repo_dir, "config", "user.name", "Evals")
    # The copied skills and agents mustn't show up as changes the skill under test would ship
    (repo_dir / ".git/info/exclude").write_text(".claude/\n")
    (repo_dir / "README.md").write_text("# Scratch repo\n")
    if setup.get("pr_template_exists"):
        (repo_dir / ".github").mkdir()
        (repo_dir / ".github/pull_request_template.md").write_text("# Summary\n\n## Testing\n")
    git(repo_dir, "add", "-A")
    git(repo_dir, "commit", "-q", "-m", "chore: initial commit")
    if setup.get("current_branch", "main") != "main":
        git(repo_dir, "switch", "-q", "-c", setup["current_branch"])
    changed = list(setup.get("changed_files", []))
    changed += [f"src/file_{number}.py" for number in range(setup.get("changed_file_count", 0))]
    for name in changed:
        (repo_dir / name).parent.mkdir(parents=True, exist_ok=True)
        (repo_dir / name).write_text("PLACEHOLDER=1\n" if name.endswith(".env") else "print('changed')\n")


def run_claude(prompt, repo_dir, session_id=None, agent=None):
    """Run one turn of claude -p in repo_dir, resuming session_id or as agent if given, and return its events."""
    command = ["claude", "-p", prompt, "--setting-sources", "project", "--strict-mcp-config"]
    command += ["--output-format", "stream-json", "--verbose", "--max-turns", MAX_TURNS]
    command += ["--allowedTools", *ALLOWED_TOOLS, "--disallowedTools", *BLOCKED_TOOLS]
    if session_id:
        command += ["--resume", session_id]
    if agent:
        command += ["--agent", agent]
    result = subprocess.run(command, cwd=repo_dir, capture_output=True, text=True, timeout=TIMEOUT_SECONDS)
    return parse_events(result.stdout.splitlines())


def session_id_of(events):
    """Return the session ID from a run's events, or None."""
    return next((event["session_id"] for event in events if event.get("session_id")), None)


def transcript(turns):
    """Render each turn's user prompt, Claude's text, tool calls and tool results as plain text for the grader."""
    lines = []
    for prompt, events in turns:
        lines.append(f"USER: {prompt}")
        for event in events:
            # Only assistant and user events carry a message with content blocks
            if event.get("type") not in ("assistant", "user"):
                continue
            content = event["message"].get("content", [])
            for block in content if isinstance(content, list) else []:
                if block.get("type") == "text":
                    lines.append(f"CLAUDE: {block['text']}")
                elif block.get("type") == "tool_use":
                    lines.append(f"TOOL {block['name']}: {json.dumps(block['input'])[:500]}")
                elif block.get("type") == "tool_result":
                    status = "REFUSED OR FAILED" if block.get("is_error") else "RESULT"
                    lines.append(f"{status}: {str(block.get('content'))[:500]}")
    return "\n".join(lines)


def repo_state(repo_dir):
    """Return the repo's branch, short status and recent commits, for assertions about its final state."""
    branch = git(repo_dir, "branch", "--show-current").strip()
    status = git(repo_dir, "status", "--short") or "(clean)\n"
    return f"branch: {branch}\nstatus:\n{status}log:\n{git(repo_dir, 'log', '--oneline', '-5')}"


def grade(assertions, transcript_text, state, grader_dir):
    """Ask a safe-mode claude -p grader to judge each assertion, returning its list of results."""
    brief = GRADER_BRIEF.format(
        assertions="\n".join(f"- {assertion}" for assertion in assertions), transcript=transcript_text, state=state
    )
    command = ["claude", "-p", brief, "--safe-mode", "--strict-mcp-config", "--no-session-persistence"]
    command += ["--max-turns", "3", "--output-format", "json", "--json-schema", json.dumps(GRADER_SCHEMA)]
    result = subprocess.run(command, cwd=grader_dir, capture_output=True, text=True, timeout=TIMEOUT_SECONDS)
    return json.loads(result.stdout)["structured_output"]["results"]


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
    folder = project_folder(turns[0][1], repo_dir.resolve())
    if folder:
        shutil.rmtree(folder, ignore_errors=True)
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
