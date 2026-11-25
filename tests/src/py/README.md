# 🐍 tests/src/py

**Purpose:** what each test of the Python scripts in `src/py/` checks.

| Test | What it checks |
|---|---|
| 🧰 [test_claude_evals_common.py](test_claude_evals_common.py) | The shared eval helpers copy the skills and agents, build each scratch repo from its setup, render the transcript the grader sees, reject missing verdicts, and delete only the scratch repo's projects/ folder |
| 🗂️ [test_claude_manage_plans.py](test_claude_manage_plans.py) | The plan manager lists plans by status, files each by its status line, archives scratch plans and drafts at 14 days, and never overwrites |
| 🧪 [test_claude_run_behaviour_evals.py](test_claude_run_behaviour_evals.py) | The behaviour evals runner picks the tagged scenarios, resumes the session for a confirm reply, and checks `must_match` patterns |
| 📖 [test_claude_run_readme_evals.py](test_claude_run_readme_evals.py) | The README evals runner briefs each reader with its persona and the README, keeps each persona's readers apart, and passes a persona only at a mean of 7 with no score under 6 |
| ⚖️ [test_claude_run_rule_evals.py](test_claude_run_rule_evals.py) | The rule A/B runner's cases name real rules, its two conditions differ only by the rule, and its verdict needs a lead of a third of the runs |
| 🎯 [test_claude_run_trigger_evals.py](test_claude_run_trigger_evals.py) | The trigger evals runner picks the tagged scenarios, names the repo's skills and agents, and grades which one a run called |
| 🫥 [test_find_missed_rules.py](test_find_missed_rules.py) | The missed rules script counts a miss only when a rule applied and never loaded, and skips sessions with no matching file, from before the start date or without rules |
