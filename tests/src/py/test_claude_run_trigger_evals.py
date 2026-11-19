"""Tests for the trigger evals runner's scenario selection, config copy and grading, without a live claude run."""

import importlib.util
import json

from _paths import REPO_ROOT

SPEC = importlib.util.spec_from_file_location("runner", REPO_ROOT / "src" / "py" / "claude_run_trigger_evals.py")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)

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


def test_copy_components_flattens_grouped_skills(tmp_path):
    """Grouped skills install flat, agents keep their folders, and both count as repo components."""
    source = tmp_path / "src"
    (source / "skills/_git_skills/git-create-pr").mkdir(parents=True)
    (source / "skills/_git_skills/git-create-pr/SKILL.md").write_text("skill")
    (source / "agents/core/code-reviewer").mkdir(parents=True)
    (source / "agents/core/code-reviewer/AGENT.md").write_text("agent")
    runner.copy_components(source, tmp_path)
    assert (tmp_path / ".claude/skills/git-create-pr/SKILL.md").exists()
    assert (tmp_path / ".claude/agents/core/code-reviewer/AGENT.md").exists()
    assert runner.component_names(source) == NAMES


def test_first_component_finds_skill_or_agent():
    """A Skill call and an Agent call each report the component they name."""
    assert runner.first_component([tool_call("Skill", {"skill": "git-create-pr"})], NAMES) == "git-create-pr"
    assert runner.first_component([tool_call("Agent", {"subagent_type": "code-reviewer"})], NAMES) == "code-reviewer"


def test_first_component_ignores_built_in_skills_and_other_tools():
    """Tools and built-in skills that aren't in the repo grade as none."""
    events = [tool_call("Glob", {"pattern": "*"}), tool_call("Skill", {"skill": "code-review"})]
    assert runner.first_component(events, NAMES) == "none"


def test_project_folder_only_matches_the_scratch_repo(tmp_path):
    """Only the projects/ folder named after the scratch repo is picked for deletion."""
    repo_dir = tmp_path / "trigger_evals_ab12"
    init = {
        "type": "system",
        "subtype": "init",
        "memory_paths": {"auto": "/cfg/projects/-tmp-trigger-evals-ab12/memory/"},
    }
    assert str(runner.project_folder([init], repo_dir)) == "/cfg/projects/-tmp-trigger-evals-ab12"
    init["memory_paths"]["auto"] = "/cfg/projects/-Users-me-real-repo/memory/"
    assert runner.project_folder([init], repo_dir) is None
