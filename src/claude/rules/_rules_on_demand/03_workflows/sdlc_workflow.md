<!-- version: 1.2.0 -->
<!-- created: 2026-11-10 -->
<!-- updated: 2026-11-13 -->
<!-- applies_to: * -->
<!-- miss_cost: medium — a plan skips its intent or spec, and the change drifts from what was wanted -->
# 🔄 SDLC workflow

**Purpose:** the stages a change moves through, named as in Anthropic's [AI-native SDLC course](https://academy.claude.com/courses/ai-native-sdlc-playbook), so plans and PRs share one vocabulary, and the `intent.md` and `spec.md` files each change gets.

- 📝 **Intent:** open the plan with an Intent section on why the change matters and what success looks like, which becomes the change's `intent.md` once the plan is approved.
- 📐 **Spec:** follow with a Spec section on the requirements and design, agreed before building, which becomes its `spec.md`.
- 🗺️ **Plan:** then give the steps, each with its check as `CLAUDE.md`'s "Plan with checks" asks, and refine the plan until someone new to the repo could build from it alone.
- 🔁 **Feedback loop:** run the repo's test command, such as `make test`, before calling a step done, and fix what fails rather than skip it.
- 👀 **Review:** paste the change's `spec.md` into the PR's Spec section, then before merge check the diff against it.
