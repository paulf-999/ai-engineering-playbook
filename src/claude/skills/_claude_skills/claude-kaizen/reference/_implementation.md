# 🛠️ claude-kaizen implementation

**Purpose:** how the skill picks notes, drafts a rule and its case, and acts on each verdict.

## 🔄 Phases

| Phase | What happens |
|---|---|
| **1 — Gather** | Read every `feedback_*.md` note in the session's auto-memory folder, which the memory instructions name |
| **2 — Select** | Group notes that make the same correction, and keep a group only if it has 2 or more notes or applies beyond this repo |
| **3 — Draft** | For each kept group, draft one rule bullet and one case, then show both as a diff and wait for a yes |
| **4 — Check** | Write the approved drafts, run each case, and keep or undo it by its verdict |
| **5 — Report** | List each case's counts and verdict, and the files left changed for `/git-create-pr`, then log each rejection, and the run to `_claude_kaizen/runs.log` |

## 🔍 Selecting notes

- **Skip repo-specific notes:** a note about one repo's files, PR numbers or layout stays in memory, as 29 of 31 did in #393.
- **Skip what a rule already says:** read the existing rules first, and drop a group they already cover.
- **Skip what was rejected:** read `_claude_kaizen/rejections.md` in your Claude config directory (`$CLAUDE_CONFIG_DIR`, or `~/.claude` when unset), if it exists, and drop a group it lists unless a note not named there supports it.
- **Name the evidence:** for each group, list its notes by file name, never quoting personal details.

## ✍️ Drafting

- **Rule:** one bullet in the existing file it fits, following that file's format and the [naming standards](../../../../rules/always_on/01_standards/naming_standards.md), rather than a new file.
- **Principles over rules:** reword an existing bullet if one nearly covers the correction; otherwise draft one principle with its reason, not a narrow rule, as [Warp's article](https://claude.com/resources/articles/how-warp-builds-self-improving-agents-on-claude) advises.
- **Case:** add it to `src/claude/rules/evals.yaml` with `name`, `rule`, `prompt`, optional `setup` and `assertions`, as the existing cases do.
- **No priming:** the prompt mustn't hint at the answer the rule gives, such as using British spelling in a spelling case.
- **No questions:** end a prompt that would make Claude ask something with "don't ask me questions", since the run can't answer.

## 📏 Always-on budget

For a rule in `rules/always_on/`, run `bash src/sh/claude_validate_always_on_budget.sh`. If it fails, propose rewording or a trim of at least the overrun in the same diff, and don't drop a point another rule relies on.

## ⚖️ Verdicts

The runner tests in two stages of 5 runs per condition. Stage 1 settles a case early, and otherwise stage 2 runs 5 more and a one-sided Fisher exact test judges all 10. Each verdict prints its p, so a kept rule "passed an A/B check (p = …)".

| Verdict | Meaning | Action |
|---|---|---|
| **helps** | 5/5 against 0/5 at stage 1, or p < 0.01 over 10 runs, such as 9/10 against 3/10 | Keep the rule and its case |
| **no effect** | At stage 1, the without-rule runs all pass or the with-rule runs don't lead | Undo both and log the rejection, since Claude already behaves this way or the case can't show it |
| **hurts** | p < 0.01 over 10 runs in favour of the without-rule runs, reachable only at stage 2, since stage 1 reports a trailing rule as **no effect** | Undo both, log the rejection, and tell the user |
| **inconclusive** | Stage 2 gives p of 0.01 or more, such as 8/10 against 4/10 | Undo both without logging, so a later run can try again |

A run that fails, such as the runner crashing, is also undone and never logged.

Undo only your own edits, checking `git diff` first, and stop if another change sits in the same file.

## 🗒️ Rejections

After undoing a rule for **no effect** or **hurts**, append one line to `_claude_kaizen/rejections.md`, creating the file if needed:

```text
- 2026-11-25 · quote test output when reporting a failure · without 5/5, with 5/5, no effect · notes: feedback_a.md, feedback_b.md
```

## 🧯 Errors

| Symptom | Cause | Fix |
|---|---|---|
| `No rule eval case is named` | The case name doesn't match the one written | Check the `name:` in `rules/evals.yaml` |
| `claude isn't on PATH` | Claude Code isn't installed or logged in where `make` runs | Install it and log in, then rerun |
| No feedback notes | Memory is off, or this project has none yet | Tell the user, and stop |
