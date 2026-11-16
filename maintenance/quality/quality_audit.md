# 📊 Quality audit

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest bloat and over-engineering scores for the repo as a whole, its findings and component feedback, from each regular review, plus the latest persona review.

Each run follows the [repo rubric](quality_rubrics/_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history. Tests and rules are checked against their checklists instead, with findings going to GitHub issues.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-16 | ✅ 2 | ✅ 2 | ❌ 0 | ✅ 2 | ✅ 2 | **8/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-16 | ❌ 0 | ✅ 2 | ✅ 2 | 🟡 1 | 🟡 1 | **6/10** |

## 🔍 Why the latest scores

The blind run of `main` at `cbfe548`, after [#294](https://github.com/paulf-999/ai-engineering-playbook/pull/294) to [#297](https://github.com/paulf-999/ai-engineering-playbook/pull/297), run as `claude -p --safe-mode` in a fresh clone, with each theme below ✅ and what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 4 or more duplicates: the PR-description rules CI enforces, restated in about 7 files, the 15-line plan threshold, the `release/` exemption in 5 places, and the 40-line child minimum | Finding 1 |
| 🔗 **Cross-file consistency** | 4 or more contradictions, such as `sdlc_workflow.md` asking for a pasted Spec in every repo while the PR check asks only for `src/claude/` changes | Finding 3 |
| 🪜 **Simplest mechanism** | 3: hand-typed token counts in the PR template, the context-cost script's test-only `--check` mode, and `pip_audit.yml` beside Dependabot | Finding 2 |
| 🔮 **Built for today** | 3: the skill and agent naming line in always-on `naming_standards.md`, the `YES=1` install, and `.env` in `.worktreeinclude` | Finding 4 |

Measures: 38 support files against 93 product files, 7 of the last 50 commits (14%) on upkeep, 5 `maintenance/` files besides the audit, no placeholders, and always-on context at about 2,242 of 3,000 tokens (74.7%), 8 tokens under the line. The plan-location contradiction it found in `README.md` was fixed in [#298](https://github.com/paulf-999/ai-engineering-playbook/pull/298) after the run.

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. ✂️ **Point to enforced checks:** replace restated PR-description rules, the plan threshold and the `release/` exemption with one-line links to the check, in `pull_request_template.md`, `02_evaluation_criteria.md`, `_workflow.md`, `authoring_guide/_rules.md`, `authoring_guide/_skills.md`, `sdlc_workflow.md`, `README.md`, `CONTRIBUTING.md`, `git_branching_strategy.md` and `_budget_and_guards.md`.
2. 🪜 **Simplify the context-cost check:** drop the test-only `--check` mode in `claude_report_context_cost.sh` and the hand-typed token counts in `pull_request_template.md`, and stop a stale report failing a commit, which happened 18 times.
3. 🔗 **Fix the contradictions:** the Spec rule in `sdlc_workflow.md:9`, the 20-word citation in `pull_request_template.md:7`, the stale `created` header and "hard gates" in `AGENT.md.template`, the header test `tests/README.md:8` describes, `.claude/CLAUDE.md` in `_budget_and_guards.md:8`, the backup path in `src/claude/README.md:36`, and American spellings in installed rules.
4. 🔮 **Trim unneeded capacity:** `.env` in `.worktreeinclude` and the undocumented `all:` Makefile target.
5. 🧹 **One copy of small facts:** the `paths:` awk check in two scripts, the TODO format in `todo_logging.md` and `TODO.md.template`, and tool versions pinned in both `requirements.txt` and `.pre-commit-config.yaml`.

The run also proposed reviewing the domain style guides no session read, dropping `pip_audit.yml`, the `YES=1` install, the skill and agent naming line and unused template fields, which are left out because the style guides, templates and skill naming are kept by choice and `YES=1` was asked for in [#280](https://github.com/paulf-999/ai-engineering-playbook/issues/280).

## 💬 Component feedback

Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

### ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Routine real catches, with Makefile and ruff in pre-commit |
| [Portable paths](../../docs/guides/authoring_guide.md#-portable-paths) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`maintenance/quality/quality_rubrics/_personas.md`](quality_rubrics/_personas.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Produced concrete outside findings in 21 sessions |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked 12 of 102 plan submissions, each fixed in one round |
| [`src/claude/rules/always_on/conduct/writing_style.md`](../../src/claude/rules/always_on/conduct/writing_style.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | The user cites it as the yardstick, and `_markdown_layout.md` was read 8 times |
| [`src/claude/rules/always_on/workflows/sdlc_workflow.md`](../../src/claude/rules/always_on/workflows/sdlc_workflow.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read after every plan-hook block, and the plan fixed from it |
| [`src/claude/rules/on_demand/conduct/reporting.md`](../../src/claude/rules/on_demand/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/workflows/git.md`](../../src/claude/rules/on_demand/workflows/git.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read 11 times before branch and PR work |
| [`src/claude/rules/on_demand/workflows/saving_plans.md`](../../src/claude/rules/on_demand/workflows/saving_plans.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read 7 times before saving a plan |
| [`src/claude/rules/path_scoped/code_security.md`](../../src/claude/rules/path_scoped/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/rules/path_scoped/testing.md`](../../src/claude/rules/path_scoped/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/sh/claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Caught always-on context at about 3,887 tokens in pre-commit |
| [`src/sh/git/git_validate_branch_name.sh`](../../src/sh/git/git_validate_branch_name.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Forced 2 branch renames before push |
| [`src/sh/git/git_validate_pr_description.sh`](../../src/sh/git/git_validate_pr_description.sh) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught bad PR descriptions locally and in CI |
| [`tests/`](../../tests/) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught structure problems in the rules and helpers |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`maintenance/quality/`](./) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Hindered | The audit and re-scoring took up user turns in 46 sessions |
| [`src/claude/_templates/`](../../src/claude/_templates/) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Unused | Never used to create a file |
| [`src/claude/hooks/hook_enforcement_done_checks.sh`](../../src/claude/hooks/hook_enforcement_done_checks.sh) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Unused | Never fired in any transcript |
| [`src/claude/rules/always_on/conduct/security.md`](../../src/claude/rules/always_on/conduct/security.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Unused | Loads every session, but never visibly changed what Claude did |
| [`src/claude/rules/always_on/standards/naming_standards.md`](../../src/claude/rules/always_on/standards/naming_standards.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Unused | Loads every session, but never visibly changed what Claude did |
| [`src/claude/rules/on_demand/`](../../src/claude/rules/on_demand/) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Unused | `turn_budgets.md`, `todo_logging.md`, `claude_naming_patterns.md` and the domain style guides were never read as guidance |
| [`src/claude/rules/path_scoped/`](../../src/claude/rules/path_scoped/) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Hindered | From 11-09 to 11-11 all 12 loaded every session, with no matching files |
| [`src/sh/claude_report_context_cost.sh`](../../src/sh/claude_report_context_cost.sh) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Hindered | The freshness check failed 18 times across 14 sessions, each fixed by regenerating the report |
| [`src/sh/git/git_validate_branch_name.sh`](../../src/sh/git/git_validate_branch_name.sh) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Mixed | Caught 3 real cases, but one session skipped it 17 times with `SKIP=` |
| [`src/sh/git/git_validate_num_file_changes.sh`](../../src/sh/git/git_validate_num_file_changes.sh) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Unused | Never tripped |

## 👥 Persona review

The latest [blind persona review](quality_rubrics/_personas.md), run on 2026-11-16 against commit `bebee00` by a data engineer (DE), data analyst (DA) and engineering manager (EM), the third round after the cuts in [#288](https://github.com/paulf-999/ai-engineering-playbook/pull/288), [#291](https://github.com/paulf-999/ai-engineering-playbook/pull/291) and [#298](https://github.com/paulf-999/ai-engineering-playbook/pull/298). Each run replaces this section, with earlier runs in git history.

### 🏗️ Over-engineering verdict

No reader now calls the repo over-engineered outright, but none calls it lean either:

- 📦 **What you get:** a small, careful core, about 2,200 always-on tokens, 2 hooks and a careful installer (all three).
- ⚖️ **What surrounds it:** 40 support files against 92 product files, which DE calls a governance layer "aimed at the maintainer" and DA says a user can ignore.
- 📍 **Where:** design docs, rubrics, persona reviews and this audit (DE, DA, EM), and dependabot and pip-audit for 6 dev dependencies (DE).
- ✅ **Worth keeping:** the installer and its tests, the plan hook and the budget check.

### 🎯 Shared points

Each point two or more readers raised, ranked by how many raised it, then by impact:

| # | Theme | Raised by | Impact | Status |
|---|---|---|---|---|
| 1️⃣ | **One team's conventions installed by default** | DE, DA, EM | Blocks use | Labelled as examples in [#285](https://github.com/paulf-999/ai-engineering-playbook/pull/285) and [#298](https://github.com/paulf-999/ai-engineering-playbook/pull/298); an opt-in pack is open |
| 2️⃣ | **The dbt example breaks its own rules** | DE, DA, EM | Confuses | [#281](https://github.com/paulf-999/ai-engineering-playbook/issues/281) |
| 3️⃣ | **Style rules should be opt-in, not opt-out** | DE, DA | Blocks use | `STYLE=0` added in [#298](https://github.com/paulf-999/ai-engineering-playbook/pull/298); the default stays on by choice |
| 4️⃣ | **Data and infra guides lack evidence** | DE, EM | Confuses | Labelled unproven in [#298](https://github.com/paulf-999/ai-engineering-playbook/pull/298), pending [#281](https://github.com/paulf-999/ai-engineering-playbook/issues/281) |

Single-reader asks: an analyst install path in the README and softer test rules for exploratory scripts (DA), and deleting the skill and agent templates (DE), which stay by choice.

All three readers named the same strengths: the installer, the always-on budget and the repo's honesty about itself.
