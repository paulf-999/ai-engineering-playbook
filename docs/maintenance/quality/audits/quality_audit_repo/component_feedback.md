<!-- version: 1.0.2 -->
<!-- created: 2026-11-11 -->
<!-- updated: 2026-11-11 -->
# 💬 Component feedback

**Purpose:** how each Claude config component fared in the session transcripts at each regular review, as the [target architecture](../../../../target_architecture/target_architecture.md#-measures) asks.

This page is part of the [repo quality audit](../quality_audit_repo.md). Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

## ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`src/claude/rules/_rules_on_demand/03_workflows/saving_plans.md`](../../../../../src/claude/rules/_rules_on_demand/03_workflows/saving_plans.md) | [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read after plan approval, and 39 `_plans/active/` folders were written |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../../../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked plans with no Intent or Spec heading, and each was resubmitted |
| [`src/claude/rules/_rules_on_demand/03_workflows/sdlc_workflow.md`](../../../../../src/claude/rules/_rules_on_demand/03_workflows/sdlc_workflow.md) | [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read after each of the hook's block messages pointed to it |
| [`src/claude/rules/_rules_on_demand/03_workflows/git.md`](../../../../../src/claude/rules/_rules_on_demand/03_workflows/git.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read about 16 times before git work |
| [`src/sh/claude_validate_always_on_budget.sh`](../../../../../src/sh/claude_validate_always_on_budget.sh) | [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Runs on every commit and passes |
| [`src/claude/rules/_rules_on_demand/02_conduct/reporting.md`](../../../../../src/claude/rules/_rules_on_demand/02_conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/_rules_on_demand/claude_config/portable_paths.md`](../../../../../src/claude/rules/_rules_on_demand/claude_config/portable_paths.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/claude/rules/_path_scoped_rules/testing.md`](../../../../../src/claude/rules/_path_scoped_rules/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/_path_scoped_rules/code_security.md`](../../../../../src/claude/rules/_path_scoped_rules/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/_path_scoped_rules/style_guides/python.md`](../../../../../src/claude/rules/_path_scoped_rules/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/rules/03_workflows/claude_plans.md`](../../../../../src/claude/rules/03_workflows/claude_plans.md), phase gates | [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | The user drove multi-phase work one phase at a time, such as "i've merged 24, start phase 4" |

## ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| Other on-demand rules and style guides in [`src/claude/rules/_rules_on_demand/`](../../../../../src/claude/rules/_rules_on_demand/), and the templates in [`src/claude/_templates/`](../../../../../src/claude/_templates/) | [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Unused | No installed copy was read, and the skill and agent templates are planned |
