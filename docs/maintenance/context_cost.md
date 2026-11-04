<!-- version: 1.0.7 -->
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
| 1 | `CLAUDE.md` | ~542 |
| 2 | `rules/01_essentials/claude_response_standards.md` | ~218 |
| 3 | `rules/01_essentials/naming_standards.md` | ~194 |
| 4 | `rules/01_essentials/writing_style.md` | ~305 |
| 5 | `rules/02_claude_standards/behaviour.md` | ~390 |
| 6 | `rules/02_claude_standards/claude_plans.md` | ~157 |
| 7 | `rules/02_claude_standards/git.md` | ~325 |
| 8 | `rules/02_claude_standards/security.md` | ~201 |
| | **Subtotal** | **~2334** |

## 📂 With matching files

| # | File | Globs | Tokens |
|---|---|---|---|
| 1 | `rules/02_claude_standards/path_scoped_rules/code_security.md` | `**/*.py`, `**/*.sh`, `**/*.sql`, `**/*.js`, `**/*.ts` | ~195 |
| | **Subtotal** | | **~195** |

## 💤 On demand

| # | File | Tokens |
|---|---|---|
| 1 | `rules/_rules_on_demand/authoring_guidelines.md` | ~264 |
| 2 | `rules/_rules_on_demand/claude_naming_patterns.md` | ~199 |
| 3 | `rules/_rules_on_demand/guiding_principles.md` | ~436 |
| 4 | `rules/_rules_on_demand/permission_recommendations.md` | ~154 |
| 5 | `rules/_rules_on_demand/portable_paths.md` | ~189 |
| 6 | `rules/_rules_on_demand/saving_plans.md` | ~169 |
| 7 | `rules/_rules_on_demand/todo_logging.md` | ~141 |
| 8 | `rules/_rules_on_demand/turn_budgets.md` | ~174 |
| 9 | `rules/_rules_on_demand/writing_style/_audience_and_depth.md` | ~324 |
| 10 | `rules/_rules_on_demand/writing_style/_drafts_and_errors.md` | ~199 |
| 11 | `rules/_rules_on_demand/writing_style/_markdown_layout.md` | ~264 |
| | **Subtotal** | **~2517** |
