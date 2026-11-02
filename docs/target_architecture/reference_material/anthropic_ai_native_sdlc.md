<!-- version: 2.0.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🧭 Anthropic: The AI-native SDLC Playbook

For anyone shaping the target architecture: what Anthropic's AI-native SDLC (software development lifecycle) course recommends, where its limits are, and which parts may fit a personal playbook.

## 📋 Executive Summary

- **What it is:** an Anthropic course of twelve "plays", or recommended practices, for using Claude Code across six delivery stages, from planning to maintenance.
- **Core idea:** each stage leaves a versioned file for the next (`intent.md`, then `spec.md`, then `plan.md`), and humans stay accountable for every judgement call.
- **Controls:** written guidance such as skills and `CLAUDE.md` steers Claude, while hooks and required CI checks, which run automatically, enforce what must always hold.
- **Evidence:** every play suggests an early and a later measure of success, but the course reports no measured results.
- **For this playbook:** three plays fit as they are: plan mode (Claude proposes a plan before editing) with a committed `plan.md`, a lean `CLAUDE.md`, and a one-command feedback loop.

## 🔗 Source

- **Course:** [The AI-native SDLC playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook), Claude Academy (Anthropic), 14 lessons, about 1 hour of reading.
- **Version:** the course publishes no date or version, and every lesson was read in full on 2026-11-02.
- **Citing:** name the lesson and that access date.
- **Labels:** the overview, plays and caveats pages report the source, while the reading and relevance pages are this playbook's interpretation.

## 📚 Pages

- **[Overview](anthropic_ai_native_sdlc/_overview.md):** the course's shape, thread and suggested starting plays.
- **[Plays by stage](anthropic_ai_native_sdlc/_plays_by_stage.md):** each play's core practice and how to measure it.
- **[Caveats](anthropic_ai_native_sdlc/_caveats.md):** the course's audience, evidence and vendor limits.
- **[Our reading](anthropic_ai_native_sdlc/_our_reading.md):** what the course means for reviewing and designing this playbook.
- **[Relevance to this playbook (proposed, not yet adopted)](anthropic_ai_native_sdlc/_relevance.md):** which plays to adopt, adapt or leave out.
