# 🏗️ Repo review

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest repo review's bloat and over-engineering scores, findings and component feedback, scored against the [repo rubric](../quality_rubrics/_repo.md).

Each run follows that rubric: one cold reader runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history. Tests and rules are checked against their checklists instead, with findings going to GitHub issues.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-21 | ✅ 2 | ✅ 2 | ❌ 0 | ✅ 2 | ✅ 2 | **8/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-21 | 🟡 1 | 🟡 1 | ✅ 2 | 🟡 1 | 🟡 1 | **6/10** |

## 🔍 Why the latest scores

This is the second blind run of the day, of `main` at `46c3fb2` after [#476](https://github.com/paulf-999/ai-engineering-playbook/pull/476), run as `claude -p --safe-mode` in a fresh clone. Measures: 58 support files against 178 product files, 11 of the last 50 commits (22%) on upkeep, 7 `maintenance/` files besides the audit, no placeholders, and always-on context at about 2,890 tokens, under the 2,900 ceiling.

| Theme | Why it scores this |
|---|---|
| 🎯 **Single source** | 6 repeated facts: the PR file limit and branch pattern in `git-create-pr`, the kaizen run counts, the files needing Evaluation criteria, the rule-kinds table and the 40-line floor |
| 🔗 **Cross-file consistency** | 5 contradictions: a broken protected-files link in the rubric, the README evals' readers, `RUNS` "per side", "one line" against one bullet per red flag, and file naming without the house style |
| 🔁 **Upkeep cost** | 22%, and 5 of the 11 commits only edit `governance_audit.md` |
| 🪜 **Simplest mechanism** | 3: `governance_audit.md` beside the repo review, the done-checks hook beside `CLAUDE.md`'s Done means, and test helpers listed by name in `.pre-commit-config.yaml` |
| 🔮 **Built for today** | 4: `YES=1` in the installer, `RUNS` in the eval runners, `path_scoped/01_standards/` with no sibling, and `style_guides/jira/` for one file |

## 🎯 Current findings

The latest run's findings still open, ranked by how much each would cut. Each run replaces this list, and items on the [protected files](../../protected_files.md) page are left out.

1. ✅ **Done-checks hook:** it re-fires after the checks have run, in `hook_enforcement_done_checks.sh`.
2. 🔁 **Audit upkeep:** edits to `governance_audit.md` are 5 of the 11 upkeep commits.
3. 🔮 **Unused options:** `YES=1` in `claude_install_config.sh` and `RUNS` in the rule and README eval runners.
4. 🎯 **Two repeats left:** the kaizen run counts in `claude-kaizen/SKILL.md` and its `_implementation.md`, and the 40-line floor in `authoring_guide.md` and `_rule_classification.md`.
5. 🌳 **Worktree hook:** its block is often a one-time retry, in `hook_enforcement_worktree_edits.sh`.

## 💬 Component feedback

Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

### ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`.github/workflows/ci.yml`](../../../.github/workflows/ci.yml) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught a real missing `yaml` dependency |
| [`CLAUDE.md`](../../../CLAUDE.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Its Done means had Claude run the tests in 42 sessions and pre-commit in 40 |
| [`maintenance/quality/quality_rubrics/_personas.md`](../quality_rubrics/_personas.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Produced concrete outside findings in 21 sessions |
| [`maintenance/quality/quality_rubrics/_repo.md`](../quality_rubrics/_repo.md) | [#430](https://github.com/paulf-999/ai-engineering-playbook/pull/430) | Its measures ran as written and settled the five measured themes without judgement |
| [Portable paths](../../../docs/guides/authoring_guide.md#-portable-paths) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/claude/agents/core/code-reviewer/`](../../../src/claude/agents/core/code-reviewer/) | [#PRD](https://github.com/paulf-999/ai-engineering-playbook/pull/PRD), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Used in 4 sessions, productively |
| [`src/claude/agents/core/technical-writer/`](../../../src/claude/agents/core/technical-writer/) | [#PRD](https://github.com/paulf-999/ai-engineering-playbook/pull/PRD), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Used in 28 sessions for docs work |
| [`src/claude/hooks/hook_enforcement_done_checks.sh`](../../../src/claude/hooks/hook_enforcement_done_checks.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Since #388, fires 1 to 4 times a session, each on that session's own edits |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#PRD](https://github.com/paulf-999/ai-engineering-playbook/pull/PRD), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked about 60 plans that were missing a heading, in about 30 sessions |
| [`src/claude/hooks/hook_enforcement_worktree_edits.sh`](../../../src/claude/hooks/hook_enforcement_worktree_edits.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Fired 42 times in 20 sessions, 3 of them false positives on `/private/tmp` sandboxes |
| [`src/claude/hooks/hook_reminder_kaizen_due.sh`](../../../src/claude/hooks/hook_reminder_kaizen_due.sh) | [#PRD](https://github.com/paulf-999/ai-engineering-playbook/pull/PRD), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Fired in 2 sessions, as intended |
| [`src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md`](../../../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | With the plan hook, keeps plans opening with Intent and Spec |
| [`src/claude/rules/always_on/01_standards/writing_style.md`](../../../src/claude/rules/always_on/01_standards/writing_style.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | The markdown style rule, now `claude_markdown_style.md`, was read on demand in 8 to 11 sessions |
| [`src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md`](../../../src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Read, with the testing rules, before writing a new hook and its tests |
| [`src/claude/rules/on_demand/01_standards/conduct/reporting.md`](../../../src/claude/rules/on_demand/01_standards/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/01_standards/git.md`](../../../src/claude/rules/on_demand/01_standards/git.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/on_demand/02_preferences/claude_working_files/_saving_plans.md`](../../../src/claude/rules/on_demand/02_preferences/claude_working_files/_saving_plans.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/path_scoped/01_standards/code_security.md`](../../../src/claude/rules/path_scoped/01_standards/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/01_standards/testing.md`](../../../src/claude/rules/path_scoped/01_standards/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/skills/_claude_skills/claude-kaizen/`](../../../src/claude/skills/_claude_skills/claude-kaizen/) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Ran 4 times after the kaizen nudges |
| [`src/claude/skills/_git_skills/git-create-pr/`](../../../src/claude/skills/_git_skills/git-create-pr/) | [#PRD](https://github.com/paulf-999/ai-engineering-playbook/pull/PRD), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Called in 28 sessions, the most-used skill |
| [`src/sh/claude_validate_always_on_budget.sh`](../../../src/sh/claude_validate_always_on_budget.sh) | [#PRD](https://github.com/paulf-999/ai-engineering-playbook/pull/PRD), [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#430](https://github.com/paulf-999/ai-engineering-playbook/pull/430), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Kept new rules out of always-on once the budget was nearly reached |
| [`src/sh/git/git_validate_branch_name.sh`](../../../src/sh/git/git_validate_branch_name.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Run often, with real catches |
| [`src/sh/git/git_validate_num_file_changes.sh`](../../../src/sh/git/git_validate_num_file_changes.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Never failed, but moved large PRs onto `release/` branches |
| [`src/sh/git/git_validate_pr_description.sh`](../../../src/sh/git/git_validate_pr_description.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Run often, with real catches |
| [`tests/`](../../../tests/) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | `make test` run often |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`src/claude/hooks/hook_enforcement_done_checks.sh`](../../../src/claude/hooks/hook_enforcement_done_checks.sh) | [#PRD](https://github.com/paulf-999/ai-engineering-playbook/pull/PRD) | Hindered | Re-fires after the checks have run, and Claude replies it already ran them |
| [`src/claude/hooks/hook_enforcement_worktree_edits.sh`](../../../src/claude/hooks/hook_enforcement_worktree_edits.sh) | [#PRD](https://github.com/paulf-999/ai-engineering-playbook/pull/PRD) | Hindered | Often a one-time block that Claude simply retries |
| [`src/claude/skills/`](../../../src/claude/skills/) | [#PRD](https://github.com/paulf-999/ai-engineering-playbook/pull/PRD) | Unused | `jira-create-issue`, `confluence-create-page` and `claude-capture-session-prompts` never ran, and `git-review-pr` ran once |
| [`src/claude/skills/_claude_skills/claude-kaizen/`](../../../src/claude/skills/_claude_skills/claude-kaizen/) | [#PRD](https://github.com/paulf-999/ai-engineering-playbook/pull/PRD) | Hindered | Two runs on the same 32 notes kept no rules |
