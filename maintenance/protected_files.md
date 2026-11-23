# 🛡️ Protected files

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the files, checks and processes this repo keeps on purpose, so reviews and trims leave them alone even when a reviewer proposes cutting them.

- 🚫 **Declined, not acted on:** when a review proposes cutting an item here, record the finding as declined and link this page.
- 🔀 **Changing the list:** add or remove an item by PR, like any other change.

## 🔒 Never trimmed

Their content stays as it is, so bloat and always-on trims come from other files.

| File | Why it's protected |
|---|---|
| [`README.md`](../README.md) | It's the entry page for cold, non-technical readers, so a rewrite keeps its size |
| [`CLAUDE.md`](../CLAUDE.md) and [`src/claude/CLAUDE.md`](../src/claude/CLAUDE.md) | Always-on trims come from `rules/always_on/` instead |
| [`ai_sdlc_workflow.md`](../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) | It's the team's workflow for a change, from Intent to Review |
| [`01_principles.md`](../docs/target_architecture/design_principles/01_principles.md) | It sets the principles the rest of the repo is built on |
| [`_budget_and_guards.md`](../docs/target_architecture/architecture/_budget_and_guards.md) | It describes the always-on budget and the guards that enforce it |
| Each skill's `skill.contract.yaml` and [its template](../src/claude/_templates/skills/skill.contract.yaml.template), with every field | It sets the skill's scope, written before its `SKILL.md`, and its fields are kept for future use |

## 🧰 Never removed

These can be slimmed, but not removed or made opt-in.

| Item | Why it's protected |
|---|---|
| The 4 git checks: [branch name](../src/sh/git/git_validate_branch_name.sh), [PR size](../src/sh/git/git_validate_num_file_changes.sh), [PR description](../src/sh/git/git_validate_pr_description.sh) and the PR title check in [`ci.yml`](../.github/workflows/ci.yml) | The team already knows this git process |
| [`hook_enforcement_plan_sections.sh`](../src/claude/hooks/hook_enforcement_plan_sections.sh) | It stays on for every engineer, not opt-in |
| [`hook_enforcement_plan_review.sh`](../src/claude/hooks/hook_enforcement_plan_review.sh) | It stays on for every engineer, not opt-in |
| [`context_cost.md`](context_cost.md), with its script, test, pre-commit check and `make context_cost` | The per-file token table stays current |
| [`src/claude/_templates/`](../src/claude/_templates/) | The skill and agent templates are kept for porting |
| [`src/sh/shell_utils.sh`](../src/sh/shell_utils.sh) and its copies in [`_templates/utils/`](../src/claude/_templates/utils/) | They're kept as separate copies by choice |
| [`docs/target_architecture/architecture/`](../docs/target_architecture/architecture/) | The child pages split the design for the maintainer's reading |
| [`style_guides/`](../src/claude/rules/on_demand/style_guides/) | A heavy guide is slimmed rather than deleted |
| The [repo audit](quality/quality_audit.md), the [quality rubrics](quality/quality_rubrics.md) and the persona review | They're how the repo checks itself |
| The README evals in [`claude_run_readme_evals.py`](../src/py/claude_run_readme_evals.py), with its test and `make evals README=1` | They score the README with cold new and experienced readers, beside the persona review |
| The `ALWAYS_ON_TOKEN_BUDGET` and `MAX_FILES_ALLOWED` overrides | The tests use them |
| The further-reading list in [`reference_material/README.md`](../docs/target_architecture/reference_material/README.md) | It's kept as a reading list |
| The `*_team_conventions.md` files beside their guides in [`rules/`](../src/claude/rules/) | The split is the team's chosen layout |
| [`agents/core/`](../src/claude/agents/core/) | It follows the `agents/<group>/` naming pattern |
| The `01_standards/` and `02_preferences/` kind folders in `always_on/` and `on_demand/`, and `01_standards/` in `path_scoped/` | `test_rules_structure.py` checks every rule sits in one |
| [`style_guides/jira/`](../src/claude/rules/on_demand/style_guides/jira/) | It follows the guide-plus-children layout of the other style guides |
| The model grader in [`claude_run_behaviour_evals.py`](../src/py/claude_run_behaviour_evals.py) | Most behaviour assertions judge meaning, and `must_match` already covers literal patterns |
| `kaizen_nudges.log`, written by [`hook_reminder_kaizen_due.sh`](../src/claude/hooks/hook_reminder_kaizen_due.sh) | It's the kaizen trial's evidence until the trial ends on 2026-12-03 |

## ℹ️ Unused isn't a reason to cut

A `src/claude/` component that transcripts show going unused stays, since the repo holds the intended setup, not one project's usage.
