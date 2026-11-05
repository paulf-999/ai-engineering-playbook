<!-- version: 2.0.1 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-04 -->
# 🏷️ Claude naming patterns

**Purpose:** the name each kind of Claude config artefact takes, with an example of each.

| Artefact | Pattern | Example |
|---|---|---|
| 📝 **Rule** | `<concept>.md`, named for the concept it covers | `naming_standards.md` |
| 🛠️ **Skill** | `<domain>_<action>`, a domain then an imperative verb | `confluence_create_page` |
| 🪝 **Hook** | `hook_<type>_<domain>.sh`, where type is `enforcement`, `style_guide` or `session_start` | `hook_enforcement_naming_convention.sh` |
| 🤖 **Agent** | `agents/<group>/<name>/AGENT.md` | `agents/core/technical_writer/AGENT.md` |

- 🗂️ **Group related rules:** put rules for one domain in a subfolder, such as `style_guides/sql.md`.
- 💤 **On-demand files:** name them the same way, and put them in `_rules_on_demand/`.
