# 🏗️ Repo review

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest repo review's bloat and over-engineering scores, findings and component feedback, scored against the [repo rubric](../quality_rubrics/_repo.md).

Each run follows that rubric: one cold reader runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history. Tests and rules are checked against their checklists instead, with findings going to GitHub issues.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-21 | ✅ 2 | ✅ 2 | ❌ 0 | ❌ 0 | ✅ 2 | **6/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-21 | ❌ 0 | ✅ 2 | ✅ 2 | 🟡 1 | 🟡 1 | **6/10** |

## 🔍 Why the latest scores

This is the blind run of `main` at `d3258d1`, run as `claude -p --safe-mode` in a fresh clone. Measures: 58 support files against 178 product files, 9 of the last 50 commits (18%) on upkeep, 7 `maintenance/` files besides the audit, no placeholders, and always-on context at about 2,890 of 3,000 tokens (96%).

| Theme | Why it scores this |
|---|---|
| 🎯 **Single source** | 8 repeated facts: the config principles, install options, hook list, skill and agent naming, the PR-description rule, the H1 and Purpose rule, the budget and size numbers, and the review cadence |
| 📦 **Always-on headroom** | About 2,890 of 3,000 tokens (96%), over the 95% line |
| 🔗 **Cross-file consistency** | 8 contradictions, among them unread `must_not_match` eval fields, the kaizen hook in project installs, `git-review-pr` requiring an agent, and `governance_audit.md` saying CI runs context cost |
| 🪜 **Simplest mechanism** | 4: an LLM grader for regex-checkable rule evals, the readme evals beside the persona review, `governance_audit.md` beside the protected audit, and the `make evals` bootstrap beside `make deps` |
| 🔮 **Built for today** | 5: unread eval YAML fields, `YES=1` and `DENY_MANIFEST` in the installer, `agents/core/`, `kaizen_nudges.log` and the run-length table in `turn_budgets.md` |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and items on the [protected files](../../protected_files.md) page are left out.

1. 🔗 **One home per repeated fact:** link the principles, install options, hook list, PR-description rule and cadence to one canonical copy.
2. 🧪 **Unread eval fields:** strip the `evals.yaml` fields no runner reads, or wire `must_not_match` and `follow_up_replies` into `claude_run_behaviour_evals.py`.
3. 🗃️ **Second audit:** fold what still matters in `governance_audit.md` into the protected audit, and fix its stale lines.
4. 🪜 **Readme evals:** `claude_run_readme_evals.py` overlaps the protected persona review.
5. 📦 **Always-on trim:** cut about 200 tokens from `rules/always_on/`, starting with the naming line `claude_naming_patterns.md` already holds.

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
| [`src/claude/agents/core/code-reviewer/`](../../../src/claude/agents/core/code-reviewer/) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Called about 36 times |
| [`src/claude/agents/core/technical-writer/`](../../../src/claude/agents/core/technical-writer/) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Called about 608 times |
| [`src/claude/hooks/hook_enforcement_done_checks.sh`](../../../src/claude/hooks/hook_enforcement_done_checks.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Since #388, fires 1 to 4 times a session, each on that session's own edits |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Made plans add Intent and Spec about 66 times in 38 sessions, with no complaints |
| [`src/claude/hooks/hook_enforcement_worktree_edits.sh`](../../../src/claude/hooks/hook_enforcement_worktree_edits.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Fired 42 times in 20 sessions, 3 of them false positives on `/private/tmp` sandboxes |
| [`src/claude/hooks/hook_reminder_kaizen_due.sh`](../../../src/claude/hooks/hook_reminder_kaizen_due.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Nudged in 4 sessions, and `/claude-kaizen` followed in 2, on trial to 2026-12-03 |
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
| [`src/claude/skills/_git_skills/git-create-pr/`](../../../src/claude/skills/_git_skills/git-create-pr/) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | About 173 runs and 261 PRs, the most-used component |
| [`src/sh/claude_validate_always_on_budget.sh`](../../../src/sh/claude_validate_always_on_budget.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#430](https://github.com/paulf-999/ai-engineering-playbook/pull/430), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Run often |
| [`src/sh/git/git_validate_branch_name.sh`](../../../src/sh/git/git_validate_branch_name.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Run often, with real catches |
| [`src/sh/git/git_validate_num_file_changes.sh`](../../../src/sh/git/git_validate_num_file_changes.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Never failed, but moved large PRs onto `release/` branches |
| [`src/sh/git/git_validate_pr_description.sh`](../../../src/sh/git/git_validate_pr_description.sh) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Run often, with real catches |
| [`tests/`](../../../tests/) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | `make test` run often |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`src/claude/skills/`](../../../src/claude/skills/) | [#474](https://github.com/paulf-999/ai-engineering-playbook/pull/474) | Unused | `claude-capture-session-prompts`, `jira-create-issue` and `confluence-create-page` never ran, and `git-review-pr` ran twice |
