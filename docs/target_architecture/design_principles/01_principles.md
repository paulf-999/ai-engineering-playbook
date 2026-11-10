<!-- version: 1.7.2 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-10 -->
# 🧱 Design principles: Principles

**Purpose:** the principles every new or changed component (a rule, skill, hook or agent) must follow, and how each one is checked.

They're part of this repo's [design principles](../design_principles.md), which also define session transcripts.

| Principle | What it means | Checked by | Source |
|---|---|---|---|
| 🌱 **Minimal by default** | Beyond the [required core](../target_architecture.md#-tiers) of `CLAUDE.md`, the always-on rules, tests and CI, everything is optional. | A budget check on context loaded every session | [Review of the old setup](../current_architecture/03_complexity_without_evidence.md) |
| 💰 **Every component earns its cost** | It earns its place during a trial that ends at the next review, and each old file is reviewed for bloat first. | Its PR's answers to the [evaluation criteria](02_evaluation_criteria.md) | [Review of the old setup](../current_architecture/03_complexity_without_evidence.md), plus [DORA research](../reference_material/core/dora_ai_capabilities/03_findings.md) on irrelevant context |
| 🔒 **Enforce what must hold** | Use a hook, test or CI check, not prose. | The PR naming that check | [Anthropic's SDLC course](../reference_material/core/anthropic_ai_native_sdlc/04_our_reading.md) |
| 🔁 **No duplicate controls** | A rule never restates a CI or pre-commit check. | The "No duplicate" criterion | [Handover review](../reference_material/core/handover_review.md) |
| 🔌 **Opt-in, never mandatory** | No workflow requires a skill or agent. | The "No orchestration" criterion | [Handover review](../reference_material/core/handover_review.md) |
| 📏 **Measure outcomes and overhead** | Measure tasks' [outcomes and overhead](../target_architecture.md#-measures) at each review. | The [repo review](../../maintenance/quality/audits/quality_audit_repo.md), from session transcripts and git history | [Review of the old setup](../current_architecture/03_complexity_without_evidence.md), plus [Anthropic's SDLC course](../reference_material/core/anthropic_ai_native_sdlc/01_overview.md) on indicators |
| 🗑️ **Retire what doesn't pay** | Remove a component after two sessions show it got in the way, or if it's unused between reviews. | The regular review | [Handover review](../reference_material/core/handover_review.md) |
| 🧑 **Humans own judgement calls** | A person merges every PR and decides scope and design. | Changes reach `main` only by PR, though approval isn't enforced | [Anthropic's SDLC course](../reference_material/core/anthropic_ai_native_sdlc/01_overview.md) |

## 🔢 Numbers and tests

These limits back the principles:

- 📏 **3,000-token budget:** the most text that may load into every session, a tenth of what the [old configuration](../current_architecture/01_snapshot.md) loads.
  - **Why this size:** it's roughly what [Anthropic's advice](https://code.claude.com/docs/en/memory) to keep `CLAUDE.md` under 200 lines allows, by our estimate.
- 📖 **Per-file caps:** an on-demand rule may cost 1,200 tokens each time Claude reads it, and a path-scoped rule 500.
  - **Why 1,200:** every on-demand rule fitted under it when it was set, so it stops growth without forcing splits.
  - **Why 500:** a path-scoped rule loads unasked and stacks with others that match the same file, so it's capped tighter, near `CLAUDE.md`'s size.
- 🗓️ **Review every 20 tasks or 4 weeks:** often enough to drop unused parts, with enough evidence to judge each one.
- 🚩 **Two sessions, not one:** a single session where a part got in the way may be chance.
- 🔪 **Halving test:** at each review, ask whether removing half the rules, skills, hooks and agents would make results noticeably worse.
  - **If not:** the setup is bigger than it needs to be.

## ♻️ Carried over

These principles from the [old configuration's guiding principles](https://github.com/paulf-999/claude_ai_playbook/blob/915685f/src/claude/rules/01_essentials/guiding_principles.md) still apply:

- Make every change easy to reverse.
- Grow in small stages.
- Load essentials first, and detail only on demand.
- Link to live sources rather than keeping lists that go stale.
