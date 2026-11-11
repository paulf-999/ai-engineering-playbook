<!-- version: 1.1.2 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-11 -->
# 🎯 AI-native SDLC course: Relevance to this playbook

**Purpose:** which of the course's plays suit this repo, as a proposal not yet adopted.

This page is part of the [summary of Anthropic's SDLC course](../anthropic_ai_native_sdlc.md). Each row proposes adopting a play as it is, adapting it, or leaving it out:

| Play | Proposed | Why |
|---|---|---|
| 📝 Capture intent, requirements and design | Adapt | Intent and Spec sections at the top of each plan, saved as `intent.md` and `spec.md` once it is approved, suit a single maintainer, who also acts as product owner |
| 🗺️ Plan mode and `plan.md` | Adapt | Plans stay in the Claude config directory, since this repo's config is installed there rather than worked on in each repo |
| 📘 `CLAUDE.md` | Adopt | Its one-page limit, and adding a fix once Claude repeats a mistake, are both easy to check |
| 🧠 Skills | Adapt | Only for knowledge that must be applied consistently, backed by a hook or CI check |
| 🔀 Parallel sessions and subagents | Adapt | Separate checkouts fit, but one reviewer limits how many sessions help |
| 🔁 Feedback loop | Adopt | `make test` and `pre-commit run --all-files` already give one command each |
| 🧪 Continuous evals | Adapt | A small set of repeatable test tasks is feasible, once API cost and upkeep are weighed |
| 👀 PR review loop | Adapt | A review checklist fits, though a solo maintainer can't separate author and approver |
| 🚧 Hooks as approval gates | Adapt | Project hooks only, since a personal setup has no admin-locked settings |
| 🚀 CI/CD integration, closing the loop on metrics | Out of scope for now | Both need a deployed service, which this repo doesn't have |
