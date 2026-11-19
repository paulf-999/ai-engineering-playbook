# 🚀 Getting started

**Purpose:** how to install the Claude Code instructions, check they work, and undo them, for someone using them rather than maintaining this repo.

## 📥 1. Clone the repo

```bash
git clone https://github.com/paulf-999/ai-engineering-playbook.git
cd ai-engineering-playbook
```

Use a git clone, not a zip download, since the installer copies only the files git tracks.

## 🧩 What the rules assume

The dbt and Airflow rules follow one team's conventions, so they fit best where your project matches them:

| Area | The rules assume |
|---|---|
| 🏷️ **dbt model names** | Layer prefixes `staging_`, `mart_` and `pub_`, each layer in its own folder under `models/` |
| 📸 **dbt snapshots** | Snapshots built in the Snowflake `WAREHOUSE` schema |
| 🌬️ **Airflow DAGs** | DAGs read their settings through a shared `your_dags_package.includes.common` module |

Where your project differs, Claude follows these names anyway, so check what it writes. The general standards, such as testing and security, apply to any project.

## 🎯 2. Choose where to install

| Install | Command | Applies to | Use it when |
|---|---|---|---|
| 🏗️ **One repo** | `make install PROJECT=<path to repo>` | That repo only, through its `.claude/` folder | You want the team's rules in your team's repo, such as its dbt project |
| 🌍 **Everywhere** | `make install` | Every project you open in Claude Code | You want the same behaviour in all your work |

- 🤔 **Not sure?** Start with one repo: it changes nothing else, and `make uninstall PROJECT=<path to repo>` undoes it.
- 🤝 **For a team:** commit the repo's `.claude/` folder, so everyone gets the same rules. Check `git status` first, since the install also writes its own `settings.json` and record files there.

## 🔧 What installing changes

Besides adding instructions, installing changes how Claude works wherever you installed it:

- 💬 **Replies:** Claude uses British spelling and offers options before big changes. Its scannable reply format is [opt-in](../../src/claude/README.md#-preferences): `make install PREFERENCES=1`.
- 🗺️ **Plans:** a long plan must say what you want and how to check it's done, and work of 3 or more stages pauses after each one for your go-ahead.
- 🪝 **Automatic checks:** one blocks long plans that skip those sections, one sends Claude back to run the repo's checks before it finishes, and one stops Claude's first edit in a shared repo folder so it works in its own copy. A one-repo install leaves out the last two unless you add `HOOKS=1`.
- 🔒 **Files:** Claude's file tools can't read `.env` files. Saving plans and notes outside your repos is opt-in too.

## ▶️ 3. Run it

Run the command you chose in your own terminal, since the installer asks you to type `install` and refuses to run inside Claude Code. It lists every file it will add, so nothing changes until you confirm. Any file it replaces is backed up first to `backups/` in your [Claude config directory](#-words-youll-meet).

A one-repo install leaves out the check that sends Claude back to run the repo's tests before it finishes, and the one that moves it into its own copy of the repo, so add `HOOKS=1` to include them.

To also get the scannable reply format and saved plans, add `PREFERENCES=1` to an "Everywhere" install, since preferences never go into a one-repo install. The [preferences table](../../src/claude/README.md#-preferences) says what each does.

## 🧪 4. Try it

Open Claude Code in your dbt repo and ask:

> Add a dbt model that counts each customer's orders.

With the instructions installed, you should see Claude:

- 🏷️ name the model with its layer prefix, such as `mart_`, and put it in that layer's folder;
- 🧱 build it from CTEs, ending in a `final` CTE;
- 📝 write a YAML file describing the model and every column, with `unique` and `not_null` tests;

The [before-and-after example](../examples/dbt/dbt_before_and_after.md) shows one such run, next to the same request without the instructions.

## 🛠️ 5. If nothing changes

- 📂 **Check the files landed:** look for `.claude/rules/` and `.claude/.playbook_install_manifest` in the repo, or the same in `~/.claude` for an "Everywhere" install.
- 🔄 **Start a new session:** Claude Code reads the instructions when a session starts.
- 📄 **Open a matching file:** dbt rules load only once Claude works on a file under `models/`, so ask about a specific model.

## ↩️ 6. Undo it

Run `make uninstall` in your own terminal, with the same `PROJECT=` if you used one. It lists the files it will remove, asks you to type `uninstall`, then removes what the install added and restores the files it backed up.

## 📖 Words you'll meet

The few words this repo uses that you might not know:

| Term | Meaning |
|---|---|
| 📁 **Claude config directory** | The folder Claude Code reads its instructions and settings from, `~/.claude` unless `$CLAUDE_CONFIG_DIR` is set |
| 📏 **Rule** | A short markdown file telling Claude how to do one thing, such as name a dbt model |
| 📂 **`always_on`, `path_scoped`, `on_demand`** | The folders that decide when a rule loads: every session, only when Claude works on matching files, or only when another rule points Claude to it |
| 🔢 **Tokens** | Claude's unit of context, capped for always-on files by the [always-on budget](../target_architecture/design_principles/01_principles.md#-numbers-and-tests) |
| 🪝 **Hook** | A small script Claude Code runs by itself at set moments, such as when Claude says it has finished |
| 📝 **Intent and Spec** | The two sections a long plan opens with, on what you want and what will be built, per [`ai_sdlc_workflow.md`](../../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) |
| 🛑 **Phase gate** | A pause after each stage of multi-stage work, such as after each PR, so you can check it before Claude goes on |
