<!-- version: 1.1.1 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-13 -->
# 🛠️ Authoring skills

**Purpose:** how to lay out, describe and test a new skill for Claude's config.

This page is part of the authoring guidelines, `on_demand/claude_config/authoring_guidelines.md`.

## 📁 Folder layout

- 📄 **SKILL.md:** about 60 lines from `_templates/skills/SKILL.md.template`, leaving longer detail to `reference/`.
- 📜 **Contract:** a `skill.contract.yaml` from its template, written before `SKILL.md`, since it sets the scope.
- 📚 **reference/:** the files Claude reads while running the skill, starting with `_implementation.md`.
- 🧪 **tests/:** `evals.yaml` with the test scenarios, plus a plain-language `README.md` saying what it is.
- 🚫 **Nothing else:** add no other folders, apart from one script at the skill's root if it runs code.

## 🎯 Scope and triggers

- 🏷️ **Name:** `<domain>-<action>`, a domain then an imperative verb, such as `git-create-pr`, matching the folder name, per the [Agent Skills spec](https://agentskills.io/specification).
- 🚧 **Not for:** list in the contract's `not_for` what the skill doesn't do, since that boundary matters most.
- 🗣️ **Description:** use the phrases people type to ask for it, with the other verbs and names they'd use, and keep it short, since every description loads in every session.
- ✋ **Confirm first:** set `confirmation_required: true` for anything irreversible or visible to others, such as a push.

## ✅ Before merging

- 🧪 **Evals:** add evals that cover its main triggers and one case where it shouldn't fire.
- 🔐 **Safety:** read secrets from the environment, validate input before it reaches a shell or API, and hard-code no paths.
- 📋 **Evaluation criteria:** answer the PR template's Evaluation criteria section.
- 🏅 **Review:** have a fresh-context reviewer score it against a rubric for its type, modelled on `docs/maintenance/quality/themes/quality_themes_rules.md`, in the playbook repo.
