# :pencil2: Pull Request Summary

[What the change does, in one sentence of about 20 words or up to 3 bullets. Link each file, issue or PR it names with a full GitHub URL.]

## :mag: (Optional) Additional Details

[If needed, only what a reviewer must or should know, as a list of 5 items at most. Open each with an emoji and a bold keyword, per the [authoring guide](https://github.com/paulf-999/ai-engineering-playbook/blob/main/docs/guides/authoring_guide.md), keep it to about 20 words, and link any file, issue or PR with a full GitHub URL.]

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

## :microscope: How Has This Been Tested?

This PR was tested as follows:

<details>
<summary>Show testing checklist</summary>

- [ ] DEV / Local testing by developer
- [ ] UAT testing
- [ ] Other (please specify)

</details>

<!-- Claude config PRs only, which CI checks:
- Changes src/claude/? Add "## :robot: Claude: Plan" so a reviewer can check the diff against the approved plan. With no
  saved plan, the section holds only the line "No saved plan: " and the reason. Otherwise, open it with this callout:

  > [!NOTE]
  > These files follow the advice in Anthropic's [AI-native SDLC course](https://academy.claude.com/courses/ai-native-sdlc-playbook).

  Then add the line "This PR was created against the following Claude plan:" and five menus, in this order. Put each in
  its own <details> ... </details>, with its <summary> on one line:

  <summary>Show intent.md</summary>
  <summary>Show spec.md</summary>
  <summary>Show plan.md</summary>
  Paste each file as it stands, without plan.md's progress notes, home folder paths or private details.

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
