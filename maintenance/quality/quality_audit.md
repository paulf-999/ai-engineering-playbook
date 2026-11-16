# 📊 Quality audit

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest bloat and over-engineering scores for the repo as a whole, its findings and component feedback, from each regular review, plus the latest persona review.

Each run follows the [repo rubric](quality_rubrics/_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history. Tests and rules are checked against their checklists instead, with findings going to GitHub issues.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-16 | ✅ 2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | **8/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-16 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | **8/10** |

## 🔍 Why the latest scores

The blind run of `main` at `31d7582`, after [#288](https://github.com/paulf-999/ai-engineering-playbook/pull/288) and [#291](https://github.com/paulf-999/ai-engineering-playbook/pull/291), with each theme below ✅ and what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 3 duplicates: the evaluation-criteria line in 4 files, the 15-line plan rule, and which tests earn their place | Findings 1 and 3 |
| 📦 **Always-on headroom** | About 2,280 of 3,000 tokens, or 76%, just over the 75% line | Finding 4 |
| 🔗 **Cross-file consistency** | 2 contradictions: when a PR needs a Plan Spec, and whether skill PRs answer the evaluation criteria | Findings 3 and 5 |
| 🔮 **Built for today** | 2 unused capacities: the skill contract template and the per-project `HOOKS=1` install | The template is kept by choice |

Measures: 40 support files against 92 product files, 8 of the last 50 commits (16%) on upkeep, 7 `maintenance/` files and no placeholders.

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🧪 **Fold `test_maintenance.md`:** move its sizing rules into the tests checklist in `_repo.md`, which already repeats its Need and No-duplicate checks.
2. 🔗 **One home for the criteria line:** keep it in `02_evaluation_criteria.md` and the PR template, and link to it from `.github/CONTRIBUTING.md` and `_workflow.md`.
3. ✂️ **Point to the plan hook:** trim the Intent and Spec bullets in `sdlc_workflow.md`, since the hook enforces them, to bring always-on context under 75%.
4. 📝 **Match the Plan Spec scope:** say in `_workflow.md` that any `src/claude/` change needs one, as the PR template and its check require.
5. 🧩 **Skills and the criteria:** decide whether skill PRs answer the evaluation criteria, and make `_skills.md` and the CI check agree.

The run also proposed dropping the skill contract template, which is left out because the templates are kept by choice.

## 💬 Component feedback

Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

### ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml) | [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Claude debugged a PR description failure from the CI log |
| [Portable paths](../../docs/guides/authoring_guide.md#-portable-paths) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked plans with no Intent or Spec in 8 or more sessions, and later plans open with `## Intent` |
| [`src/claude/rules/always_on/conduct/writing_style.md`](../../src/claude/rules/always_on/conduct/writing_style.md) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | The user cites it as the yardstick for docs |
| [`src/claude/rules/always_on/workflows/sdlc_workflow.md`](../../src/claude/rules/always_on/workflows/sdlc_workflow.md) | [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Its phase gates paced multi-phase work, and Claude followed it after each plan-hook block |
| [`src/claude/rules/on_demand/conduct/reporting.md`](../../src/claude/rules/on_demand/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/workflows/git.md`](../../src/claude/rules/on_demand/workflows/git.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read about 16 times before git work |
| [`src/claude/rules/on_demand/workflows/saving_plans.md`](../../src/claude/rules/on_demand/workflows/saving_plans.md) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read after a plan was approved |
| [`src/claude/rules/path_scoped/code_security.md`](../../src/claude/rules/path_scoped/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/rules/path_scoped/testing.md`](../../src/claude/rules/path_scoped/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/sh/claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh) | [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Caught always-on context at about 3,887 tokens, over the budget |
| [`src/sh/git/git_validate_branch_name.sh`](../../src/sh/git/git_validate_branch_name.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Forced 2 branch renames before push |
| [`src/sh/git/git_validate_pr_description.sh`](../../src/sh/git/git_validate_pr_description.sh) | [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught leftover evaluation-criteria placeholders in 5 sessions |
| [`tests/`](../../tests/) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught structure problems in the rules and helpers |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`.github/workflows/pip_audit.yml`](../../.github/workflows/pip_audit.yml) | 2026-11-16 | Unused | Never failed and never referenced |
| [`maintenance/test_maintenance.md`](../test_maintenance.md) | 2026-11-16 | Unused | Never guided any work |
| [`src/claude/_templates/`](../../src/claude/_templates/) | 2026-11-16 | Unused | Edited about 57 times, never used to create a file |
| [`src/claude/hooks/hook_enforcement_done_checks.sh`](../../src/claude/hooks/hook_enforcement_done_checks.sh) | 2026-11-16 | Unused | Its block message never fires in any transcript |
| [`src/claude/rules/always_on/conduct/security.md`](../../src/claude/rules/always_on/conduct/security.md) | 2026-11-16 | Unused | No evidence it guided any work |
| [`src/claude/rules/always_on/standards/claude_response_standards.md`](../../src/claude/rules/always_on/standards/claude_response_standards.md) | 2026-11-16 | Hindered | The user called replies "too long" and "too verbose", possibly from when a per-prompt hook injected it |
| [`src/claude/rules/on_demand/`](../../src/claude/rules/on_demand/) | 2026-11-16 | Unused | Apart from `git.md` and `saving_plans.md`, edited but never read to guide work |
| [`src/claude/rules/path_scoped/`](../../src/claude/rules/path_scoped/) | 2026-11-16 | Unused | Shown only while being edited |
| [`src/sh/claude_report_context_cost.sh`](../../src/sh/claude_report_context_cost.sh) | 2026-11-16 | Hindered | 26 failures across 11 sessions, none since [#256](https://github.com/paulf-999/ai-engineering-playbook/pull/256) |
| [`src/sh/git/git_validate_pr_description.sh`](../../src/sh/git/git_validate_pr_description.sh) | 2026-11-16 | Hindered | CI failed on formatting nits, though running it locally helped |

## 👥 Persona review

The latest [blind persona review](quality_rubrics/_personas.md), run on 2026-11-16 against commit `31d7582` by a data engineer (DE), data analyst (DA) and engineering manager (EM). Each run replaces this section, with earlier runs in git history.

### 🏗️ Over-engineering verdict

All three readers still found the repo over-engineered in what maintains it, not in what it installs:

- 📦 **What you get:** modest and sensible, in about 2,300 always-on tokens, 2 hooks and guides that load only when needed.
- 📍 **Where:** the scored rubric, the persona rubric and this audit (all three), the token report and PR-template CI checks (DE, EM), and commitlint running twice (DE).
- 🔧 **What they'd change:** EM would replace the scored rubric with a short checklist, DE would drop the duplicate commitlint job, and DA asked for nothing here.
- 🪞 **Stale evidence:** all three quoted the previous audit's 4/10 Over-engineering score, which this run replaces.
- ✅ **Worth keeping:** the installer, both hooks and the token-budget check.

### 🎯 Shared points

Each point two or more readers raised, ranked by how many raised it, then by impact:

| # | Theme | Raised by | Impact | Status |
|---|---|---|---|---|
| 1️⃣ | **Personal style and plan gates load for everyone** | DE, DA, EM | Blocks use | Kept as one config |
| 2️⃣ | **Maintenance layer outweighs the product** | DE, DA, EM | Confuses | The repo rubric and audit are kept; this run updates the stale scores |
| 3️⃣ | **The dbt example isn't evidence** | DE, DA, EM | Confuses | [#281](https://github.com/paulf-999/ai-engineering-playbook/issues/281) |
| 4️⃣ | **On-demand and path-scoped rules are unproven** | DE, DA, EM | Confuses | Open, with evals in [#234](https://github.com/paulf-999/ai-engineering-playbook/issues/234) |
| 5️⃣ | **Team conventions still need rewriting** | DE, DA, EM | Confuses | Gathered into one file in [#285](https://github.com/paulf-999/ai-engineering-playbook/pull/285); an opt-in overlay is open |

Single-reader asks: drop the duplicate commitlint job (DE), a "pick what you need" page and an analyst path (DA), and outcome measures such as review comments per PR (EM).

All three readers named the same strengths: the installer, the loading tiers, the enforced always-on budget and the repo's honesty about itself.
