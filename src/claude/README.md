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

## 🧭 Three kinds of rule

| Kind | What it is | Example | Lives in | Installs |
|---|---|---|---|---|
| 🧰 **Standard** | Good practice for anyone using the tool | Pin your Docker base image | Everywhere below | Always |
| 🏢 **Team convention** | This team's own choices for its shared work | `staging_`, `mart_` and `pub_` dbt prefixes | `team_conventions/` folders | With everything else |
| 👤 **Preference** | One person's taste in how Claude replies and keeps their files | Bold-keyword bullets | `preferences/` folders | Only with `PREFERENCES=1` |

- 🏢 **Team conventions:** these are this team's choices, and they install with everything else. To use your own, change the files in `team_conventions/`, by PR or in your own copy of the repo. There's no switch to turn them off.
- 🚧 **Moving in:** dbt's, SQL's, Airflow's, Ansible's, Terraform's and Python's conventions are in `team_conventions/` so far. The Docker guides still mark theirs with a 🏢 banner, and the other guides mix them in, until they move.

## 👤 Preferences

Preferences are one person's taste in how Claude replies and where it keeps their own files, rather than a [standard or team convention](#-three-kinds-of-rule), so they install only if you ask:

| Preference | What it does | Example | Why you might want it |
|---|---|---|---|
| 📤 **Reply format** | Opens each longer reply with a bold Summary, short themed bullets and numbered next steps | A reply you can scan in seconds, ending "1. 🚀 **Ship it** (recommended)" | Faster to read long answers |
| 🔑 **Bold-keyword bullets** | Starts each rule or definition bullet with its key term in bold, in replies, docs, tickets and commits | "**Scope:** build only what was asked for." | Lists you can skim by their first words |
| 🗂️ **Saved plans** | Saves each approved plan, with its intent and spec, to `~/.claude_work/_plans/` | `~/.claude_work/_plans/active/2026_11_16_rule_kinds/plan.md` | Plans outlive the session and stay out of your repos |
| 📝 **TODO list** | Adds "add to my TODOs" items to a table in your config's `TODO.md` | A numbered row with a priority and what "done" means | One place for follow-ups |
| 🧱 **Markdown layout** | Gives headings, bullets and table rows an emoji, caps lists at 5 items, and opens each list with a lead-in | A doc whose sections and bullets each start with an emoji | Pages that scan the same way |
| 📄 **Drafts, errors and session notes** | Saves drafts to `~/_drafts/`, error write-ups to `~/_errors/`, and long-task notes to `~/.claude_work/_sessions/` | `~/_drafts/jira/2026_11_16_login_bug.md` | Drafts and notes are kept in one place you can find |

- 📥 **Install:** `make install PREFERENCES=1` adds them, a plain `make install` keeps them, and `make install PREFERENCES=0` removes them.
- 💰 **Cost:** about 280 tokens in every session for the reply and layout preferences and 200 for the working-files ones, per the [context cost report](../../maintenance/context_cost.md).
- ⬆️ **Upgrading:** an existing `TODO.md`, saved plans and drafts stay where they are, but without `PREFERENCES=1` Claude no longer reads or adds to them.
- 🚚 **Projects:** they never go into a project install, since that folder is shared.
- 💬 **Without them:** Claude still offers options, just not as a numbered list, and still uses British spelling, so ask if you want American English.

## 🏗️ Installing into one repo

To share the config with a team, install it into a repo's `.claude/` folder and commit that folder:

```bash
make install PROJECT=../my_dbt_repo
```

- 🪝 **Hooks:** add `HOOKS=1` to include the done checks hook, which is left out by default.
- 🛡️ **Backups:** anything replaced is backed up to the `backups/` folder in your Claude config directory, outside the repo.

## 🛠️ Changing it

- 🤝 **Team conventions:** propose a change to a `team_conventions/` file by PR here, then reinstall, since `make install` replaces edits made to the installed copy, per [the three kinds](#-three-kinds-of-rule).
- 📐 **Shape:** the [authoring guide](../../docs/guides/authoring_guide.md) covers writing a rule, skill or agent.
- ⚖️ **Need:** the [evaluation criteria](../../docs/target_architecture/design_principles/02_evaluation_criteria.md) decide whether a component earns its context cost.
- ✅ **Checks:** `make test` checks rule structure, and pre-commit keeps always-on context within budget.
