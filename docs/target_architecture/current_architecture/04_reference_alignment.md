<!-- version: 1.1.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# 🔍 Current architecture: Alignment with the reference material

**Purpose:** how far the old Claude configuration already follows Anthropic's SDLC course and DORA's research.

This page is part of the [current architecture](../current_architecture.md) review of commit `915685f`. It uses two sources:

- 🔄 **SDLC course:** Anthropic's [course on the AI-native software development lifecycle](../reference_material/anthropic_ai_native_sdlc.md), built from short practices it calls plays.
- 📊 **DORA:** the [AI Capabilities Model from DevOps Research and Assessment](../reference_material/dora_ai_capabilities.md), cited by printed page.

## ✅ In place

| Practice | Source | What the old setup has |
|---|---|---|
| 🔁 Feedback loop | SDLC | Tests, pre-commit hooks and CI that can fail a change |
| 🗃️ Version control | DORA | All config versioned, with a set commit-message format |
| 👀 PR review | SDLC | A PR review skill and a read-only reviewer agent |
| 🌳 Parallel sessions | SDLC | A rule to use a separate checkout when sessions may overlap |

## 🟡 Partly in place

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

## ❌ Not yet in place

| Practice | Source | What's missing |
|---|---|---|
| 📝 Intent and spec first | SDLC | No step to write down intent and requirements before building |
| 📈 Outcome measures | SDLC | No component records an early signal or a later result |
