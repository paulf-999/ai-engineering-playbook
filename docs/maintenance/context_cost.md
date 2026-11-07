<!-- version: 1.0.25 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-07 -->
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
| | **Subtotal** | **~546** |

## 📂 With matching files

| # | File | Globs | Tokens |
|---|---|---|---|
| | **Subtotal** | | **~0** |

## 💤 On demand

| # | File | Tokens |
|---|---|---|
| 1 | `_templates/README.md` | ~1188 |
| 2 | `_templates/skills/_quality_scorecard_template.md` | ~1258 |
| 3 | `rules/_rules_on_demand/claude_config/authoring_guidelines.md` | ~552 |
| 4 | `rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_agents.md` | ~360 |
| 5 | `rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_rules.md` | ~472 |
| 6 | `rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_skills.md` | ~433 |
| 7 | `rules/_rules_on_demand/claude_config/claude_naming_patterns.md` | ~197 |
| 8 | `rules/_rules_on_demand/claude_config/guiding_principles.md` | ~447 |
| 9 | `rules/_rules_on_demand/claude_config/portable_paths.md` | ~189 |
| 10 | `rules/_rules_on_demand/claude_config/turn_budgets.md` | ~174 |
| | **Subtotal** | **~5272** |
