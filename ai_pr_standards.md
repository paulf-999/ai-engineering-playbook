# 🤖 AI PR standards

**Purpose:** nine rules for pull requests (PRs) that use AI, grouped by stage.

They cover PRs only. For data and access, see the [security rule](src/claude/rules/always_on/01_standards/security.md).

## ✍️ Before opening a PR

- **1. Named author:** a person, never an agent, must be the PR's named author.
- **2. Reasons:** you must explain why the complex or non-obvious parts are there. AI can draft it, but you approve it, and the PR says so as "Drafted by AI, approved by <name>".
- **3. What was run:** you must report each check that was run, who ran it (you, the AI or CI) and its result.
- **4. Unneeded additions:** you should remove anything the AI added that the task didn't need.
- **5. Existing tools:** you must prefer existing tools over custom AI-written code, and give the reason when a dependency file changes.

## 📬 Opening a PR

- **6. Pace:** agents must not open PRs faster than reviewers can clear them, so an author can have three open.
- **7. One topic:** you must give the agent one topic per PR, and split what it produces.

## 👀 Reviewing a PR

- **8. Right approver:** you shouldn't shop for an approval, or count an AI review as one.
- **9. Guardrails:** AI shouldn't change its own guardrails, the files that set or run these checks, without review.

## ⚖️ How strict each rule is

- 🟡 **Should or must:** a rule is a "should" until a required check covers some of it, and then becomes a "must".
- 🧾 **Evidence, not truth:** a check proves that evidence exists, such as a written reason, not that it's true or the author's own.
- 🚦 **Review status:** `git-review-pr` sets `ai_pr_standards_review` on the commit it reviewed, which fails while a Must or Should finding is neither fixed nor declined with a reason.
  - **Limit:** anyone with write access could set it by hand.
- 📌 **Which copy applies:** `git-review-pr` judges a PR by the base branch's copy of this file, so a PR can't relax the rules it's judged by.
