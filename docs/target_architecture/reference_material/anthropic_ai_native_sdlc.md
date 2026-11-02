<!-- version: 2.0.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🧭 Anthropic: The AI-native SDLC Playbook

For anyone shaping the target architecture: what Anthropic's AI-native SDLC (software development lifecycle) course recommends, where its limits are, and which parts may fit a personal playbook.

- **Source:** [The AI-native SDLC playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook), Claude Academy (Anthropic), 14 lessons, about 1 hour of reading.
- **Version:** the course publishes no date or version, and every lesson was read in full on 2026-11-02.
- **Citing:** name the lesson and that access date.
- **Labels:** the overview, plays and caveats pages report the source, while the reading and relevance pages are this playbook's interpretation.

## 📋 Executive Summary

- **What it is:** a one-hour Anthropic course of twelve "plays" for using Claude Code across six delivery stages, from planning to maintenance.
- **Core idea:** each stage leaves a versioned file for the next (`intent.md`, then `spec.md`, then `plan.md`), and humans stay accountable for every judgement call.
- **Controls:** skills and `CLAUDE.md` guide Claude, while hooks and required CI checks enforce whatever must always hold.
- **Evidence:** every play suggests an early and a later measure of success, but the course reports no measured results.
- **For this playbook:** adopt plan mode (Claude proposes a plan before editing anything) with a committed `plan.md`, a lean `CLAUDE.md` and a one-command feedback loop, and adapt most other plays to a solo maintainer.

## 📚 Pages

- **[Overview](anthropic_ai_native_sdlc/_overview.md):** the course's shape, thread and suggested starting plays.
- **[Plays by stage](anthropic_ai_native_sdlc/_plays_by_stage.md):** the twelve plays by stage, with their core practice and suggested indicators.
- **[Caveats](anthropic_ai_native_sdlc/_caveats.md):** the course's audience, evidence and vendor limits.
- **[Our reading](anthropic_ai_native_sdlc/_our_reading.md):** this playbook's reading of the course.
- **[Relevance to this playbook (proposed, not yet adopted)](anthropic_ai_native_sdlc/_relevance.md):** which plays fit a personal playbook, as a proposal.
