<!-- version: 1.0.1 -->
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
| `_rules_on_demand/` | 7 | 7.0/10 | 2026-11-05 | • 💪 **Strongest:** 2 files tied at 7.7/10, including `guiding_principles.md`<br>• ⚠️ **Weakest:** `jira.md` (5.8/10) |

---

## 🚀 Recommended next actions

Ranked by impact, highest first, with always-on rules before lazy-load rules.

| # | Action | Why | Source |
|---|---|---|---|
| 1 | • 🔧 **`jira.md`:** make the required fields agree between the parent and its children | • 🔻 **Score:** 5.8/10, the lowest | [`scorecard_jira.md`](_rules_on_demand/style_guides/scorecard_jira.md) |
| 2 | • 🔗 **`jira.md` and `datetime.md`:** give each an inbound pointer, which lands with the always-on rules | • 🍂 **Unreachable:** nothing in the new config points to either yet | [`scorecard_datetime.md`](_rules_on_demand/style_guides/utilities/scorecard_datetime.md) |
| 3 | • 🧮 **`authoring_guidelines.md`:** add the complexity formula and hard gates the rubrics cite, or repoint the rubrics | • 🍂 **Drift:** four rubrics cite content it doesn't hold | [`scorecard_authoring_guidelines.md`](_rules_on_demand/claude_config/scorecard_authoring_guidelines.md) |
| 4 | • ✏️ **`portable_paths.md`:** settle the clash over `~/.claude` as a fallback | • ⚠️ **Clarity:** two bullets contradict each other | [`scorecard_portable_paths.md`](_rules_on_demand/claude_config/scorecard_portable_paths.md) |
| 5 | • ✏️ **`turn_budgets.md`:** make the cap ranges stop overlapping | • ⚠️ **Clarity:** a cap of 20 or 25 fits two rows | [`scorecard_turn_budgets.md`](_rules_on_demand/claude_config/scorecard_turn_budgets.md) |

---

## 📄 All scorecards

Sorted by Overall score, highest first.

| Scorecard | Overall | Date Updated | Recommended improvements |
|---|---|---|---|
| [`scorecard_guiding_principles.md`](_rules_on_demand/claude_config/scorecard_guiding_principles.md) | 7.7/10 | 2026-11-05 | Spell out the engineer test, and give the Cost bullet a decision step |
| [`scorecard_turn_budgets.md`](_rules_on_demand/claude_config/scorecard_turn_budgets.md) | 7.7/10 | 2026-11-05 | Make the cap ranges stop overlapping, and add a row for read-only CI runs |
| [`scorecard_portable_paths.md`](_rules_on_demand/claude_config/scorecard_portable_paths.md) | 7.5/10 | 2026-11-05 | Settle the clash between never hard-coding `~/.claude` and using it as the fallback |
| [`scorecard_claude_naming_patterns.md`](_rules_on_demand/claude_config/scorecard_claude_naming_patterns.md) | 7.0/10 | 2026-11-05 | Label example names as from the earlier config, and match the agent name format |
| [`scorecard_authoring_guidelines.md`](_rules_on_demand/claude_config/scorecard_authoring_guidelines.md) | 6.7/10 | 2026-11-05 | Add, or repoint the rubrics away from, the complexity formula and hard gates they cite |
| [`scorecard_datetime.md`](_rules_on_demand/style_guides/utilities/scorecard_datetime.md) | 6.5/10 | 2026-11-05 | Give it an inbound pointer, which lands with the always-on rules |
| [`scorecard_jira.md`](_rules_on_demand/style_guides/scorecard_jira.md) | 5.8/10 | 2026-11-05 | Make the required fields agree between the parent and its children |

---

## 🔄 Keeping this current

- **Same commit:** update this file whenever a scorecard it covers is created or re-scored.
- **Recompute:** re-average the Overall scores and re-check the strongest and weakest files.
- **Bump dates:** set a tier's `Date Updated` to the re-scored scorecard's `Date Updated`.
- **Prune actions:** remove an action once its scorecard no longer lists it.
- **Template:** this file follows [`_templates/scorecard/scorecard_summary.md.template`](../../../../../../src/claude/_templates/scorecard/scorecard_summary.md.template).
