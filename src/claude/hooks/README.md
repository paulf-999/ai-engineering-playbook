# 🪝 hooks

**Purpose:** scripts Claude Code runs at set points in a session, to enforce what a rule alone can't.

| File | Rule | What it does |
|---|---|---|
| ✅ [`hook_enforcement_done_checks.sh`](ai_sdlc_workflow/hook_enforcement_done_checks.sh) | [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md) | Enforces the Feedback loop step in [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md): when Claude stops after editing tracked files that are still changed, sends it back once to run the checks the repo's `CLAUDE.md` says define done, unless it already ran one of them after its last edit |
| 📋 [`hook_enforcement_plan_sections.sh`](ai_sdlc_workflow/hook_enforcement_plan_sections.sh) | [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md) | Enforces the Intent and Spec steps in [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md): before Claude exits plan mode, blocks a long plan that has no Intent or Spec heading, and says the Executive summary comes first |
| 🔍 [`hook_enforcement_plan_review.sh`](ai_sdlc_workflow/hook_enforcement_plan_review.sh) | [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md) | Checks the plan layout in [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md): before Claude exits plan mode, has a cold `claude -p --safe-mode` reviewer score a long plan's Intent, Spec, Plan, writing style and decisions, which the Executive summary lists, and blocks below 10/10 for up to 2 rounds per plan, sending Claude to ask you about decisions findings, then passes the findings on for you. It lets a plan through if the reviewer fails or takes over 60 seconds, shows a status message while it runs, then each outcome with any scores, in the conversation for a block and in the approval dialog otherwise, and logs each outcome to `plan_reviews.log` in the project's memory folder |
| 🔁 [`hook_reminder_kaizen_due.sh`](claude_kaizen/hook_reminder_kaizen_due.sh) | [`/claude-kaizen`](../skills/_claude_skills/claude-kaizen/SKILL.md) | On a trial: in a fresh session in a repo with rule evals, stays silent until enough feedback notes are new since the last `/claude-kaizen` run, then once a day has Claude draft rules after the first task, and logs the nudge to `_claude_kaizen/nudges.log` in the Claude config directory |
| 🌳 [`hook_enforcement_worktree_edits.sh`](git/hook_enforcement_worktree_edits.sh) | [`git.md`](../rules/on_demand/01_standards/git.md) | Enforces the Worktrees bullet in [`git.md`](../rules/on_demand/01_standards/git.md): blocks a session's first edit in a repo's main folder once, so Claude moves into its own worktree when another session may share it |

## 🤖 Why the plan review isn't an agent

The plan review stays a hook, with no dedicated agent, for these reasons:

- 🪝 **Always fires:** the hook runs on every long plan, whereas an agent runs only when Claude calls it.
- 🙈 **Blind:** the hook fixes the reviewer's prompt, whereas Claude writes an agent's brief and can prime it.
- 👯 **One rubric:** an agent would still need the hook to block and log, giving the rubric two homes.
- 🔄 **Revisit if:** on-demand reviews, or reviewers that read the repo, are wanted.
