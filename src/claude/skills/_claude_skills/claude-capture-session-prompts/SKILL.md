---
name: claude-capture-session-prompts
description: Write one day's Claude Code prompts to a markdown table, with secrets masked — use when asked to capture session prompts, audit session prompts or audit my Claude prompts
tags:
  criticality: could
  status: active
  tested: true
---

## 🤖 Instructions for Claude

- **Pre-check:** confirm `python3 --version` is 3.10 or newer, and if not tell the user and stop.
- **Read first:** read `reference/_implementation.md` for the output folder, the overwrite check and the errors.
- **Always:** run `python3 "${CLAUDE_SKILL_DIR}/capture_session_prompts.py" --output-dir <folder> [--date YYYY-MM-DD]`, and never build the table by hand.
- **Always:** pick `<folder>` from any session notes rule your config has, and otherwise use the current folder, as an absolute path.
- **Never:** paste raw `history.jsonl` lines into the chat, since they skip the script's secret masking.
- **Never:** re-run with `--force` without asking, since the report may hold the user's edits.

## 🎯 Purpose

Turns a day's prompts into a table to review the day or plan the next one:

- **One date** — every prompt from one local date, today by default, with its time and project folder.
- **Secrets masked** — keys, tokens and password values become `[REDACTED]` before anything is written.
- **Edits kept** — an existing report is never replaced unless you ask.

## 💡 Example Usage

```text
$ /claude-capture-session-prompts
Wrote 24 prompts to /Users/you/notes/2026_11_18_claude_prompts.md

$ group these by theme and list what's still pending
[Claude reads the report and adds a theme and status to each row]
```

## ✨ Best For

Looking back over one day's prompts to spot pending work for the next session.

**Caveats:** masking matches known formats and values of 8 or more characters, so a short or unusual secret can still get through.

- **No categories:** the script records time, project and prompt only, so ask Claude to add themes or status afterwards.
- **One date:** run it once per date to cover several days.

## 📚 References

- `capture_session_prompts.py` — the script the skill runs
- `reference/_implementation.md` — the output folder, the overwrite check and errors
- `tests/evals.yaml` — 6 scenarios covering the capture, the overwrite check, masking and two cases where it shouldn't fire
