<!-- version: 2.1.3 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-13 -->
<!-- applies_to: src/claude/**, **/.claude/** -->
<!-- miss_cost: low — names drift from the house patterns -->
# 🏷️ Claude naming patterns

**Purpose:** the name each kind of Claude config artefact takes, with an example of each.

| Artefact | Pattern | Example |
|---|---|---|
| 📝 **Rule** | `<concept>.md`, named for the concept it covers | `naming_standards.md` |
| 🛠️ **Skill** | `<domain>-<action>`, a domain then an imperative verb, per the [Agent Skills spec](https://agentskills.io/specification) | `confluence-create-page` |
| 🤖 **Agent** | `agents/<group>/<domain>-<purpose>/AGENT.md`, hyphenated to match skills | `agents/core/technical-writer/AGENT.md` |

- 🗂️ **Group related rules:** put rules for one domain in a subfolder, such as `style_guides/sql.md`.
- 💤 **On-demand files:** name them the same way, and put them in `on_demand/`.
