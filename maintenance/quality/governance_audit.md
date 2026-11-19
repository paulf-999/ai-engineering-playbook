# 🏛️ Governance audit

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest verdict on each guard, recurring review and test file: the problem it prevents, the evidence that it fired or helped, and whether to keep, slim or drop it.

An external review asked whether each guard prevents a real problem, or only adds process. This run, on 2026-11-18 against `main` at `3f966a8`, gathered each item's evidence from the CI run history and a search of 132 session transcripts. A transcript count is the number of sessions holding the guard's failure message, so the figures are approximate. The tests were added on 2026-11-19 from a search of 152 transcripts. Earlier runs are in git history.

## ⚖️ Verdicts

| Verdict | Items |
|---|---|
| ✅ **Keep** | 23 |
| 🔒 **Keep (decided)** | 8 |
| ✂️ **Slim** | 2 |
| 🗑️ **Drop** | 1 |

"Keep (decided)" marks an item the maintainer has already chosen to keep, so this audit records its evidence without re-proposing it.

## 🛡️ Guards

| # | Guard | Problem it prevents | Evidence it fired or helped | Verdict |
|---|---|---|---|---|
| 1 | 💰 [Always-on budget](../../src/sh/claude_validate_always_on_budget.sh), 3,000 tokens | Context bloat in every session | Caught one overrun at about 3,887 tokens, and now reads about 2,244 | ✅ Keep |
| 2 | 📏 [Rule size](../../tests/src/claude/test_rules_structure.py), 110 lines | Rules too long to read in one go | Failed in 2 sessions, each followed by a split | ✅ Keep |
| 3 | 📦 [PR size](../../src/sh/git/git_validate_num_file_changes.sh) | PRs too big to review | 3 CI failures, each moved onto a `release/` branch | 🔒 Keep (decided) |
| 4 | 🌿 [Branch name](../../src/sh/git/git_validate_branch_name.sh), in CI and pre-commit | Branches that break the naming rules | Caught bad prefixes in 6 sessions, with 1 false fire on a detached HEAD | 🔒 Keep (decided) |
| 5 | 🏷️ PR title and commitlint | Messages that aren't Conventional Commits | Caught bad commit messages in 4 sessions, with 1 false fire in CI on a Dependabot PR | 🔒 Keep (decided) |
| 6 | 📝 [PR description](../../src/sh/git/git_validate_pr_description.sh) | PR bodies missing sections or with bad links | 4 CI failures, each fixed before merge | 🔒 Keep (decided) |
| 7 | 💸 [Context-cost table](../../src/sh/claude_report_context_cost.sh) | A stale token report | The most frequent failure: 3 of the 14 CI failures, and 14 sessions locally | 🔒 Keep (decided) |
| 8 | 🔐 [pip-audit](../../.github/workflows/pip_audit.yml), weekly | Known vulnerabilities in dependencies | Never fired, and costs nothing to run | ✅ Keep |

## 🪝 Hooks

| # | Hook | Problem it prevents | Evidence it fired or helped | Verdict |
|---|---|---|---|---|
| 9 | 📋 [Plan sections](../../src/claude/hooks/hook_enforcement_plan_sections.sh) | Plans with no Intent or Spec | Blocked plans in 29 sessions | 🔒 Keep (decided) |
| 10 | ✅ [Done checks](../../src/claude/hooks/hook_enforcement_done_checks.sh) | Finishing without running the repo's checks | Fired in 15 sessions, though `CLAUDE.md` alone had Claude run the tests in 42. It also fired on another session's uncommitted changes | ✂️ Slim: now fires only for changed files the session itself edited |
| 11 | 🌳 [Worktree edits](../../src/claude/hooks/hook_enforcement_worktree_edits.sh) | Two sessions editing the same working tree | Fired in 7 sessions on its first day, and a session that day found another session's changes on `main` | ✅ Keep, too new to judge |

## 🔁 Recurring reviews and measures

