# 🤖 tests/src/claude

**Purpose:** what each test of the Claude config in `src/claude/` checks.

| Test | What it checks |
|---|---|
| ✅ [hooks/ai_sdlc_workflow/test_hook_enforcement_done_checks.py](hooks/ai_sdlc_workflow/test_hook_enforcement_done_checks.py) | The done checks hook stops Claude once to run the repo's checks after files change |
| 🗂️ [hooks/ai_sdlc_workflow/test_hook_enforcement_plan_sections.py](hooks/ai_sdlc_workflow/test_hook_enforcement_plan_sections.py) | The plan sections hook blocks a plan that has no Intent or Spec heading |
| 🔍 [hooks/ai_sdlc_workflow/test_hook_enforcement_plan_review.py](hooks/ai_sdlc_workflow/test_hook_enforcement_plan_review.py) | The plan review hook blocks a long plan scored under 10/10, passes it with the findings after 2 blocks, gives the next plan its own 2, lets a plan through when the reviewer fails, and tells the user and logs each outcome |
| 🌳 [hooks/git/test_hook_enforcement_worktree_edits.py](hooks/git/test_hook_enforcement_worktree_edits.py) | The worktree edits hook blocks a session's first edit in a repo's main folder once, and never one in a worktree |
| 🔁 [hooks/claude_kaizen/test_hook_reminder_kaizen_due.py](hooks/claude_kaizen/test_hook_reminder_kaizen_due.py) | The kaizen reminder hook stays silent below 5 new feedback notes, counts only notes since the last run, and logs each nudge |
| 📐 [test_rules_structure.py](test_rules_structure.py) | Every rule file under `src/claude/rules/` meets the rule template's structural gates |
| 🔎 [test_git_review_pr_comment_lookup.py](skills/_git_skills/git-review-pr/test_git_review_pr_comment_lookup.py) | `git-review-pr` finds the user's own earlier review of the same PR, in the current or older comment format, and no other comment |
| 🔐 [test_git_review_pr_secret_check.py](skills/_git_skills/git-review-pr/test_git_review_pr_secret_check.py) | `git-review-pr`'s secret check flags known secret shapes by line number only, and passes ordinary review text |
