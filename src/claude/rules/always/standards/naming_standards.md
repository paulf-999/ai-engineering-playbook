<!-- version: 2.2.5 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-13 -->
<!-- applies_to: * -->
<!-- miss_cost: low — names stop saying what a file holds -->
# 📛 Naming standards

**Purpose:** how to name new files, folders and config artefacts, so a reader knows what each holds without opening it.

- 🔤 **snake_case:** use lowercase words joined by underscores, with no hyphens or spaces, and keep existing names as they are.
  - **Except skills and agents:** join their words with hyphens, such as `git-create-pr`, since the [Agent Skills spec](https://agentskills.io/specification) allows only lowercase letters, digits and hyphens, and agents match skills.
- 🎯 **Self-describing:** make the name say what it holds, so `naming_standards.md` beats `standards.md`.
- 📈 **Name for scale:** fit the wider group it belongs to, so `naming_standards.md` beats `hook_naming.md`.

## 📚 Read on demand

- `on_demand/claude_config/claude_naming_patterns.md`, in your Claude config directory, before naming a new rule, skill or agent.
- `on_demand/style_guides/utilities/datetime.md`, when writing a date or time into a name, code, metadata or a log.
