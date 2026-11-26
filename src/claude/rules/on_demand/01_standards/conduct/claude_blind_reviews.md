# 🙈 Blind reviews

**Purpose:** how to get an unprimed score from a reviewer, a model given only the file and a rubric, so your own framing doesn't inflate the result.

## 📝 Brief and setup

- ✂️ **Minimal brief:** give only the file path, the rubric path and a one-line task, with no summary of the rubric or house style.
- 🧊 **No context:** run each reviewer as its own `claude -p --safe-mode` process from a fresh clone, with read-only `--allowedTools` and the prompt on stdin.
- 🚫 **No subagents:** never use an in-session subagent as a reviewer, since it loads your config.
- 🔁 **Circular rubrics:** add a separate critique reviewer when the file being scored is itself a rubric.

## 🏁 Rounds and results

- 🧮 **Three reviewers:** run 3 reviewers in parallel, each in its own clone, and record the median for each theme.
- ⚡ **Fast rounds:** use narrow Sonnet reviewers that report only blocking and should-fix issues.
- 🛑 **Round cap:** stop after 2 rounds, then build.
- 🤖 **Not human:** say in the write-up that the reviewers were models.

## 📞 Called by

This rule is invoked by [`rules/always_on/01_standards/behaviour.md`](../../../always_on/01_standards/behaviour.md), before running a blind or cold review of a doc, plan or repo.
