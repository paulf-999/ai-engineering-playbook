<!-- version: 1.2.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# 🔎 DORA report: Findings worth carrying forward

**Purpose:** specific findings from DORA's report that are worth using in this repo's design.

This page is part of the [summary of DORA's AI Capabilities Model](../dora_ai_capabilities.md), and "p." means the report's printed page, one less than the PDF page. This page uses these terms:

- 🥇 **Gold-standard code:** the repositories and branches that best show current conventions.
- 🗺️ **Value stream mapping:** drawing every step from idea to production to find where work waits.

## 📦 Small batches and version control

The report recommends these habits:

- 📏 **Batch size:** "Any batch of code that takes longer than a week to complete is too big", with a daily commit to trunk (p. 48).
- ⚖️ **Trade-off:** small batches slightly reduce how effective people feel, which the report judges worth it for product performance (pp. 46–48).
- 🤖 **Agent files:** keep files such as `CLAUDE.md` and AI prompts in version control, as about 21% of respondents do for prompts (pp. 39–40).
- ✍️ **Commit messages:** explain why, for example with Conventional Commits (p. 40).

## 🤖 AI context

These findings cover what to give AI:

- 🧠 **Curate it:** give AI relevant context rather than volume, since irrelevant context degrades its answers (pp. 32–33).
  - **Code:** index only gold-standard code.
- 📚 **Distil it:** have AI summarise a key source, then have a human expert check the summary (p. 32).

## 🏢 Stance, users and planning

These findings sit beyond the code itself:

- 🚦 **AI stance:** sort uses into prohibited, permitted with guardrails, and allowed (p. 18).
- 📝 **Spec-driven development:** writing requirements before code, named as an emerging way to keep AI-written code aligned with users (p. 55).
- 🗺️ **Value stream mapping:** it strengthens AI's effect on organisational performance (p. 74).
- 🎯 **Prioritisation:** the report's guide to choosing what to improve first weighs what a team can change by itself (p. 90), which in a one-person repo is almost everything.
