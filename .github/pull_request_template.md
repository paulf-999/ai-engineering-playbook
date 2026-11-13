# :pencil2: Pull Request Summary

[What the change does, in one sentence of about 20 words or up to 3 bullets. Link each file, issue or PR it names with a full GitHub URL.]

## :mag: (Optional) Additional Details

[If needed, only what a reviewer must or should know, in 5 bullets or fewer. Open each with an emoji and a bold keyword, keep it to about 20 words, per [`writing_style.md`](https://github.com/paulf-999/ai-engineering-playbook/blob/main/src/claude/rules/02_conduct/writing_style.md), and link any file, issue or PR with a full GitHub URL.]

## :hammer_and_wrench: Type of PR Change

Choose one:

- [ ] :sparkles: **Feature**: Non-breaking; adds new functionality.
- [ ] :feather: **Trivial change**: Non-breaking; minor change with minimal impact.
- [ ] :bug: **Bugfix**: Non-breaking; fixes an issue.
- [ ] :recycle: **Refactoring/housekeeping**: Non-breaking; restructures code or tidies repository.
- [ ] :book: **Documentation**: Non-breaking; adds or updates documentation.
- [ ] :boom: **Breaking Change**: Changes existing functionality; rollout may require coordination.

[If there are breaking changes, provide details here.]

## :microscope: How Has This Been Tested?

> [!TIP]
> **✅ Adequately tested:** [one-sentence verdict, such as "`make test` and pre-commit pass, with new cases for the change". If testing has gaps, use `> [!WARNING]` and **⚠️ Testing gaps:** instead.]

<details>
<summary>Testing checklist</summary>

- [ ] DEV / Local testing by developer
- [ ] Other (please specify)

</details>

## :robot: Claude: Plan Spec (spec.md) - Requirements and Design

<details>
<summary>Approved plan's spec</summary>

> ℹ️ **What is `spec.md`?** The requirements and design from Claude's approved plan, which the diff is built to.

[For a `src/claude/` change, paste its `spec.md`, so a reviewer can check the diff against it. Otherwise, say "Not applicable" and why.]

</details>

## :balance_scale: Claude: Evaluation Criteria for Claude Config Changes

> [!TIP]
> **✅ Safe to approve:** [one-sentence verdict, such as "no red flags; always-on context unchanged". If a red flag is left unresolved, use `> [!WARNING]` and **⚠️ Needs a decision:** instead.]

[Needed when the PR changes `src/claude/`, filled by a fresh-context reviewer agent given only the diff and the criteria. Add a row for each ❌ Misaligned standard. Keep each Why under 10 words. Otherwise, replace this section's content with "Not applicable".]

Checked against the [evaluation criteria](https://github.com/paulf-999/ai-engineering-playbook/blob/main/docs/target_architecture/design_principles/02_evaluation_criteria.md).

| Standard | Result | Why |
|---|---|---|
| :triangular_flag_on_post: Always-on weight | [✅ or ❌] | [files made always-on, or "none"] |
| :test_tube: Clean exit | [✅ or ❌] | [how one small PR would remove it] |

All other standards ✅ Aligned. Trial ⏳ due at the next review.

## :bulb: Best Practices

- Keep the PR as small as possible, splitting into multiple PRs if needed.
- Explain reasons behind changes that might not be obvious or are complex.
