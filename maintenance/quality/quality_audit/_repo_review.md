# 🏗️ Repo review

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest repo review's bloat and over-engineering scores, findings and component feedback, scored against the [repo rubric](../quality_rubrics/_repo.md).

Each run follows that rubric: one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history. Tests and rules are checked against their checklists instead, with findings going to GitHub issues.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-19 | ✅ 2 | ❌ 0 | 🟡 1 | ❌ 0 | ✅ 2 | **5/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-19 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **9/10** |

## 🔍 Why the latest scores

The blind run of `main` at `0d241b6`, 102 commits after the last run at `6008ce9`. Since then [#310](https://github.com/paulf-999/ai-engineering-playbook/pull/310) fixed the last run's findings, [#411](https://github.com/paulf-999/ai-engineering-playbook/pull/411) began installing preferences by default, and the ported skills brought their contracts, test READMEs and tags. The rubric is unchanged, so the scores compare with the last run. It ran as `claude -p --safe-mode` in a fresh clone, with each theme below ✅ and what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🧾 **Evidence of need** | The 6 `skill.contract.yaml` files have no reader or inbound link, and only `_authoring_skills.md:6` says to write one | Finding 2 |
| 🎯 **Single source** | 5 duplicates: the 20-file PR limit across `git-create-pr/`, each skill's `tests/README.md` restating its `evals.yaml`, each contract restating its `SKILL.md`, the `on_demand/` install note in both `src/claude/README.md` and `src/claude/rules/README.md`, and the preference token costs copied into `src/claude/README.md:66` | Findings 2, 3 and 5 |
| 📦 **Always-on headroom** | About 2,997 of 3,000 tokens (99.9%), up from 74.8%, mostly the ~555 tokens of the two preference rules that #411 installs by default | Finding 1 |
| 🔗 **Cross-file consistency** | 3 contradictions: `git-create-pr/SKILL.md:18` flags 20 or more files where CI fails only above 20, `src/claude/README.md:66` puts the working-files preferences at about 200 tokens against a measured 263, and `governance_audit.md:27` still says about 2,244 tokens | Finding 5 |

Measures: 53 support files against 175 product files, 7 of the last 50 commits (14%) on upkeep, 6 `maintenance/` files besides the audit, no placeholders, and always-on context at about 2,997 of 3,000 tokens (99.9%).

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 📦 **Win back always-on headroom:** trim the always-on rules towards 75% of the budget, starting with where `behaviour.md`'s "Present options" overlaps "Simpler options" in `src/claude/CLAUDE.md`.
2. ✂️ **Delete the skill contracts:** remove the 6 `skill.contract.yaml` files, 233 lines that nothing reads, and their mentions in `_authoring_skills.md` and `src/claude/_templates/README.md`.
3. 🧹 **Fold the skill test READMEs:** merge each skill's `tests/README.md`, 139 lines in all, into its `evals.yaml` descriptions, keeping the note on how `make evals` runs once in `_authoring_skills.md`.
4. 🏷️ **Drop the unread tags:** remove the `tags:` block, with `criticality`, `status` and `tested`, from the 6 `SKILL.md` files, since nothing reads it.
5. 🔗 **One home for two facts:** have `git-create-pr`'s `SKILL.md`, `reference/_implementation.md` and `evals.yaml` defer to `git_validate_num_file_changes.sh` and match its "more than 20", link `src/claude/README.md:66` to the context cost report, and refresh `governance_audit.md:27`.

The run also proposed making the two preference rules on-demand or opt-in, trimming `src/claude/CLAUDE.md`, and changing the skill template's contract and tags. These are left out because preferences install by default by choice, `CLAUDE.md` stays as it is, and the templates are kept for porting.

## 💬 Component feedback

Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

### ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`.github/workflows/ci.yml`](../../../.github/workflows/ci.yml) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught a real missing `yaml` dependency |
| [`CLAUDE.md`](../../../CLAUDE.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Its Done means had Claude run the tests in 42 sessions and pre-commit in 40 |
| [`maintenance/quality/quality_rubrics/_personas.md`](../quality_rubrics/_personas.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Produced concrete outside findings in 21 sessions |
| [`maintenance/quality/quality_rubrics/_repo.md`](../quality_rubrics/_repo.md) | [#NNN](https://github.com/paulf-999/ai-engineering-playbook/pull/NNN) | Its measures ran as written and settled the five measured themes without judgement |
| [Portable paths](../../../docs/guides/authoring_guide.md#-portable-paths) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked 12 sessions' plans, each rewritten properly, though also some trivial non-repo plans |
| [`src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md`](../../../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Followed whenever the plan hook pointed to it |
| [`src/claude/rules/always_on/01_standards/writing_style.md`](../../../src/claude/rules/always_on/01_standards/writing_style.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | The markdown style rule, now `claude_markdown_style.md`, was read on demand in 8 to 11 sessions |
| [`src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md`](../../../src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Read, with the testing rules, before writing a new hook and its tests |
| [`src/claude/rules/on_demand/01_standards/conduct/reporting.md`](../../../src/claude/rules/on_demand/01_standards/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/01_standards/git.md`](../../../src/claude/rules/on_demand/01_standards/git.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/on_demand/02_preferences/claude_working_files/_saving_plans.md`](../../../src/claude/rules/on_demand/02_preferences/claude_working_files/_saving_plans.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/path_scoped/01_standards/code_security.md`](../../../src/claude/rules/path_scoped/01_standards/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/rules/path_scoped/01_standards/testing.md`](../../../src/claude/rules/path_scoped/01_standards/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/sh/claude_validate_always_on_budget.sh`](../../../src/sh/claude_validate_always_on_budget.sh) | [#NNN](https://github.com/paulf-999/ai-engineering-playbook/pull/NNN), [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Its per-file breakdown showed at once where the always-on tokens go |
| [`src/sh/git/git_validate_branch_name.sh`](../../../src/sh/git/git_validate_branch_name.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Caught `docs/` and `refactor/` prefixes and commits on `main`, with one false fire on a detached HEAD |
| [`src/sh/git/git_validate_num_file_changes.sh`](../../../src/sh/git/git_validate_num_file_changes.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Never failed, but moved large PRs onto `release/` branches |
| [`src/sh/git/git_validate_pr_description.sh`](../../../src/sh/git/git_validate_pr_description.sh) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught bad PR descriptions locally and in CI |
| [`tests/`](../../../tests/) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | `make test` found local failures in 21 sessions before any PR |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`src/claude/`](../../../src/claude/) | [#NNN](https://github.com/paulf-999/ai-engineering-playbook/pull/NNN) | Unused | The hooks, skills and agents weren't exercised by a read-only run, with no transcripts in the clone |
| [`src/sh/claude_validate_always_on_budget.sh`](../../../src/sh/claude_validate_always_on_budget.sh) | [#NNN](https://github.com/paulf-999/ai-engineering-playbook/pull/NNN) | Hindered | Lists `agents/core/README.md` as a ~0-token agent description, which is harmless but noisy |
