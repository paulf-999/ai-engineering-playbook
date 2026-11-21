"""Tests for the trigger evals runner's scenario selection, config copy and grading, without a live claude run."""

import importlib
import json
import sys

from _paths import REPO_ROOT

# The runner imports the shared eval helpers by name, as it does when run as a script
sys.path.insert(0, str(REPO_ROOT / "src" / "py"))
runner = importlib.import_module("claude_run_trigger_evals")

NAMES = {"git-create-pr", "code-reviewer"}


def tool_call(name, tool_input):
    """Return one stream-json assistant event that calls a tool."""
    return {"type": "assistant", "message": {"content": [{"type": "tool_use", "name": name, "input": tool_input}]}}


def test_load_scenarios_keeps_only_tagged_ones(tmp_path):
    """Only scenarios with a trigger: key are run."""
    evals = {
        "evals": [
            {"name": "tagged", "trigger": "none", "input": {"prompt": "hello"}},
            {"name": "untagged", "input": {"prompt": "bye"}},
        ]
    }
    (tmp_path / "evals.yaml").write_text(json.dumps(evals))
    assert runner.load_scenarios(tmp_path) == [{"name": "tagged", "prompt": "hello", "trigger": "none"}]


def test_component_names_cover_grouped_skills_and_agents(tmp_path):
    """Grouped skills and agents both count as repo components, by folder name."""
    (tmp_path / "skills/_git_skills/git-create-pr").mkdir(parents=True)
    (tmp_path / "skills/_git_skills/git-create-pr/SKILL.md").write_text("skill")
    (tmp_path / "agents/core/code-reviewer").mkdir(parents=True)
    (tmp_path / "agents/core/code-reviewer/AGENT.md").write_text("agent")
    assert runner.component_names(tmp_path) == NAMES


def test_first_component_finds_skill_or_agent():
    """A Skill call and an Agent call each report the component they name."""
    assert runner.first_component([tool_call("Skill", {"skill": "git-create-pr"})], NAMES) == "git-create-pr"
    assert runner.first_component([tool_call("Agent", {"subagent_type": "code-reviewer"})], NAMES) == "code-reviewer"


def test_first_component_ignores_built_in_skills_and_other_tools():
    """Tools and built-in skills that aren't in the repo grade as none."""
    events = [tool_call("Glob", {"pattern": "*"}), tool_call("Skill", {"skill": "code-review"})]
    assert runner.first_component(events, NAMES) == "none"
