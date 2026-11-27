# :pencil2: Pull Request Summary

[What the change does, in one sentence of about 20 words or up to 3 bullets. Link each file, issue or PR it names with a full GitHub URL.]

## :mag: (Optional) Additional Details

[If needed, only what a reviewer must or should know, as a list of 5 items at most. Open each with an emoji and a bold keyword, per the [authoring guide](https://github.com/paulf-999/ai-engineering-playbook/blob/main/docs/guides/authoring_guide.md), keep it to about 20 words, and link any file, issue or PR with a full GitHub URL.]

## :thinking: Why Is This Change Needed?

[Say why the complex or non-obvious parts are there, as up to 5 bullets that each open with an emoji and a bold keyword and colon. If a dependency file changes, add a line that starts "Dependency reason: " with why existing tools weren't enough.]

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

[List each command or check that was run, and its result, including failures. For a check not run, write "Not run: " and the reason.]

<!-- Extra sections, which reviewers check:
- Does this PR build a saved plan (intent.md, spec.md and plan.md, which `make list_plans` lists)? In any PR, whatever
  it changes, add "## :robot: Claude: Plan" so a reviewer can check the diff against the approved plan. With no saved
  plan for this PR, leave the section out, unless the PR changes src/claude/, when it holds only the line
  "No saved plan: " and the reason. Otherwise, copy the skeleton below and replace each <placeholder>:
  - In the intent.md, spec.md and plan.md menus, paste each file as it stands, but leave out plan.md's progress notes,
    and any home folder paths or private details from all three files.
  - In the measures menu, write "not recorded" rather than an estimate, and replace each "pending" before merging.
  - In the governance menu, write "none" for an empty bullet.

  ## :robot: Claude: Plan

  This PR was built against this Claude plan, per Anthropic's [AI-native SDLC course](https://academy.claude.com/courses/ai-native-sdlc-playbook).

  <details><summary>Show Claude plan</summary>

  **What is `intent.md`?**
  It describes the problem being solved, and how we'll know the change worked.

  <details><summary>Show intent.md</summary>

  <intent.md>

  </details>

  **What is `spec.md`?**
  It describes what changes and what's left out.

  <details><summary>Show spec.md</summary>

  <spec.md>

  </details>

  **What is `plan.md`?**
  It lists the decisions agreed, the steps to build the change, and the check that proves each step.

  <details><summary>Show plan.md</summary>

  <plan.md>

  </details>

  **What are the measures?**
  They show how the work went, such as planning time, test results and rework.

  <details><summary>Show measures</summary>

  | Measure | Value |
  |---|---|
  | Time to a saved intent | <intent.md: Saved minus Started, the time of the first conversation> |
  | Intent edits after the spec | <intent.md: Edits after spec> |
  | Spec edits after the plan | <spec.md: Edits after plan> |
  | Diff matches the plan | <yes, or each departure> |
  | Checks run | <each command and its result> |
  | First-pass CI | <pending, then the first commit's result> |
  | Rework | <pending, then the number of commits after the PR opened> |

  </details>

  **What is governance?**
  It records who approved the plan, plus any policy conflicts, risks and open questions.

  <details><summary>Show governance</summary>

  - **Approved by:** <role, never a name>
  - **Policy conflicts:** <each conflict>
  - **Risks:** <each risk>
  - **Open questions carried forward:** <each question>

  </details>

  </details>

- Changes src/claude/CLAUDE.md, or a file in src/claude/rules/always_on/ or src/claude/hooks/? Also add
  "## :balance_scale: Claude: Evaluation Criteria". Open it with the line
  "This PR was checked against the following [evaluation criteria](<link>):", linking to
  https://github.com/paulf-999/ai-engineering-playbook/blob/main/docs/target_architecture/design_principles/02_evaluation_criteria.md
  Then put one bullet per red flag, as "- 🚩 **<keyword>:** <file or issue>; <decision and why>.", or the single line
  "No red flags.", in "<details><summary>Show red flags</summary> ... </details>", keeping the heading outside it. -->

## :bulb: Best Practices

- Keep the PR as small as possible, splitting into multiple PRs if needed.
- Explain reasons behind changes that might not be obvious or are complex.
