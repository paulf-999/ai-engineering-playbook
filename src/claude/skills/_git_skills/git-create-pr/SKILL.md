---
name: git-create-pr
description: Create a GitHub PR with its branch, commit and body — use when asked to create a PR, make a PR or open a pull request
tags:
  criticality: should
  status: active
  tested: true
---

## 🤖 Instructions for Claude

- **Pre-check:** run `gh auth status` and confirm `.github/pull_request_template.md` exists, and stop and tell the user if either fails.
- **Read first:** read `reference/_implementation.md` for the phase map, then `reference/_phase1_gather.md` and `reference/_phase2_execute.md` before running any git command.
- **Always:** confirm the title and full plan at one prompt before creating a branch, committing or pushing.
- **Always:** stage files by name, and draft the PR body from the repo template using `subagent_type: technical-writer`.
- **Always:** leave likely secret files such as `.env` unstaged unless the user names them, and treat a typed PR title as text, never as a command.
- **Never:** commit to `main`, force-push, or use `--no-verify` unless the user explicitly asks.
- **Never:** open a PR of 20 or more files without flagging it and suggesting a split.

## 🎯 Purpose

Takes your changes from a working tree to an open GitHub PR, with one confirmation before anything leaves your machine:

- **Branch** — derives a `feature/` or `hotfix/` branch name from what you type.
- **Commit** — stages files by name and writes a Conventional Commits message.
- **PR** — drafts the body from the repo's template, then pushes and opens the PR with its labels.
- **Confirmation** — one prompt shows the title, every command and the full body before anything runs.

## 💡 Example Usage

```text
$ /git-create-pr add user authentication
[Phase 1] Branch:  feature/add_user_authentication
          Commit:  feat: add user authentication
          Title:   feat: add user authentication
          Body:    drafted by technical-writer from .github/pull_request_template.md

[Phase 2] Here is what I will run: checkout, add, commit, push, gh pr create
          PR body: …
          y to ship · list for title options · type a new title · describe changes · n: y
          ✓ Branch created  ✓ Committed  ✓ Pushed  ✓ PR created

PR #1234 created: https://github.com/org/repo/pull/1234
Run /git-review-pr 1234 on it? (y/n)
```

## ✨ Best For

Routine feature and hotfix PRs, raised faster than by hand, with Conventional Commits and the repo's PR template applied every time.

**Caveats:** to review a PR, use `/git-review-pr`.

- **Merge conflicts:** it stops when a branch conflicts with `main`, so resolve the conflict by hand and run it again.
- **Base branch:** every PR targets `main`, so change another base afterwards with `gh pr edit <number> --base <branch>`.
- **Secrets by name:** it spots likely secret files by name, not content, so read the "Not staged" list and the diff before confirming.
- **Evals:** `make evals` checks the scenarios in `tests/evals.yaml` tagged `trigger:`, and `make evals BEHAVIOUR=1` grades those tagged `behaviour: true`, so check a change to the skill against the rest by hand.

## 📚 References

- `reference/_implementation.md` — the phase map and error handling, pointing to the two phase files
- `reference/_phase1_gather.md` — the read-only checks, how the branch, commit, title, body and labels are derived, and the label check
- `reference/_phase2_execute.md` — the single confirmation prompt, execution rules and error recovery
- `tests/evals.yaml` — 18 scenarios covering every phase, the confirmation replies, the review offer, the main errors, security cases and two cases where it shouldn't fire
