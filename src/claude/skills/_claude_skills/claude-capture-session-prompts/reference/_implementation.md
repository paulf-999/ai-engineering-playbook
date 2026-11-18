# 🛠️ claude-capture-session-prompts implementation

**Purpose:** how the skill picks its output folder, protects an existing report and handles errors.

## 🔄 Phases

| Phase | What happens |
|---|---|
| **1 — Capture** | Run the script, which reads `history.jsonl` from `$CLAUDE_CONFIG_DIR`, or `~/.claude` when unset, and writes the report |
| **2 — Review** | On request, read the report and add what the user asks for, such as a theme or status per row |

## 📁 Output folder

- **Session notes rule:** if your config says where session notes go, pass that folder.
- **No rule:** pass the current folder, and tell the user the report's path.
- **File name:** the script names the report `YYYY_MM_DD_claude_prompts.md`, after the captured date.

## ✋ Existing report

The script exits with code 1 and writes nothing when a report for that date exists, since it may hold the user's edits. Ask the user, then either re-run with `--force` or edit the existing report.

## 🧯 Errors

| Symptom | Cause | Fix |
|---|---|---|
| `No prompts found` | No prompts on that date, or the wrong config directory | Check the date, and that `CLAUDE_CONFIG_DIR` names the config Claude Code uses |
| `invalid fromisoformat value` | The date isn't `YYYY-MM-DD` | Re-run with a valid date, such as `--date 2026-11-18` |
| Times an hour out | The machine's time zone isn't the one wanted | Set it for the run, such as `TZ=Europe/London python3 ...` |
| Permission denied | The output folder isn't writable | Pass a different `--output-dir` |
