<!-- version: 1.0.0 -->
<!-- created: 2026-11-10 -->
<!-- updated: 2026-11-10 -->
<!-- applies_to: * -->
<!-- miss_cost: medium — a plan skips its intent or spec, and the change drifts from what was wanted -->
<!-- loading: on demand — read when claude_plans.md's pointer sends Claude here, while drafting a plan -->
# 🔄 SDLC workflow

**Purpose:** the stages a change moves through, named as in Anthropic's [AI-native SDLC course](https://academy.claude.com/courses/ai-native-sdlc-playbook), so plans and PRs share one vocabulary.

- 📝 **Intent:** open the plan with why the change matters and what success looks like, standing in for `intent.md`, the course's first file in a change.
- 📐 **Spec:** follow with the requirements and design, agreed before building, standing in for `spec.md`, the course's second file.
- 🗺️ **Plan:** then give the steps, each with its check as `CLAUDE.md`'s "Plan with checks" asks, and refine the plan until someone new to the repo could build from it alone.
- 🔁 **Feedback loop:** run the repo's test command, such as `make test`, before calling a step done, and fix what fails rather than skip it.
- 👀 **Review:** before merge, check the PR's diff against the plan's Spec.
