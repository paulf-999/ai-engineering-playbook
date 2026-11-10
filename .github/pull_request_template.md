# :pencil2: Pull Request Summary

[Summary of the change in 1–2 sentences, linking each file, issue or PR it names with a full GitHub URL.]

## :mag: (Optional) Additional Details

[If needed, only what a reviewer must or should know, in 5 bullets or fewer, with full GitHub URLs for any file, issue or PR.]

## :hammer_and_wrench: Type of PR Change

Choose one:

- [ ] :sparkles: **Feature**: Non-breaking; adds new functionality.
- [ ] :feather: **Trivial change**: Non-breaking; minor change with minimal impact.
- [ ] :bug: **Bugfix**: Non-breaking; fixes an issue.
- [ ] :recycle: **Refactoring/housekeeping**: Non-breaking; restructures code or tidies repository.
- [ ] :book: **Documentation**: Non-breaking; adds or updates documentation.
- [ ] :boom: **Breaking Change**: Changes existing functionality; rollout may require coordination.

[If there are breaking changes, provide details here.]

## :balance_scale: Evaluation criteria for Claude config changes

> [!TIP]
> **✅ Safe to approve:** [the reviewer's one-sentence verdict, such as "no red flags, and always-on context stays within budget". If a red flag or failed check is left unresolved, use `> [!WARNING]` and **⚠️ Needs a decision:** instead.]

[Needed when the PR changes `src/claude/`: the verdict callout above, then the table, with one row per standard. The author fills the Author rows with numbers from the scripts, and a fresh-context reviewer agent, given only the diff and the evaluation criteria, fills the Reviewer rows and the verdict. Result is ✅ Aligned, ❌ Misaligned or ⏳ Not yet due. Otherwise, write "Not applicable" in place of the callout, the sentences above the table and the table.]

This table checks the change against the [evaluation criteria for Claude config components](https://github.com/paulf-999/ai-engineering-playbook/blob/main/docs/target_architecture/design_principles/02_evaluation_criteria.md), the standards each rule, skill, hook or agent in `src/claude/` must meet to keep the config lean and evidence-led. Each row is one standard, and Result says whether the change meets it.

| Review area | Standard | Filled by | Result | Why |
|---|---|---|---|---|
| :triangular_flag_on_post: Red flags | Always-on weight | Author | [✅ Aligned or ❌ Misaligned] | [the always-on total from `claude_validate_always_on_budget.sh`, before and after] |
| :triangular_flag_on_post: Red flags | Per-turn overhead | Author | [✅ Aligned or ❌ Misaligned] | [each hook event the PR adds, or "no hooks change"] |
| :toolbox: Shape | Cost | Author | [✅ Aligned or ❌ Misaligned] | [the always-on total as a share of the 3,000-token budget] |
| :toolbox: Shape | On-demand cost | Author | [✅ Aligned or ❌ Misaligned] | [the largest on-demand read it changes, from `context_cost.md`, against the 1,200-token cap] |
| :triangular_flag_on_post: Red flags | Advisory-only control | Reviewer | [✅ Aligned or ❌ Misaligned] | [why] |
| :toolbox: Shape | No duplicate | Reviewer | [✅ Aligned or ❌ Misaligned] | [why] |
| :toolbox: Shape | Right mechanism | Reviewer | [✅ Aligned or ❌ Misaligned] | [why] |
| :toolbox: Shape | Tier | Reviewer | [✅ Aligned or ❌ Misaligned] | [why] |
| :toolbox: Shape | No orchestration | Reviewer | [✅ Aligned or ❌ Misaligned] | [why] |
| :test_tube: Working | Signals | Reviewer | [✅ Aligned or ❌ Misaligned] | [the early signal and later result to watch] |
| :test_tube: Working | Clean exit | Reviewer | [✅ Aligned or ❌ Misaligned] | [how one small PR would remove it] |
| :test_tube: Working | Trial | Reviewer | ⏳ Not yet due | Checked at the next review, once it's been used |

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
