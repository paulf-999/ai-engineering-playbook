# 🧪 Test stage

**Purpose:** how Claude checks its own work before a person sees it, and proves that a bug is fixed.

Test design lives in the [testing rules](../testing.md), so this page covers how checks fit a change.

## 🪜 Steps

1. Find the repo's one-command checks, such as `make test`, that exit non-zero on failure, and propose one if a check needs several commands.
2. Set a measurable target before starting, such as "all tests in `test_status.py` pass" or "the endpoint returns 200 with the new field".
3. Make the change, run the check, and fix the code until it passes.
4. Paste the output, rather than a claim that it passed, when reporting the task done.

## ⏱️ Keeping checks quick

These keep slow checks from delaying the user or tying up their machine:

- 🎯 **Affected evals only:** run the evals a change affects, by name where the runner allows it, and a full run only when the user asks or a shared part changes, such as the runner.
- 🎲 **Flaky tests:** save a failing run's full output, rerun that test alone, and never repeat the whole suite to chase it.
- 🖥️ **Busy machine:** before a long run, check whether other sessions are running tests or evals, such as with `pgrep -f '/[p]ytest( |$)|^claude -p'`, which lists the process ID of each `pytest` or `claude -p` run it spots, and if so tell the user and offer to wait.
- ⏳ **Long runs:** before a check likely to take over 2 minutes, say roughly how long and why it's needed.

## 🐞 Bug fixes

Open a bug-fix plan with a failing test, then the fix:

1. Reproduce the bug as a test.
2. Run it, and confirm it fails for the expected reason.
3. Commit the failing test on its own, where the repo's hooks and [`git.md`](../git.md) allow it, or otherwise paste its failing output before the fix.
4. Fix the code without changing that test.
5. Run the test, then the whole suite, and paste both outputs.

## 🔒 Protecting the checks

Claude can't weaken a test during a fix:

- 🚫 **No shortcuts:** never edit, skip, delete or loosen a test to make a fix pass.
- 🤔 **Wrong test:** if the test itself looks wrong, stop and ask.
- 🛡️ **If it must always hold:** a hook can block test edits during a fix, or review can reject a fix that changes an existing test.

## 📸 Screenshot loop

For UI work, where a browser or screenshot tool is available:

1. Implement the change, and take a screenshot.
2. Compare it with the agreed mock-up, and list the differences.
3. Adjust and repeat, with two or three rounds being normal.

## 🧑‍⚖️ Fresh verifier

- 👁️ **Final check:** for risky work, ask a subagent with a fresh context to run the change, so the author's assumptions don't colour the verdict.
- 📋 **Report only:** have it exercise the change and its nearest neighbours, then list what differs from the plan, without fixing anything.
- 🔁 **Not a substitute:** it follows the checks above, which run throughout the task.

## 🧮 Evals

An eval is a real task with checks that define an acceptable result.

- 📚 **Suite:** collect 20 to 50 recent tasks, and replace cases that no longer tell good from bad.
- ⏰ **When:** rerun the affected ones when `CLAUDE.md`, skills, hooks or the model change, or on a set cadence.
- 🚨 **Incidents:** add one for each production incident, written by the team that owned it.
- 🏢 **If CI can run Claude:** run the suite there and review any change that lowers the pass rate before merge.

## ⚖️ Governance

- 🗃️ **Evidence:** test output, build logs and screenshots come from the tools, in the session and the PR.
- ✍️ **Approval:** the code owner reviews intent and risk, and the config's owning team approves eval-gated changes.

## 📏 Measures

- ⏱️ **Early signs:** first-pass CI success, eval pass rate, and time for an incident to become an eval.
- 📉 **Later results:** review time, change failure rate, and regressions caught in CI against those found in production.

## 📞 Called by

This rule is invoked by [`rules/on_demand/01_standards/ai_sdlc_stages.md`](../ai_sdlc_stages.md), before planning or making a bug fix, or when setting up checks or evals.
