# 🚀 Getting started

**Purpose:** how to install the Claude Code instructions, check they work, and undo them, for someone using them rather than maintaining this repo.

## ✅ 1. Check you have what it needs

You need Claude Code, plus `git`, `bash`, `make` and `jq` on macOS or Linux. Check each prints a version:

```bash
claude --version
git --version
bash --version
make --version
jq --version
```

If one is missing, install it with `brew install <name>` on macOS or `sudo apt install <name>` on Ubuntu, such as `brew install jq`. You don't need Python or `make deps`, which are only for people changing this repo.

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
- 🤝 **For a team:** commit the repo's `.claude/` folder, so everyone gets the same rules. Check `git status` first, since the install also writes its own `settings.json` and record files there.

## ▶️ 4. Run it

Run the command you chose in your own terminal, not by asking Claude to run it, since the installer refuses to run from inside Claude Code. It lists every file it will add, then asks you to type `install`, so nothing changes until you confirm. Any file it replaces is backed up to `backups/` in your Claude config directory first.

A one-repo install leaves out the check that sends Claude back to run the repo's tests before it finishes, so add `HOOKS=1` to include it.

To also get the scannable reply format and saved plans, add `PREFERENCES=1` to an "Everywhere" install, since preferences never go into a one-repo install. The [preferences table](../../src/claude/README.md#-preferences) says what each does.

## 🔧 What installing changes

Besides adding instructions, installing changes how Claude works in every project:

- 💬 **Replies:** Claude uses British spelling and offers options before big changes. Its scannable reply format is [opt-in](../../src/claude/README.md#-preferences): `make install PREFERENCES=1`.
- 🗺️ **Plans:** a long plan must say what you want and how to check it's done, and work of 3 or more stages pauses after each one for your go-ahead.
- 🪝 **Automatic checks:** one blocks long plans that skip those sections, and one sends Claude back to run the repo's checks before it finishes, which a one-repo install leaves out unless you add `HOOKS=1`.
- 🔒 **Files:** Claude's file tools can't read `.env` files. Saving plans and notes outside your repos is opt-in too.

## 🧪 5. Try it

Open Claude Code in your dbt repo and ask:

> Add a dbt model that counts each customer's orders.

With the instructions installed, you should see Claude:

- 🏷️ name the model with its layer prefix, such as `mart_`, and put it in that layer's folder;
- 🧱 build it from CTEs, ending in a `final` CTE;
- 📝 write a YAML file describing the model and every column, with `unique` and `not_null` tests;

The [before-and-after example](../examples/dbt_before_and_after.md) shows one such run, next to the same request without the instructions.

## 🛠️ 6. If nothing changes

- 📂 **Check the files landed:** look for `.claude/rules/` and `.claude/.playbook_install_manifest` in the repo, or the same in `~/.claude` for an "Everywhere" install.
- 🔄 **Start a new session:** Claude Code reads the instructions when a session starts.
- 📄 **Open a matching file:** dbt rules load only once Claude works on a file under `models/`, so ask about a specific model.

## ↩️ 7. Undo it

Run `make uninstall` in your own terminal, with the same `PROJECT=` if you used one. It lists the files it will remove, asks you to type `uninstall`, then removes what the install added and restores the files it backed up.

## 📖 Words you'll meet

The [terms](../../src/claude/README.md#-terms) explain the few words this repo uses that you might not know, such as hook, phase gate and always-on.
