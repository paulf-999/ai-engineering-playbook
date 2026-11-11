<!-- version: 1.0.0 -->
<!-- created: 2026-11-11 -->
<!-- updated: 2026-11-11 -->
# 💬 Component feedback

**Purpose:** how each Claude config component fared in the session transcripts at each regular review, as the [target architecture](../../../../target_architecture/target_architecture.md#-measures) asks.

This page is part of the [repo quality audit](../quality_audit_repo.md). Each review adds its Helped rows at the top and keeps the earlier ones, but replaces the Unused and Hindered rows, since those are what it acts on.

## ✅ Helped

| Date | Run | Component | Evidence |
|---|---|---|---|
| 2026-11-11 | #168 | `hooks/hook_enforcement_plan_sections.sh` | Blocked plans with no Intent or Spec heading, and each was resubmitted |
| 2026-11-11 | #168 | `_rules_on_demand/03_workflows/sdlc_workflow.md` | Read after each of the hook's block messages pointed to it |
| 2026-11-11 | #168 | `_rules_on_demand/03_workflows/saving_plans.md` | Read after plan approval, and 39 `_plans/active/` folders were written |
| 2026-11-11 | #168 | `src/sh/claude_validate_always_on_budget.sh` | Runs on every commit and passes |
| 2026-11-11 | #161 | `hooks/hook_enforcement_plan_sections.sh` | Blocked 16 plans that lacked Intent or Spec, each sent to `sdlc_workflow.md`, at one resubmit each |
| 2026-11-11 | #161 | `_rules_on_demand/03_workflows/sdlc_workflow.md` and `saving_plans.md` | Read about 6 and 12 times, through the hook and after plan approval |
| 2026-11-11 | #161 | `_rules_on_demand/03_workflows/git.md`, `reporting.md` and `portable_paths.md` | Read about 16, 6 and 5 times |
| 2026-11-11 | #161 | `_path_scoped_rules/testing.md`, `code_security.md` and `python.md` | Loaded in 13 or 14 sessions each, where matching files were open |
| 2026-11-11 | #149 | `hooks/hook_enforcement_plan_sections.sh` | Blocked a plan with no Intent or Spec in 3 sessions and sent Claude to `sdlc_workflow.md`, which was then read |
| 2026-11-11 | #149 | `_rules_on_demand/03_workflows/saving_plans.md` | The most-read on-demand rule, and approved plans landed in `_plans/active/` |
| 2026-11-11 | #149 | `_rules_on_demand/03_workflows/git.md` | Read 6 times |
| 2026-11-10 | #143 | `03_workflows/claude_plans.md`, phase gates | The user drove multi-phase work one phase at a time, such as "i've merged 24, start phase 4" |
| 2026-11-10 | #143 | `_rules_on_demand/03_workflows/saving_plans.md` | Read from the installed path twice, and approved plans landed in `_plans/` |

## ⚠️ Unused or hindered, latest run

| Date | Run | Component | Effect | Evidence |
|---|---|---|---|---|
| 2026-11-11 | #168 | Other on-demand rules, style guides and templates | Unused | No installed copy was read, and the skill and agent templates are planned |
