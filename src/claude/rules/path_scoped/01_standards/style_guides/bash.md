---
paths:
  - "**/*.sh"
---
# 🖥️ Bash Style Guide

**Purpose:** shell scripting standards for safety and consistency, alongside what `shellcheck` checks. This team's variable casing and script helpers are in [`02_team_conventions/bash.md`](../../02_team_conventions/bash.md), which loads with this guide.

## 📄 Script structure

Start each new script from the repo's own script template, if it has one.

## 🛡️ Safety flags

Start every script with `#!/bin/bash` then `set -euo pipefail`, so it stops on a failed command, an unset variable or a failed pipe.

## 🏷️ Naming conventions

- **Functions:** `snake_case`
- **Variables:** one case throughout, the team's in its conventions
- **Script files:** `snake_case.sh`

## 📦 Variables and conditionals

- **Quote all references:** use `"${VAR}"`, not `$VAR`, including inside conditionals.
- **Function scope:** declare local variables with `local`.
- **Prefer `[[ ]]`** over `[ ]`, which is safer and more expressive.

## 📌 General

- **Suppressions:** disable a `shellcheck` warning only with a reason, such as `# shellcheck disable=SC2034  # template placeholder`.
- **Absolute paths:** use them where the working directory may vary.
- **Comments:** place above the code they describe, and keep them accurate.
