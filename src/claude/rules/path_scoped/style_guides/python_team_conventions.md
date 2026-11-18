---
paths:
  - "**/*.py"
---
# 🐍 Python team conventions

**Purpose:** this team's own Python choices. Another team can replace them with its own, while the standards stay in `python.md`.

- 🏷️ **Single letters:** no single-letter names outside loop counters.
- 📝 **Docstring fields:** reST, such as `:param:`.
- 💬 **Comments:** above the code they describe, never at the end of a line.
- 📏 **Limits:** 4 or fewer parameters (`max-args = 4`), 3 or fewer nesting levels (`max-nested-blocks = 3`), functions aimed at 30 lines and split past 40, and 120-character lines. These tighten ruff's defaults of 5, 5 and 50 statements, and loosen its 88.
- 🏷️ **Module metadata:** only `__author__` and `__version__`.
- 🔽 **Function order:** the entry point first, then the functions it calls.
- 🔧 **Test helpers:** `_make_*()` helpers in place of custom fixtures.
- 📁 **Test grouping:** `# --- <topic> tests ---` comments.

## 📚 Read on demand

- [`on_demand/style_guides/python_team_conventions/_environment.md`](../../on_demand/style_guides/python_team_conventions/_environment.md), in your Claude config directory, when setting up a virtual environment or dependencies.
- [`on_demand/style_guides/python_team_conventions/_testing.md`](../../on_demand/style_guides/python_team_conventions/_testing.md), before writing test setup helpers or grouping tests.
