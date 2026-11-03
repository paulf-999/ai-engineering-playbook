<!-- version: 1.1.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# 🏗️ Target architecture

For anyone building or reviewing this repo's Claude configuration: what it contains, what loads when, and how its cost and benefit are measured.

- 🚧 **Target, not current:** this page describes the design, and [Status and terms](design_principles.md#-status-and-terms) says which parts are built and defines terms such as CI.

## 📋 Executive Summary

- 🌱 **Mandatory:** the `CLAUDE.md` files, `make test`, CI and the guards, plus hooks and always-on rules only on evidence.
- 📥 **On demand:** everything else loads only when a task calls for it.
- 💰 **Budget:** every session's fixed context stays under 3,000 tokens.
- 📏 **Measures:** tasks log outcomes, and milestones log overhead.

## 🎚️ Tiers

| Tier | Contains | Loads |
|---|---|---|
| 🔒 **Mandatory** | • **Context:** [`CLAUDE.md`](../../CLAUDE.md) and the [global template](../../src/templates/global_claude.md).<br>• **Checks:** `make test`, CI and the guards.<br>• **On evidence only:** hooks and rules without `paths:`. | Every session, or every PR |
| 🧰 **Optional** | • **Skills:** procedures, such as raising a PR.<br>• **Agents:** helpers with a separate context, such as a reviewer. | When the engineer or Claude invokes one |
| 📂 **Task-specific** | • **Path-scoped rules:** guidance with `paths:` frontmatter for certain files. | When a matching file is open |

- 🧭 **Which tier:** the [evaluation criteria](design_principles/02_evaluation_criteria.md#-what-shape) match each need to a mechanism, which sets its tier.

## 💰 Always-on budget

- 📏 **Measure:** total characters ÷ 4 of what loads into every session.
- 📂 **Counted:** the `CLAUDE.md` files and their `@` imports, rules without `paths:`, and skill and agent descriptions.
- 🚧 **Ceiling:** [3,000 tokens](design_principles/01_principles.md#-why-these-numbers), raised only by a PR that links logged evidence.

## 🛡️ Guards

| Guard | Fails when | Enforced by |
|---|---|---|
| 💰 **Always-on budget** | The estimate exceeds 3,000 tokens | A CI check |
| 📦 **PR size** | Over 20 files change, except on a `release/` branch | [`git_validate_num_file_changes.sh`](../../src/sh/git/git_validate_num_file_changes.sh), run by CI |

## 📏 Measures

- 📝 **Task log:** a markdown table in this repo, with one row per task.
- 🗓️ **Milestone:** every 20 tasks or 4 weeks, whichever comes first.

| Measure | Definition | Unit | Recorded |
|---|---|---|---|
| ⏱️ **Time to acceptance** | Working time from first prompt to accepted change | Minutes | Per task |
| 🔁 **Rework** | Later fixes for defects in the accepted change | Count of fix commits | On the original task's row |
| ✋ **Interventions** | Times the engineer corrected Claude or redid its work | Count | Per task |
| 💬 **Component feedback** | Components that helped, hindered or went unused | One line each | Per task |
| 💰 **Always-on tokens** | The budget estimate above | Tokens | Per milestone |
| 🧰 **Upkeep** | Time spent changing the configuration | Hours | Per milestone |

- 🗑️ **Acting on feedback:** each milestone [retires components that don't pay](design_principles/01_principles.md) and runs the [halving test](design_principles/01_principles.md#-why-these-numbers): could half the components go without harm?
