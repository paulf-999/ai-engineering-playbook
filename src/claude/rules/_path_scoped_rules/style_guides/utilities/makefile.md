---
<!-- version: 1.3.0 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-05 -->
paths:
  - "**/Makefile"
  - "**/*.mk"
---

# 🛠️ Makefile Style Guide & Standards

**Purpose:** Define the team's standards for writing and structuring Makefiles.

## ⚠️ Accepted exceptions

A Makefile may break three of these rules on purpose:

- **Coloured `@echo`:** status lines use `@echo` with colour codes, so each line prints in order with the recipe's shell steps.
- **Uppercase colour constants:** shared terminal codes such as `INFO` and `COLOUR_OFF` stay uppercase to stand apart from settings.
- **`SHELL = <path>`:** setting the shell with `=` behaves the same as `:=` for a fixed value.

## 📚 Read on demand

- **Read on demand:** `_rules_on_demand/style_guides/utilities/makefile/_naming_conventions.md`, in your Claude config directory, when naming a target or variable.
- **Read on demand:** `_rules_on_demand/style_guides/utilities/makefile/_variables_operators_and_commands.md`, when setting `SHELL`, printing output, assigning variables or silencing commands.
