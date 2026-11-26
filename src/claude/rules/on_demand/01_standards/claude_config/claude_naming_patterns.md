# 🏷️ Claude naming patterns

**Purpose:** the name each kind of Claude config artefact takes, with an example of each.

| Artefact | Pattern | Example |
|---|---|---|
| 📝 **Rule** | `<concept>.md`, named for the concept it covers | `naming_standards.md` |
| 🛠️ **Skill** | `<domain>-<action>`, a domain then an imperative verb, per the [Agent Skills spec](https://agentskills.io/specification) | `confluence-create-page` |
| 🤖 **Agent** | `agents/<group>/<domain>-<purpose>/AGENT.md`, hyphenated to match skills | `agents/core/technical-writer/AGENT.md` |

- 🗂️ **Group related rules:** put rules for one domain in a subfolder, such as `style_guides/sql.md`.
- 📁 **Working folders:** start a folder you or a component adds to the Claude config directory with `_`, such as `_claude_kaizen/`, and leave the ones Claude Code makes, such as `memory/`, as they are.
- 🔽 **Child files:** start a file with `_` when only its parent rule links to it, as in `terraform/_terraform_naming.md`, and make the rest of the name read alone, without its folder.
- 🕵️ **Test new names:** when naming several files at once, give 3 cold readers (`claude -p --safe-mode --max-turns 1`) their contents without titles or filenames, and keep the names they agree on.
- 💤 **On-demand files:** name them the same way, and put them in the repo's `rules/on_demand/`, which installs to `_on_demand/`.

## 📞 Called by

This rule is invoked by [`rules/always_on/01_standards/naming_standards.md`](../../../always_on/01_standards/naming_standards.md), before naming a new rule, skill, agent or config folder.
