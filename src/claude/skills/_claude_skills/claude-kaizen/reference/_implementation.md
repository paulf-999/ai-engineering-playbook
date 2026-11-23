# 🛠️ claude-kaizen implementation

**Purpose:** how the skill picks notes, drafts a rule and its case, and acts on each verdict.

## 🔄 Phases

| Phase | What happens |
|---|---|
| **1 — Gather** | Read every `feedback_*.md` note in the session's auto-memory folder, which the memory instructions name |
| **2 — Select** | Group notes that make the same correction, and keep a group only if it has 2 or more notes or applies beyond this repo |
| **3 — Draft** | For each kept group, draft one rule bullet and one case, then show both as a diff and wait for a yes |
| **4 — Prove** | Write the approved drafts, run each case, and keep or undo it by its verdict |
| **5 — Report** | List each case's counts and verdict, and the files left changed for `/git-create-pr`, then log the run to `kaizen_runs.log` |

## 🔍 Selecting notes

- **Skip repo-specific notes:** a note about one repo's files, PR numbers or layout stays in memory, as 29 of 31 did in #393.
- **Skip what a rule already says:** read the existing rules first, and drop a group they already cover.
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

| Verdict | Meaning | Action |
|---|---|---|
| **helps** | With the rule passes at least 2 more of 3 runs | Keep the rule and its case |
| **no effect** | Neither condition leads by 2 runs | Undo both, since Claude already behaves this way or the case can't show it |
| **hurts** | Without the rule passes at least 2 more runs | Undo both, and tell the user |

Undo only your own edits, checking `git diff` first, and stop if another change sits in the same file.

## 🧯 Errors

| Symptom | Cause | Fix |
|---|---|---|
| `No rule eval case is named` | The case name doesn't match the one written | Check the `name:` in `rules/evals.yaml` |
| `claude isn't on PATH` | Claude Code isn't installed or logged in where `make` runs | Install it and log in, then rerun |
| No feedback notes | Memory is off, or this project has none yet | Tell the user, and stop |
