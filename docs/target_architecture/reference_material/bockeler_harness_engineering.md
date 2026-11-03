<!-- version: 1.1.1 -->
<!-- created: 2026-11-03 -->
<!-- updated: 2026-11-03 -->
# 🧰 Böckeler: Harness engineering for coding agent users

**Purpose:** what Birgitta Böckeler's article on building controls around a coding agent argues, where its limits are, and what it means for this repo.

It's one of the summaries listed in this repo's [reference material](README.md).

## 📋 Executive Summary

- 🧰 **What it is:** a practitioner's model, from outside Anthropic, of the "outer harness", the controls a user adds around a coding agent.
- 💡 **Core idea:** combine guides, which steer the agent before it acts, with sensors, which check its work afterwards so it can correct itself.
- ⚙️ **Two kinds:** computational controls such as tests are fast and reliable, while inferential ones such as AI review add judgement but vary.
- ⚠️ **Limit:** checking code quality is the easy part, and checking that software does what's needed is still unsolved.

## 🔗 Source

- 📄 **Article:** [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html), Birgitta Böckeler (Thoughtworks), on martinfowler.com.
- 📅 **Version:** published 2026-04-02, replacing a memo from 2026-02-17, so cite the section heading.
- 🗓️ **Captured:** 2026-11-03, after reading the whole article.

## 📋 The article says

The article makes these points, by section:

- 🧭 **Guides and sensors:** with only sensors an agent repeats its mistakes, and with only guides it never learns whether they worked ("Feedforward and Feedback").
- ⚙️ **Computational and inferential:** deterministic checks are cheap enough to run on every change, while model-based ones are slower and less predictable ("Computational vs Inferential").
- 🔁 **Steering loop:** whenever an issue recurs, the person improves the guides and sensors so it's less likely next time ("The steering loop").
- 🧪 **Behaviour is unsolved:** relying on AI-written tests to show code behaves correctly is "not good enough yet" ("Behaviour harness").

### ➕ Also in the article

- 🧑 **The human's role:** a harness should "direct" human input to where it matters most, not remove it ("The role of the human").
- ❓ **Open question:** whether a sensor that never fires means good code or poor detection ("A starting point - and open questions").

## 🎯 What it means for this repo

This section is this repo's reading, not the article's, and the principles named are in this repo's [design principles](../design_principles/01_principles.md):

- 🗺️ **Mapping:** `CLAUDE.md`, rules and skills are inferential guides, while pre-commit hooks, tests and CI are computational sensors.
- 🔒 **Enforcement:** preferring computational sensors for what must hold is "Enforce what must hold", with a source outside Anthropic.
- 🔁 **Task log:** the steering loop matches adding a component only after a gap recurs in the [task log](../../maintenance/task_log.md), this repo's record of real tasks.
- 🗑️ **Retiring:** a check that never fires may be working, so retiring parts unused between reviews should apply to guidance, not sensors.
- ⚠️ **Limit:** it's one practitioner's model, written for teams, with no measured results.
