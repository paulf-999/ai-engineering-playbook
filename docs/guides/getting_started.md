# 🚀 Getting started

**Purpose:** how to install the Claude Code instructions, check they work, and undo them, for someone using them rather than maintaining this repo.

## ✅ 1. Check you have what it needs

You need Claude Code, plus `git`, `bash` and `jq` on macOS or Linux. Check each prints a version:

```bash
git --version
bash --version
jq --version
```

If `jq` is missing, install it with `brew install jq` on macOS or `sudo apt install jq` on Ubuntu. You don't need Python or `make deps`, which are only for people changing this repo.

## 📥 2. Clone the repo

```bash
git clone https://github.com/paulf-999/ai-engineering-playbook.git
cd ai-engineering-playbook
```

Use a git clone, not a zip download, since the installer copies only the files git tracks.

## 🎯 3. Choose where to install

| Install | Command | Applies to | Use it when |
|---|---|---|---|
| 🏗️ **One repo** | `make install PROJECT=<path to repo>` | That repo only, through its `.claude/` folder | You want the team's rules in your team's repo, such as its dbt project |
| 🌍 **Everywhere** | `make install` | Every project you open in Claude Code | You want the same behaviour in all your work |

- 🤔 **Not sure?** Start with one repo: it changes nothing else, and `make uninstall PROJECT=<path to repo>` undoes it.
- 🤝 **For a team:** commit the repo's `.claude/` folder, so everyone gets the same rules.

## ▶️ 4. Run it

Run the command you chose. It lists every file it will add, then asks you to type `install`, so nothing changes until you confirm. Any file it replaces is backed up to `backups/` in your Claude config directory first.

To also get the scannable reply format and saved plans, add `PREFERENCES=1` to an "Everywhere" install, since preferences never go into a one-repo install. The [preferences table](../../src/claude/README.md#-preferences) says what each does.

## 🧪 5. Try it

Open Claude Code in your dbt repo and ask:

> Add a dbt model that counts each customer's orders.

With the instructions installed, you should see Claude:

- 🏷️ name the model with its layer prefix, such as `mart_`, and put it in that layer's folder;
- 🧱 build it from CTEs, ending in a `final` CTE;
- 📝 write a YAML file describing the model and every column, with `unique` and `not_null` tests;
- ⚠️ point out anything the project is missing, such as an undeclared source.

The [before-and-after example](../examples/dbt_before_and_after.md) shows one such run, next to the same request without the instructions.

## 🛠️ 6. If nothing changes

- 📂 **Check the files landed:** look for `.claude/rules/` in the repo, or `rules/` in `~/.claude` for an "Everywhere" install.
- 🔄 **Start a new session:** Claude Code reads the instructions when a session starts.
- 📄 **Open a matching file:** dbt rules load only once Claude works on a file under `models/`, so ask about a specific model.

## ↩️ 7. Undo it

Run `make uninstall`, with the same `PROJECT=` if you used one. It removes what the install added and restores the files it backed up.

## 📖 Words you'll meet

The [terms](../../src/claude/README.md#-terms) explain the few words this repo uses that you might not know, such as hook, phase gate and always-on.
