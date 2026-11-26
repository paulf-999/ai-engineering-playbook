---
name: claude-kaizen
description: Turn recurring corrections into A/B-proved rules — run /claude-kaizen, or when the reminder suggests it
# slash-only, so its description costs no always-on context; the reminder hook names the command instead
disable-model-invocation: true
---

## 🤖 Instructions for Claude

- **Pre-check:** pick the flow, and stop if neither fits.
  - **Playbook:** the current repo has `src/claude/rules/evals.yaml` and a `make evals` target, so rules and cases go there and `make evals RULES=1` runs them.
  - **Plugin:** Claude Code fills in the paths below for a plugin install, so they start with a real folder rather than a dollar sign. Rules go in your Claude config directory's `rules/`, cases in `${CLAUDE_PLUGIN_DATA}/evals.yaml`, and the runner is `"${CLAUDE_PLUGIN_DATA}/venv/bin/python" "${CLAUDE_PLUGIN_ROOT}/scripts/claude_run_rule_evals.py"`, run with `RULE_EVALS_FILE` set to that cases file, `RULES_DIR` to that `rules/` folder, and `CASE=<name>`.
- **Drafts ready:** if this session already drafted rules, start from those the user likes.
- **Read first:** read `reference/_implementation.md` for how to pick notes, draft a case and read the verdict.
- **Always:** show each draft rule bullet and its case as a diff, and edit files only after an explicit yes.
- **Always:** say a case costs 24 runs and 24 grades of plan usage, before running it with `RUNS=12` and `CASE=<name>`.
- **Always:** keep a rule only on a **helps** verdict, and for any other verdict undo your own edits and log the rejection to `_claude_kaizen/rejections.md` in your Claude config directory (`$CLAUDE_CONFIG_DIR`, or `~/.claude` when unset).
- **Always:** at the end, append `YYYY-MM-DD notes=<read> proposed=<drafted> kept=<kept>` to `_claude_kaizen/runs.log` there, in either flow.
- **Never:** commit, push or open a PR. In the playbook flow, `/git-create-pr` does that once the user is happy, and in the plugin flow the approved rule simply stays in your config's `rules/`.
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
[diff for writing_style.md, reporting.md and the cases file]
Write these and run their A/B cases? Each costs 24 runs and 24 grades. (y/n) y
iso_dates_in_prose: without 0/12, with 12/12, helps — kept
failure_output_quoted: without 12/12, with 12/12, no effect — undone
Kept 1 rule in the working tree. Run /git-create-pr to open the PR (playbook flow).
```

## ✨ Best For

A periodic look back, such as once a sprint, at what you've had to correct Claude on.

**Caveats:** a **no effect** verdict can mean Claude already behaves well, so the rule isn't worth its context cost.

- **Budget:** an always-on rule must fit the always-on budget, so the skill proposes a trim when it's over.
- **One repo:** it reads the current project's notes only.
- **Install:** `make install` in the playbook repo, or `/plugin marketplace add paulf-999/ai-engineering-playbook` then `/plugin install claude-kaizen@ai-engineering-playbook` anywhere else.

## 📚 References

- `reference/_draft.md` — drafting without being asked, when the playbook's session-start reminder fires
- `reference/_implementation.md` — picking notes, drafting a case, the budget and the verdicts
- `evals.yaml` — 3 scenarios, each run by `make evals`, in the playbook repo only
- [How Warp builds self-improving agents on Claude](https://claude.com/resources/articles/how-warp-builds-self-improving-agents-on-claude) — the feedback-to-edit loop this skill follows
