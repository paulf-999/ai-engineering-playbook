# 🪝 hooks

**Purpose:** scripts Claude Code runs at set points in a session, to enforce what a rule alone can't.

| File | What it does |
|---|---|
| ✅ [`hook_enforcement_done_checks.sh`](hook_enforcement_done_checks.sh) | When Claude stops after changing tracked files, sends it back once to run the checks the repo's `CLAUDE.md` says define done |
| 📋 [`hook_enforcement_plan_sections.sh`](hook_enforcement_plan_sections.sh) | Before Claude exits plan mode, blocks a plan of 15 or more lines that has no Intent or Spec heading |
