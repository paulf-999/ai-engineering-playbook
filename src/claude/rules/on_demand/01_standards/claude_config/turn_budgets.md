# 🔄 Turn budgets

**Purpose:** how to cap turns when running Claude Code without a person watching, so a run can't loop and overspend.

- 🎯 **Always cap:** pass `--max-turns N` on every non-interactive run, such as `claude -p` in a script, skill or CI job.
- 📏 **Default:** 20 turns suits most tasks, and a run that needs more should get a higher cap set on purpose.

| Run | Cap |
|---|---|
| 🧹 **Linting or formatting** | 5 to 10 |
| 🛠️ **Writing or refactoring code** | 15 to 20 |
| 🔗 **Build, test and deploy** | 20 to 30 |
| 🔭 **Open-ended research** | 25 to 50 |

- 🚩 **Red flag:** a run that keeps hitting its cap is bigger than estimated, so split it rather than just raising the cap.

## 📞 Called by

This rule is invoked by:

- [`rules/on_demand/01_standards/claude_config/guiding_principles.md`](guiding_principles.md), before testing a config change with `claude -p` or another unattended run.
- [`rules/on_demand/01_standards/conduct/automation_controls.md`](../conduct/automation_controls.md), when setting turn caps for other unattended runs.
