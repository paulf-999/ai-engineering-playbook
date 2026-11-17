# 💰 Context cost

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** how many tokens the global Claude config adds to every session, and to the tasks that need more, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/` and prints every file's tokens in the terminal, a pre-commit hook rewrites and stages it when a commit changes `src/claude/`, and CI fails if it's out of date, so don't edit the tables by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../docs/target_architecture/architecture/_budget_and_guards.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 👤 **Every session, if opted in:** preferences, which load in every session only after `make install PREFERENCES=1`. They count towards the budget only for those users, but the budget check always counts them, the worst case.
- 📂 **Path-scoped rules:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

## 🔒 Every session

| # | File | Tokens |
|---|---|---|
| 1 | `CLAUDE.md` | ~523 |
| 2 | `rules/always_on/01_standards/conduct/behaviour.md` | ~334 |
| 3 | `rules/always_on/01_standards/conduct/security.md` | ~205 |
| 4 | `rules/always_on/01_standards/conduct/writing_style.md` | ~233 |
| 5 | `rules/always_on/01_standards/naming_standards.md` | ~228 |
| 6 | `rules/always_on/01_standards/workflows/sdlc_workflow.md` | ~256 |
| 7 | `rules/always_on/02_team_conventions/house_style.md` | ~87 |
| | **Subtotal** | **~1868** |

## 👤 Every session, if opted in

| # | File | Tokens |
|---|---|---|
| 1 | `rules/always_on/03_preferences/claude_output_format.md` | ~277 |
| 2 | `rules/always_on/03_preferences/working_files.md` | ~204 |
| | **Subtotal** | **~482** |

## 💤 Only when needed

| Load type | Files | Tokens |
|---|---|---|
| 📂 Path-scoped rules, with matching files | 22 | ~8400 |
| 💤 On demand, via a pointer | 59 | ~28900 |
