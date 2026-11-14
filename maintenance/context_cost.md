# 💰 Context cost

**Purpose:** how many tokens the global Claude config adds to every session, and to the tasks that need more, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/` and prints every file's tokens in the terminal, and a pre-commit check fails if it's out of date, so don't edit the tables by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../docs/target_architecture/README.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 📂 **Path-scoped rules:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

## 🔒 Every session

| # | File | Tokens |
|---|---|---|
| 1 | `CLAUDE.md` | ~534 |
| 2 | `rules/always/conduct/behaviour.md` | ~311 |
| 3 | `rules/always/conduct/security.md` | ~203 |
| 4 | `rules/always/conduct/writing_style.md` | ~310 |
| 5 | `rules/always/standards/claude_response_standards.md` | ~218 |
| 6 | `rules/always/standards/naming_standards.md` | ~247 |
| 7 | `rules/always/workflows/sdlc_workflow.md` | ~404 |
| | **Subtotal** | **~2229** |

## 💤 Only when needed

| Load type | Files | Tokens |
|---|---|---|
| 📂 Path-scoped rules, with matching files | 12 | ~3700 |
| 💤 On demand, via a pointer | 80 | ~41600 |
