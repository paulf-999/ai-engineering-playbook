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
| 2 | `agents/core/code-reviewer/AGENT.md` (description) | ~42 |
| 3 | `agents/core/technical-writer/AGENT.md` (description) | ~37 |
| 4 | `rules/always_on/01_standards/ai_sdlc_workflow.md` | ~256 |
| 5 | `rules/always_on/01_standards/behaviour.md` | ~371 |
| 6 | `rules/always_on/01_standards/house_style_team_conventions.md` | ~87 |
| 7 | `rules/always_on/01_standards/naming_standards.md` | ~256 |
| 8 | `rules/always_on/01_standards/security.md` | ~224 |
| 9 | `rules/always_on/01_standards/writing_style.md` | ~255 |
| 10 | `skills/_atlassian_skills/confluence-create-page/SKILL.md` (description) | ~52 |
| 11 | `skills/_atlassian_skills/jira-create-issue/SKILL.md` (description) | ~44 |
| 12 | `skills/_git_skills/git-create-pr/SKILL.md` (description) | ~36 |
| 13 | `skills/_git_skills/git-review-pr/SKILL.md` (description) | ~43 |
| | **Subtotal** | **~2232** |

## 👤 Every session, if opted in

| # | File | Tokens |
|---|---|---|
| 1 | `rules/always_on/02_preferences/claude_output_format.md` | ~294 |
| 2 | `rules/always_on/02_preferences/claude_working_files.md` | ~264 |
| | **Subtotal** | **~558** |

## 💤 Only when needed

| Load type | Files | Tokens |
|---|---|---|
| 📂 Path-scoped rules, with matching files | 22 | ~8900 |
| 💤 On demand, via a pointer | 76 | ~45100 |
