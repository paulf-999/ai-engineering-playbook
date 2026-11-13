# 🚧 Implementation status

**Purpose:** which parts of the [target architecture](target_architecture.md) are built, which are outstanding, and the effort each outstanding part needs.

## 📋 Executive Summary

Of the design's 18 components, 13 are built, 1 is partly built, 2 are not built, 1 is deferred and 1 is out of scope. The largest gap is skills and agents, since none has been ported yet.

## 📊 Status by component

Status is ✅ Built, 🟡 Partly, ❌ Not built, ⏸️ Deferred or 🚫 Out of scope. Effort is S (a few hours), M (about a day, in one PR) or L (several PRs). Each component links to the section that describes it:

| Component | Status | Evidence | Outstanding | Effort |
|---|---|---|---|---|
| 🔒 **[Required tier](target_architecture.md#️-tiers)** | ✅ Built | [`CLAUDE.md`](../../CLAUDE.md), [global `CLAUDE.md`](../../src/claude/CLAUDE.md), and the [plan sections](../../src/claude/hooks/hook_enforcement_plan_sections.sh) and [done checks](../../src/claude/hooks/hook_enforcement_done_checks.sh) hooks | — | — |
| 💤 **[On-demand rules](target_architecture.md#️-tiers)** | ✅ Built | [`src/claude/rules/on_demand/`](../../src/claude/rules/on_demand/) | — | — |
| 🧰 **[Skills and agents](target_architecture.md#️-tiers)** | ❌ Not built | Only the templates in [`src/claude/_templates/`](../../src/claude/_templates/) | Review each old-config file, then port, slim or drop it ([#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7), [#85](https://github.com/paulf-999/ai-engineering-playbook/issues/85)) | L |
| 📂 **[Task-specific tier](target_architecture.md#️-tiers)** | ✅ Built | [`src/claude/rules/path_scoped/`](../../src/claude/rules/path_scoped/) | — | — |
| 🔐 **[Tool access](target_architecture.md#️-tiers)** | ✅ Built | No MCP servers or allowlist shipped, and the `.env` deny rules in [`claude_install_config.sh`](../../src/sh/claude_install_config.sh) | — | — |
| 🗺️ **[Plan first](target_architecture.md#-workflow)** | ✅ Built | [`saving_plans.md`](../../src/claude/rules/on_demand/workflows/saving_plans.md) | — | — |
| 📝 **[Intent and spec](target_architecture.md#-workflow)** | ✅ Built | [`sdlc_workflow.md`](../../src/claude/rules/on_demand/workflows/sdlc_workflow.md), the plan sections hook, and the PR template's Plan Spec section | — | — |
| 🔁 **[Feedback loop](target_architecture.md#-workflow)** | ✅ Built | The [`Makefile`](../../Makefile), [`.pre-commit-config.yaml`](../../.pre-commit-config.yaml), [CI](../../.github/workflows/ci.yml) and the done checks hook | — | — |
| 👀 **[PR review loop](target_architecture.md#-workflow)** | 🟡 Partly | The [PR template](../../.github/pull_request_template.md)'s Plan Spec and criteria sections, checked by [`pr_description.yml`](../../.github/workflows/pr_description.yml) | Port the reviewer agent ([#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7)) | M |
| 🧪 **[Evals](target_architecture.md#-workflow)** | ⏸️ Deferred | — | — | — |
| 🚀 **[CI/CD metrics](target_architecture.md#-workflow)** | 🚫 Out of scope | — | — | — |
| ✍️ **[Agent commits](target_architecture.md#-workflow)** | ✅ Built | [`git.md`](../../src/claude/rules/on_demand/workflows/git.md) and the `no-commit-to-branch` hook in [`.pre-commit-config.yaml`](../../.pre-commit-config.yaml) | — | — |
| 💰 **[Always-on budget](target_architecture.md#-always-on-budget)** | ✅ Built | [`claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh) | — | — |
| 📏 **[Rule size guard](target_architecture.md#️-design-guards)** | ✅ Built | [`test_rules_structure.py`](../../tests/src/claude/test_rules_structure.py) | — | — |
| 📦 **[PR size guard](target_architecture.md#️-design-guards)** | ✅ Built | [`git_validate_num_file_changes.sh`](../../src/sh/git/git_validate_num_file_changes.sh) | — | — |
| 💬 **[Component feedback](target_architecture.md#-measures)** | ✅ Built | [`component_feedback.md`](../../maintenance/quality/audits/quality_audit_repo/component_feedback.md) | — | — |
| 💰 **[Always-on tokens](target_architecture.md#-measures)** | ✅ Built | [`context_cost.md`](../../maintenance/context_cost.md) | — | — |
| 🔪 **[Halving test](target_architecture.md#-measures)** | ❌ Not built | No review records running it | Run it at the next review and record the answer | S |
