<!-- version: 1.0.3 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-04 -->
# 💰 Context cost

**Purpose:** how many tokens each file in the global Claude config adds, and when it loads, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/`, and a pre-commit check fails if it's out of date, so don't edit the table by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../target_architecture/target_architecture.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 📂 **With matching files:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

| File | Loads | Tokens |
|---|---|---|
| `CLAUDE.md` | Every session | ~598 |
| `rules/01_essentials/claude_response_standards.md` | Every session | ~218 |
| `rules/01_essentials/claude_usage_standards/naming_standards.md` | Every session | ~194 |
| `rules/01_essentials/claude_usage_standards/writing_style.md` | Every session | ~305 |
| `rules/02_claude_standards/behaviour.md` | Every session | ~323 |
| `rules/02_claude_standards/git.md` | Every session | ~325 |
| `rules/02_claude_standards/path_scoped_rules/code_security.md` | With matching files: `**/*.py`, `**/*.sh`, `**/*.sql`, `**/*.js`, `**/*.ts` | ~195 |
| `rules/02_claude_standards/security.md` | Every session | ~201 |
| `rules/_rules_lazy_load/claude_naming_patterns.md` | On demand, via a pointer | ~199 |
| `rules/_rules_lazy_load/guiding_principles.md` | On demand, via a pointer | ~333 |
| `rules/_rules_lazy_load/permission_recommendations.md` | On demand, via a pointer | ~154 |
| `rules/_rules_lazy_load/writing_style/_audience_and_depth.md` | On demand, via a pointer | ~324 |
| `rules/_rules_lazy_load/writing_style/_drafts_and_errors.md` | On demand, via a pointer | ~199 |
| `rules/_rules_lazy_load/writing_style/_markdown_layout.md` | On demand, via a pointer | ~264 |
| **Every-session total** | | **~2165** |
