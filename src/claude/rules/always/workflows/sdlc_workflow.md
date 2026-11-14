<!-- created: 2026-11-10 -->
<!-- applies_to: * -->
<!-- miss_cost: medium — a plan skips its intent or spec, or multi-phase work runs past a wrong turn and needs redoing -->
# 🔄 SDLC workflow

**Purpose:** the stages a change moves through, named as in Anthropic's [AI-native SDLC course](https://academy.claude.com/courses/ai-native-sdlc-playbook), so plans and PRs share one vocabulary, and when to pause for the user's approval.

- 📝 **Intent:** open the plan with an Intent section on why the change matters and what success looks like, which becomes the change's `intent.md` once the plan is approved.
- 📐 **Spec:** follow with a Spec section on the requirements and design, agreed before building, which becomes its `spec.md`.
- 🗺️ **Plan:** then give the steps, each with its check as `CLAUDE.md`'s "Plan with checks" asks, and refine the plan until someone new to the repo could build from it alone.
- 🔁 **Feedback loop:** run the repo's test command, such as `make test`, before calling a step done, and fix what fails rather than skip it.
- 👀 **Review:** paste the change's `spec.md` into the PR's "Plan Spec" section, then before merge check the diff against it.

## 🛑 Pausing for approval

- 🛑 **Phase gates:** for work of 3 or more phases, each a stage that ends in something the user can check, such as a PR, stop after each phase, say what it delivered, and wait for a go-ahead, since early feedback stops wasted phases.
  - **Skip when:** the user waives gates, or the work has a single phase.
- 🗂️ **Plan approval:** the "Implement the following plan:" message Claude Code sends after you accept a plan isn't a go-ahead, so wait for an explicit one.

## 📚 Read on demand

- `on_demand/workflows/saving_plans.md`, in your Claude config directory, once a plan is approved.
