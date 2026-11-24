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
- Changes src/claude/? Add "## :robot: Claude: Plan" holding the approved plan's saved intent.md, spec.md and plan.md,
  so a reviewer can check the diff against them, or say why it has none. Open it with the line "This PR was created
  against the following Claude plan:", then put each file in its own "<details><summary>Show intent.md</summary> ...
  </details>", in that order and named to match, keeping the heading outside. Paste each file as it stands, without
  plan.md's progress notes, home folder paths or private details.
- Changes src/claude/CLAUDE.md, a rule in rules/always_on/ or a hook? Also add "## :balance_scale: Claude: Evaluation Criteria".
  Open it with the line "This PR was checked against the following [evaluation criteria](<link>):", linking to
  https://github.com/paulf-999/ai-engineering-playbook/blob/main/docs/target_architecture/design_principles/02_evaluation_criteria.md
  Then put one bullet per red flag, as "- 🚩 **<keyword>:** <file or issue>; <decision and why>.", or the single line
  "No red flags.", in "<details><summary>Show red flags</summary> ... </details>", keeping the heading outside it. -->

## :bulb: Best Practices

- Keep the PR as small as possible, splitting into multiple PRs if needed.
- Explain reasons behind changes that might not be obvious or are complex.
