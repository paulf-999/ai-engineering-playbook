# 💬 Component feedback

**Purpose:** how each Claude config component fared in the session transcripts at each regular review, as the [target architecture](../../../../docs/target_architecture/README.md#-measures) asks.

This page is part of the [repo quality audit](../quality_audit_repo.md). Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

## ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked plans with no Intent or Spec heading in 4 sessions, and Claude fixed and resubmitted each |
| [`src/claude/rules/always/workflows/claude_plans.md`](../../../../src/claude/rules/always/workflows/claude_plans.md), phase gates | [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | The user drove multi-phase work one phase at a time, such as "i've merged 24, start phase 4" |
| [`src/claude/rules/path_scoped/code_security.md`](../../../../src/claude/rules/path_scoped/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/rules/path_scoped/testing.md`](../../../../src/claude/rules/path_scoped/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/on_demand/conduct/reporting.md`](../../../../src/claude/rules/on_demand/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/workflows/git.md`](../../../../src/claude/rules/on_demand/workflows/git.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read about 16 times before git work |
| [`src/claude/rules/on_demand/workflows/saving_plans.md`](../../../../src/claude/rules/on_demand/workflows/saving_plans.md) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read after a plan was approved |
| [`src/claude/rules/on_demand/workflows/sdlc_workflow.md`](../../../../src/claude/rules/on_demand/workflows/sdlc_workflow.md) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read twice, each time after the hook's block message pointed to it |
| [`src/claude/rules/on_demand/claude_config/portable_paths.md`](../../../../src/claude/rules/on_demand/claude_config/portable_paths.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/sh/claude_validate_always_on_budget.sh`](../../../../src/sh/claude_validate_always_on_budget.sh) | [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Runs on every commit and passes |
| [`src/sh/git/git_validate_branch_name.sh`](../../../../src/sh/git/git_validate_branch_name.sh) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Caught 6 bad branch names before push |

## ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`.github/workflows/pr_description.yml`](../../../../.github/workflows/pr_description.yml), score-row warning | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Mixed | 34 warnings in 4 sessions, which prompt the audit-only re-score PRs |
| Other stacks' style guides in [`src/claude/rules/path_scoped/style_guides/`](../../../../src/claude/rules/path_scoped/style_guides/), and the planned templates in [`src/claude/_templates/`](../../../../src/claude/_templates/) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Unused | No sign they loaded in this repo's sessions, which have none of those files, and the skill and agent templates are planned |
| [`src/sh/bump_file_headers.sh`](../../../../src/sh/bump_file_headers.sh) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Hindered | Its "review, re-stage and commit again" stop adds a second commit attempt to nearly every commit, 51 times, though headers are kept by choice |
