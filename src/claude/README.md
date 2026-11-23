# 🧠 Claude config

**Purpose:** the source of a global Claude Code config, which `make install` copies into your Claude config directory, so edit it here rather than in the installed copy.

## 📦 What's here

| Path | What it holds |
|---|---|
| 🧭 [`CLAUDE.md`](CLAUDE.md) | Behavioural guidelines Claude reads every session |
| 📏 [`rules/`](rules/) | Short rule files, grouped by when they load |
| 🪝 [`hooks/`](hooks/) | Scripts Claude Code runs at set points, such as before a tool call or when Claude stops |
| 🛠️ [`skills/`](skills/) | Step-by-step workflows you run by name, such as `/git-create-pr`, grouped in [`_atlassian_skills/`](skills/_atlassian_skills/README.md), [`_claude_skills/`](skills/_claude_skills/README.md) and [`_git_skills/`](skills/_git_skills/README.md), which install flat |
| 🤖 [`agents/`](agents/) | Subagents Claude delegates to for a separate context, such as a blind code review |
| 📋 [`_templates/`](_templates/README.md) | Starting points for new rules, skills, agents and scripts |

## ⏱️ When rules load

Every rule costs context, so its top folder, `always_on/`, `path_scoped/` or `on_demand/`, decides how often it loads, per the [rules README](rules/README.md). A kind folder inside it, `01_standards/` or `02_preferences/`, says what [kind of rule](#-three-kinds-of-rule) it is. A team convention sits beside the standard it extends as `<name>_team_conventions.md`, and style guides sit in `style_guides/`.

<details>
<summary>Where on-demand and child files go</summary>

- 📍 **Install location:** `on_demand/` installs beside `rules/`, not inside it, since Claude Code loads files in `rules/` by itself.
- 🧩 **Child files:** a name starting with `_` marks detail split from a parent rule, read only when the parent points to it.

</details>

## 📖 Terms

The few words this config uses that you might not know are in the getting-started guide's [words you'll meet](../../docs/guides/getting_started.md#-words-youll-meet).

## 🧭 Three kinds of rule

Each rule is a standard, a team convention or a preference, which decides whether it installs.

- 🧭 **Sorting:** the [rule kinds guide](../../docs/guides/authoring_guide/_rule_classification.md) sets out each kind, where it lives, when it installs and how a rule is sorted.

## 👤 Preferences

<details>
<summary>Show the preferences, their cost and limits</summary>

| Preference | What it does |
|---|---|
| 📤 **Reply format** | Opens each longer reply with a bold Summary, short themed bullets and numbered next steps |
| 🔑 **Bold-keyword bullets** | Starts each rule or definition bullet with its key term in bold, in replies, docs, tickets and commits |
| 🗂️ **Saved plans** | Saves each approved plan, with its intent and spec, to `~/.claude_work/_plans/` |
| 📝 **TODO list** | Adds "add to my TODOs" items to a table in your config's `TODO.md` |
| ✏️ **Writing style** | Keeps prose brief, with one idea per sentence, and says what something does before how it works |
| 🧱 **Markdown style** | Gives headings, bullets and table rows an emoji, caps lists at 5 items, and opens each list with a lead-in |
| 📄 **Drafts, errors and session notes** | Saves drafts to `~/_drafts/`, error write-ups to `~/_errors/`, and long-task notes to `~/.claude_work/_sessions/` |

- 📥 **Install:** the [getting-started guide](../../docs/guides/getting_started.md#️-3-run-it) says which installs include them.
- 💰 **Cost:** the reply and working-files preferences load in every session and the rest on demand, and the [context cost report](../../maintenance/context_cost.md) gives each one's tokens.
- ⚠️ **Limits:** without them Claude stops reading an existing `TODO.md`, plans or drafts, and offers options unnumbered, still in British spelling.

</details>

## 🏗️ Installing into one repo

To share the config with a team, run `make install PROJECT=../my_dbt_repo` to install it into that repo's `.claude/` folder, then commit the folder.

- 📥 **Options:** the [getting-started guide](../../docs/guides/getting_started.md#️-3-run-it) covers the hooks a one-repo install leaves out, and where replaced files are backed up.

## 🛠️ Changing it

Change the config by PR here, then reinstall.

<details>
<summary>Conventions, shape, need and checks</summary>

- 🤝 **Team conventions:** change a `_team_conventions` file by PR here, then reinstall, since `make install` overwrites the installed copy.
- 📐 **Shape:** the [authoring guide](../../docs/guides/authoring_guide.md) covers writing a rule, skill or agent.
- ⚖️ **Need:** the [evaluation criteria](../../docs/target_architecture/design_principles/02_evaluation_criteria.md) decide if a component earns its context cost.
- ✅ **Checks:** `make test` checks rule structure, and pre-commit keeps always-on context within budget.

</details>
