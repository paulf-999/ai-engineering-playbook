<!-- version: 1.0.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🏛️ Current architecture

For anyone shaping the target architecture: what the current Claude configuration repo contains, what works well, and which lessons the next design must carry forward so complexity stays in proportion to evidence.

## 📋 Executive Summary

- **What it is:** [`claude_ai_playbook`](https://github.com/paulf-999/claude_ai_playbook), a personal Claude Code configuration installed onto each machine with `make install`.
- **Strengths:** a safe installer, a real test suite and automated checks make it reproducible and portable.
- **Main risk:** 36 always-on rule files load about 30,000 tokens into every session, whatever the task.
- **Reference fit:** measured against Anthropic's [AI-native SDLC (software development lifecycle) course](target_architecture/reference_material/anthropic_ai_native_sdlc.md) and the [AI Capabilities Model by DORA (DevOps Research and Assessment)](target_architecture/reference_material/dora_ai_capabilities.md), it has a strong feedback loop but no intent-first step or outcome measures.
- **For the target:** keep the current format, and reshape the core rule files around those sources' findings.

## 📸 Snapshot

- **Commit:** `915685f` on `main`, dated 2026-10-31 and inspected on 2026-11-02, so everything on this page describes that commit.

| Component | Count | How it loads | What it's for |
|---|---|---|---|
| `CLAUDE.md` | 1 file, 42 lines | • **Always:** every session. | • **Index:** core principles and imports. |
| Always-on rules | 36 files, about 1,900 lines | • **Always:** every session, about 30,000 tokens. | • **Standards:** behaviour, writing, naming, git, security and response format. |
| Path-scoped rules | 10 files, plus 10 style guides added at install | • **On match:** only when Claude opens a matching file. | • **Detail:** authoring, directory, rule-loading, testing and plan-format rules, plus language style guides. |
| Lazy-loaded rules | 29 files | • **On demand:** read only when a rule points to them. | • **Detail:** bulky children and rarely needed guidance. |
| Reference docs | 184 markdown files, including 108 quality scorecards and the 10 style guides installed as path-scoped rules | • **On demand:** read by people, or by Claude when a rule points to them. | • **Records:** style guides, and scorecards recording each artefact's independently reviewed quality. |
| Skills | 8 | • **On request:** when a trigger phrase matches. | • **Workflows:** packaged multi-step tasks, such as raising a PR or a Jira ticket. |
| Agents | 3 | • **On spawn:** as a separate Claude instance with its own context. | • **Independence:** code review, technical writing and scorecard review. |
| Hooks | 5 scripts, 4 registered | • **Automatic:** run by Claude Code on prompts and tool calls. | • **Guards and reminders:** naming and file-location checks, a stale-settings warning and a per-turn response-format reminder. |
| Tests and checks | 81 test files, 22 pre-commit hooks, 1 CI workflow | • **On commit and PR:** checks before each commit, then CI (continuous integration) on GitHub. | • **Verification:** structure, hooks, skills and scripts. |

## ✅ What works well

- **Safe installer:** `make install` previews every step, needs a typed confirmation, backs up the old config and refuses to run without a real terminal.
- **Portability:** paths resolve from the config-folder setting (`CLAUDE_CONFIG_DIR`) or the script's own location, backed by tests.
- **Executable verification:** the tests, pre-commit hooks (checks run before each commit) and CI can fail a bad change.
- **Lazy loading:** path-scoped and on-demand rules keep detail out of most sessions.
- **Independent review:** when asked, a reviewer agent scores work in a fresh context, so the author doesn't mark its own work.
- **Recorded decisions:** `docs/decisions/` explains why key choices were made.

## ⚠️ Where complexity outran evidence

- **Always-on weight:** most tasks need only a fraction of the guidance that loads every session.
- **Per-turn overhead:** a prompt hook injects the response format and timing rules into every turn, including trivial ones.
- **Rules about rules:** authoring, scorecard and metadata standards add upkeep that doesn't change engineering outcomes directly.
- **Advisory controls:** most safeguards, including "ask before acting", are prose rules that rely on Claude checking itself.
- **No outcome data:** there's no record of delivery time, rework or human effort to show which components help.

## 🔍 Alignment with the reference material

- **Scope:** the practices the [SDLC relevance page](target_architecture/reference_material/anthropic_ai_native_sdlc/05_relevance.md) and [DORA applicability page](target_architecture/reference_material/dora_ai_capabilities/05_applicability.md) propose for this playbook, plus the outcome indicators every SDLC play names.
- **Source:** SDLC rows name the course stage the play belongs to, such as Build or Test.
- **Status:** ✅ aligned, 🟡 partly aligned, ❌ not yet in place.

| Practice | Source | Current repo | Status |
|---|---|---|---|
| Feedback loop | SDLC, Test | • **Has:** tests, pre-commit hooks and CI that can fail a change. | ✅ |
| Version control | DORA | • **Has:** all config versioned, with a `type(scope): description` commit format. | ✅ |
| PR review loop | SDLC, Deploy | • **Has:** a PR review skill and a read-only reviewer agent. | ✅ |
| Parallel sessions | SDLC, Build | • **Has:** a rule suggesting a separate git worktree, a second checkout of the repo, when sessions or subagents may overlap. | ✅ |
| Small batches | DORA | • **Has:** a 20-file PR limit, with an exception for `release/` branches.<br>• **Gap:** 59 of the 364 PRs merged by that commit changed 20 or more files. | 🟡 |
| Plan mode and `plan.md` | SDLC, Build | • **Has:** plan mode, where Claude proposes a plan before editing, plus a pause for approval after each phase.<br>• **Gap:** plans sit in the installed config folder, outside version control. | 🟡 |
| Lean `CLAUDE.md` | SDLC, Build | • **Has:** a 42-line `CLAUDE.md` and a skill that turns repeated corrections into rules.<br>• **Gap:** the always-on rules it brings in run far beyond one page. | 🟡 |
| Curated context | DORA | • **Has:** path-scoped and on-demand rules.<br>• **Gap:** DORA warns that irrelevant context degrades answers, yet most guidance loads every session (pp. 32–33). | 🟡 |
| Skills paired with enforcement | SDLC, Build | • **Has:** 8 skills and 4 registered hooks.<br>• **Gap:** no list shows which must-hold rules a hook, test or CI check enforces. | 🟡 |
| Hooks as approval gates | SDLC, Deploy | • **Has:** hooks for naming, file location and stale settings.<br>• **Gap:** nothing blocks a skipped confirmation. | 🟡 |
| AI stance | DORA | • **Has:** risky-action and security rules.<br>• **Gap:** uses aren't sorted into prohibited, guarded and allowed tiers (p. 18). | 🟡 |
| Continuous evals | SDLC, Test | • **Has:** repeatable test tasks for agent behaviour, with a runner that scores them on request.<br>• **Gap:** none run automatically or in CI. | 🟡 |
| Intent and spec first | SDLC, Plan and Design | • **Gap:** no `intent.md` or `spec.md` step, so requirements are often settled during implementation. | ❌ |
| Outcome measures | SDLC, every play | • **Gap:** no component has an early signal or later outcome measure recorded. | ❌ |

## 🛠️ Proposed changes to the core rule files

- **Why these two:** they are the always-on files that set Claude's guiding principles and its naming and writing standards.
- **Format:** keep both files' current shape, a principles table and a short index, and change only their content.

| File | Keep | Proposed change |
|---|---|---|
| [`guiding_principles.md`](https://github.com/paulf-999/claude_ai_playbook/blob/915685f/src/claude/rules/01_essentials/guiding_principles.md) | • **Principles:** load detail only when needed, keep changes easy to undo, grow features in stages, put essentials first, and point to live sources rather than lists that go stale.<br>• **Format:** the four-column principles table. | • **Merge overlaps:** combine the three rows on real need, token cost and automation payback into one principle, "Every component earns its cost".<br>• **Curated context:** add DORA's finding that irrelevant context degrades answers to that merged principle.<br>• **Enforce what must hold:** add the SDLC split between advisory guidance and enforced controls.<br>• **Measure outcomes:** give each new component, and each one kept after the [issue #7](https://github.com/paulf-999/ai-engineering-playbook/issues/7) review, a leading (early) and a lagging (later) indicator.<br>• **Human accountability:** state that humans own every judgement call. |
| [`claude_usage_standards.md`](https://github.com/paulf-999/claude_ai_playbook/blob/915685f/src/claude/rules/01_essentials/claude_usage_standards.md) | • **Role:** a short index of directory, naming and writing standards.<br>• **Loading:** children load on their own. | • **Change files:** for multi-file or architectural tasks, write a `spec.md` (intent and acceptance criteria) and a `plan.md` in `.claude/changes/<date>_<topic>/`, committed in the repo being changed.<br>• **Rule location:** the standard lives in the global config, while each change's files live with the change and its PR.<br>• **Current state only:** remove the "Why this file exists" history note, which breaks the writing style's own rule. |

## 🧭 Lessons for the target architecture

- **Start minimal:** begin with `CLAUDE.md`, one test command and CI, then add a component only once a real problem recurs.
- **Apply the halving test:** ask whether removing half the components would make outcomes materially worse.
- **Keep the strengths:** carry over everything under What works well unchanged.
