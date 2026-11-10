<!-- version: 1.1.4 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-10 -->
# 📝 Authoring rules

**Purpose:** how to place, write, wire up and check a new rule for Claude's config.

This page is part of the authoring guidelines, `_rules_on_demand/claude_config/authoring_guidelines.md`.

## 🚪 Pick the tier

- 🔒 **Every session:** put a rule in `rules/01_standards/`, `02_conduct/` or `03_workflows/` only if every task needs it, and check the always-on budget still holds.
- 📂 **Certain files:** put a rule tied to one kind of file in `rules/_path_scoped_rules/`, with a `paths:` setting naming the files.
- 💤 **On demand:** put everything else in `rules/_rules_on_demand/`, which `make install` moves beside `rules/`, so it never loads by itself.
- 🧭 **When unsure:** choose on demand, since an always-on rule is the exception, not the default.

## 🔗 Wire it up

- 👉 **Pointers:** reach an on-demand file with a `**Read on demand:**` line naming its path, in your Claude config directory, and when to read it.
- 🆕 **New-file gap:** a path-scoped rule loads only once a matching file is open, so point to it on demand too, for the first file of its kind.
- 🧩 **Children:** name each child in its parent, and keep links to other files in those pointer lines rather than a Related section.
- 🧪 **Test the pointer:** run a lean session on a matching task, and check Claude reads the file before acting.
- 🧾 **Usage lines:** give each entry-point rule `applies_to` and `miss_cost` lines straight after its header, since its folder already sets how it loads, and its children inherit them.

## ✅ Before merging

- 🛡️ **Enforcement:** a rule backed by a hook, test or CI check gets a test in the repo's `tests/` folder.
- 🔎 **Checks:** run `make test` and `pre-commit run --all-files`, which include the rule structure test and the always-on budget check.
- 📋 **Evaluation criteria:** answer the PR template's Evaluation criteria section for each file.
- 🏅 **Review:** have one fresh-context reviewer on Sonnet score every rule the PR changes, per `docs/maintenance/quality/themes/quality_themes_rules.md`, in the playbook repo.
- 🔁 **Trial:** remove it at the next regular review if the session transcripts show it hasn't paid its way.
