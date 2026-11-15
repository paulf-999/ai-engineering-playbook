# 📊 Quality audit

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest bloat and over-engineering scores for the repo as a whole, its findings and component feedback, from each regular review.

Each run follows the [repo rubric](quality_rubrics/_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history. Tests and rules are checked against their checklists instead, with findings going to GitHub issues.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-15 | ✅ 2 | ✅ 2 | ❌ 0 | 🟡 1 | 🟡 1 | **6/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-15 | ❌ 0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **7/10** |

## 🔍 Why the latest scores

The blind run of `main` at #244, with each theme below ✅ and what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 6 or more duplicates, such as the 110-line rule cap in 5 places, the 3,000-token budget in 3 and the fresh-context reviewer process in 5 | Finding 1 |
| 📦 **Always-on headroom** | About 2,397 of 3,000 tokens, or 79.9%, just over the 75% line | Move always-on detail to on-demand files |
| 🚧 **Placeholders** | 1, "not built yet" in [`docs/target_architecture/README.md`](../../docs/target_architecture/README.md) | Link the build progress issue without the phrase |
| 🔗 **Cross-file consistency** | 8 or more contradictions, such as Ruff 0.17.4 in `requirements.txt` but v0.17.3 in `.pre-commit-config.yaml` | Finding 4 |
| 🪜 **Simplest mechanism** | 3 issues: MoSCoW scoring of every test, the plan-sections hook blocking trivial plans, and a PR title check that repeated commitlint, which #251 replaced | Findings 2 and 3 |

Upkeep cost is ✅ at 10 of the last 50 commits, or exactly 20%, and Process weight is ✅ at 8 `maintenance/` files against 92 product files.

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🎯 **One home per limit:** #254 gave the 110-line cap and the reviewer process one home each, and folded the agents guide's "Before merging" into the skills guide's. The 3,000-token budget stays in the budget script and `01_principles.md`, plus the frozen repo rubric.
2. 🏷️ **Fewer MoSCoW labels:** keep `# MoSCoW:` tags only where the tests checklist's Core coverage needs them, since the transcripts show `maintenance/test_maintenance.md` almost unused.
3. 🪶 **Let small plans pass:** #254 lets plans of fewer than 15 non-blank lines through `hook_enforcement_plan_sections.sh` without Intent and Spec.
4. 🔗 **Fix the contradictions:** #253 fixed the Ruff version, the hooks in `_tiers.md`, the budget script's pointer, `maturity` in `agent_skills_spec.md` and the `AGENT.md.template` checklist, and #245 the install note. Still open are the H1 and `~` paths in `SKILL.md.template`, `~` paths in `_drafts_and_errors.md`, Python 3.10 and flake8 in `python_environment.md`, and the skills and agents exclusion in `git_validate_pr_description.sh`.

## 💬 Component feedback

Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

### ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Claude debugged a PR description failure from the CI log |
| [Portable paths](../../docs/guides/authoring_guide.md#-portable-paths) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked 9 plans with no Intent or Spec heading, and Claude fixed and resubmitted each |
| [`src/claude/rules/always/conduct/writing_style.md`](../../src/claude/rules/always/conduct/writing_style.md) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | The user cites it as the yardstick for docs |
| [`src/claude/rules/always/workflows/sdlc_workflow.md`](../../src/claude/rules/always/workflows/sdlc_workflow.md) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Its phase gates paced multi-phase work, and Claude followed it after each plan-hook block |
| [`src/claude/rules/on_demand/conduct/reporting.md`](../../src/claude/rules/on_demand/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/workflows/git.md`](../../src/claude/rules/on_demand/workflows/git.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read about 16 times before git work |
| [`src/claude/rules/on_demand/workflows/saving_plans.md`](../../src/claude/rules/on_demand/workflows/saving_plans.md) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read after a plan was approved |
| [`src/claude/rules/path_scoped/code_security.md`](../../src/claude/rules/path_scoped/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/rules/path_scoped/testing.md`](../../src/claude/rules/path_scoped/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/sh/claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Caught always-on context at about 3,887 tokens, over the budget |
| [`src/sh/git/git_validate_branch_name.sh`](../../src/sh/git/git_validate_branch_name.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Forced 2 branch renames before push |
| [`src/sh/git/git_validate_pr_description.sh`](../../src/sh/git/git_validate_pr_description.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught too many bullets and leftover template placeholders |
| [`tests/`](../../tests/) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught structure problems in the rules and helpers |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`.github/workflows/pip_audit.yml`](../../.github/workflows/pip_audit.yml) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Unused | No sign in the transcripts |
| [`maintenance/old_setup_review.md`](../old_setup_review.md) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Unused | Never opened |
| [`maintenance/quality/quality_rubrics/`](quality_rubrics/) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Hindered | Re-scores dominated user turns; [#189](https://github.com/paulf-999/ai-engineering-playbook/pull/189) batched them, for the next run to confirm |
| [`maintenance/test_maintenance.md`](../test_maintenance.md) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Unused | Read twice, both by one subagent |
| [`src/claude/hooks/hook_enforcement_done_checks.sh`](../../src/claude/hooks/hook_enforcement_done_checks.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Unused | Never fired in any transcript |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Hindered | Blocks trivial plans too, called "heavy for quick SQL work"; [#254](https://github.com/paulf-999/ai-engineering-playbook/pull/254) lets small plans pass, for the next run to confirm |
| [`src/claude/rules/always/conduct/behaviour.md`](../../src/claude/rules/always/conduct/behaviour.md) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Hindered | The user flagged it as overlapping the phase gates; it now covers only the start of work, for the next run to confirm |
| [`src/claude/rules/always/conduct/security.md`](../../src/claude/rules/always/conduct/security.md) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Unused | No sign it was applied |
| [`src/claude/rules/always/standards/claude_response_standards.md`](../../src/claude/rules/always/standards/claude_response_standards.md) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Mixed | Injected 1,671 times, yet the user still called replies "too verbose" |
| [`src/claude/rules/always/standards/naming_standards.md`](../../src/claude/rules/always/standards/naming_standards.md) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Unused | Discussed, but never shown applied |
| [`src/claude/rules/path_scoped/`](../../src/claude/rules/path_scoped/) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Unused | Loaded often, with no sign they changed behaviour |
| [`src/sh/claude_report_context_cost.sh`](../../src/sh/claude_report_context_cost.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Hindered | Its "out of date" check failed 13 times, including in CI; [#256](https://github.com/paulf-999/ai-engineering-playbook/pull/256) makes the hook rewrite and stage it, for the next run to confirm |
| [`src/sh/git/git_validate_branch_name.sh`](../../src/sh/git/git_validate_branch_name.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Hindered | Fired on `main` or a detached HEAD, so Claude skipped it with `SKIP=`; it now passes there, for the next run to confirm |
| [`src/sh/git/git_validate_num_file_changes.sh`](../../src/sh/git/git_validate_num_file_changes.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Unused | Never fired |
