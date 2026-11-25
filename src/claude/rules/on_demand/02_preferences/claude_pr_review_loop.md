# 🔁 PR review loop

**Purpose:** how Claude reviews and fixes a new pull request (PR) in a capped loop, and which PRs skip it.

## 🎚️ Pick the tier

Show one of these as the `Review:` line in the `git-create-pr` confirmation prompt, which the user can change:

| Tier | When | What runs |
|---|---|---|
| 🪶 `Review: none` | 25 changed lines or fewer, counting additions plus deletions, and no risky paths | CI only, with no review offer |
| 🔁 `Review: loop (max 2 fix rounds)` | Every other PR | The loop below |

- ⚠️ **Risky paths:** hooks, scripts, CI workflows, install code, settings, dependencies and security code, such as authentication, permissions or secret handling, always loop.
- ✋ **Approval:** `y` at the prompt approves the tier, and on a loop covers its fix commits and normal pushes to the PR branch, with no prompt each round.

## 🔁 Run the loop

Each round runs these steps, with at most 2 fix rounds, so 3 reviews:

1. **Review:** run `git-review-pr <number> --dry-run` with a fresh reviewer that isn't told earlier scores or findings, and answer its "address any of these?" prompt with `n`.
2. **Check the stops:** finish if one below applies.
3. **Fix:** make the smallest change for each Must (blocking) and Should (important) finding.
4. **Leave or decline:** list each Could (optional) without fixing it, and decline a wrong finding with a reason rather than padding the PR.
5. **Push:** rerun the repo's checks, then commit and push to the PR branch, never to `main` and never with force.

## 🛑 Stop

- ✅ **Clean exit:** no Must or Should findings, and every scored theme is at 9 or above.
- 🔢 **Cap:** the third review is done.
- 🧱 **No progress:** a fix round clears no findings, or a theme is below 9 with no finding to explain it, so report the score rather than invent a fix.
- ❌ **Failed check:** a check fails without an obvious fix.
- 🧭 **Scope:** a fix would change the PR's scope, so ask the user first.

## 🏁 Finish

- 📄 **PR body:** refresh it if a fix made it inaccurate.
- ⏳ **CI:** wait for it to finish.
- 📊 **Report:** give the exit reason, first and last scores per theme, declined findings with reasons, and what's left.
- 📬 **Posting:** offer to post the final review, and post its saved draft only on a `y`.

## 📞 Called by

This rule is invoked by [`rules/always_on/02_preferences/claude_pr_review.md`](../../always_on/02_preferences/claude_pr_review.md), before running `git-create-pr`.
