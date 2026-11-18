# 🧠 Claude config

This folder is the source of a global Claude Code config. `make install` copies it into your Claude config directory, so edit it here rather than in the installed copy.

## 📦 What's here

| Path | What it holds |
|---|---|
| 🧭 [`CLAUDE.md`](CLAUDE.md) | Behavioural guidelines Claude reads every session |
| 📏 [`rules/`](rules/) | Short rule files, grouped by when they load |
| 🪝 [`hooks/`](hooks/) | Scripts Claude Code runs on tool calls or when Claude stops |
| 📋 [`_templates/`](_templates/README.md) | Starting points for new rules, skills, agents and scripts |

## ⏱️ When rules load

Every rule costs context, so its top folder, `always_on/`, `path_scoped/` or `on_demand/`, decides how often it loads, per the [rules README](rules/README.md). A kind folder inside it, `01_standards/`, `02_team_conventions/` or `03_preferences/`, says what [kind of rule](#-three-kinds-of-rule) it is.

- 📍 **Install location:** `on_demand/` installs beside `rules/`, not inside it, since Claude Code loads all of `rules/` every session.
- 🧩 **Child files:** a name starting with `_` marks detail split from a parent rule, read only when the parent points to it.

## 📖 Terms

| Term | Meaning |
|---|---|
| 📁 **Claude config directory** | The folder Claude Code reads its instructions and settings from, `~/.claude` unless `$CLAUDE_CONFIG_DIR` is set |
| 📏 **Rule** | A short markdown file telling Claude how to do one thing, such as name a dbt model |
| 🔢 **Tokens** | Claude's unit of context, capped for always-on files by the [always-on budget](../../docs/target_architecture/design_principles/01_principles.md#-numbers-and-tests) |
| 🪝 **Hook** | A small script Claude Code runs by itself at set moments, such as when Claude says it has finished |
| 📝 **Intent and Spec** | The two sections a long plan opens with, on what you want and what will be built, per [`ai_sdlc_workflow.md`](rules/always_on/01_standards/ai_sdlc_workflow.md) |
| 🛑 **Phase gate** | A pause after each stage of multi-stage work, such as after each PR, so you can check it before Claude goes on |

## 🧭 Three kinds of rule

| Kind | What it is | Example | Lives in | Installs |
|---|---|---|---|---|
| 🧰 **Standard** | Good practice for anyone using the tool | Pin your Docker base image | `01_standards/` folders | Always |
| 🏢 **Team convention** | This team's own choices for its shared work | `staging_`, `mart_` and `pub_` dbt prefixes | `02_team_conventions/` folders | With everything else |
| 👤 **Preference** | One person's taste in how Claude replies and keeps their files | Bold-keyword bullets | `03_preferences/` folders | Only with `PREFERENCES=1` |

- 🧭 **Sorting:** the [rule kinds guide](../../docs/guides/authoring_guide/_authoring_rule_kinds.md) sets out how a rule is sorted into one of the three.

## 👤 Preferences

They install only if you ask:

| Preference | What it does |
|---|---|
| 📤 **Reply format** | Opens each longer reply with a bold Summary, short themed bullets and numbered next steps |
| 🔑 **Bold-keyword bullets** | Starts each rule or definition bullet with its key term in bold, in replies, docs, tickets and commits |
| 🗂️ **Saved plans** | Saves each approved plan, with its intent and spec, to `~/.claude_work/_plans/` |
| 📝 **TODO list** | Adds "add to my TODOs" items to a table in your config's `TODO.md` |
| 🧱 **Markdown layout** | Gives headings, bullets and table rows an emoji, caps lists at 5 items, and opens each list with a lead-in |
| 📄 **Drafts, errors and session notes** | Saves drafts to `~/_drafts/`, error write-ups to `~/_errors/`, and long-task notes to `~/.claude_work/_sessions/` |

- 📥 **Install:** `make install PREFERENCES=1` adds them, a plain `make install` keeps them, and `make install PREFERENCES=0` removes them.
- 💰 **Cost:** about 280 tokens in every session for the reply and layout preferences and 200 for the working-files ones, per the [context cost report](../../maintenance/context_cost.md).
- ⚠️ **Limits:** they never go into a project install, and without them Claude stops reading an existing `TODO.md`, plans or drafts, and offers options unnumbered, still in British spelling.

## 🏗️ Installing into one repo

To share the config with a team, run `make install PROJECT=../my_dbt_repo` to install it into that repo's `.claude/` folder, then commit the folder.

- 🪝 **Hooks:** add `HOOKS=1` to include the done checks hook, which is left out by default.
- 🛡️ **Backups:** replaced files go to `backups/` in your Claude config directory, outside the repo.

## 🛠️ Changing it

- 🤝 **Team conventions:** change a `02_team_conventions/` file by PR here, then reinstall, since `make install` overwrites the installed copy.
- 📐 **Shape:** the [authoring guide](../../docs/guides/authoring_guide.md) covers writing a rule, skill or agent.
- ⚖️ **Need:** the [evaluation criteria](../../docs/target_architecture/design_principles/02_evaluation_criteria.md) decide if a component earns its context cost.
- ✅ **Checks:** `make test` checks rule structure, and pre-commit keeps always-on context within budget.
