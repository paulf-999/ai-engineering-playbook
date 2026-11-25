# :pencil2: Pull Request Summary

[What the change does, in one sentence of about 20 words or up to 3 bullets. Link each file, issue or PR it names with a full GitHub URL.]

## :mag: (Optional) Additional Details

[If needed, only what a reviewer must or should know, as a list of 5 items at most. Open each with an emoji and a bold keyword, per the [authoring guide](https://github.com/paulf-999/ai-engineering-playbook/blob/main/docs/guides/authoring_guide.md), keep it to about 20 words, and link any file, issue or PR with a full GitHub URL.]

## :thinking: Why

[Say, in your own words, why the complex or non-obvious parts are there. If a dependency file changes, add a line that starts "Dependency reason: " with why existing tools weren't enough.]

## :hammer_and_wrench: Type of PR Change

Choose one:

- [ ] :sparkles: **Feature**: Non-breaking; adds new functionality.
- [ ] :feather: **Trivial change**: Non-breaking; minor change with minimal impact.
- [ ] :bug: **Bugfix**: Non-breaking; fixes an issue.
- [ ] :recycle: **Refactoring/housekeeping**: Non-breaking; restructures code or tidies repository.
- [ ] :book: **Documentation**: Non-breaking; adds or updates documentation.
- [ ] :boom: **Breaking Change**: Changes existing functionality; rollout may require coordination.

[If there are breaking changes, provide details here.]

## :link: Related Issue(s)

[Link related issues or tickets here]

## :computer: What I ran

[List each command or check you ran yourself, with its result, rather than what the AI says it ran.]

## :microscope: How Has This Been Tested?

This PR was tested as follows:

<details>
<summary>Show testing checklist</summary>

- [ ] DEV / Local testing by developer
- [ ] UAT testing
- [ ] Other (please specify)

</details>

<!-- Extra sections, which CI checks:
- Does this PR build a saved plan (intent.md, spec.md and plan.md)? In any PR, whatever it changes, add
  "## :robot: Claude: Plan" so a reviewer can check the diff against the approved plan. With no saved plan for this PR,
  leave the section out, unless the PR changes src/claude/, when it holds only the line "No saved plan: " and the
  reason. Otherwise, open it with this callout:

  > [!NOTE]
  > These files follow the advice in Anthropic's [AI-native SDLC course](https://academy.claude.com/courses/ai-native-sdlc-playbook).

  Then add the line "This PR was created against the following Claude plan:" and five menus, in this order. Put each in
  its own <details> ... </details>, with its <summary> on one line. Copy the question and answer above each
  <summary> too, but put them outside the menu: the text first, then a blank line, then <details>:

  **What is `intent.md`?**
  It describes the problem being solved, and how we'll know the change worked. It starts the process and is prompted by:

  - an idea
  - a ticket
  - an alert

  <summary>Show intent.md</summary>

  **What is `spec.md`?**
  It describes what changes and what's left out.

  <summary>Show spec.md</summary>

  **What is `plan.md`?**
  It lists the decisions agreed, the steps to build the change, and the check that proves each step.

  <summary>Show plan.md</summary>
  In these three menus, paste each file as it stands, without plan.md's progress notes, home folder paths or private details.

  **What are the measures?**
  They show how the work went, such as planning time, test results and rework.

  <summary>Show measures</summary>
  Write "not recorded" rather than an estimate. Replace each "pending" before merging.

  | Measure | Value |
  |---|---|
  | Time to a saved intent | <intent.md: Saved minus Started, the time of the first conversation> |
  | Intent edits after the spec | <intent.md: Edits after spec> |
  | Spec edits after the plan | <spec.md: Edits after plan> |
  | Diff matches the plan | <yes, or each departure> |
  | Checks run | <each command and its result> |
  | First-pass CI | <pending, then the first commit's result> |
  | Rework | <pending, then the number of commits after the PR opened> |

  **What is governance?**
  It records who approved the plan, plus any policy conflicts, risks and open questions.

  <summary>Show governance</summary>
  Write "none" for an empty bullet.

  - **Approved by:** <role, never a name>
  - **Policy conflicts:** <each conflict>
  - **Risks:** <each risk>
  - **Open questions carried forward:** <each question>

- Changes src/claude/CLAUDE.md, a rule in rules/always_on/ or a hook? Also add "## :balance_scale: Claude: Evaluation Criteria".
  Open it with the line "This PR was checked against the following [evaluation criteria](<link>):", linking to
  https://github.com/paulf-999/ai-engineering-playbook/blob/main/docs/target_architecture/design_principles/02_evaluation_criteria.md
  Then put one bullet per red flag, as "- 🚩 **<keyword>:** <file or issue>; <decision and why>.", or the single line
  "No red flags.", in "<details><summary>Show red flags</summary> ... </details>", keeping the heading outside it. -->

## :bulb: Best Practices

- Keep the PR as small as possible, splitting into multiple PRs if needed.
- Explain reasons behind changes that might not be obvious or are complex.
