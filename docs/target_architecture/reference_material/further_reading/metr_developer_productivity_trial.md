<!-- version: 1.3.3 -->
<!-- created: 2026-11-03 -->
<!-- updated: 2026-11-10 -->
# ⚖️ METR: AI and experienced open-source developers

**Purpose:** what METR's randomised controlled trial found about early-2025 AI tools and experienced developers' speed, where its limits are, and what it means for this repo.

It's one of the summaries listed in this repo's [reference material](../README.md).

## 📋 Executive Summary

- ⚖️ **What it is:** a randomised controlled trial with experienced developers working on their own projects.
- 📉 **Finding:** with AI allowed, 16 experienced developers took 19% longer on 246 real tasks in their own mature projects (Abstract).
- 🪞 **Perception gap:** the same developers believed afterwards that AI had cut their time by 20% (Abstract).
- 🎯 **For this repo:** measure what a component does, rather than trusting how helpful it feels.

## 🔗 Source

- 📄 **Paper:** [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089), Joel Becker, Nate Rush, Beth Barnes and David Rein, METR (Model Evaluation & Threat Research).
- 📅 **Version:** arXiv v2, revised 2025-07-25, CC BY 4.0, so cite the section.
- 🗓️ **Captured:** 2026-11-03, after reading the main text and Appendices B and C.1.

## 📋 The paper says

The paper reports these points, by section:

- 🧪 **Design:** developers listed real issues and forecast each one's time before a coin flip allowed or barred AI for it (2.2).
- 🛠️ **Tools:** mostly Cursor Pro with Claude 3.5 and 3.7 Sonnet, the frontier of February to June 2025 (Abstract).
- 🔮 **Forecasts:** developers expected a 24% speed-up, and economics and machine learning experts expected 39% and 38% (3.1).
- ⏱️ **Where time went:** with AI, developers coded and searched less, and prompted, waited, reviewed output and idled more (3.2).
- 🔍 **Causes:** 5 of 21 candidate factors had evidence behind them, including over-optimism, familiarity with the code, and AI missing unwritten project knowledge (3.3, C.1).

### ➕ Also in the paper

- ✅ **Acceptance:** developers accepted under 44% of Cursor's suggestions, and spent about 9% of AI-allowed time reviewing and cleaning its output (C.1.4).
- 🚫 **Not shown:** that AI fails to speed up most developers, other settings or future tools (Appendix B).

## 🎯 What it means for this repo

This section is this repo's reading, not the paper's:

- 📏 **Measure, don't ask:** pair [component feedback](../../target_architecture.md#-measures), itself a self-report, with evidence from session transcripts and git history.
- 🧠 **Unwritten knowledge:** AI lacking tacit project knowledge supports writing it into `CLAUDE.md`.
- 🔄 **Contrast with DORA:** the [DORA research summarised here](../core/dora_ai_capabilities.md) rests on surveys, while this trial timed real tasks directly.
- ⚠️ **Limit:** 16 developers on 2025 tools, so a caution, not evidence that current tools slow anyone down.
