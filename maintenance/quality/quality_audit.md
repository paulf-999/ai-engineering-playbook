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
| 2026-11-15 | ❌ 0 | ✅ 2 | ✅ 2 | ❌ 0 | ❌ 0 | **4/10** |

## 🔍 Why the latest scores

The blind run of `main` at [#261](https://github.com/paulf-999/ai-engineering-playbook/pull/261), with each theme below ✅ and what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 4 duplicates, such as the 5-bullet cap restated in 4 files and the 15-line plan threshold in 3 | Finding 4 |
| 📦 **Always-on headroom** | About 2,418 of 3,000 tokens, or 80.6%, over the 75% line | Move always-on detail to on-demand files |
| 🚧 **Placeholders** | 1, "not built yet" in [`docs/target_architecture/README.md`](../../docs/target_architecture/README.md) | Link the build progress issue without the phrase |
| 🔗 **Cross-file consistency** | 6 contradictions, such as `Makefile:38` printing the project path twice when `PROJECT` is set | Finding 3 |
| 🪜 **Simplest mechanism** | 4 issues: the PR-body parser, the MoSCoW scheme, layout-only rule tests and the commitlint `pr_title` job | Findings 1 and 2 |
| 🔮 **Built for today** | 4 or more unused capacities, such as the 10-column TODO template and `dir_exists` in `shell_utils.sh`, which nothing calls | Finding 5 |

Upkeep cost is ✅ at 9 of the last 50 commits, or 18%, and Process weight is ✅ at 8 `maintenance/` files against 92 product files.

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. ✂️ **Grep the PR body:** keep the description check, but swap the 128-line parser in `git_validate_pr_description.sh` for a grep for the template's default lines.
2. 🏷️ **Drop the MoSCoW tags:** remove `tests/test_moscow_tags.py`, most of `maintenance/test_maintenance.md` and the 83 `# MoSCoW:` comments, since two of the four levels can never be used.
3. 🔗 **Fix the contradictions:** `Makefile:38`, the done-checks hook in `_tiers.md:9` against `src/claude/README.md:42`, the hook red flag `_tiers.md:14` cites, `~/.claude` in `README.md` against `$CLAUDE_CONFIG_DIR`, "3-line header" in `test_rules_structure.py`, and "re-scores every test and rule" in `.github/CONTRIBUTING.md`.
4. 🎯 **One home per fact:** the 5-bullet cap in `_markdown_layout.md`, `rule.md.template` and the PR template, the 15-line plan threshold in `sdlc_workflow.md` and `_workflow.md`, and the branch regex and 20-file limit in `docs/guides/git_branching_strategy.md`.
5. 🔮 **Trim unused capacity:** `TODO.md.template`, `dir_exists` and `CRITICAL` in `shell_utils.sh`, the `FETCH_HEAD` fallback in `git_validate_num_file_changes.sh`, the "Sign it's working" column in `_workflow.md`, and `-rxX` in `pyproject.toml`.

The run also proposed removing the done-checks hook, `pip_audit.yml` and the layout-only rule tests, which are left out because they're kept by choice.

## 💬 Component feedback

Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

### ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Claude debugged a PR description failure from the CI log |
| [Portable paths](../../docs/guides/authoring_guide.md#-portable-paths) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked plans with no Intent or Spec in 8 or more sessions, and later plans open with `## Intent` |
| [`src/claude/rules/always/conduct/writing_style.md`](../../src/claude/rules/always/conduct/writing_style.md) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | The user cites it as the yardstick for docs |
| [`src/claude/rules/always/workflows/sdlc_workflow.md`](../../src/claude/rules/always/workflows/sdlc_workflow.md) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Its phase gates paced multi-phase work, and Claude followed it after each plan-hook block |
| [`src/claude/rules/on_demand/conduct/reporting.md`](../../src/claude/rules/on_demand/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/workflows/git.md`](../../src/claude/rules/on_demand/workflows/git.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read about 16 times before git work |
| [`src/claude/rules/on_demand/workflows/saving_plans.md`](../../src/claude/rules/on_demand/workflows/saving_plans.md) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read after a plan was approved |
| [`src/claude/rules/path_scoped/code_security.md`](../../src/claude/rules/path_scoped/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/rules/path_scoped/testing.md`](../../src/claude/rules/path_scoped/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/sh/claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Caught always-on context at about 3,887 tokens, over the budget |
| [`src/sh/git/git_validate_branch_name.sh`](../../src/sh/git/git_validate_branch_name.sh) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Forced 2 branch renames before push |
| [`src/sh/git/git_validate_pr_description.sh`](../../src/sh/git/git_validate_pr_description.sh) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught leftover evaluation-criteria placeholders in 5 sessions |
| [`tests/`](../../tests/) | [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught structure problems in the rules and helpers |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`.github/pull_request_template.md`](../../.github/pull_request_template.md) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR) | Hindered | The user complained of "huge streams" of bullets in Additional Details, and its layout needed repeated fixes |
| [`.github/workflows/pip_audit.yml`](../../.github/workflows/pip_audit.yml) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR) | Unused | No scan output in any transcript |
| [`maintenance/test_maintenance.md`](../test_maintenance.md) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR) | Unused | Only mentioned inside audit output |
| [`src/claude/hooks/hook_enforcement_done_checks.sh`](../../src/claude/hooks/hook_enforcement_done_checks.sh) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR) | Unused | Never fired in any transcript |
| [`src/claude/rules/on_demand/`](../../src/claude/rules/on_demand/) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR) | Unused | Its rules and style guides were edited, but never read to guide work |
| [`src/claude/rules/path_scoped/`](../../src/claude/rules/path_scoped/) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR) | Unused | Loaded, but never shown changing behaviour |
| [`src/sh/claude_install_config.sh`](../../src/sh/claude_install_config.sh) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR) | Hindered | Hook registration drifted and needed a fix plan |
| [`src/sh/claude_report_context_cost.sh`](../../src/sh/claude_report_context_cost.sh) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR) | Hindered | "Out of date" failures in 8 or more sessions, from before [#256](https://github.com/paulf-999/ai-engineering-playbook/pull/256) made the hook rewrite the report, so not yet confirmed |
| [`src/sh/git/git_validate_branch_name.sh`](../../src/sh/git/git_validate_branch_name.sh) | [RUN_PR](https://github.com/paulf-999/ai-engineering-playbook/pull/RUN_PR) | Mixed | Blocked commits to `main`, but failed falsely on a detached HEAD, in sessions from before [#259](https://github.com/paulf-999/ai-engineering-playbook/pull/259), so not yet confirmed |
