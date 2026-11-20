# 🏗️ Repo review

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest repo review's bloat and over-engineering scores, findings and component feedback, scored against the [repo rubric](../quality_rubrics/_repo.md).

Each run follows that rubric: one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history. Tests and rules are checked against their checklists instead, with findings going to GitHub issues.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-20 | ✅ 2 | ✅ 2 | ❌ 0 | ❌ 0 | ✅ 2 | **6/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-20 | ❌ 0 | ✅ 2 | ✅ 2 | 🟡 1 | 🟡 1 | **6/10** |

## 🔍 Why the latest scores

The blind run of `main` at `2aae82a`, after [#432](https://github.com/paulf-999/ai-engineering-playbook/pull/432), [#434](https://github.com/paulf-999/ai-engineering-playbook/pull/434), [#436](https://github.com/paulf-999/ai-engineering-playbook/pull/436) and [#449](https://github.com/paulf-999/ai-engineering-playbook/pull/449) worked through the last run's findings. The rubric is unchanged, but this reviewer used helper agents and read 168 session transcripts, so its judged themes ran stricter. Over-engineering fell from 9 to 6, mostly on 8 contradictions, which this PR fixes. It ran as `claude -p --safe-mode` in a fresh clone, with each theme below ✅ and what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 9 repeated facts: the 20-file PR limit, the 3,000-token budget, the 15-line plan threshold, the 110-line rule cap, the kaizen 5-note threshold, `PREFERENCES=0`, the `HOOKS=1` exception, the three load folders and which PRs need a Plan Spec | Finding 2 |
| 📦 **Always-on headroom** | About 2,779 of 3,000 tokens (92.6%), down from 99.9% after #432 but still over the 90% line | Finding 5 |
| 🔗 **Cross-file consistency** | 8 contradictions: retiring unused parts in `design_principles.md:10`, 3 hooks named in `_tiers.md:9` and `getting_started.md:42` against 4 registered, evals still "next" in `_workflow.md:14`, the dropped halving test in `target_architecture/README.md:38`, who sets the budget in `protected_files.md:21`, every preference loading each session in `src/claude/README.md:66`, 3 test counts and a link claim in `governance_audit.md` | Fixed in this PR |
| 🪜 **Simplest mechanism** | 4: 64 of 89 eval scenarios no runner reads, 3 eval runners picked by a nested `$(if)` at `Makefile:70`, an LLM grader where a pattern check would do, and `kaizen_nudges.log` read only by its test | Findings 1 and 3 |
| 🔮 **Built for today** | 5: the 28 team-conventions files, `agents/core/` and `reference_material/core/` as only subfolders, `style_guides/jira/` for one file, and `PREFERENCES=1`, which changes nothing | Finding 4 |

Measures: 54 support files against 174 product files, 8 of the last 50 commits (16%) on upkeep, 7 `maintenance/` files besides the audit, no placeholders, and always-on context at about 2,779 of 3,000 tokens (92.6%).

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🧪 **Tag or drop the unrun eval scenarios:** 64 of the 89 scenarios in the 8 `evals.yaml` files have no `trigger:` or `behaviour: true` tag, so no runner reads them, including all 6 of `claude-capture-session-prompts`'.
2. 🔗 **One home per repeated fact:** link the 20-file limit in `git-create-pr`'s files to `git_validate_num_file_changes.sh`, and give `PREFERENCES=0`, `HOOKS=1`, the budget, the rule cap, the kaizen threshold, the Plan Spec rule and the load folders one home each, across `src/claude/README.md`, `getting_started.md`, `src/claude/rules/README.md` and `implementation_overview.md`.
3. 🪜 **Simplify the eval runners:** the 3 runners in `src/py/`, about 460 lines, are picked by a nested `$(if)` at `Makefile:70`, and `claude_run_behaviour_evals.py:151` grades with a model where a pattern check would do.
4. 🔮 **Flatten one-child folders:** `agents/core/`, `reference_material/core/` and `style_guides/jira/` each hold one item, and `PREFERENCES=1` in `claude_install_config.sh:156-171` changes nothing.
5. 📦 **Finish the always-on trim:** cut about 80 more tokens from `rules/always_on/` to get under 90% of the budget.

The run also proposed folding the thin team-conventions files back into their guides, trimming the 15-line threshold from `ai_sdlc_workflow.md`, a 75% always-on target and dropping `kaizen_nudges.log`. These are left out because the team-conventions split is the team's chosen layout, `ai_sdlc_workflow.md` is a [protected file](../../protected_files.md), 90% is the chosen target, and the log is the kaizen trial's evidence until 2026-12-03.

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
| [`src/claude/agents/core/technical-writer/`](../../../src/claude/agents/core/technical-writer/) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Drafted PR bodies in 22 sessions, up to 11 times in one |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked plans in 30 sessions, each accepted after one rewrite |
| [`src/claude/hooks/hook_enforcement_worktree_edits.sh`](../../../src/claude/hooks/hook_enforcement_worktree_edits.sh) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Fired in 12 sessions, and 9 then moved into a worktree |
| [`src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md`](../../../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Followed whenever the plan hook pointed to it |
| [`src/claude/rules/always_on/01_standards/writing_style.md`](../../../src/claude/rules/always_on/01_standards/writing_style.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | The markdown style rule, now `claude_markdown_style.md`, was read on demand in 8 to 11 sessions |
| [`src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md`](../../../src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Read, with the testing rules, before writing a new hook and its tests |
| [`src/claude/rules/on_demand/01_standards/conduct/reporting.md`](../../../src/claude/rules/on_demand/01_standards/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/01_standards/git.md`](../../../src/claude/rules/on_demand/01_standards/git.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/on_demand/02_preferences/claude_working_files/_saving_plans.md`](../../../src/claude/rules/on_demand/02_preferences/claude_working_files/_saving_plans.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/path_scoped/01_standards/code_security.md`](../../../src/claude/rules/path_scoped/01_standards/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/rules/path_scoped/01_standards/testing.md`](../../../src/claude/rules/path_scoped/01_standards/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/skills/_claude_skills/claude-kaizen/`](../../../src/claude/skills/_claude_skills/claude-kaizen/) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Ran twice |
| [`src/claude/skills/_git_skills/git-create-pr/`](../../../src/claude/skills/_git_skills/git-create-pr/) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Ran 22 times, each ending with a PR link |
| [`src/sh/claude_validate_always_on_budget.sh`](../../../src/sh/claude_validate_always_on_budget.sh) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#430](https://github.com/paulf-999/ai-engineering-playbook/pull/430), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Caught 4 real overruns |
| [`src/sh/git/git_validate_branch_name.sh`](../../../src/sh/git/git_validate_branch_name.sh) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Rejected 10 bad branch names |
| [`src/sh/git/git_validate_num_file_changes.sh`](../../../src/sh/git/git_validate_num_file_changes.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Never failed, but moved large PRs onto `release/` branches |
| [`src/sh/git/git_validate_pr_description.sh`](../../../src/sh/git/git_validate_pr_description.sh) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught missing sections in 10 sessions |
| [`tests/`](../../../tests/) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | `make test` found local failures in 21 sessions before any PR |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`src/claude/agents/core/code-reviewer/`](../../../src/claude/agents/core/code-reviewer/) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Rarely used | Used in 3 sessions |
| [`src/claude/hooks/hook_enforcement_done_checks.sh`](../../../src/claude/hooks/hook_enforcement_done_checks.sh) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Hindered | Fired up to 24 times in one session on another session's changes, in 2 sessions before #388's fix |
| [`src/claude/hooks/hook_reminder_kaizen_due.sh`](../../../src/claude/hooks/hook_reminder_kaizen_due.sh) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Unused | Never nudged in a transcript, during its trial to 2026-12-03 |
| [`src/claude/skills/`](../../../src/claude/skills/) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Unused | `claude-capture-session-prompts`, `jira-create-issue` and `confluence-create-page` never ran, and `git-review-pr` ran once |
| [`src/sh/claude_report_context_cost.sh`](../../../src/sh/claude_report_context_cost.sh) | [#452](https://github.com/paulf-999/ai-engineering-playbook/pull/452) | Hindered | Its pre-commit check failed 14 times, since it stages `context_cost.md` but still fails the commit, so each needed a second commit |
