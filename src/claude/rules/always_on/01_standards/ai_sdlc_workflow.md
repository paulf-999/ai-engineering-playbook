# 🔄 SDLC workflow

**Purpose:** how Claude Code takes a software change from idea to merged pull request (PR), through the software development lifecycle (SDLC).

Claude loads this rule in every session. It's based on Anthropic's [AI-native SDLC course](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction).

**Flow:** settle decisions → write a plan → you approve it → build and review → merge.

## 🤝 Settle decisions

- 🎯 **Material choice:** one that changes the outcome, scope, files or published wording, or is hard to undo.
- 💬 **Discuss first:** before writing a plan, ask about material choices in rounds of up to 4 questions until none is open.
- 📌 **Minor choices:** list them as assumptions rather than ask.

## 🗺️ Plan layout

A plan is the proposal the user approves before Claude edits anything. If it's 15 lines or more, use only these sections, in order; shorter plans need no set layout:

| Section | Answers | Contains | Saved in |
|---|---|---|---|
| `Executive summary` | What was agreed? | **Outcome**, **Decisions agreed**, **Assumptions** | `plan.md` |
| `1. Intent` | Why, and how will we know it worked? | **Problem**, **Proposed outcome**, **Success**, **Affected users and systems**, **Constraints**, **Open questions** | `intent.md` |
| `2. Spec` | What changes, and what's left out? | **Change**, **Files changed**, **Why**, **Out of scope** | `spec.md` |
| `3. Plan` | Which steps, and what proves each? | Numbered steps, each with its check, and no other headings | `plan.md` |

- ✏️ **Bullets:** write each bold name as a bullet, saying "none" where empty.
- 💾 **Saving:** after approval, save these three files outside the repo, as `claude_saved_plans.md` sets out, if installed.

## 🔨 Build and review

- 🔁 **Feedback loop:** run the repo's test command, such as `make test`, before calling a step done, and fix what fails rather than skip it.
- 👀 **Review:** paste the saved files into the PR description's "Claude: Plan" section, if the repo's template has one, then check the diff against the Spec before merge.

## 🛑 Pause for approval

- 🚦 **Phase gates:** in work of 3 or more phases, each ending in something to check, such as a PR, stop after each, say what it delivered and wait for a go-ahead, unless the user waives this.

## 📚 Read on demand

- [`on_demand/01_standards/ai_sdlc_stages.md`](../../on_demand/01_standards/ai_sdlc_stages.md), in your Claude config directory (`~/.claude` by default), before work on an SDLC stage.
- [`on_demand/02_preferences/claude_saved_plans.md`](../../on_demand/02_preferences/claude_saved_plans.md), in your Claude config directory, when writing a plan, if installed.
