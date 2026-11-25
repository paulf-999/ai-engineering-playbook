# 🔁 PR review loop

**Purpose:** how Claude reviews and fixes a new pull request (PR) in a capped loop, and which PRs get a single review instead.

## 🎚️ Pick the tier

Show one of these as the `Review:` line in the `git-create-pr` confirmation prompt, which the user can change:

| Tier | When | What runs |
|---|---|---|
| 🪶 `Review: once` | 25 changed lines or fewer, counting additions plus deletions, and no risky paths | One review with no fixes, then Finish |
| 🔁 `Review: loop (max 1 fix round)` | Every other PR | The loop below |

- ⚠️ **Risky paths:** hooks, scripts, CI workflows, install code, settings, dependencies and security code, such as authentication, permissions or secret handling, always loop.
- ✋ **Approval:** `y` at the prompt approves the tier and posting its final review, and on a loop also covers its fix commits and normal pushes to the PR branch, with no prompt for each.

## 🔁 Run the loop

A single review runs step 1 alone, and a loop runs these steps each round, with at most 1 fix round, so 2 reviews:

1. **Review:** run `git-review-pr <number> --dry-run` with a fresh reviewer that isn't told earlier scores or findings, and answer its "address any of these?" prompt with `n`.
2. **Leave or decline:** list each Could (optional) without fixing it, and decline a finding that's wrong or that the user has already decided, with a reason, rather than padding the PR.
3. **Check the stops:** finish if one below applies.
4. **Fix:** make the smallest change for each Must (blocking) and Should (important) finding left.
5. **Push:** rerun the repo's checks, then commit and push to the PR branch, never to `main` and never with force.

## 🛑 Stop

- ✅ **Clean exit:** no Must or Should findings are left, counting a declined one as settled, except a Must the user hasn't decided.
- 🔢 **Cap:** the second review is done, so anything left goes to the user.
- ❌ **Failed check:** a check fails without an obvious fix.
- 🧭 **Scope:** a fix would change the PR's scope, so ask the user first.

## 🏁 Finish

- 📄 **PR body:** refresh it if a fix made it inaccurate.
- ⏳ **CI:** wait for it to finish.
- 📊 **Report:** give the exit reason, first and last scores per theme, declined findings with reasons, and what's left.
- 📬 **Posting:** on every PR, post the final review's saved draft before any merge, once its secret check passes, and link it in the report. If the check flags anything, post and merge nothing until the user decides. The tier's `y` is the approval `git-review-pr` asks for, a deliberate exception to showing the user each comment before it's sent.

## 📞 Called by

This rule is invoked by [`rules/always_on/02_preferences/claude_pr_review.md`](../../always_on/02_preferences/claude_pr_review.md), before running `git-create-pr`.
