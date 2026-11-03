<!-- version: 1.0.0 -->
<!-- created: 2026-11-03 -->
<!-- updated: 2026-11-03 -->
# 📈 DORA: State of AI-assisted Software Development 2025

**Purpose:** what DORA's 2025 survey found about AI adoption and its outcomes, where its limits are, and what it means for this repo.

It's one of the summaries listed in this repo's [reference material](README.md), and leaves out the report's seven capabilities, which have their [own summary](dora_ai_capabilities.md).

## 📋 Executive Summary

- 📊 **What it is:** DORA's annual survey, run from 13 June to 21 July 2025, with 4,867 respondents and 78 interviews (pp. 4, 103, 115).
- 📈 **Finding:** higher AI adoption goes with more throughput and better individual, team and product outcomes, but also more delivery instability (p. 38).
- 🎯 **For this repo:** speed at the keyboard reaches outcomes only if checking keeps up, so measure outcomes rather than feel.

## 🔗 Source

- 📄 **Report:** [State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/), v. 2025.2, Google LLC with IT Revolution, CC BY-NC-SA 4.0 (pp. 97, 141).
- 🗓️ **Captured:** 2026-11-03, after reading in full the PDF linked from [cloud.google.com/dora](https://cloud.google.com/dora).
- 🔢 **Page numbers:** "p." means the printed page, which in this report matches the PDF page.

## 📋 The report says

- 🤖 **Adoption:** 90% use AI at work, for a median of two hours a day, and over 80% feel more productive (pp. 24–25, 30).
- 🤔 **Trust:** 30% have "a little" or "no trust at all" in AI output, which the report calls healthy scepticism (pp. 5, 31).
- 📉 **Stubborn outcomes:** adoption has no link with friction or burnout, and instability still hurts product performance despite faster delivery (pp. 39, 41).
- 🔀 **Friction moves:** it "shifts from manual grind to deciding and verifying", such as vetting code that only looks correct (p. 40).
- ⚙️ **Customisation:** a UC Berkeley study of student developers recommends repo-level config files so AI tools follow a project's conventions (p. 28).

## ⚠️ Limits

- 🔗 **Comparisons, not effects:** the authors present their estimates as comparisons between similar people, not proven causes (p. 48, note 20).
- 🙋 **Self-report:** every outcome, throughput and instability included, comes from survey answers (pp. 138–139).
- 🏢 **Publisher:** Google Cloud runs DORA and GitHub wrote a chapter (pp. 8, 79), and both sell AI coding tools, so they gain from good news about AI.

## 🎯 What it means for this repo

This section is this repo's reading, not the report's:

- 📏 **Outcomes over feel:** high felt productivity beside rising instability backs logging [rework and interventions](../target_architecture.md#-measures), not just whether Claude seemed helpful.
- 🧾 **Config needs evidence:** the Berkeley advice fits a `CLAUDE.md`, but that study never tested config files, so each component still has to earn its place.
- ⚖️ **Contrast with METR:** the report cites [METR's trial](metr_developer_productivity_trial.md), where timed tasks showed developers felt faster while being slower, a gap a survey can't rule out (p. 35).
