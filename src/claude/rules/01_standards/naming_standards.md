<!-- version: 2.2.0 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-09 -->
<!-- applies_to: * -->
<!-- miss_cost: low — names stop saying what a file holds -->
<!-- loading: always-on — any session can create a file -->
# 📛 Naming standards

**Purpose:** how to name new files, folders and config artefacts, so a reader knows what each holds without opening it.

- 🔤 **snake_case:** use lowercase words joined by underscores, with no hyphens or spaces, and keep existing names as they are.
  - **Except skills and agents:** join their words with hyphens, such as `git-create-pr`, since the [Agent Skills spec](https://agentskills.io/specification) allows only lowercase letters, digits and hyphens, and agents match skills.
- 🎯 **Self-describing:** make the name say what it holds, so `naming_standards.md` beats `standards.md`.
- 📋 **Offer options:** before naming something new, propose 3 or 4 candidates with one marked recommended, since naming is the user's call.
- 📈 **Name for scale:** fit the wider group it belongs to, so `naming_standards.md` beats `hook_naming.md`.

- **Read on demand:** `_rules_on_demand/claude_config/claude_naming_patterns.md`, in your Claude config directory, before naming a new rule, skill, hook or agent.
- **Read on demand:** `_rules_on_demand/style_guides/utilities/datetime.md`, when writing a date or time into a name, code, metadata or a log.
