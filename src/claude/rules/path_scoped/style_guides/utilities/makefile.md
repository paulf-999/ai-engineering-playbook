---
paths: "**/Makefile, **/*.mk"
---
# 🛠️ Makefile Style Guide & Standards

**Purpose:** Define the team's standards for writing and structuring Makefiles.

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

## 🧮 Assignment and recipes

- **`:=` not `=`:** assign with `:=` (simply expanded), which evaluates once, so a variable can't change later because something it refers to changed. See [makefiletutorial.com — Flavors and Modification](https://makefiletutorial.com#flavors-and-modification).
- **`@` to silence:** prefix a command with `@` to stop Make printing the command itself before running it.
- **`$@` for the target:** use `$@`, which expands to the current target's name, instead of repeating the name in the recipe.

```makefile
build:
	@mkdir -p $@
```

## ⚠️ Accepted exceptions

A Makefile may break three of these rules on purpose:

- **Coloured `@echo`:** status lines use `@echo` with colour codes, so each line prints in order with the recipe's shell steps.
- **Uppercase colour constants:** shared terminal codes such as `INFO` and `COLOUR_OFF` stay uppercase to stand apart from settings.
- **`SHELL = <path>`:** setting the shell with `=` behaves the same as `:=` for a fixed value.
