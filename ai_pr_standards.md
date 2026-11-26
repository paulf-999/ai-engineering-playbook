# 🤖 AI PR standards

> [!NOTE]
> **Work in progress:** these rules are on trial, so the review status, human-author and open-PR checks report but don't block a merge.

**Purpose:** six rules for pull requests (PRs) that use AI, grouped by stage.

They cover PRs only. For data and access, see the [security rule](src/claude/rules/always_on/01_standards/security.md).

## ✍️ Before opening a PR

- **1. Named author:** a person, never an agent, should be the PR's author or assignee, though Dependabot's PRs need neither.
- **2. Unneeded additions:** you should remove anything the AI added that the task didn't need.
- **3. Existing tools:** you must prefer existing tools over custom AI-written code, and give the reason when a dependency file changes.

## 📬 Opening a PR

- **4. Pace:** agents shouldn't open PRs faster than reviewers can clear them, so only an author's six oldest PRs ready for review should merge, and newer ones wait until older ones merge. Drafts don't count, since they can't merge.
- **5. One topic:** you must give the agent one topic per PR, and split what it produces.

## 👀 Reviewing a PR

- **6. Right approver:** you shouldn't shop for an approval, or count an AI review as one.
  - **Solo maintainer:** your own merge is the approval, and the AI review is only advice.

## ⚖️ How strict each rule is

- 🟡 **Should or must:** a rule is a "should" until a required check covers some of it, and then becomes a "must".
- 🧾 **Evidence, not truth:** a check proves that evidence exists, such as a written reason, not that it's true or the author's own.
- 🚦 **Review status:** `git-review-pr` sets `ai_pr_standards_review` on the commit it reviewed, which fails while a Must or Should finding is neither fixed nor declined with a reason.
  - **Advisory:** it blocks a merge only where repo settings require it.
  - **Limit:** anyone with write access could set it by hand.
- 📌 **Which copy applies:** `git-review-pr` judges a PR by the base branch's copy of this file, and CI runs the base branch's copy of the checks, so a PR can't relax the rules it's judged by.
