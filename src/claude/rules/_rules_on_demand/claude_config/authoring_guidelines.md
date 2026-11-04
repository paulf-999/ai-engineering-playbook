<!-- version: 2.0.2 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-04 -->
# 🛠️ Authoring guidelines

**Purpose:** how to structure a new rule, skill or agent for Claude's config, once the guiding principles say it's worth adding.

## 📝 Rules

- 🚪 **Pick the tier:** put a rule under `rules/` only if every session needs it, add `paths:` if only some files do, and otherwise use `_rules_on_demand/`.
- 🔗 **Pointers:** reach an on-demand file with a "Read on demand" line naming its path, in your Claude config directory, and when to read it.
- 🧪 **Test the pointer:** run a lean session on a matching task, and check Claude reads the file before acting.

## 🛠️ Skills and agents

- 📁 **Skill layout:** give each skill a folder holding a short `SKILL.md`, with longer detail in a `reference/` folder it reads while running.
- 📝 **Descriptions:** keep skill and agent descriptions short, since every one loads in every session.
- 🤖 **When an agent:** use one only when the work needs its own context or an independent view, such as a blind review.
- 🏷️ **Names:** follow the patterns in `_rules_on_demand/claude_config/claude_naming_patterns.md`.
