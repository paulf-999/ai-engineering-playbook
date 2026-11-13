<!-- version: 2.1.4 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-13 -->
# 🏛️ Current architecture

**Purpose:** what the Claude configuration this repo replaces contains, what works well in it, and the lessons the new design carries forward.

That configuration is [`claude_ai_playbook`](https://github.com/paulf-999/claude_ai_playbook), a personal Claude Code setup installed on each machine with `make install`. This page describes it at commit `915685f`, dated 2026-10-31.

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

## ✅ What works well

The strengths the new design keeps.

### 🛡️ Safety and verification

- 🔐 **Safe installer:** `make install` previews every step, needs a typed confirmation, and backs up the old config first.
- 🌍 **Portability:** scripts find the config folder from a setting or their own location, rather than a fixed path, and tests check this.
- 🧪 **Checks that can fail:** tests, pre-commit hooks and CI can each block a bad change.

### 🧩 Design and review

- 💤 **Loading on demand:** rules for certain files, or rarely needed detail, stay out of most sessions.
- 👀 **Independent review:** a reviewer agent can score work in a fresh context, so the author doesn't mark its own work.
- 📜 **Recorded decisions:** a `docs/decisions/` folder in that repo explains why key choices were made.

## 🚩 Where complexity outran evidence

Where the old configuration grew heavier than the evidence for it justified. It found five problems:

- 🏋️ **Always-on weight:** about 30,000 tokens of rules load into every session, whatever the task, and nothing measures how many a task uses.
- 🔁 **Per-turn overhead:** a hook adds the response-format rules to every prompt, including trivial ones.
- 📐 **Rules about rules:** standards for writing rules, scoring them and dating them add upkeep without changing engineering results.
- 🗣️ **Advisory controls:** most safeguards, such as "ask before acting", are written rules that rely on Claude checking itself.
- 📉 **No outcome data:** nothing records delivery time, rework or human effort, so nobody can tell which components help.

## 🔍 Alignment with the reference material

How far the old configuration already follows Anthropic's SDLC course and DORA's research. It uses two sources:

- 🔄 **SDLC course:** Anthropic's [course on the AI-native software development lifecycle](reference_material/core/anthropic_ai_native_sdlc.md), built from short practices it calls plays.
- 📊 **DORA:** the [AI Capabilities Model from DevOps Research and Assessment](reference_material/core/dora_ai_capabilities.md), cited by printed page.

### ✅ In place

| Practice | Source | What the old setup has |
|---|---|---|
| 🔁 Feedback loop | SDLC | Tests, pre-commit hooks and CI that can fail a change |
| 🗃️ Version control | DORA | All config versioned, with a set commit-message format |
| 👀 PR review | SDLC | A PR review skill and a read-only reviewer agent |
| 🌳 Parallel sessions | SDLC | A rule to use a separate checkout when sessions may overlap |

### 🟡 Partly in place

| Practice | Source | What it has | What's missing |
|---|---|---|---|
| 📦 Small batches | DORA | A 20-file PR limit | 59 of 364 merged PRs changed 20 or more files |
| 🗂️ Plan first | SDLC | Plan mode, with a pause for approval after each phase | Plans aren't kept in the repo |
| 🪶 Lean `CLAUDE.md` | SDLC | A 42-line `CLAUDE.md` | The rules it pulls in run far past one page |
| 🎯 Curated context | DORA | Rules that load only for certain files | Most guidance still loads every session, though irrelevant context degrades answers (pp. 32–33) |
| 🛠️ Skills backed by checks | SDLC | Skills and hooks | No list shows which rules a hook, test or CI check enforces |
| 🪝 Hooks as approval gates | SDLC | Hooks for naming, file location and settings | Nothing blocks a skipped confirmation |
| 🧭 AI stance | DORA | Rules on risky actions and security | Uses aren't sorted into banned, guarded and allowed (p. 18) |
| 🧪 Continuous evals | SDLC | Repeatable test tasks for agent behaviour | None run automatically or in CI |

### ❌ Not yet in place

| Practice | Source | What's missing |
|---|---|---|
| 📝 Intent and spec first | SDLC | No step to write down intent and requirements before building |
| 📈 Outcome measures | SDLC | No component records an early signal or a later result |

## 🎓 Lessons for the new design

- 🌱 **Start minimal:** begin with `CLAUDE.md`, one test command and CI, then review each component on its own for the patterns that made this setup costly, before porting, slimming or dropping it.
- 🔪 **Halving test:** ask whether removing half the components would make results noticeably worse.
- 💪 **Keep the strengths:** carry over everything in [What works well](#-what-works-well).
