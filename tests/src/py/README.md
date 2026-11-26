# 🐍 tests/src/py

**Purpose:** what each test of the Python scripts in `src/py/` checks.

| Test | What it checks |
|---|---|
| 🏛️ [test_claude_run_architecture_review.py](test_claude_run_architecture_review.py) | The architecture review runner clones a repo without its untracked files, copies a folder without `.env` files or followed symlinks, or a single file, keeps the other readers when one fails, briefs each lens with only the scratch path, splits and resolves each cited file, and ranks files by how many readers named them |
| 🧰 [test_claude_evals_common.py](test_claude_evals_common.py) | The shared eval helpers pick the case `CASE` names, copy the skills and agents, build each scratch repo from its setup, render the transcript and capped diff the grader sees, set a permission mode only when asked, reject missing verdicts, and delete only the scratch repo's projects/ folder |
| 🗂️ [test_claude_manage_plans.py](test_claude_manage_plans.py) | The plan manager lists plans by status, files each by its status line, archives scratch plans and drafts at 14 days, and never overwrites |
| 🧪 [test_claude_run_behaviour_evals.py](test_claude_run_behaviour_evals.py) | The behaviour evals runner picks the tagged scenarios, or only the one `CASE` names, resumes the session for a confirm reply, and checks `must_match` patterns |
| 📖 [test_claude_run_readme_evals.py](test_claude_run_readme_evals.py) | The README evals runner briefs each reader with its persona and the README, keeps each persona's readers apart, and passes a persona only at a mean of 7 with no score under 6 |
| ⚖️ [test_claude_run_rule_evals.py](test_claude_run_rule_evals.py) | The rule A/B runner's cases name real rules, its two conditions differ only by the rule, its runs may edit files, the grader sees the diff, failed runs print their reasons, and its verdict needs a lead of a third of the runs |
| 🎯 [test_claude_run_trigger_evals.py](test_claude_run_trigger_evals.py) | The trigger evals runner picks the tagged scenarios, names the repo's skills and agents, and grades which one a run called |
| ⚙️ [test_claude_render_settings.py](test_claude_render_settings.py) | The settings renderer escapes paths and stops for an unlisted hook, and its template lists exactly the shipped hooks |
| 🫥 [test_find_missed_rules.py](test_find_missed_rules.py) | The missed rules script counts a miss only when a rule applied and never loaded, and skips sessions with no matching file, from before the start date or without rules |
