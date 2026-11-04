<!-- version: 2.1.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-04 -->
# 🏛️ Current architecture

**Purpose:** what the Claude configuration this repo replaces contains, what works well in it, and the lessons the new design carries forward.

That configuration is [`claude_ai_playbook`](https://github.com/paulf-999/claude_ai_playbook), a personal Claude Code setup installed on each machine with `make install`. These pages describe it at commit `915685f`, dated 2026-10-31.

## 📋 Executive Summary

- 💪 **Strengths:** a safe installer, a real test suite and automated checks make it reproducible and portable.
- ⚠️ **Main risk:** about 30,000 tokens of rules load into every session, whatever the task.
- 🔍 **Against the reference material:** it has a strong feedback loop, but no step for capturing intent first and no outcome measures.
- 🎯 **For the new design:** start small, and reshape two core rule files around those findings.

## 📖 The pages

Read them in this order:

1. [Snapshot of each component](current_architecture/01_snapshot.md), with its size, how it loads and what it's for.
2. [Strengths to keep](current_architecture/02_what_works_well.md).
3. [Where complexity outran evidence](current_architecture/03_complexity_without_evidence.md).
4. [Alignment with Anthropic's SDLC course and DORA research](current_architecture/04_reference_alignment.md).
5. [Proposed changes to two core rule files](current_architecture/05_proposed_changes.md).

## 🎓 Lessons for the new design

- 🌱 **Start minimal:** begin with `CLAUDE.md`, one test command and CI, then port components in small batches, each checked for the patterns that made this setup costly.
- 🔪 **Halving test:** ask whether removing half the components would make results noticeably worse.
- 💪 **Keep the strengths:** carry over everything on the strengths page.
