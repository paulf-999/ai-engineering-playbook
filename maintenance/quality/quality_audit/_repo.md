# 🏗️ Repo

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest bloat and over-engineering scores, findings and component feedback, as part of the [quality audit](../quality_audit.md).

Each run follows the [repo rubric](../quality_rubrics/_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-11 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **9/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-11 | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | **8/10** |

## 🔍 Why the latest scores

The blind run of `main` at #170, with each theme below ✅ and what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 3 duplicates: the grade scale in the Rules and Tests rubrics, turning Intent and Spec into `intent.md` and `spec.md` in `sdlc_workflow.md`, `saving_plans.md` and `target_architecture.md`, and running `make test` before a PR in `CLAUDE.md`, `tests/README.md` and `CONTRIBUTING.md` | Findings 3 and 5 |
| 🔁 **Upkeep cost** | 16 of the last 50 commits, or 32%, of which 11 edit the repo rubric between reviews | Finding 1 |
| 🪜 **Simplest mechanism** | 2 issues: about 7 tests in `test_rules_structure.py` that test the checks themselves, and a `# MoSCoW:` label on each of the 96 test functions per `test_maintenance.md` | Findings 2 and 4 |

The one contradiction left, `target_architecture.md` still naming a per-prompt hook red flag that `02_evaluation_criteria.md` no longer lists, is within ✅. Always-on headroom is ✅ at about 2,248 of 3,000 tokens, only 2 tokens under the 75% line.

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🧊 **Freeze the rubric:** save edits to `quality_rubrics.md` for the regular review, which would take Upkeep to about 5 of 50.
2. 🧪 **Tests of the checks:** drop the 7 or so tests in `test_rules_structure.py` that only show each check can fail, and rely on the checks running against the real rules.
3. 📝 **One home for Intent and Spec:** fold `saving_plans.md` into `sdlc_workflow.md`, or have one point to the other, and have `target_architecture.md` link rather than restate.
4. 🏷️ **Fewer MoSCoW labels:** keep `# MoSCoW:` labels only where the tests audit's Core coverage needs them.
5. 🎯 **Small fixes:** keep the grade scale in one rubric, align the per-prompt hook line in `target_architecture.md` with `02_evaluation_criteria.md`, and optionally drop the Evals and CI/CD rows from the Workflow table.

## 💬 Component feedback

Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

### ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked plans with no Intent or Spec heading in 4 sessions, and Claude fixed and resubmitted each |
| [`src/claude/rules/always/workflows/sdlc_workflow.md`](../../../src/claude/rules/always/workflows/sdlc_workflow.md), phase gates | [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | The user drove multi-phase work one phase at a time, such as "i've merged 24, start phase 4" |
| [`src/claude/rules/path_scoped/code_security.md`](../../../src/claude/rules/path_scoped/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/rules/path_scoped/testing.md`](../../../src/claude/rules/path_scoped/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/on_demand/conduct/reporting.md`](../../../src/claude/rules/on_demand/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/workflows/git.md`](../../../src/claude/rules/on_demand/workflows/git.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read about 16 times before git work |
| [`src/claude/rules/on_demand/workflows/saving_plans.md`](../../../src/claude/rules/on_demand/workflows/saving_plans.md) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read after a plan was approved |
| [`src/claude/rules/always/workflows/sdlc_workflow.md`](../../../src/claude/rules/always/workflows/sdlc_workflow.md) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read twice, each time after the hook's block message pointed to it |
| [Portable paths](../../../docs/guides/authoring_guide.md#-portable-paths), then `portable_paths.md` | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/sh/claude_validate_always_on_budget.sh`](../../../src/sh/claude_validate_always_on_budget.sh) | [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Runs on every commit and passes |
| [`src/sh/git/git_validate_branch_name.sh`](../../../src/sh/git/git_validate_branch_name.sh) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Caught 6 bad branch names before push |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`.github/workflows/pr_description.yml`](../../../.github/workflows/pr_description.yml), score-row warning | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Mixed | 34 warnings in 4 sessions, which prompt the audit-only re-score PRs |
| Other stacks' style guides in [`src/claude/rules/path_scoped/style_guides/`](../../../src/claude/rules/path_scoped/style_guides/), and the planned templates in [`src/claude/_templates/`](../../../src/claude/_templates/) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Unused | No sign they loaded in this repo's sessions, which have none of those files, and the skill and agent templates are planned |
