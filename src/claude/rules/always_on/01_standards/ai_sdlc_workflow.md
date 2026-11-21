# 🔄 SDLC workflow

**Purpose:** the stages a change moves through, named as in Anthropic's AI-native SDLC course, and when to pause for the user's approval.

- 📝 **Intent:** open a plan of 15 lines or more with a `1. Intent` section whose first line reads "Why this change is needed, and how we'll know it worked.", then **Why** and **Success** bullets.
- 📐 **Spec:** follow with a `2. Spec` section, agreed before building, whose first line reads "What changes, in which files, and what's deliberately left out.", then **Change**, **Files changed**, **Why** and **Out of scope** bullets, in that order.
- 🗺️ **Plan:** end with a `3. Verification` section whose first line reads "The steps to build it, each with the check that proves it's done.", then numbered steps, each with its check, and no other headings.
- 🔁 **Feedback loop:** run the repo's test command, such as `make test`, before calling a step done, and fix what fails rather than skip it.
- 👀 **Review:** paste the Spec into the PR's "Plan Spec" section when it has one, then check the diff against it before merge.

## 🛑 Pausing for approval

- 🛑 **Phase gates:** for work of 3 or more phases, each ending in something the user can check, such as a PR, stop after each, say what it delivered and wait for a go-ahead, since early feedback stops wasted phases.
  - **Skip when:** the user waives gates, or the work has a single phase.