| # | Item | Problem it prevents | Evidence it fired or helped | Verdict |
|---|---|---|---|---|
| 12 | 🗓️ [Review every 20 tasks or 4 weeks](../../docs/target_architecture/design_principles/01_principles.md#-numbers-and-tests) | Parts that don't pay building up | The repo is 18 days old and has had 6 reviews, so the cadence hasn't yet applied | ✅ Keep |
| 13 | 🔪 Halving test | A setup bigger than it needs to be | Never recorded as run, and the [outcome runs](../../docs/examples/dbt/dbt_outcomes_measured.md) now measure part of it | 🗑️ Drop: removed from the principles and measures |
| 14 | 🚩 [Two sessions, not one](../../docs/target_architecture/design_principles/01_principles.md#-numbers-and-tests) | Cutting a part on one bad session | Never applied, and the maintainer has overruled its "or if it's unused" half | ✂️ Slim: retire a part only when two sessions show it got in the way |
| 15 | 📏 [Component feedback and tokens](../../docs/target_architecture/architecture/_measures.md) | Reviews with no evidence | Recorded in the [quality audit](quality_audit.md#-component-feedback), and the source of most of this page's evidence | ✅ Keep |
| 16 | 📄 `ai_sdlc_workflow.md` and `CLAUDE.md` | Not assessed | Not assessed | 🔒 Keep (decided) |

## 🧪 Tests

Each test file is judged against the [keep or delete criteria](../../tests/README.md#-which-tests-to-keep). The count is the number of sessions where one of its tests failed, and a count of 0 is no reason to drop a test that guards a core promise.

| # | Test file | What it protects | Tests | Sessions failed | Verdict |
|---|---|---|---|---|---|
| 17 | 📐 [Rules structure](../../tests/src/claude/test_rules_structure.py) | Rule size, pointers and folder placement | 19 | 11 | ✅ Keep |
| 18 | 📦 [Install config](../../tests/src/sh/test_claude_install_config.py) | Install, upgrade, uninstall, backups and preferences | 28 | 9 | ✅ Keep |
| 19 | ✅ [Done checks hook](../../tests/src/claude/test_hook_enforcement_done_checks.py) | Stopping once to run the repo's checks | 9 | 1 | ✅ Keep |
| 20 | 📋 [Plan sections hook](../../tests/src/claude/test_hook_enforcement_plan_sections.py) | Blocking plans with no Intent or Spec | 5 | 0 | ✅ Keep |
| 21 | 🌳 [Worktree edits hook](../../tests/src/claude/test_hook_enforcement_worktree_edits.py) | Blocking a first edit in the main folder | 7 | 0 | ✅ Keep |
| 22 | 💸 [Context-cost report](../../tests/src/sh/test_claude_report_context_cost.py) | An accurate token report | 5 | 1 | 🔒 Keep (decided) |
| 23 | 💰 [Always-on budget](../../tests/src/sh/test_claude_validate_always_on_budget.py) | The 3,000-token cap and what counts towards it | 5 | 1 | ✅ Keep |
| 24 | 🧱 [Script structure](../../tests/src/sh/test_script_structure.py) | Every script follows the bash template | 3 | 1 | ✅ Keep |
| 25 | 🧰 [Shell utils](../../tests/src/sh/test_shell_utils.py) | The shared shell helpers, tested once | 4 | 0 | ✅ Keep |
| 26 | 🌿 [Branch name](../../tests/src/sh/git/test_git_validate_branch_name.py) | Valid and invalid names, and a detached HEAD | 4 | 0 | ✅ Keep |
| 27 | 📏 [PR file count](../../tests/src/sh/git/test_git_validate_num_file_changes.py) | Both sides of the file limit, and the `release/` skip | 7 | 0 | ✅ Keep |
| 28 | 📝 [PR description](../../tests/src/sh/git/test_git_validate_pr_description.py) | Required sections, and no shell execution of the body | 5 | 0 | ✅ Keep |
| 29 | 🎯 [Trigger evals runner](../../tests/src/py/test_claude_run_trigger_evals.py) | Scenario selection, config copy and grading | 5 | 0 | ✅ Keep |
| 30 | 🧠 [Behaviour evals runner](../../tests/src/py/test_claude_run_behaviour_evals.py) | Scenario selection, scratch repo setup and transcripts | 7 | 0 | ✅ Keep |
| 31 | ⚖️ [Rule evals runner](../../tests/src/py/test_claude_run_rule_evals.py) | Case loading, repo preparation and the verdict margin | 3 | 0 | ✅ Keep |
| 32 | 🔐 [Review PR secret check](../../tests/src/claude/skills/_git_skills/git-review-pr/test_git_review_pr_secret_check.py) | Catching secrets without echoing them | 3 | 0 | ✅ Keep |
| 33 | 🗒️ [Capture session prompts](../../tests/src/claude/skills/_claude_skills/claude-capture-session-prompts/test_capture_session_prompts.py) | One date's prompts, masked secrets, no overwrite | 4 | 0 | ✅ Keep |
| 34 | 🛠️ [Makefile](../../tests/test_makefile.py) | `make deps` installs only into a virtualenv | 2 | 0 | ✅ Keep |

## 🎯 Findings for the team

Points this run raised outside the guards, for the team to decide rather than to cut:

1. 📸 **The snapshot convention scored lowest:** in the blind review of the [outcome runs](../../docs/examples/dbt/dbt_outcomes_measured.md), all 3 reviewers gave the snapshot built to the [team's convention](../../src/claude/rules/path_scoped/style_guides/dbt_team_conventions.md#-snapshots) 2 out of 5. They called the extra `dim_` model, the `check` strategy and the `WAREHOUSE` schema over-built. The reviewers didn't know the team's reasons, so the convention is left unchanged.
