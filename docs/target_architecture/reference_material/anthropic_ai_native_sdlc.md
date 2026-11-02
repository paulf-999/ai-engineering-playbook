<!-- version: 2.0.3 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🧭 Anthropic: The AI-native SDLC Playbook

For anyone shaping the target architecture: what Anthropic's AI-native SDLC (software development lifecycle) course recommends, where its limits are, and which parts may fit a personal playbook.

## 📋 Executive Summary

- **What it is:** an Anthropic course of twelve "plays", or recommended practices, for using Claude Code across six delivery stages, from planning to maintenance.
- **Core idea:** each stage leaves a versioned file for the next (`intent.md`, then `spec.md`, then `plan.md`), and humans stay accountable for every judgement call.
- **Controls:** written guidance steers Claude, such as skills (reusable instruction files) and `CLAUDE.md` (a project file Claude reads each session), while hooks (scripts triggered by Claude's actions) and required CI (continuous integration) checks enforce what must always hold.
- **Evidence:** every play suggests an early and a later measure of success, but the course reports no measured results.
- **For this playbook:** the [relevance page](anthropic_ai_native_sdlc/05_relevance.md) proposes which plays to adopt, adapt or leave out.

## 🔗 Source

- **Course:** [The AI-native SDLC playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook), Claude Academy (Anthropic), 14 lessons, about 1 hour of reading.
- **Version:** the course publishes no date or version, and every lesson was read in full on 2026-11-02.
- **Citing:** name the lesson and that access date.
- **Labels:** the overview, plays and caveats pages describe what the course says, while the reading and relevance pages give this playbook's interpretation.

## 📋 The course says: overview

- **Read:** [Overview](anthropic_ai_native_sdlc/01_overview.md), the course's shape, thread and suggested starting plays.

## 🔄 The course says: plays by stage

- **Read:** [Plays by stage](anthropic_ai_native_sdlc/02_plays_by_stage.md), each play's core practice and how to measure it.

## ⚠️ Caveats

- **Read:** [Caveats](anthropic_ai_native_sdlc/03_caveats.md), the course's audience, evidence and vendor limits.

## 🔍 Our reading

- **Read:** [Our reading](anthropic_ai_native_sdlc/04_our_reading.md), what the course means for reviewing and designing this playbook.

## 🎯 Relevance to this playbook (proposed, not yet adopted)

- **Read:** [Relevance to this playbook](anthropic_ai_native_sdlc/05_relevance.md), which plays to adopt, adapt or leave out.
