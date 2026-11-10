<!-- version: 1.0.2 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-10 -->
# 🧠 Claude config

**Purpose:** a high-level map of the Claude Code config in this folder, for someone new to the repo.

This folder is the source of a global Claude Code config, the instructions that shape how Claude works in every project. `make install` copies it into your Claude config directory, `$CLAUDE_CONFIG_DIR` or `~/.claude`, so edit it here rather than in the installed copy.

## 📦 What's here

| Path | What it holds |
|---|---|
| 🧭 [`CLAUDE.md`](CLAUDE.md) | The behavioural guidelines Claude reads at the start of every session |
| 📏 [`rules/`](rules/) | Short rule files, grouped by when they load |
| 🪝 [`hooks/`](hooks/) | Scripts Claude Code runs on a tool call, which `make install` registers in `settings.json`, such as the check that a plan opens with Intent and Spec |
| 📋 [`_templates/`](_templates/README.md) | Starting points for new rules, skills, agents and scripts |

## ⏱️ When rules load

Every rule costs context, so each one loads only as often as it's needed. Its folder decides when:

| Folder | Loads |
|---|---|
| 🔁 `01_standards/`, `02_conduct/`, `03_workflows/` | In every session: naming and reply standards, how Claude behaves, and planning habits |
| 📂 `_path_scoped_rules/` | Only when Claude works on a matching file, such as the Python guide for `.py` files, set by each rule's `paths:` list |
| 💤 `_rules_on_demand/` | Only when another rule's "Read on demand" pointer sends Claude there, since the install moves this folder out of `rules/` |

A file whose name starts with `_` is a child: detail split out of a parent rule, read only when the parent points to it.

## 🛠️ Changing it

- 📐 **Shape:** the [authoring guidelines](rules/_rules_on_demand/claude_config/authoring_guidelines.md) cover how to write a rule, skill or agent.
- ⚖️ **Need:** the [evaluation criteria](../../docs/target_architecture/design_principles/02_evaluation_criteria.md) decide whether a new component earns its context cost.
- ✅ **Checks:** `make test` checks each rule's structure, and pre-commit keeps the always-on context within budget.
