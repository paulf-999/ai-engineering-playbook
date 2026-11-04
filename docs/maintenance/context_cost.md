<!-- version: 1.0.9 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-04 -->
# 💰 Context cost

**Purpose:** how many tokens each file in the global Claude config adds, and when it loads, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/`, and a pre-commit check fails if it's out of date, so don't edit the tables by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../target_architecture/target_architecture.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 📂 **With matching files:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

## 🔒 Every session

| # | File | Tokens |
|---|---|---|
| 1 | `CLAUDE.md` | ~546 |
| 2 | `rules/01_ways_of_working/behaviour.md` | ~396 |
| 3 | `rules/01_ways_of_working/claude_plans.md` | ~162 |
| 4 | `rules/01_ways_of_working/git.md` | ~325 |
| 5 | `rules/01_ways_of_working/security.md` | ~204 |
| 6 | `rules/02_communication/claude_response_standards.md` | ~218 |
| 7 | `rules/02_communication/naming_standards.md` | ~197 |
| 8 | `rules/02_communication/writing_style.md` | ~318 |
| | **Subtotal** | **~2368** |

## 📂 With matching files

| # | File | Globs | Tokens |
|---|---|---|---|
| 1 | `rules/_path_scoped_rules/code_security.md` | `**/*.py`, `**/*.sh`, `**/*.sql`, `**/*.js`, `**/*.ts` | ~195 |
| | **Subtotal** | | **~195** |

## 💤 On demand

| # | File | Tokens |
|---|---|---|
| 1 | `rules/_rules_on_demand/01_ways_of_working/saving_plans.md` | ~169 |
| 2 | `rules/_rules_on_demand/01_ways_of_working/todo_logging.md` | ~141 |
| 3 | `rules/_rules_on_demand/02_communication/writing_style/_audience_and_depth.md` | ~324 |
| 4 | `rules/_rules_on_demand/02_communication/writing_style/_drafts_and_errors.md` | ~199 |
| 5 | `rules/_rules_on_demand/02_communication/writing_style/_markdown_layout.md` | ~264 |
| 6 | `rules/_rules_on_demand/claude_config/authoring_guidelines.md` | ~268 |
| 7 | `rules/_rules_on_demand/claude_config/claude_naming_patterns.md` | ~199 |
| 8 | `rules/_rules_on_demand/claude_config/guiding_principles.md` | ~447 |
| 9 | `rules/_rules_on_demand/claude_config/permission_recommendations.md` | ~154 |
| 10 | `rules/_rules_on_demand/claude_config/portable_paths.md` | ~189 |
| 11 | `rules/_rules_on_demand/claude_config/turn_budgets.md` | ~174 |
| | **Subtotal** | **~2531** |
