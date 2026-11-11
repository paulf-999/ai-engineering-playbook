<!-- version: 3.0.8 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-11 -->
<!-- applies_to: src/claude/**, **/.claude/** -->
<!-- miss_cost: medium — a new rule, skill or agent drifts from the house structure -->
# 🛠️ Authoring guidelines

**Purpose:** how to build a new rule, skill or agent for Claude's config, once the guiding principles say it's worth adding.

This page is the entry point for authoring, and its rules, skills and agents guides follow below.

## ✅ Before you start

- 🧭 **Right mechanism:** put a fact for every session in `CLAUDE.md`, guidance for certain files in a path-scoped rule, a procedure in a skill, and work that needs its own context in an agent.
- 🔁 **No duplicate:** search the rules, skills and agents for one that already covers the need, and extend it rather than adding another.
- 📋 **Start from a template:** copy the matching file from `_templates/`, rather than starting from a blank page.

## 📏 Quality gates for every file

- 🏷️ **Header:** place and bump the `version`, `created` and `updated` lines as the playbook repo's `docs/maintenance/file_headers.md` says.
- 🎯 **Opening:** an H1 with an emoji, then a one-line **Purpose:** saying what the file does.
- 1️⃣ **One concept:** keep each file to one concept and about 110 lines, and split anything longer into a parent and 2 or more `<parent>/_<aspect>.md` children.
- 🔑 **Bullets:** open each with a bold keyword and keep it to one sentence.
- 🌍 **Paths:** hard-code no home folder or username, per `portable_paths.md`.

## 📚 Read on demand

- **Read on demand:** `_rules_on_demand/claude_config/authoring_guidelines/_authoring_rules.md`, in your Claude config directory, before writing or reviewing a rule.
- **Read on demand:** `_rules_on_demand/claude_config/authoring_guidelines/_authoring_skills.md`, before writing or reviewing a skill, planned since none exist yet.
- **Read on demand:** `_rules_on_demand/claude_config/authoring_guidelines/_authoring_agents.md`, before writing or reviewing an agent, planned since none exist yet.
- **Read on demand:** `_rules_on_demand/claude_config/claude_naming_patterns.md`, before naming a new rule, skill or agent.
- **Read on demand:** `_templates/README.md`, for the template each kind of file starts from.
