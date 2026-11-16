# 🧠 Claude config

This folder is the source of a global Claude Code config: `make install` copies it into your Claude config directory, `$CLAUDE_CONFIG_DIR` or `~/.claude`, so edit it here rather than in the installed copy.

## 📦 What's here

| Path | What it holds |
|---|---|
| 🧭 [`CLAUDE.md`](CLAUDE.md) | Behavioural guidelines Claude reads every session |
| 📏 [`rules/`](rules/) | Short rule files, grouped by when they load |
| 🪝 [`hooks/`](hooks/) | Scripts Claude Code runs on tool calls or when Claude stops |
| 📋 [`_templates/`](_templates/README.md) | Starting points for new rules, skills, agents and scripts |

## ⏱️ When rules load

Every rule costs context, so its folder decides how often it loads:

| Folder | Loads |
|---|---|
| 🔁 `always_on/` | Every session |
| 📂 `path_scoped/` | When Claude works on a file matching the rule's `paths:` list |
| 💤 `on_demand/` | When a rule's "Read on demand" pointer or a hook sends Claude there |

- 📍 **Install location:** `on_demand/` installs beside `rules/`, not inside it, since Claude Code loads all of `rules/` every session.
- 🧩 **Child files:** a name starting with `_` marks detail split from a parent rule, read only when the parent points to it.

## 📖 Terms

- 📁 **Claude config directory:** the folder Claude Code reads its instructions and settings from, `~/.claude` unless `$CLAUDE_CONFIG_DIR` is set.
- 📏 **Rule:** a short markdown file telling Claude how to do one thing, such as name a dbt model.
- ⏱️ **Always-on, path-scoped and on-demand:** when a rule loads: every session, only when Claude works on a matching file such as a dbt model, or only when another rule points Claude to it.
- 🔢 **Tokens:** the unit Claude's working memory is measured in, about three-quarters of a word. The always-on budget caps everything that loads in every session, at the figure in the [design principles](../../docs/target_architecture/design_principles/01_principles.md#-numbers-and-tests).
- 🪝 **Hook:** a small script Claude Code runs by itself at set moments, such as when Claude says it has finished.
- 📝 **Intent and Spec:** the two sections a long plan opens with, on what you want and what will be built, per [`sdlc_workflow.md`](rules/always_on/workflows/sdlc_workflow.md). A quick request, such as one query, needs no plan.
- 🛑 **Phase gate:** a pause after each stage of multi-stage work, such as after each PR, so you can check it before Claude goes on.

## 🏢 Installing into one repo

To share the config with a team, install it into a repo's `.claude/` folder and commit that folder:

```bash
make install PROJECT=../my_dbt_repo
```

- 🪝 **Hooks:** add `HOOKS=1` to include the done checks hook, which is left out by default.
- 🛡️ **Backups:** anything replaced is backed up to the `backups/` folder in your Claude config directory, outside the repo.

## 🛠️ Changing it

- 🤝 **Team conventions:** propose a change by PR here, then reinstall, since `make install` replaces edits made to the installed copy.
- 📐 **Shape:** the [authoring guide](../../docs/guides/authoring_guide.md) covers writing a rule, skill or agent.
- ⚖️ **Need:** the [evaluation criteria](../../docs/target_architecture/design_principles/02_evaluation_criteria.md) decide whether a component earns its context cost.
- ✅ **Checks:** `make test` checks rule structure, and pre-commit keeps always-on context within budget.
