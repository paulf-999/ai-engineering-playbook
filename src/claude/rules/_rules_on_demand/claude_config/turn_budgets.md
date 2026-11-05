<!-- version: 2.0.1 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-05 -->
<!-- applies_to: **/*.sh, **/.github/workflows/** -->
<!-- miss_cost: medium — an unattended run loops and overspends -->
<!-- loading: lazy — read when guiding_principles.md points here, before an unattended run -->
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
