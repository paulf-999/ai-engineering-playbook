<!-- version: 1.0.21 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-05 -->
# 💰 Context cost

**Purpose:** how many tokens each file in the global Claude config adds, and when it loads, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/`, and a pre-commit check fails if it's out of date, so don't edit the tables by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../target_architecture/target_architecture.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 📂 **With matching files:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

## 🔒 Every session

| # | File | Tokens |
|---|---|---|
| | **Subtotal** | **~0** |

## 📂 With matching files

| # | File | Globs | Tokens |
|---|---|---|---|
| | **Subtotal** | | **~0** |

## 💤 On demand

| # | File | Tokens |
|---|---|---|
| | **Subtotal** | **~0** |
