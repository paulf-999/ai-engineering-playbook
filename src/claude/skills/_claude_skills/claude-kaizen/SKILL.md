---
name: claude-kaizen
description: Turn recurring corrections into A/B-proved rules — run /claude-kaizen, or when the reminder suggests it
# slash-only, so its description costs no always-on context; the reminder hook names the command instead
disable-model-invocation: true
---

## 🤖 Instructions for Claude

- **Pre-check:** confirm the current repo has `src/claude/rules/evals.yaml` and a `make evals` target, and if not, say to run the skill from the playbook repo and stop.
- **Read first:** read `reference/_implementation.md` for how to pick notes, draft a case and read the verdict.
- **Always:** show each draft rule bullet and its `rules/evals.yaml` case as a diff, and edit files only after an explicit yes.
- **Always:** say a case costs 6 runs and 6 grades of plan usage, run in parallel in under a minute, before running `make evals RULES=1 CASE=<name>`.
- **Always:** keep a rule only on a **helps** verdict, and undo your own edits for any other verdict.
- **Always:** at the end, append `YYYY-MM-DD notes=<read> proposed=<drafted> kept=<kept>` to `kaizen_runs.log` in the auto-memory folder, which resets the reminder hook's count.
- **Never:** commit, push or open a PR, since `/git-create-pr` does that once the user is happy.
- **Never:** quote a feedback note's personal details, such as a name, in a rule or case.

## 🎯 Purpose

Turns the corrections you keep giving Claude into team rules, but only those that measurably change what Claude does:

- **Recurring only** — a correction joins only if it recurs or applies beyond one repo.
- **Proved** — each rule ships with an A/B case run with and without the rule.
- **Your call** — every rule is a diff you approve, and nothing is committed.

## 💡 Example Usage

```text
$ /claude-kaizen
Read 31 feedback notes. 2 candidates recur and apply beyond this repo:
  1. Write dates as YYYY-MM-DD (4 notes)
  2. Quote test output when reporting a failure (2 notes)
[diff for writing_style.md, claude_task_reporting.md and rules/evals.yaml]
Write these and run their A/B cases? About a minute of plan usage. (y/n) y
iso_dates_in_prose: without 0/3, with 3/3, helps — kept
failure_output_quoted: without 3/3, with 3/3, no effect — undone
Kept 1 rule in the working tree. Run /git-create-pr to open the PR.
```

## ✨ Best For

A periodic look back, such as once a sprint, at what you've had to correct Claude on.

**Caveats:** a **no effect** verdict can mean Claude already behaves well, so the rule isn't worth its context cost.

- **Budget:** an always-on rule must fit the always-on budget, so the skill proposes a trim when it's over.
- **One repo:** it reads the current project's notes only.

## 📚 References

- `reference/_implementation.md` — picking notes, drafting a case, the budget and the verdicts
- `evals.yaml` — 3 scenarios, each run by `make evals`
