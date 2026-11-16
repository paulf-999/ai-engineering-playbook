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

> [!NOTE]
> **✅ Adequately tested:** [one-sentence verdict, such as "`make test` and pre-commit pass, with new cases for the change". If testing has gaps, use `> [!WARNING]` and **⚠️ Testing gaps:** instead.]

<details>
<summary>Testing checklist</summary>

- [ ] DEV / Local testing by developer
- [ ] Other (please specify)

</details>

## :white_check_mark: Checklist

- [ ] Pre-commit hooks pass
- [ ] 20 files or fewer changed, or on a `release/` branch (see `docs/guides/git_branching_strategy.md`)

<!-- Claude config PRs only, which CI checks:
- Changes src/claude/? Add "## :robot: Claude: Plan Spec (spec.md)" holding the approved plan's spec.md, so a reviewer
  can check the diff against it, or say why it has none.
- Changes src/claude/CLAUDE.md, a rule in rules/always_on/ or a hook? Also add "## :balance_scale: Claude: Evaluation Criteria"
  naming any red flag, such as "No red flags.", per the evaluation criteria:
  https://github.com/paulf-999/ai-engineering-playbook/blob/main/docs/target_architecture/design_principles/02_evaluation_criteria.md -->

## :bulb: Best Practices

- Keep the PR as small as possible, splitting into multiple PRs if needed.
- Explain reasons behind changes that might not be obvious or are complex.
