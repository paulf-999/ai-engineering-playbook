<!-- version: 1.0.0 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-05 -->
# 📊 Rule Scorecards Summary

**Purpose:** One-glance rollup of every rule scorecard, showing where quality is weakest and what to fix first, without opening each file.

This page is part of the [quality scorecards](../README.md) home.

---

## 📋 Scores by tier

- **Overall:** the mean of every scorecard's Overall score in that tier.
- **Strongest and weakest:** the highest- and lowest-scoring file in that tier, by Overall score.
- **Date Updated:** the latest `Date Updated` among that tier's scorecards.
- **Priority:** the tiers that load every session (`01_standards/`, `02_conduct/` and `03_workflows/`) rank above `_rules_on_demand/` and `_path_scoped_rules/`, which load only on demand or with matching files.

| Tier | Scored | Overall | Date Updated | Strengths and gaps |
|---|---|---|---|---|
| — | 0 | — | — | Nothing scored yet |

---

## 🚀 Recommended next actions

Ranked by impact, highest first, with always-on rules before lazy-load rules.

| # | Action | Why | Source |
|---|---|---|---|
| — | Nothing to do until a scorecard exists | — | — |

---

## 📄 All scorecards

Sorted by Overall score, highest first.

| Scorecard | Overall | Date Updated | Recommended improvements |
|---|---|---|---|
| — | — | — | Nothing scored yet |

---

## 🔄 Keeping this current

- **Same commit:** update this file whenever a scorecard it covers is created or re-scored.
- **Recompute:** re-average the Overall scores and re-check the strongest and weakest files.
- **Bump dates:** set a tier's `Date Updated` to the re-scored scorecard's `Date Updated`.
- **Prune actions:** remove an action once its scorecard no longer lists it.
- **Template:** this file follows [`_templates/scorecard/scorecard_summary.md.template`](../../../../../../src/claude/_templates/scorecard/scorecard_summary.md.template).
