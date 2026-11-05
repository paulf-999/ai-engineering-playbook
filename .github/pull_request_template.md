# :pencil2: Pull Request Summary

[Summary of the change in 1–2 sentences, linking each file, issue or PR it names with a full GitHub URL.]

## :mag: (Optional) Additional Details

[If needed, only what a reviewer must or should know, in 5 bullets or fewer, with full GitHub URLs for any file, issue or PR.]

## :balance_scale: Evaluation criteria

> [!TIP]
> **✅ Safe to approve:** [one sentence saying why, such as "no red flags, and always-on context stays within budget". If a red flag or failed check is left unresolved, use `> [!WARNING]` and **⚠️ Needs a decision:** instead.]

[Needed when the PR changes `src/claude/`: the verdict callout above, then the table, with one row per standard. Result is ✅ Aligned, ❌ Misaligned or ⏳ Not yet due. Otherwise, write "Not applicable" in place of the callout, the sentence above the table and the table.]

This table checks the change against the repo's [evaluation criteria](https://github.com/paulf-999/ai-engineering-playbook/blob/main/docs/target_architecture/design_principles/02_evaluation_criteria.md), so a reviewer can see at a glance whether it meets each standard for a lean, evidence-led config. Each row is one standard, and Result says whether the change meets it.

| Review area | Standard | Result | Why |
|---|---|---|---|
| :triangular_flag_on_post: Red flags | Always-on weight | [✅ Aligned or ❌ Misaligned] | [each file it hits, with the decision and why, or "no hits"] |
| :triangular_flag_on_post: Red flags | Per-turn overhead | [✅ Aligned or ❌ Misaligned] | [why] |
| :triangular_flag_on_post: Red flags | Advisory-only control | [✅ Aligned or ❌ Misaligned] | [why] |
| :toolbox: Shape | No duplicate | [✅ Aligned or ❌ Misaligned] | [why] |
| :toolbox: Shape | Right mechanism | [✅ Aligned or ❌ Misaligned] | [why] |
| :toolbox: Shape | Tier | [✅ Aligned or ❌ Misaligned] | [why] |
| :toolbox: Shape | Cost | [✅ Aligned or ❌ Misaligned] | [why] |
| :toolbox: Shape | No orchestration | [✅ Aligned or ❌ Misaligned] | [why] |
| :test_tube: Working | Signals | [✅ Aligned or ❌ Misaligned] | [the early signal and later result to watch] |
| :test_tube: Working | Clean exit | [✅ Aligned or ❌ Misaligned] | [how one small PR would remove it] |
| :test_tube: Working | Trial | ⏳ Not yet due | Checked at the next review, once it's been used |

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

<details>
<summary>Testing checklist</summary>

- [ ] DEV / Local testing by developer
- [ ] UAT testing
- [ ] Other (please specify)

</details>

## :white_check_mark: Checklist

- [ ] Pre-commit hooks pass
- [ ] 20 files or fewer changed, or on a `release/` branch (see `docs/guides/git_branching_strategy.md`)

## :bulb: Best Practices

- Keep the PR as small as possible, splitting into multiple PRs if needed.
- Explain reasons behind changes that might not be obvious or are complex.
