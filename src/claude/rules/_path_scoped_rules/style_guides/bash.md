---
<!-- version: 1.5.1 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-07 -->
<!-- applies_to: **/*.sh -->
<!-- miss_cost: medium — scripts fail silently or break on unexpected input -->
<!-- loading: path-scoped — loads with shell scripts -->
paths:
  - "**/*.sh"
---

# 🖥️ Bash Style Guide

**Purpose:** Establish shell scripting conventions for safety, consistency, and maintainability across all Bash scripts in the team.

## 📄 Script structure

Start each new script from the repo's own script template, if it has one, so its sections come in the right order: shebang, safety flags, description and usage lines, shared utilities, trap, section headers and logging.

- **Read on demand:** `_templates/utils/template_bash_script.sh`, in your Claude config directory, when the repo has no script template of its own.

## 🛡️ Safety flags

All scripts must begin with:

```bash
#!/bin/bash
set -euo pipefail
```

- **`-e`:** stop on the first command that fails.
- **`-u`:** stop on an unset variable instead of treating it as empty.
- **`-o pipefail`:** fail a pipeline when any command in it fails, not only the last.

## 🔧 Shell utilities

If the repo has a shared utilities file, source it at the top of every script, by a path built from the script's own location:

```bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/shell_utils.sh"  # adjust the path from SCRIPT_DIR to where the file sits
```

- **Provides:** `log_message`, `print_section_header`, `dir_exists`, `file_exists`, `handle_interruption`
- **Log levels:** use the correct constant for the severity:
  - `${DEBUG}` (cyan) — script start/end, general flow
  - `${DEBUG_DETAILS}` (purple) — lower-level detail
  - `${INFO}` (green) — informational messages
  - `${WARNING}` (yellow) — non-fatal warnings
  - `${ERROR}` (red) — errors
  - `${CRITICAL}` (bold red) — critical failures

## 🔩 Tooling

- **Linting:** all scripts must pass `shellcheck` before committing
- **Suppression:** only suppress warnings with a documented reason:

```bash
# shellcheck disable=SC2034  # intentionally unused: template placeholder
```

## 🏷️ Naming conventions

- **Functions:** `snake_case`
- **Variables:** `UPPER_SNAKE_CASE`
- **Script files:** `snake_case.sh`

## 📦 Variables

- **Quote all references:** use `"${VAR}"` not `$VAR`
- **Function scope:** declare local variables with `local`

## 🔀 Conditionals

- **Prefer `[[ ]]`** over `[ ]` — safer and more expressive
- **Quote variables:** inside all conditionals

## 📌 General

- **Absolute paths:** use them where the working directory may vary
- **Avoid `ls` parsing:** use globs or `find` instead
- **Comments:** place above the code they describe, not at the end — keep them accurate and up to date
