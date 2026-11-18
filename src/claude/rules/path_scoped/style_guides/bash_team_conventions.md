---
paths:
  - "**/*.sh"
---
# 🖥️ Bash team conventions

**Purpose:** this team's own shell choices. Another team can replace them with its own, while the standards stay in `bash.md`.

- 🔠 **Variables:** `UPPER_SNAKE_CASE` for every variable.
- 🧰 **Helpers:** the team's script template and `shell_utils.sh` helpers, below.

## 📚 Read on demand

- `_templates/utils/template_bash_script.sh`, in your Claude config directory, when the repo has no script template of its own.
- `_templates/utils/shell_utils.sh`, in your Claude config directory, for its functions and which log level suits each message, when the repo has a shared `shell_utils.sh`.
