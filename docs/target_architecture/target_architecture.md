<!-- version: 1.5.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# 🏗️ Target architecture

**Purpose:** what the new Claude configuration contains, what loads when, and how its cost and benefit are measured.

This page describes the design, and the [design principles' status section](design_principles.md#-status-and-terms) says which parts are built so far.

## 📋 Executive Summary

- 🌱 **Small core:** only `CLAUDE.md`, the tests and the CI checks are required.
- 📥 **On demand:** everything else loads only when a task calls for it.
- 💰 **Budget:** a CI check caps the text loaded into every session.
- 📏 **Measures:** each task logs its outcome, and regular reviews log overhead.

## 🎚️ Tiers

Every component sits in one of three tiers:

| Tier | Contains | Loads |
|---|---|---|
| 🔒 **Required** | [`CLAUDE.md`](../../CLAUDE.md), the [global `CLAUDE.md` template](../../src/templates/global_claude.md), `make test` and the CI checks, including the guards below | Every session, or every PR |
| 🧰 **Optional** | Skills, which are step-by-step procedures, and agents, which work in a separate context | When the engineer or Claude asks for one |
| 📂 **Task-specific** | Path-scoped rules, whose `paths:` setting names the files they apply to | When a matching file is open |

- 🧭 **Choosing a tier:** the [evaluation criteria](design_principles/02_evaluation_criteria.md#-what-shape) match each need to a mechanism, which sets its tier.
- 🛑 **Hooks and always-on rules:** they join the required tier only with evidence that they're needed.

## 💰 Always-on budget

- 📏 **Measure:** the tokens that load into every session, estimated as total characters ÷ 4.
- 📂 **Counted:** the `CLAUDE.md` files and their `@` imports, rules with no `paths:` setting, and skill and agent descriptions.
- 🚫 **Not counted:** auto memory's `MEMORY.md`, which Claude Code also loads every session but keeps on each machine, outside the repo, and caps at 200 lines or 25KB.
- 🚧 **Ceiling:** set in the [principles' numbers](design_principles/01_principles.md#-numbers-and-tests), and raised only by a PR that links logged evidence.

## 🛡️ Design guards

These checks protect the design itself, alongside the repo's other [CI checks](../../.github/workflows/ci.yml):

| Guard | Fails when | How it runs |
|---|---|---|
| 💰 **Always-on budget** | The estimate exceeds the ceiling | [`claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh), as a pre-commit hook that CI also runs |
| 📦 **PR size** | A PR changes more files than its limit allows, except on a `release/` branch | Runs [`git_validate_num_file_changes.sh`](../../src/sh/git/git_validate_num_file_changes.sh) |

## 📏 Measures

Each task gets a row in the [task log](../maintenance/task_log.md), and the [regular review](design_principles/01_principles.md#-numbers-and-tests) adds overhead figures:

| Measure | Definition | Unit | Recorded |
|---|---|---|---|
| ⏱️ **Time to acceptance** | Working time from first prompt to accepted change | Minutes | Per task |
| 🔁 **Rework** | Later fixes for defects in the accepted change | Count of fix commits | On the original task's row |
| ✋ **Interventions** | Times the engineer corrected Claude or redid its work | Count | Per task |
| 💬 **Component feedback** | Components that helped, hindered or went unused | One line each | Per task |
| 💰 **Always-on tokens** | The budget estimate above | Tokens | Per review |
| 🧰 **Upkeep** | Time spent changing the configuration | Hours | Per review |

- 🗑️ **Acting on feedback:** each review removes [components that don't pay](design_principles/01_principles.md) and runs the [halving test](design_principles/01_principles.md#-numbers-and-tests).
