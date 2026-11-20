# 🔄 SDLC workflow

**Purpose:** the stages a change moves through, named as in Anthropic's AI-native SDLC course, and when to pause for the user's approval.

- 📝 **Intent:** open a plan of 15 lines or more with an Intent section of **Why** and **Success** bullets.
- 📐 **Spec:** follow with a Spec section, agreed before building, of **Change**, **Files changed**, **Why** and **Out of scope** bullets, in that order.
- 🗺️ **Plan:** end with numbered Verification steps, each with its check, and no other headings.
- 🔁 **Feedback loop:** run the repo's test command, such as `make test`, before calling a step done, and fix what fails rather than skip it.
- 👀 **Review:** paste the Spec into the PR's "Plan Spec" section when it has one, then check the diff against it before merge.

## 🛑 Pausing for approval

- 🛑 **Phase gates:** for work of 3 or more phases, each ending in something the user can check, such as a PR, stop after each, say what it delivered and wait for a go-ahead, since early feedback stops wasted phases.
  - **Skip when:** the user waives gates, or the work has a single phase.
