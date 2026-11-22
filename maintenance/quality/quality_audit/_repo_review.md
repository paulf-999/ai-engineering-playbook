# 🏗️ Repo review

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest repo review's bloat and over-engineering scores, findings and component feedback, scored against the [repo rubric](../quality_rubrics/_repo.md).

Each run follows that rubric: one cold reader runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history. Tests and rules are checked against their checklists instead, with findings going to GitHub issues.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-22 | ✅ 2 | ✅ 2 | ❌ 0 | ✅ 2 | ✅ 2 | **8/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-22 | ❌ 0 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | **6/10** |

## 🔍 Why the latest scores

This is a blind run of `main` at `88a8f83`, after [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477) and [#478](https://github.com/paulf-999/ai-engineering-playbook/pull/478), run as `claude -p --safe-mode` in a fresh clone. Measures: 55 support files against 178 product files, 12 of the last 50 commits (24%) on upkeep, 7 `maintenance/` files besides the audit, no placeholders, and always-on context at about 2,890 tokens, under the 2,900 ceiling.

| Theme | Why it scores this |
|---|---|
| 🎯 **Single source** | 7 repeated facts: secrets in `security.md` and `code_security.md`, skill and agent naming, the `cost < 500` assertion example, the plan split into `intent.md`, `spec.md` and `plan.md`, no stacked PRs, `git push` not gated, and the shared design principles |
| 🔗 **Cross-file consistency** | 8 contradictions: `git-create-pr`'s eval count and commit scope, the rule template's plain pointer, test speed of 1 against 5 seconds, the helper exclude in `tests/README.md`, the done-checks test count in `governance_audit.md`, the hooks description in `src/claude/README.md` and the examples in `rules/always_on/README.md` |
| 🔁 **Upkeep cost** | 24%, and 5 of the 12 commits only edit `governance_audit.md` |
| 🪜 **Simplest mechanism** | 3: the done-checks hook beside `CLAUDE.md`'s Done means, `governance_audit.md` beside the repo review, and 4 eval runners picked by nested `Makefile` flags |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and items on the [protected files](../../protected_files.md) page are left out. The 2-round fix cap is spent, so these stay open for the next review.

1. 🎯 **One home per principle:** link `design_principles.md`, `02_evaluation_criteria.md`, `guiding_principles.md` and `authoring_guide.md` to `01_principles.md` instead of restating it.
2. 🔗 **Merge overlapping rules:** `security.md` with `code_security.md`, `naming_standards.md` with `claude_naming_patterns.md`, `_testing_design_pattern.md` with `python/testing/_assertions.md`, and `git.md` with `automation_controls.md`, keeping the plan split only in `ai_sdlc_workflow.md`.
3. ✅ **Slim the done-checks hook:** `hook_enforcement_done_checks.sh` fired 49 times in 17 sessions before #478, so check its fix at the next review.
4. 🔗 **Fix the 8 contradictions:** small cuts in the files named in the Why table above.
5. 🧪 **Speed up `make test`:** transcripts show it taking about 171 seconds, 152 of them in `test_claude_install_config.py`, though it ran in 36 seconds on this PR.

The run also proposed folding `governance_audit.md` into this page and `protected_files.md`. It's left out, since retiring it was declined.

## 💬 Component feedback

Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

### ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`.github/workflows/ci.yml`](../../../.github/workflows/ci.yml) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught a real missing `yaml` dependency |
| [`.pre-commit-config.yaml`](../../../.pre-commit-config.yaml) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM) | ruff fixed code in about 27 sessions, and commitlint caught bad messages in 5 |
| [`CLAUDE.md`](../../../CLAUDE.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Its Done means had Claude run the tests in 42 sessions and pre-commit in 40 |
| [`maintenance/quality/quality_rubrics/_personas.md`](../quality_rubrics/_personas.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Produced concrete outside findings in 21 sessions |
| [`maintenance/quality/quality_rubrics/_repo.md`](../quality_rubrics/_repo.md) | [#430](https://github.com/paulf-999/ai-engineering-playbook/pull/430) | Its measures ran as written and settled the five measured themes without judgement |
| [Portable paths](../../../docs/guides/authoring_guide.md#-portable-paths) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/claude/agents/core/code-reviewer/`](../../../src/claude/agents/core/code-reviewer/) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM), [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Spawned 18 times across about 8 sessions |
| [`src/claude/agents/core/technical-writer/`](../../../src/claude/agents/core/technical-writer/) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM), [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Spawned 315 times across about 76 sessions, the default for drafting docs |
| [`src/claude/hooks/hook_enforcement_done_checks.sh`](../../../src/claude/hooks/hook_enforcement_done_checks.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Since #388, fires 1 to 4 times a session, each on that session's own edits |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM), [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Gave plans the right sections, though one transcript calls it heavy for quick SQL work |
| [`src/claude/hooks/hook_enforcement_worktree_edits.sh`](../../../src/claude/hooks/hook_enforcement_worktree_edits.sh) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Blocked 26 times in 15 sessions, several times exposing another session in the same folder |
| [`src/claude/hooks/hook_reminder_kaizen_due.sh`](../../../src/claude/hooks/hook_reminder_kaizen_due.sh) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM), [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Nudged in about 28 sessions, and `/claude-kaizen` runs followed |
| [`src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md`](../../../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | The plan hook sends Claude here, and plans then had the right sections |
| [`src/claude/rules/always_on/01_standards/writing_style.md`](../../../src/claude/rules/always_on/01_standards/writing_style.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | The markdown style rule, now `claude_markdown_style.md`, was read on demand in 8 to 11 sessions |
| [`src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md`](../../../src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Read, with the testing rules, before writing a new hook and its tests |
| [`src/claude/rules/on_demand/01_standards/conduct/reporting.md`](../../../src/claude/rules/on_demand/01_standards/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/01_standards/git.md`](../../../src/claude/rules/on_demand/01_standards/git.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/on_demand/02_preferences/claude_working_files/_saving_plans.md`](../../../src/claude/rules/on_demand/02_preferences/claude_working_files/_saving_plans.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/path_scoped/01_standards/code_security.md`](../../../src/claude/rules/path_scoped/01_standards/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/01_standards/testing.md`](../../../src/claude/rules/path_scoped/01_standards/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/skills/_claude_skills/claude-kaizen/`](../../../src/claude/skills/_claude_skills/claude-kaizen/) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Called 8 times, each leading to follow-up fixes |
| [`src/claude/skills/_git_skills/git-create-pr/`](../../../src/claude/skills/_git_skills/git-create-pr/) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM), [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Called 169 times across about 78 sessions, the most-used component |
| [`src/sh/claude_validate_always_on_budget.sh`](../../../src/sh/claude_validate_always_on_budget.sh) | [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#430](https://github.com/paulf-999/ai-engineering-playbook/pull/430), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Kept new rules out of always-on once the budget was nearly reached |
| [`src/sh/git/git_validate_branch_name.sh`](../../../src/sh/git/git_validate_branch_name.sh) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Caught bad branch names in 18 sessions |
| [`src/sh/git/git_validate_num_file_changes.sh`](../../../src/sh/git/git_validate_num_file_changes.sh) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Flagged oversized PRs in 3 sessions |
| [`src/sh/git/git_validate_pr_description.sh`](../../../src/sh/git/git_validate_pr_description.sh) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught missing PR sections in 9 sessions |
| [`tests/`](../../../tests/) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | `make test` run often |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`src/claude/hooks/hook_enforcement_done_checks.sh`](../../../src/claude/hooks/hook_enforcement_done_checks.sh) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM) | Hindered | Fired 49 times in 17 sessions, often after the checks had run, and no session yet shows #478's fix |
| [`src/claude/rules/on_demand/`](../../../src/claude/rules/on_demand/) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM) | Unused | No on-demand rule or style guide was read at its current path |
| [`src/claude/skills/`](../../../src/claude/skills/) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM) | Unused | `claude-capture-session-prompts`, `jira-create-issue` and `confluence-create-page` were never invoked |
| [`src/claude/skills/_git_skills/git-review-pr/`](../../../src/claude/skills/_git_skills/git-review-pr/) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM) | Unused | Used in 1 session, then waived as unneeded for the user's own PRs |
| [`src/sh/claude_validate_always_on_budget.sh`](../../../src/sh/claude_validate_always_on_budget.sh) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM) | Hindered | Went over budget in 15 sessions and was waived twice, so any new always-on rule trips it |
| [`tests/`](../../../tests/) | [#PRNUM](https://github.com/paulf-999/ai-engineering-playbook/pull/PRNUM) | Hindered | Transcripts show `make test` taking about 171 seconds, 152 of them in `test_claude_install_config.py` |
