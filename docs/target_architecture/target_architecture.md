<!-- version: 1.7.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-10 -->
# 🏗️ Target architecture

**Purpose:** what the new Claude configuration contains, what loads when, and how its cost and benefit are measured.

This page describes the design, and the [design principles' status section](design_principles.md#-status-and-terms) says which parts are built so far.

## 📋 Executive Summary

A small required core loads in every session, and every other component loads only when needed and is removed if a regular review shows it doesn't pay.

- 🌱 **Small core:** only `CLAUDE.md`, the tests and the CI checks are required.
- 📥 **On demand:** everything else loads only when a task calls for it.
- 💰 **Budget:** a CI check caps the text loaded into every session.
- 📏 **Measures:** each regular review measures outcomes and overhead from session transcripts and git history.

## 🎚️ Tiers

Every component sits in one of three tiers:

| Tier | Contains | Loads |
|---|---|---|
| 🔒 **Required** | [`CLAUDE.md`](../../CLAUDE.md), the [global `CLAUDE.md` template](../../src/claude/CLAUDE.md), `make test` and the CI checks, including the guards below | Every session, or every PR |
| 🧰 **Optional** | Skills, which are step-by-step procedures, and agents, which work in a separate context | When the engineer or Claude asks for one |
| 📂 **Task-specific** | Path-scoped rules, whose `paths:` setting names the files they apply to | When a matching file is open |

- 🧭 **Choosing a tier:** the [evaluation criteria](design_principles/02_evaluation_criteria.md#-what-shape) match each need to a mechanism, which sets its tier.
- 🛑 **Hooks and always-on rules:** porting one into the required tier raises a [red flag](design_principles/02_evaluation_criteria.md#-review-each-file), and the always-on budget still caps them.

## 💰 Always-on budget

- 📏 **Measure:** the tokens that load into every session, estimated as total characters ÷ 4, leaving out HTML comments, which Claude Code strips.
- 📂 **Counted:** the `CLAUDE.md` files and their `@` imports, rules with no `paths:` setting, and skill and agent descriptions, in both the project's `.claude/` and the global config in `src/claude/`.
- 🚫 **Not counted:** auto memory's `MEMORY.md`, which Claude Code also loads every session but keeps on each machine, outside the repo, and caps at 200 lines or 25KB.
- 🚧 **Ceiling:** set in the [principles' numbers](design_principles/01_principles.md#-numbers-and-tests), and raised only by a PR that links logged evidence.

## 🛡️ Design guards

These checks protect the design itself, alongside the repo's other [CI checks](../../.github/workflows/ci.yml):

| Guard | Fails when | How it runs |
|---|---|---|
| 💰 **Always-on budget** | The estimate exceeds the ceiling | [`claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh), as a pre-commit hook that CI also runs |
| 📖 **Per-file caps** | An on-demand rule costs more than its [read cap](design_principles/01_principles.md#-numbers-and-tests) to read, or a path-scoped rule more than its cap | [`test_rules_structure.py`](../../tests/src/claude/test_rules_structure.py), in the pytest run that CI also runs |
| 📦 **PR size** | A PR changes more files than its limit allows, except on a `release/` branch | Runs [`git_validate_num_file_changes.sh`](../../src/sh/git/git_validate_num_file_changes.sh) |

## 📏 Measures

Each [regular review](design_principles/01_principles.md#-numbers-and-tests) takes these from the session transcripts and git history since the last review, and records them in the [repo audit](../maintenance/quality/audits/quality_audit_repo.md):

| Measure | Definition | Unit |
|---|---|---|
| ⏱️ **Time to acceptance** | Working time from first prompt to accepted change | Minutes |
| 🔁 **Rework** | Later fixes for defects in the accepted change | Count of fix commits |
| ✋ **Interventions** | Times the engineer corrected Claude or redid its work | Count |
| 💬 **Component feedback** | Components that helped, hindered or went unused | One line each |
| 💰 **Always-on tokens** | The budget estimate above | Tokens |
| 🧰 **Upkeep** | Time spent changing the configuration | Hours |

- 🗑️ **Acting on feedback:** each review removes [components that don't pay](design_principles/01_principles.md) and runs the [halving test](design_principles/01_principles.md#-numbers-and-tests).
