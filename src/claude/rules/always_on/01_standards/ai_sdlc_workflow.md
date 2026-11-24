# 🔄 SDLC workflow

**Purpose:** how to plan and ship a change, adapted from Anthropic's [AI-native SDLC course](https://academy.claude.com/courses/ai-native-sdlc-playbook).

## 🤝 Settling decisions

- 🎯 **Material choice:** one that changes the outcome, scope, files or published wording, or is hard to undo.
- 💬 **Discuss first:** before writing a plan, ask about material choices in rounds of up to 4 questions until none is open.
- 📌 **Minor choices:** list them as assumptions rather than ask.

## 🗺️ Plan layout

A plan of 15 lines or more has only these sections, in order. Open each with its first line, if it has one, then add what follows.

| Section | First line | Then |
|---|---|---|
| `Executive summary` | None | **Outcome**, **Decisions agreed** and **Assumptions** bullets, saying "none" where there are none |
| `1. Intent` | "Why this change is needed, and how we'll know it worked." | **Why** and **Success** bullets |
| `2. Spec` | "What changes, in which files, and what's deliberately left out." | **Change**, **Files changed**, **Why** and **Out of scope** bullets, agreed before building |
| `3. Plan` | "The steps to build it, each with the check that proves it's done." | Numbered steps, each with its check, and no other headings |

- 💾 **Saved files:** once you approve, the saved-plans preference, if installed, saves the sections as `intent.md`, `spec.md` and `plan.md`, which keeps the summary.

## 🔨 Building and review

- 🔁 **Feedback loop:** run the repo's test command, such as `make test`, before calling a step done, and fix what fails rather than skip it.
- 👀 **Review:** paste the Spec into the PR's "Plan Spec" section when it has one, then check the diff against it before merge.

## 🛑 Pausing for approval

- 🛑 **Phase gates:** for work of 3 or more phases, each ending in something the user can check, such as a PR, stop after each, say what it delivered and wait for a go-ahead, since early feedback stops wasted phases.
  - **Skip when:** the user waives gates, or the work has a single phase.
