# 🤖 AI PR standards

**Purpose:** nine rules for pull requests (PRs) that use AI, grouped by stage.

They cover PRs only. For data and access, see the [security rule](src/claude/rules/always_on/01_standards/security.md).

## ✍️ Before opening a PR

- **1. Named author:** a person, never an agent, should be the PR's named author.
- **2. Reasons:** explain, in your own words, why the complex or non-obvious parts are there.
- **3. What you ran:** report what you ran yourself, not what the AI says it ran.
- **4. Unneeded additions:** remove anything the AI added that the task didn't need.
- **5. Existing tools:** prefer existing tools over custom AI-written code.

## 📬 Opening a PR

- **6. Pace:** don't let agents open PRs faster than reviewers can clear them.
- **7. One topic:** give the agent one topic per PR, and split what it produces.

## 👀 Reviewing a PR

- **8. Right approver:** don't shop for an approval, and don't count an AI review as one.
- **9. Guardrails:** AI shouldn't change its own guardrails, the files that set or run these checks, without review.

## ⚖️ How strict each rule is

- 🟡 **Should:** every rule here is a "should" until a required check enforces it, and then becomes a "must".
- 🧾 **Evidence, not truth:** a check proves that evidence exists, such as a written reason, not that it's true or the author's own.
- 📌 **Which copy applies:** `git-review-pr` judges a PR by the base branch's copy of this file, so a PR can't relax the rules it's judged by.
