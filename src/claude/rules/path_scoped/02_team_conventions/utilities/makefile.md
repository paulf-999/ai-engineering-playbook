---
paths:
  - "**/Makefile"
  - "**/*.mk"
---
# 🛠️ Makefile team conventions

**Purpose:** this team's own Makefile choices. Another team can replace them with its own, while the standards stay in `style_guides/utilities/makefile.md`.

## 🏷️ Naming

- **Targets:** lowercase, with words separated by underscores, such as `test_debug`.
- **Variables:** lowercase too, such as `build_dir := $(current_dir)/build`, except variables special to Make, such as `SHELL`, or inherited from the environment, which keep their own case.

## 🐚 `SHELL` variable

- **Rule:** every Makefile must set `SHELL` explicitly, so it never inherits an unexpected shell from the environment.
- **Value:** any explicit shell is fine, such as `/bin/sh` for portable recipes or `/bin/bash` when recipes use bash features.

```makefile
SHELL := /bin/sh
```

## 💬 Displaying text

- **Rule:** print messages with GNU Make's built-in functions, which report through Make itself rather than a shell.
- **Timing:** `$(info)` inside a recipe prints when Make expands the recipe, before any of its shell lines run.
- **When to use `@echo`:** use it instead when the message must appear in order between shell lines, such as a progress line.

```makefile
$(error   text…)   # fatal — halts execution
$(warning text…)   # non-fatal warning
$(info    text…)   # informational
```

## 🧮 Assignment

- **`:=` not `=`:** assign with `:=` (simply expanded), which evaluates once, so a variable can't change later because something it refers to changed. See [makefiletutorial.com — Flavors and Modification](https://makefiletutorial.com#flavors-and-modification).

## ⚠️ Accepted exceptions

A Makefile may break three of these rules on purpose:

- **Coloured `@echo`:** status lines use `@echo` with colour codes, so each line prints in order with the recipe's shell steps.
- **Uppercase colour constants:** shared terminal codes such as `INFO` and `COLOUR_OFF` stay uppercase to stand apart from settings.
- **`SHELL = <path>`:** setting the shell with `=` behaves the same as `:=` for a fixed value.
