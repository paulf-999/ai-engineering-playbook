# 🐍 tests/src/py

**Purpose:** what each test of the Python scripts in `src/py/` checks.

| Test | What it checks |
|---|---|
| 🧰 [test_claude_evals_common.py](test_claude_evals_common.py) | The shared eval helpers copy the skills and agents, build each scratch repo from its setup, render the transcript the grader sees, and delete only the scratch repo's projects/ folder |
| 🧪 [test_claude_run_behaviour_evals.py](test_claude_run_behaviour_evals.py) | The behaviour evals runner picks the tagged scenarios, resumes the session for a confirm reply, and checks `must_match` patterns |
| ⚖️ [test_claude_run_rule_evals.py](test_claude_run_rule_evals.py) | The rule A/B runner's cases name real rules, its two conditions differ only by the rule, and its verdict needs a 2-run margin |
| 🎯 [test_claude_run_trigger_evals.py](test_claude_run_trigger_evals.py) | The trigger evals runner picks the tagged scenarios, names the repo's skills and agents, and grades which one a run called |
