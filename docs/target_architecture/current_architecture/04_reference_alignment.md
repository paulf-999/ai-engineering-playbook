<!-- version: 1.0.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🔍 Current architecture: Alignment with the reference material

For anyone shaping the target architecture: how far the repo already follows the Anthropic SDLC course and DORA findings.

- **Part of:** [Current architecture](../current_architecture.md).
- 📌 **Snapshot:** everything here describes [`claude_ai_playbook`](https://github.com/paulf-999/claude_ai_playbook) at commit `915685f`, dated 2026-10-31.
- 🔄 **SDLC:** software development lifecycle, from Anthropic's [AI-native SDLC course](../reference_material/anthropic_ai_native_sdlc.md).
- 📊 **DORA:** DevOps Research and Assessment, whose [AI Capabilities Model](../reference_material/dora_ai_capabilities.md) is cited by printed page number.

## 🗺️ Reading the table

- 🎯 **Scope:** the practices the [SDLC relevance page](../reference_material/anthropic_ai_native_sdlc/05_relevance.md) and [DORA applicability page](../reference_material/dora_ai_capabilities/05_applicability.md) propose for this playbook, plus the outcome indicators every SDLC play names.
- 📚 **Source:** SDLC rows name the course stage the play belongs to, such as Build or Test.
- 🚦 **Status:** ✅ aligned, 🟡 partly aligned, ❌ not yet in place.

| Practice | Source | Current repo | Status |
|---|---|---|---|
| 🔁 Feedback loop | SDLC, Test | Tests, pre-commit hooks and CI that can fail a change. | ✅ |
| 🗃️ Version control | DORA | All config versioned, with a `type(scope): description` commit format. | ✅ |
| 👀 PR review loop | SDLC, Deploy | A PR review skill and a read-only reviewer agent. | ✅ |
| 🌳 Parallel sessions | SDLC, Build | A rule suggesting a separate git worktree, a second checkout of the repo, when sessions or subagents may overlap. | ✅ |
| 📦 Small batches | DORA | • **Has:** a 20-file PR limit, except for `release/` branches.<br>• **Gap:** 59 of the 364 PRs merged by that commit changed 20+ files. | 🟡 |
| 🗂️ Plan mode and `plan.md` | SDLC, Build | • **Has:** plan mode, where Claude proposes a plan first, with an approval pause per phase.<br>• **Gap:** plans sit in the installed config, unversioned. | 🟡 |
| 🪶 Lean `CLAUDE.md` | SDLC, Build | • **Has:** a 42-line `CLAUDE.md` and a skill turning repeated corrections into rules.<br>• **Gap:** the always-on rules it imports run far beyond one page. | 🟡 |
| 🎯 Curated context | DORA | • **Has:** path-scoped and on-demand rules.<br>• **Gap:** DORA warns that irrelevant context degrades answers, yet most guidance loads every session (pp. 32–33). | 🟡 |
| 🛠️ Skills paired with enforcement | SDLC, Build | • **Has:** 8 skills and 4 registered hooks.<br>• **Gap:** no list shows which must-hold rules a hook, test or CI check enforces. | 🟡 |
| 🪝 Hooks as approval gates | SDLC, Deploy | • **Has:** hooks for naming, file location and stale settings.<br>• **Gap:** nothing blocks a skipped confirmation. | 🟡 |
| 🧭 AI stance | DORA | • **Has:** risky-action and security rules.<br>• **Gap:** uses aren't sorted into prohibited, guarded and allowed tiers (p. 18). | 🟡 |
| 🧪 Continuous evals | SDLC, Test | • **Has:** repeatable test tasks for agent behaviour, with a runner that scores them on request.<br>• **Gap:** none run automatically or in CI. | 🟡 |
| 📝 Intent and spec first | SDLC, Plan and Design | No `intent.md` or `spec.md` step, so requirements are often settled during implementation. | ❌ |
| 📈 Outcome measures | SDLC, every play | No component has an early signal or later outcome measure recorded. | ❌ |
