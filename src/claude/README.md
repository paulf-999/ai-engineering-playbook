<!-- version: 1.0.8 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-13 -->
# 🧠 Claude config

**Purpose:** a high-level map of the Claude Code config in this folder, for someone new to the repo.

This folder is the source of a global Claude Code config, the instructions that shape how Claude works in every project. `make install` copies it into your Claude config directory, `$CLAUDE_CONFIG_DIR` or `~/.claude`, so edit it here rather than in the installed copy.

## 📦 What's here

| Path | What it holds |
|---|---|
| 🧭 [`CLAUDE.md`](CLAUDE.md) | The behavioural guidelines Claude reads at the start of every session |
| 📏 [`rules/`](rules/) | Short rule files, grouped by when they load |
| 🪝 [`hooks/`](hooks/) | Scripts Claude Code runs on a tool call or when Claude stops, which `make install` registers in `settings.json`, such as the check that a plan opens with Intent and Spec, which runs only when Claude leaves plan mode, so quick tasks never hit it |
| 📋 [`_templates/`](_templates/README.md) | Starting points for new rules, skills, agents and scripts |

## ⏱️ When rules load

Every rule costs context, so each one loads only as often as it's needed. Its folder decides when:

| Folder | Loads |
|---|---|
| 🔁 `always/` | In every session: naming and reply standards, how Claude behaves, and planning habits |
| 📂 `path_scoped/` | Only when Claude works on a matching file, such as the Python guide for `.py` files, set by each rule's `paths:` list |
| 💤 `on_demand/` | Only when another rule's "Read on demand" pointer, or a hook's block message, sends Claude there, since the install moves this folder out of `rules/` |

A file whose name starts with `_` is a child: detail split out of a parent rule, read only when the parent points to it.

Inside `on_demand/`, the `conduct/` and `workflows/` folders hold the detail that the every-session rules in `always/conduct/` and `always/workflows/` point to.

## 🛠️ Changing it

- 📐 **Shape:** the [authoring guidelines](rules/on_demand/claude_config/authoring_guidelines.md) cover how to write a rule, skill or agent.
- ⚖️ **Need:** the [evaluation criteria](../../docs/target_architecture/design_principles/02_evaluation_criteria.md) decide whether a new component earns its context cost.
- ✅ **Checks:** `make test` checks each rule's structure, and pre-commit keeps the always-on context within budget.
