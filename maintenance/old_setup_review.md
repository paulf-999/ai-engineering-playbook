# 🏛️ Old setup review

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** what the Claude configuration this repo replaces contains, what works well in it, and the lessons the new design carries forward.

That configuration is [`claude_ai_playbook`](https://github.com/paulf-999/claude_ai_playbook), a personal Claude Code setup installed on each machine with `make install`. It came first, and this repo began replacing it in late October 2026. This page describes it at commit `915685f`, dated 2026-10-31.

## 📋 Executive Summary

- 💪 **Strengths:** a safe installer, a real test suite and automated checks make it reproducible and portable.
- ⚠️ **Main risk:** about 30,000 tokens of rules load into every session, whatever the task.
- 🔍 **Against the reference material:** it has a strong feedback loop, but no step for capturing intent first and no outcome measures.
- 🎯 **For the new design:** start small, and reshape two core rule files around those findings.

## 📸 Snapshot

Each component, how it loads into Claude, and what it's for. Rules that load "always" add to every session's context, so they cost tokens whatever the task:

| Component | Count | How it loads | What it's for |
|---|---|---|---|
| 📄 `CLAUDE.md` | 1 file, 42 lines | Always | Index of core principles and imports |
| 📥 Always-on rules | 36 files, about 1,900 lines | Always, about 30,000 tokens | Standards for behaviour, writing, naming, git, security and response format |
| 📂 Path-scoped rules | 10 files, plus 10 language style guides moved from the reference docs at install | Only when Claude opens a matching file | Detailed guidance for certain file types |
| 💤 Lazy-loaded rules | 29 files | Only when another rule tells Claude to read them | Detail split out of longer rules, and rarely needed guidance |
| 📚 Reference docs | 184 files, including 108 quality scorecards | Read by people, or by Claude when a rule points to them | Style guides, and records of each component's reviewed quality |
| 🛠️ Skills | 8 | When a trigger phrase matches | Multi-step workflows, such as raising a PR |
| 🤖 Agents | 3 | When started, as a separate Claude with its own context | Code review, technical writing and quality review |
| 🪝 Hooks | 5 scripts, 4 switched on in settings | Automatically, on prompts and tool calls | Naming and file-location checks, a settings warning and a per-turn reminder |
| 🧪 Tests and checks | 81 test files, 22 pre-commit hooks, 1 CI workflow | Before each commit, then in CI for each PR | Checks on structure, hooks, skills and scripts |

## 🚩 Where complexity outran evidence

Where the old configuration grew heavier than the evidence for it justified. It found five problems:

- 🏋️ **Always-on weight:** about 30,000 tokens of rules load into every session, whatever the task, and nothing measures how many a task uses.
- 🔁 **Per-turn overhead:** a hook adds the response-format rules to every prompt, including trivial ones.
- 📐 **Rules about rules:** standards for writing rules, scoring them and dating them add upkeep without changing engineering results.
- 🗣️ **Advisory controls:** most safeguards, such as "ask before acting", are written rules that rely on Claude checking itself.
- 📉 **No outcome data:** nothing records delivery time, rework or human effort, so nobody can tell which components help.

## 🎓 Lessons for the new design

- 🌱 **Start minimal:** begin with `CLAUDE.md`, one test command and CI, then review each component on its own for the patterns that made this setup costly, before porting, slimming or dropping it.
- 🔪 **Halving test:** ask whether removing half the components would make results noticeably worse.
- 💪 **Keep the strengths:** carry over its safe installer, portable paths, checks that can fail, on-demand loading and fresh-context review.
