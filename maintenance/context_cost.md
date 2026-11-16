# 💰 Context cost

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** how many tokens the global Claude config adds to every session, and to the tasks that need more, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/` and prints every file's tokens in the terminal, a pre-commit hook rewrites and stages it when a commit changes `src/claude/`, and CI fails if it's out of date, so don't edit the tables by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../docs/target_architecture/architecture/_budget_and_guards.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 📂 **Path-scoped rules:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

## 🔒 Every session

| # | File | Tokens |
|---|---|---|
| 1 | `CLAUDE.md` | ~520 |
| 2 | `rules/always_on/conduct/behaviour.md` | ~320 |
| 3 | `rules/always_on/conduct/security.md` | ~202 |
| 4 | `rules/always_on/conduct/writing_style.md` | ~310 |
| 5 | `rules/always_on/standards/claude_response_standards.md` | ~217 |
| 6 | `rules/always_on/standards/naming_standards.md` | ~246 |
| 7 | `rules/always_on/workflows/sdlc_workflow.md` | ~288 |
| | **Subtotal** | **~2106** |

## 💤 Only when needed

| Load type | Files | Tokens |
|---|---|---|
| 📂 Path-scoped rules, with matching files | 12 | ~4400 |
| 💤 On demand, via a pointer | 52 | ~29300 |
