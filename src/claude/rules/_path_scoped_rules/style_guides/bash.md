---
paths:
  - "**/*.sh"
---
<!-- version: 1.6.2 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-11 -->
<!-- applies_to: shell scripts -->
<!-- miss_cost: medium — scripts fail silently or break on unexpected input -->
# 🖥️ Bash Style Guide

**Purpose:** shell scripting conventions for safety and consistency, alongside what `shellcheck` checks.

## 📄 Script structure

Start each new script from the repo's own script template, if it has one.

- **Read on demand:** `_templates/utils/template_bash_script.sh`, in your Claude config directory, when the repo has no script template of its own.

## 🛡️ Safety flags

Start every script with `#!/bin/bash` then `set -euo pipefail`, so it stops on a failed command, an unset variable or a failed pipe.

## 🏷️ Naming conventions

- **Functions:** `snake_case`
- **Variables:** `UPPER_SNAKE_CASE`
- **Script files:** `snake_case.sh`

## 📦 Variables and conditionals

- **Quote all references:** use `"${VAR}"`, not `$VAR`, including inside conditionals.
- **Function scope:** declare local variables with `local`.
- **Prefer `[[ ]]`** over `[ ]`, which is safer and more expressive.

## 📌 General

- **Suppressions:** disable a `shellcheck` warning only with a reason, such as `# shellcheck disable=SC2034  # template placeholder`.
- **Absolute paths:** use them where the working directory may vary.
- **Comments:** place above the code they describe, and keep them accurate.

- **Read on demand:** `_templates/utils/shell_utils.sh`, in your Claude config directory, for its functions and which log level suits each message, when the repo has a shared `shell_utils.sh`.
