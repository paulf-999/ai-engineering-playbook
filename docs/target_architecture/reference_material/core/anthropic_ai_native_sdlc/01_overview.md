<!-- version: 1.1.2 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-11 -->
# 📋 AI-native SDLC course: Overview

**Purpose:** how Anthropic's SDLC course is structured, and where it suggests starting.

This page is part of the [summary of Anthropic's SDLC course](../anthropic_ai_native_sdlc.md). The course is built from plays: short recommended practices, each with prerequisites, steps and two measures of success.

## 🔑 Key points

The course's structure comes down to these points:

- 🧩 **Stages:** the plays are grouped by stage: plan, design, build, test, deploy and maintain.
- 📈 **Measures:** each play names a leading indicator, an early sign it's working, and a lagging indicator, a later measure of its outcome.
- 🧵 **Thread:** read across the lessons, each stage commits a file the next one uses, from `intent.md` to `spec.md` to `plan.md`. This is the repo's synthesis, since no lesson states it.
- 🙋 **Accountability:** "Humans remain accountable for every decision that requires judgment" ([Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction)).
- 🚦 **Where to start:** with the six plays that have no prerequisites: capturing intent, plan mode, `CLAUDE.md`, skills, the feedback loop and hooks as approval gates ([Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction)).
  - **Later plays:** the rest build on these, as the introduction's dependency graph shows. Subagents need `CLAUDE.md`, evals need `CLAUDE.md` and the feedback loop, PR review needs evals and subagents, CI/CD needs PR review and hooks, and closing the loop on metrics needs CI/CD and captured intent ([Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction)).
  - **Plan mode:** Claude proposes a plan before changing anything.
