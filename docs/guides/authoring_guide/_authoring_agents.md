# 🤖 Authoring agents

**Purpose:** when to build an agent, and how to write and check one, as part of the [authoring guide](../authoring_guide.md).

- 👥 **When:** build one only when the work needs a separate context or an independent view, such as a blind review, and otherwise use a skill for a procedure or a rule for guidance.
- 🏷️ **Name and place:** follow [`claude_naming_patterns.md`](../../../src/claude/rules/on_demand/01_standards/claude_config/claude_naming_patterns.md).
- 📄 **Template:** start from `_templates/AGENT.md.template`, and keep the result to about 40 to 60 lines.
- 🗣️ **Description:** say when Claude should delegate to it, since Claude Code decides from the description alone, and keep it short, since it loads in every session.
- 🔐 **Tools:** list only what the job needs, since leaving `tools:` out grants every tool, and set `isolation: worktree` only for an agent that changes files.
- 🚧 **Constraints:** say what it doesn't do, and why.
- 🧪 **Evals:** give a scenario a self-contained `run:` prompt, with optional `must_match` patterns, and tag it `behaviour: true`, so `make evals BEHAVIOUR=1` sends it straight to the agent and grades its assertions.

## 🏁 Before merging

Run the same checks as for a skill, listed in [authoring skills](_authoring_skills.md#-before-merging).
