# 💰 Context cost

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** how many tokens the global Claude config adds to every session, and to the tasks that need more, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/` and prints every file's tokens in the terminal, a pre-commit hook rewrites and stages it when a commit changes `src/claude/`, and CI fails if it's out of date, so don't edit the tables by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../docs/target_architecture/architecture/_budget_and_guards.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 👤 **Every session, unless opted out:** preferences, which load in every session unless `make install PREFERENCES=0` leaves them out, and never in a one-repo install. The budget check always counts them, the worst case.
- 📂 **Path-scoped rules:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

## 🔒 Every session

| # | File | Tokens |
|---|---|---|
| 1 | `CLAUDE.md` | ~523 |
| 2 | `agents/core/code-reviewer/AGENT.md` (description) | ~43 |
| 3 | `agents/core/technical-writer/AGENT.md` (description) | ~27 |
| 4 | `rules/always_on/01_standards/ai_sdlc_workflow.md` | ~349 |
| 5 | `rules/always_on/01_standards/behaviour.md` | ~343 |
| 6 | `rules/always_on/01_standards/house_style_team_conventions.md` | ~80 |
| 7 | `rules/always_on/01_standards/naming_standards.md` | ~210 |
| 8 | `rules/always_on/01_standards/security.md` | ~211 |
| 9 | `rules/always_on/01_standards/writing_style.md` | ~246 |
| 10 | `skills/_atlassian_skills/confluence-create-page/SKILL.md` (description) | ~44 |
| 11 | `skills/_atlassian_skills/jira-create-issue/SKILL.md` (description) | ~34 |
| 12 | `skills/_claude_skills/claude-capture-session-prompts/SKILL.md` (description) | ~39 |
| 13 | `skills/_claude_skills/claude-kaizen/SKILL.md` (description) | ~0 |
| 14 | `skills/_git_skills/git-create-pr/SKILL.md` (description) | ~29 |
| 15 | `skills/_git_skills/git-review-pr/SKILL.md` (description) | ~37 |
| | **Subtotal** | **~2221** |

## 👤 Every session, unless opted out

| # | File | Tokens |
|---|---|---|
| 1 | `rules/always_on/02_preferences/claude_output_format.md` | ~246 |
| 2 | `rules/always_on/02_preferences/claude_working_files.md` | ~224 |
| | **Subtotal** | **~470** |

## 💤 Only when needed

| Load type | Files | Tokens |
|---|---|---|
| 📂 Path-scoped rules, with matching files | 26 | ~12000 |
| 💤 On demand, via a pointer | 84 | ~49400 |
