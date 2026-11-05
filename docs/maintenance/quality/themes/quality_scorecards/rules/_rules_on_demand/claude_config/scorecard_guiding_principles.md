<!-- version: 1.0.0 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-05 -->
# Quality Scorecard — guiding_principles.md

**Date Created:** 2026-11-05
**Date Updated:** 2026-11-05

**Overall score:** 7.7/10

**Recommended improvements:**

- Spell out the engineer test in Real problem, for example "would an engineer have built it without being asked?"
- Give the Cost bullet a decision step, such as comparing the estimate with the always-on budget or a threshold.
- Split the bullets on lines 13 and 25 so each one makes a single point.
- Record uses of the rule (a task-log row or a usage-audit hit) so the evidence goes beyond one review finding.

| Dimension | Score | Date Updated | Notes |
|---|---|---|---|
| **Clarity** | 8/10 | 2026-11-05 | • 🔍 **Actionable:** each bullet gives a concrete check, such as "about 5 or more times a month" and "about 100 lines".<br>• ⚠️ **Engineer test:** line 13, "check an engineer would have built it anyway", doesn't say what "anyway" means, so two readers could apply it differently.<br>• ⚠️ **Cost has no decision:** line 14 asks for a token estimate but doesn't say what estimate is too high. |
| **Complexity** | 6/10 | 2026-11-05 | • 🧮 **Raw complexity 4:** Concepts 3 (10 separate checks across two sections) + Scope 1 (guides edits across one tree, `src/claude/**`) + Dependencies 0 + Prerequisites 0.<br>• 💪 **One job:** every check serves one decision, whether a config change is worth its cost. |
| **Evidence of Need** | 7/10 | 2026-11-05 | • ✅ **Documented problem:** `03_complexity_without_evidence.md` records the old config's bloat (about 30,000 always-on tokens, rules about rules, advisory controls), which these checks guard against.<br>• 🔗 **Lineage:** created 2026-08-28 and carried over from `src/claude_old/` with the same body, and `01_principles.md` says its principles "still apply".<br>• ⚠️ **No recorded use:** `task_log.md` has one task row, which doesn't mention this rule, and nothing records the rule being read or changing a decision. |
| **Token Cost Justification** | N/A | 2026-11-05 | • 🎯 **Lazy:** it sits in `_rules_on_demand/` with `loading: lazy` and loads only from `CLAUDE.md`'s config-change pointer.<br>• 💰 **Size:** about 447 tokens when read, per `context_cost.md`, so it's left out of the average. |
| **Structural Compliance** | 8/10 | 2026-11-05 | • ✅ **Gates met on reading:** it has the 3-line header plus `applies_to`, `miss_cost` and `loading`, an emoji H1, a Purpose line, emoji `##` headings, 5 bullets per list and 32 lines.<br>• ⚠️ **Two-point bullets:** line 13 joins the real-problem check and the engineer test, and line 25 joins the size limit and the split instruction. |
| **Currency** | 9/10 | 2026-11-05 | • ✅ **Pointers resolve:** `authoring_guidelines.md`, `portable_paths.md` and `turn_budgets.md` all exist in `src/claude/rules/_rules_on_demand/claude_config/`.<br>• 🔍 **Unbuilt mechanisms:** line 15 suggests path-scoped rules and skills, but `src/claude/` has neither yet. That's guidance rather than a stale path, so it costs only a point. |
| **Test Coverage** | 8/10 | 2026-11-05 | • 🧪 **Structural test:** `test_rules_structure.py` covers this file, including the lazy `loading` check, and has negative cases that prove each check can fail.<br>• 🧪 **Install check:** `test_claude_install_config.py` asserts that the file installs.<br>• ⚠️ **No recorded run:** the structural test was staged but not committed when scored.<br>• ✅ **No incident record:** the rule records no incident, so it needs no content-regression test. |
| **Overall** | **7.7/10** | 2026-11-05 | • 💪 **Lean and current:** 32 lines of concrete checks, lazy-loaded, with every pointer resolving.<br>• ⚠️ **Evidence and wording:** the need rests on one review rather than recorded use, and the engineer test and Cost check need sharper wording. |

## 🔗 Related files

- `src/claude/rules/_rules_on_demand/claude_config/guiding_principles.md` — the rule being scored
- `src/claude_old/rules/_rules_on_demand/claude_config/guiding_principles.md` — Evidence of Need (the old version, with the same body)
- `docs/target_architecture/current_architecture/03_complexity_without_evidence.md` — Evidence of Need (the documented bloat problem)
- `docs/target_architecture/design_principles/01_principles.md` — Evidence of Need (says the principles still apply)
- `docs/maintenance/task_log.md` — Evidence of Need (no recorded use)
- `docs/maintenance/context_cost.md` — Token Cost Justification (about 447 tokens)
- `src/claude/CLAUDE.md` — Token Cost Justification (the read-on-demand pointer)
- `tests/src/claude/test_rules_structure.py` — Structural Compliance and Test Coverage
- `tests/src/sh/test_claude_install_config.py` — Test Coverage (install check)
