# 🧪 claude-capture-session-prompts tests

**Purpose:** what each scenario in `evals.yaml` checks, so an author can test a change to the skill against them.

Each scenario records a user request, its setup and the expected result. They aren't code, and nothing runs them yet, so treat them as worked examples to check the skill against by hand.

## 📋 Scenarios

| # | Scenario | Phase | What it checks |
|---|---|---|---|
| 1 | `capture_today_with_session_notes_rule` | Capture | Runs the script into the session notes folder, as an absolute path |
| 2 | `capture_past_date_without_rule` | Capture | Passes the named date, and writes to the current folder |
| 3 | `existing_report_asks_before_force` | Capture | Asks before overwriting a report that may hold edits |
| 4 | `raw_history_never_pasted` | Safety | Never pastes unmasked history lines into the chat |
| 5 | `summarise_current_conversation` | Not for | A summary of this conversation doesn't fire the skill |
| 6 | `multi_day_range_one_run_per_date` | Not for | Covers a range with one run per date |

- **Script tests:** `tests/src/claude/skills/_claude_skills/claude-capture-session-prompts/test_capture_session_prompts.py` checks the date filter, the masking and the overwrite check.
