<!-- created: 2026-11-10 -->
<!-- applies_to: * -->
<!-- miss_cost: medium — a plan skips its intent or spec, or multi-phase work runs past a wrong turn and needs redoing -->
# 🔄 SDLC workflow

**Purpose:** the stages a change moves through, named as in Anthropic's AI-native SDLC course, and when to pause for the user's approval.

- 📝 **Intent:** open a plan of 15 lines or more with an Intent section on why the change matters and what success looks like.
- 📐 **Spec:** follow with a Spec section on the requirements and design, agreed before building.
- 🗺️ **Plan:** then give the steps, each with its check.
- 🔁 **Feedback loop:** run the repo's test command, such as `make test`, before calling a step done, and fix what fails rather than skip it.
- 👀 **Review:** paste the Spec section into the PR's "Plan Spec" section, then before merge check the diff against it.

## 🛑 Pausing for approval

- 🛑 **Phase gates:** for work of 3 or more phases, each a stage that ends in something the user can check, such as a PR, stop after each phase, say what it delivered, and wait for a go-ahead, since early feedback stops wasted phases.
  - **Skip when:** the user waives gates, or the work has a single phase.

## 📚 Read on demand

- `on_demand/workflows/saving_plans.md`, in your Claude config directory, once a plan is approved.
