<!-- version: 1.0.1 -->
<!-- created: 2026-11-11 -->
<!-- updated: 2026-11-12 -->
# 🚧 Implementation status

**Purpose:** which parts of the [target architecture](target_architecture.md) are built, which are outstanding, and the effort each outstanding part needs.

## 📋 Executive Summary

Of the design's 18 components, 13 are built, 3 are outstanding, 1 is deferred and 1 is out of scope. The largest gap is the optional tier's skills and agents, since none has been ported yet.

## 📊 Status by component

Status is ✅ Built, 🟡 Partly, ❌ Not built, ⏸️ Deferred or 🚫 Out of scope. Effort is S (under a PR, hours), M (one PR, a day) or L (several PRs):

| Component | Section | Status | Evidence | Outstanding | Effort |
|---|---|---|---|---|---|
| 🔒 **Required tier** | [Tiers](target_architecture.md#️-tiers) | ✅ Built | [`CLAUDE.md`](../../CLAUDE.md), [global `CLAUDE.md`](../../src/claude/CLAUDE.md), and the [plan sections](../../src/claude/hooks/hook_enforcement_plan_sections.sh) and [done checks](../../src/claude/hooks/hook_enforcement_done_checks.sh) hooks, which `make install` registers | — | — |
| 💤 **On-demand rules** | [Tiers](target_architecture.md#️-tiers) | ✅ Built | [`src/claude/rules/_rules_on_demand/`](../../src/claude/rules/_rules_on_demand/) | — | — |
| 🧰 **Skills and agents** | [Tiers](target_architecture.md#️-tiers) | ❌ Not built | Only the templates in [`src/claude/_templates/`](../../src/claude/_templates/) | Port or write each one, after its bloat review | L |
| 📂 **Task-specific tier** | [Tiers](target_architecture.md#️-tiers) | ✅ Built | [`src/claude/rules/_path_scoped_rules/`](../../src/claude/rules/_path_scoped_rules/) | — | — |
| 🔐 **Tool access** | [Tiers](target_architecture.md#️-tiers) | ✅ Built | No MCP servers or permission allowlist in `src/claude/`, and [`permission_recommendations.md`](../../src/claude/rules/_rules_on_demand/claude_config/permission_recommendations.md) | — | — |
| 🗺️ **Plan first** | [Workflow](target_architecture.md#-workflow) | ✅ Built | [`saving_plans.md`](../../src/claude/rules/_rules_on_demand/03_workflows/saving_plans.md) | — | — |
| 📝 **Intent and spec** | [Workflow](target_architecture.md#-workflow) | ✅ Built | [`sdlc_workflow.md`](../../src/claude/rules/_rules_on_demand/03_workflows/sdlc_workflow.md), enforced by the plan-sections hook | — | — |
| 🔁 **Feedback loop** | [Workflow](target_architecture.md#-workflow) | ✅ Built | The [`Makefile`](../../Makefile), [`.pre-commit-config.yaml`](../../.pre-commit-config.yaml), [CI](../../.github/workflows/ci.yml) and the done checks hook | — | — |
| 👀 **PR review loop** | [Workflow](target_architecture.md#-workflow) | ❌ Not built | No reviewer agent in `src/claude/` | Port a fresh-context reviewer agent that fills a PR's evaluation criteria | M |
| 🧪 **Evals** | [Workflow](target_architecture.md#-workflow) | ⏸️ Deferred | Deferred until their API cost and upkeep are weighed | — | — |
| 🚀 **CI/CD metrics** | [Workflow](target_architecture.md#-workflow) | 🚫 Out of scope | The repo has no deployed service | — | — |
| ✍️ **Agent commits** | [Workflow](target_architecture.md#-workflow) | ✅ Built | [`git.md`](../../src/claude/rules/_rules_on_demand/03_workflows/git.md), and the `no-commit-to-branch` hook in `.pre-commit-config.yaml` | — | — |
| 💰 **Always-on budget** | [Always-on budget](target_architecture.md#-always-on-budget) | ✅ Built | [`claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh), as a pre-commit hook that CI runs | — | — |
| 📏 **Rule size guard** | [Design guards](target_architecture.md#️-design-guards) | ✅ Built | [`test_rules_structure.py`](../../tests/src/claude/test_rules_structure.py), capping rules at 110 lines | — | — |
| 📦 **PR size guard** | [Design guards](target_architecture.md#️-design-guards) | ✅ Built | [`git_validate_num_file_changes.sh`](../../src/sh/git/git_validate_num_file_changes.sh), run by CI | — | — |
| 💬 **Component feedback** | [Measures](target_architecture.md#-measures) | ✅ Built | [`component_feedback.md`](../maintenance/quality/audits/quality_audit_repo/component_feedback.md) | — | — |
| 💰 **Always-on tokens** | [Measures](target_architecture.md#-measures) | ✅ Built | [`context_cost.md`](../maintenance/context_cost.md), which a pre-commit check keeps current | — | — |
| 🔪 **Halving test** | [Measures](target_architecture.md#-measures) | 🟡 Partly | Defined in the [principles](design_principles/01_principles.md#-numbers-and-tests), but no review records running it | Run it at the next review and record the answer | S |

## 📝 Outstanding work

Sorted by effort, smallest first:

1. **Halving test (S):** run it at the next regular review and record the answer with the component feedback.
2. **PR review loop (M):** port a reviewer agent, tracked by [#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7).
3. **Skills and agents (L):** review each old-config file, then port, slim or drop it, tracked by [#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7) and [#85](https://github.com/paulf-999/ai-engineering-playbook/issues/85).
