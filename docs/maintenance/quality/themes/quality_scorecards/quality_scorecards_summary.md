<!-- version: 1.0.0 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-05 -->
# 📊 Quality Scorecards Summary

**Purpose:** One-glance rollup across every artefact type, showing where quality is weakest and what to fix first, without opening the five per-type summaries.

This page is part of the [quality scorecards](README.md) home.

---

## 📋 Scores by type

- **Overall:** the mean of every scorecard's Overall score for that type.
- **Strongest and weakest:** the highest- and lowest-scoring file of that type, by Overall score.
- **Date Updated:** the latest `Date Updated` among that type's scorecards.
- **Rules split:** always-on rules (`rules/01_standards/`, `02_conduct/` and `03_workflows/`) load in every session, so they rank above lazy-load rules, which load only on demand.

| Type | Scored | Overall | Date Updated | Strengths and gaps |
|---|---|---|---|---|
| Tests | 0 | — | — | Nothing scored yet |
| Skills | 0 | — | — | Nothing scored yet |
| Rules — always-on | 0 | — | — | Nothing scored yet |
| Rules — lazy-load | 0 | — | — | Nothing scored yet |
| Hooks | 0 | — | — | Nothing scored yet |
| Agents | 0 | — | — | Nothing scored yet |

---

## 🚀 Recommended next actions

Ranked by impact, highest first, with lazy-load rule actions last because those rules load only on demand.

| # | Action | Why | Source |
|---|---|---|---|
| — | Nothing to do until a scorecard exists | — | — |

---

## 📄 All summaries

| Summary | Scored | Overall | Date Updated |
|---|---|---|---|
| [`tests/test_scorecards_summary.md`](tests/test_scorecards_summary.md) | 0 | — | — |
| [`skills/skill_scorecards_summary.md`](skills/skill_scorecards_summary.md) | 0 | — | — |
| [`rules/rule_scorecards_summary.md`](rules/rule_scorecards_summary.md) | 0 | — | — |
| [`hooks/hook_scorecards_summary.md`](hooks/hook_scorecards_summary.md) | 0 | — | — |
| [`agents/agent_scorecards_summary.md`](agents/agent_scorecards_summary.md) | 0 | — | — |

---

## 🔄 Keeping this current

- **Same commit:** update this file whenever any per-type summary changes.
- **Recompute:** re-average the Overall scores and re-check the strongest and weakest files whenever a scorecard is re-scored.
- **Bump dates:** set a type's `Date Updated` to the re-scored scorecard's `Date Updated`.
- **Prune actions:** remove an action once its source summary no longer lists it.
- **Template:** this file follows [`_templates/scorecard/scorecard_summary.md.template`](../../../../../src/claude/_templates/scorecard/scorecard_summary.md.template).
