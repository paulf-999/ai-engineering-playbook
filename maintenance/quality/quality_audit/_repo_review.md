# 🏗️ Repo review

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest repo review's bloat and over-engineering scores, findings and component feedback, scored against the [repo rubric](../quality_rubrics/_repo.md).

Each run follows that rubric: three cold readers run its measures and score its themes, and this page keeps the median of the latest run's scores, with earlier runs in git history. Tests and rules are checked against their checklists instead, with findings going to GitHub issues.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-22 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **9/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-22 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **9/10** |

## 🔍 Why the latest scores

Three cold readers scored `main` at `acebd07`, after the fixes in [#481](https://github.com/paulf-999/ai-engineering-playbook/pull/481) to [#486](https://github.com/paulf-999/ai-engineering-playbook/pull/486), each as `claude -p --safe-mode` in its own fresh clone. Each theme above is their median, since single readers swung from 5 to 10 contradictions between runs. They scored Bloat 9, 8 and 9, and Over-engineering 10, 9 and 9. Measures: 55 support files against 178 product files, 8 of the last 50 commits (16%) on upkeep, 7 `maintenance/` files besides the audit, no placeholders, and always-on context at about 2,890 tokens, under the 2,900 ceiling.

| Theme | Why it scores this |
|---|---|
| 🎯 **Single source** | 4 to 7 repeated facts, led by the config-change checks in `guiding_principles.md`, `01_principles.md` and `02_evaluation_criteria.md`, and `PREFERENCES=0` across the rules READMEs |
| 🔗 **Cross-file consistency** | 2 to 4 contradictions, such as the further-reading row in `protected_files.md`, test counts in `governance_audit.md`, and the trial rule in `02_evaluation_criteria.md` against "unused isn't a reason to cut" |

## 🎯 Current findings

The latest run's findings, ranked by how often the three readers raised them. Each run replaces this list, and items on the [protected files](../../protected_files.md) page are left out.

1. 🎯 **One home for the config-change checks:** all three readers found them restated across `guiding_principles.md`, `01_principles.md` and `02_evaluation_criteria.md`.
2. 🔮 **Drop `YES=1`:** two readers found it serves provisioning scripts the repo doesn't have, in `claude_install_config.sh`, the `Makefile` and 2 tests.
3. 🎯 **State `PREFERENCES=0` once:** two readers found it restated in `_rule_classification.md` and the rules READMEs.

All three readers also proposed cutting or folding `governance_audit.md`. It's left out, since retiring it was declined, though slimming its hand-kept Tests table stays open.

## 💬 Component feedback

Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on, and a Hindered row goes once its fix merges.

### ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`.github/workflows/ci.yml`](../../../.github/workflows/ci.yml) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught a real missing `yaml` dependency |
| [`.pre-commit-config.yaml`](../../../.pre-commit-config.yaml) | [#489](https://github.com/paulf-999/ai-engineering-playbook/pull/489), [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480) | Caught Ruff errors in 27 sessions and a stale context-cost table in about 14 |
| [`CLAUDE.md`](../../../CLAUDE.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Its Done means had Claude run the tests in 42 sessions and pre-commit in 40 |
| [`maintenance/quality/quality_rubrics/_personas.md`](../quality_rubrics/_personas.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Produced concrete outside findings in 21 sessions |
| [`maintenance/quality/quality_rubrics/_repo.md`](../quality_rubrics/_repo.md) | [#430](https://github.com/paulf-999/ai-engineering-playbook/pull/430) | Its measures ran as written and settled the five measured themes without judgement |
| [Portable paths](../../../docs/guides/authoring_guide.md#-portable-paths) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/claude/agents/core/code-reviewer/`](../../../src/claude/agents/core/code-reviewer/) | [#489](https://github.com/paulf-999/ai-engineering-playbook/pull/489), [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480), [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Started 18 to 36 times, with no complaints |
| [`src/claude/agents/core/technical-writer/`](../../../src/claude/agents/core/technical-writer/) | [#489](https://github.com/paulf-999/ai-engineering-playbook/pull/489), [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480), [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Called 327 to 620 times, the default for PR bodies and docs |
| [`src/claude/hooks/ai_sdlc_workflow/hook_enforcement_done_checks.sh`](../../../src/claude/hooks/ai_sdlc_workflow/hook_enforcement_done_checks.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Since #388, fires 1 to 4 times a session, each on that session's own edits |
| [`src/claude/hooks/ai_sdlc_workflow/hook_enforcement_plan_sections.sh`](../../../src/claude/hooks/ai_sdlc_workflow/hook_enforcement_plan_sections.sh) | [#489](https://github.com/paulf-999/ai-engineering-playbook/pull/489), [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480), [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | After a block, 30 of 31 plans gained Intent and Spec, which the rule alone didn't achieve |
| [`src/claude/hooks/git/hook_enforcement_worktree_edits.sh`](../../../src/claude/hooks/git/hook_enforcement_worktree_edits.sh) | [#489](https://github.com/paulf-999/ai-engineering-playbook/pull/489), [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Blocked about 31 first edits, and one move found another session's changes on `main` |
| [`src/claude/hooks/claude_kaizen/hook_reminder_kaizen_due.sh`](../../../src/claude/hooks/claude_kaizen/hook_reminder_kaizen_due.sh) | [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480), [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Nudged in about 28 sessions, and `/claude-kaizen` runs followed |
| [`src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md`](../../../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) | [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | The plan hook sends Claude here, and plans then had the right sections |
| [`src/claude/rules/always_on/02_preferences/claude_writing_style.md`](../../../src/claude/rules/always_on/02_preferences/claude_writing_style.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | The markdown style rule, now `claude_markdown_style.md`, was read on demand in 8 to 11 sessions |
| [`src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md`](../../../src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Read, with the testing rules, before writing a new hook and its tests |
| [`src/claude/rules/on_demand/01_standards/conduct/claude_task_reporting.md`](../../../src/claude/rules/on_demand/01_standards/conduct/claude_task_reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/01_standards/git.md`](../../../src/claude/rules/on_demand/01_standards/git.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/on_demand/02_preferences/claude_saved_plans.md`](../../../src/claude/rules/on_demand/02_preferences/claude_saved_plans.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/path_scoped/01_standards/code_security.md`](../../../src/claude/rules/path_scoped/01_standards/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/01_standards/testing.md`](../../../src/claude/rules/path_scoped/01_standards/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/skills/_claude_skills/claude-kaizen/`](../../../src/claude/skills/_claude_skills/claude-kaizen/) | [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Called 8 times, each leading to follow-up fixes |
| [`src/claude/skills/_git_skills/git-create-pr/`](../../../src/claude/skills/_git_skills/git-create-pr/) | [#489](https://github.com/paulf-999/ai-engineering-playbook/pull/489), [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480), [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | The main way PRs ship, used in about 78 sessions |
| [`src/sh/claude_validate_always_on_budget.sh`](../../../src/sh/claude_validate_always_on_budget.sh) | [#489](https://github.com/paulf-999/ai-engineering-playbook/pull/489), [#477](https://github.com/paulf-999/ai-engineering-playbook/pull/477), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#430](https://github.com/paulf-999/ai-engineering-playbook/pull/430), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Caught about 6 overruns, one needing 5 rounds of trimming |
| [`src/sh/git/git_validate_branch_name.sh`](../../../src/sh/git/git_validate_branch_name.sh) | [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Caught bad branch names in 18 sessions |
| [`src/sh/git/git_validate_num_file_changes.sh`](../../../src/sh/git/git_validate_num_file_changes.sh) | [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Flagged oversized PRs in 3 sessions |
| [`src/sh/git/git_validate_pr_description.sh`](../../../src/sh/git/git_validate_pr_description.sh) | [#480](https://github.com/paulf-999/ai-engineering-playbook/pull/480), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught missing PR sections in 9 sessions |
| [`tests/`](../../../tests/) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | `make test` run often |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence | Response |
|---|---|---|---|---|
| [`src/claude/rules/on_demand/`](../../../src/claude/rules/on_demand/) | [#489](https://github.com/paulf-999/ai-engineering-playbook/pull/489) | Unused | Installed copies were read mainly when a hook pointed to them | Kept, since the [protected files](../../protected_files.md) page says unused isn't a reason to cut |
| [`src/claude/skills/`](../../../src/claude/skills/) | [#489](https://github.com/paulf-999/ai-engineering-playbook/pull/489) | Unused | `claude-capture-session-prompts`, `jira-create-issue` and `confluence-create-page` never ran, and `git-review-pr` ran 1 to 3 times | Kept, for the same reason |
