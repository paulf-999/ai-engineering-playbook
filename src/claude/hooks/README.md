# 🪝 hooks

**Purpose:** scripts Claude Code runs at set points in a session, to enforce what a rule alone can't.

| File | Rule | What it does |
|---|---|---|
| ✅ [`hook_enforcement_done_checks.sh`](hook_enforcement_done_checks.sh) | [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md) | Enforces the Feedback loop step in [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md): when Claude stops after changing tracked files, sends it back once to run the checks the repo's `CLAUDE.md` says define done |
| 📋 [`hook_enforcement_plan_sections.sh`](hook_enforcement_plan_sections.sh) | [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md) | Enforces the Intent and Spec steps in [`ai_sdlc_workflow.md`](../rules/always_on/01_standards/ai_sdlc_workflow.md): before Claude exits plan mode, blocks a plan of 15 or more lines that has no Intent or Spec heading |
| 🌳 [`hook_enforcement_worktree_edits.sh`](hook_enforcement_worktree_edits.sh) | [`git.md`](../rules/on_demand/01_standards/git.md) | Enforces the Worktrees bullet in [`git.md`](../rules/on_demand/01_standards/git.md): blocks a session's first edit in a repo's main folder once, so Claude moves into its own worktree when another session may share it |
