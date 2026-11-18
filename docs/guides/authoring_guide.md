# 🛠️ Authoring guide

**Purpose:** how to build a new rule, skill or agent for `src/claude/`, once the installed [guiding principles](../../src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md) say it's worth adding.

## ✅ Every file

- 🔁 **No duplicate:** search the rules, skills and agents for one that already covers the need, and extend it rather than adding another.
- 📋 **Start from a template:** copy the matching file from [`src/claude/_templates/`](../../src/claude/_templates/README.md), rather than starting from a blank page.
- 🎯 **Opening:** an H1 with an emoji, then a one-line **Purpose:** saying what the file does.
- 1️⃣ **One concept:** keep each file to one concept, and split anything broader into a parent and 2 or more `<parent>/_<aspect>.md` children.
- ✂️ **Split only when large:** split a file only once it would pass the [Rule size cap](../target_architecture/architecture/_budget_and_guards.md#️-design-guards), and give each child at least the 40 lines [`test_rules_structure.py`](../../tests/src/claude/test_rules_structure.py) checks, since a smaller one saves too little context to be worth its own file and pointer. The floor is for rules, which Claude loads, so docs pages such as this guide's own children can be shorter. Children of an always-on rule are exempt, since they split to keep every session cheap.
- 🔑 **Bullets:** open each with a bold keyword and keep it to one sentence.

## 🌍 Portable paths

Hooks, scripts and tests for the config must work on any machine:

- 🚫 **No hard-coded paths:** never hard-code a home folder, username or `~/.claude` path, since the config directory varies between machines.
- 🐍 **Python:** read the config directory from `CLAUDE_CONFIG_DIR`, using `~/.claude` only as the fallback when it's unset.
- 🐚 **Shell:** resolve paths from the script's own location, using `"$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"`.
- 🛡️ **Guard clauses too:** compare against the resolved directory, never a substring such as `*".claude/"*`.
- 📅 **Why:** hard-coded paths pass on the machine that wrote them and fail silently elsewhere, as the old config's hooks and tests did.

## 📚 By kind

- 📝 **[Rules](authoring_guide/_authoring_rules.md):** pick the tier, wire up pointers, and check it before merging.
- 🧭 **[Rule kinds](authoring_guide/_authoring_rule_kinds.md):** decide whether a rule is a standard, a team convention or a preference, and where each lives.
- 🛠️ **[Skills](authoring_guide/_authoring_skills.md):** the folder layout, scope, triggers and checks, for the skills coming soon.
- 🤖 **[Agents](authoring_guide/_authoring_agents.md):** when to build one, and how to write and check it, for the agents coming soon.
