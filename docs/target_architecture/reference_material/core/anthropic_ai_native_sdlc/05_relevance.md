# 🎯 AI-native SDLC course: Relevance to this playbook

**Purpose:** which of the course's plays suit this repo, as decided at the maintainer's review, with the ones it has adopted recorded in the [target architecture's workflow](../../../target_architecture.md#-workflow).

This page is part of the [summary of Anthropic's SDLC course](../anthropic_ai_native_sdlc.md). Each row adopts a play as it is, adapts it, defers it or leaves it out:

| Play | Decision | Why |
|---|---|---|
| 📝 Capture intent, requirements and design | Adapt | Intent and Spec sections at the top of each plan, saved as `intent.md` and `spec.md` once it is approved, suit a single maintainer, who also acts as product owner |
| 🗺️ Plan mode and `plan.md` | Adapt | Plans stay in the Claude config directory, since this repo's config is installed there rather than worked on in each repo |
| 📘 `CLAUDE.md` | Adapt | The always-on token budget replaces the one-page limit, and a fix still goes in once Claude repeats a mistake |
| 🧠 Skills | Adopt | Only for knowledge that must be applied consistently, backed by a hook or CI check, as the course advises, though none ship yet |
| 🔀 Parallel sessions and subagents | Adapt | Separate checkouts fit, but one reviewer limits how many sessions help |
| 🔁 Feedback loop | Adopt | `make test` and `pre-commit run --all-files` already give one command each |
| 🧪 Continuous evals | Deferred | A small set of repeatable test tasks is feasible, once API cost and upkeep are weighed |
| 👀 PR review loop | Adapt | A fresh-context reviewer agent fills each config PR's evaluation criteria in place of a `REVIEW.md`, though a solo maintainer can't separate author and approver |
| 🚧 Hooks as approval gates | Adapt | User-level hooks that `make install` registers and keeps in step, such as the plan sections hook, since a personal setup has no managed settings |
| 🚀 CI/CD integration, closing the loop on metrics | Out of scope for now | Both need a deployed service, which this repo doesn't have |
