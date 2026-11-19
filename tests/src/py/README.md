# 🐍 tests/src/py

**Purpose:** what each test of the Python scripts in `src/py/` checks.

| Test | What it checks |
|---|---|
| 🧪 [test_claude_run_behaviour_evals.py](test_claude_run_behaviour_evals.py) | The behaviour evals runner picks the tagged scenarios, builds each scratch repo from its setup, and renders the transcript the grader sees |
| 🎯 [test_claude_run_trigger_evals.py](test_claude_run_trigger_evals.py) | The trigger evals runner picks the tagged scenarios, copies the skills and agents, and grades which one a run called |
