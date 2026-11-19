# 🪝 hooks

**Purpose:** scripts Claude Code runs at set points in a session, to enforce what a rule alone can't.

| File | Rule | What it does |
|---|---|---|
| ✅ [`hook_enforcement_done_checks.sh`](hook_enforcement_done_checks.sh) | [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md) | Enforces the Feedback loop step in [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md): when Claude stops after editing tracked files that are still changed, sends it back once to run the checks the repo's `CLAUDE.md` says define done |
| 📋 [`hook_enforcement_plan_sections.sh`](hook_enforcement_plan_sections.sh) | [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md) | Enforces the Intent and Spec steps in [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md): before Claude exits plan mode, blocks a plan of 15 or more lines that has no Intent or Spec heading |
| 🔁 [`hook_reminder_kaizen_due.sh`](hook_reminder_kaizen_due.sh) | [`/claude-kaizen`](../skills/_claude_skills/claude-kaizen/SKILL.md) | On a trial: at session start, stays silent until 5 feedback notes are new since the last `/claude-kaizen` run, then suggests a run and logs the nudge to `kaizen_nudges.log` in the project's memory folder |
| 🌳 [`hook_enforcement_worktree_edits.sh`](hook_enforcement_worktree_edits.sh) | [`git.md`](../rules/on_demand/01_standards/git.md) | Enforces the Worktrees bullet in [`git.md`](../rules/on_demand/01_standards/git.md): blocks a session's first edit in a repo's main folder once, so Claude moves into its own worktree when another session may share it |
