<!-- version: 1.1.1 -->
<!-- created: 2026-11-03 -->
<!-- updated: 2026-11-03 -->
# 🧪 Anthropic: Demystifying evals for AI agents

**Purpose:** what Anthropic's engineering article on evals, automated tests that score an AI agent's work, recommends, where its limits are, and what it means for this repo.

It's one of the summaries listed in this repo's [reference material](README.md).

## 📋 Executive Summary

- 🧪 **What it is:** Anthropic's field guide to building evals for agents, drawn from its own and its customers' work.
- 💡 **Core idea:** start small with tasks taken from real failures, and grade what the agent produced rather than the steps it took.
- 🔍 **Trust:** read the transcripts before believing a score, because broken tasks and graders are common.
- 🎯 **For this repo:** it gives a method for testing whether each part of the Claude setup still helps.

## 🔗 Source

- 📄 **Article:** [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), by Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares and Jiri De Jonghe, Anthropic Engineering.
- 📅 **Version:** published 2026-01-09, so cite the section heading.
- 🗓️ **Captured:** 2026-11-03, after reading the whole article.

## 📋 The article says

The article makes these points, by section:

- 🌱 **Start early and small:** 20–50 simple tasks drawn from real failures is "a great start" ("Step 0. Start early").
- ⚖️ **Test both directions:** check when a behaviour should happen and when it shouldn't, or the agent learns to overdo it ("Step 3: Build balanced problem sets").
- 🎯 **Grade the outcome:** prefer code-based graders, and judge what the agent produced, not the path it took ("Step 5: Design graders thoughtfully").
- 🔁 **Capability and regression:** capability evals start with a low pass rate, while regression evals stay near 100% to catch backsliding ("Capability vs. regression evals").
- 🔍 **Read the transcripts:** Anthropic doesn't take a score "at face value" until someone has read some ("Step 7: Monitor for capability eval saturation").

### ➕ Also in the article

- 🎲 **Repeated trials:** agents vary between runs, so one pass or fail says little about a task (the section on non-determinism).
- 🚫 **Broken tasks:** a task no strong model ever passes usually means the task or grader is broken ("Step 2: Write unambiguous tasks with reference solutions").

## 🎯 What it means for this repo

This section is this repo's reading, not the article's:

- 📒 **Task log as test set:** the [task log](../../maintenance/task_log.md), this repo's record of real tasks, can supply the "real failures" to start from.
- 🔪 **Halving test:** the [halving test](../design_principles/01_principles.md#-numbers-and-tests) asks whether removing half the setup would hurt, and rerunning logged tasks with and without a part would measure it.
- ⚖️ **Skill triggers:** testing when a skill should and shouldn't run guards against it running too often.
- ⚠️ **Limit:** it's written for teams building agent products, and its evidence is case studies.
