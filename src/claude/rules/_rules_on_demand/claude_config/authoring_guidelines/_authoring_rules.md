<!-- version: 1.1.11 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-13 -->
# 📝 Authoring rules

**Purpose:** how to place, write, wire up and check a new rule for Claude's config.

This page is part of the authoring guidelines, `_rules_on_demand/claude_config/authoring_guidelines.md`.

## 🚪 Pick the tier

- 🔒 **Every session:** only for a rule every task needs, and only while the always-on budget still holds.
- 📂 **Certain files:** for a rule tied to one kind of file, with a `paths:` setting naming the files.
- 💤 **On demand:** for everything else, and whenever you're unsure, since an always-on rule is the exception.

## 🔗 Wire it up

- 👉 **Pointers:** reach an on-demand file with a bullet in a `## 📚 Read on demand` section at the end of the file, naming its path, in your Claude config directory, and when to read it, or name it in a hook's block message.
- 🆕 **New-file gap:** a path-scoped rule loads only once a matching file is open, so point to it on demand too, for the first file of its kind.
- 🧩 **Children:** name each child in its parent, and keep links to other files in those pointer lines rather than a Related section.
- 🧪 **Test the pointer:** run a lean session on a matching task, and check Claude reads the file before acting.
- 🧾 **Usage lines:** give each entry-point rule `applies_to` and `miss_cost` lines straight after its header, since its folder already sets how it loads, and its children inherit them.

## ✅ Before merging

- 🛡️ **Enforcement:** a rule backed by a hook, test or CI check gets a test in the repo's `tests/` folder.
- 🔎 **Checks:** run `make test` and `pre-commit run --all-files`, which include the rule structure test and the always-on budget check.
- 📋 **Evaluation criteria:** for an always-on rule, have a fresh-context reviewer fill the PR template's Evaluation criteria section, as the playbook repo's `.github/CONTRIBUTING.md` says.
- 🔁 **Trial:** remove it at the next regular review if the session transcripts show it hasn't paid its way.

## 📚 Read on demand

- `README.md`, in your Claude config directory, for the folder each tier lives in.
