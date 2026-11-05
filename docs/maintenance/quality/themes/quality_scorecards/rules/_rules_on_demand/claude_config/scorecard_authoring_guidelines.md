<!-- version: 1.0.0 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-05 -->
# Quality Scorecard — authoring_guidelines.md

**Date Created:** 2026-11-05
**Date Updated:** 2026-11-05

**Overall score:** 6.7/10

**Recommended improvements:**

- Define "lean session" where `_authoring_rules.md` first uses it, or link to where it's defined.
- Define the draft, tactical and strategic maturity levels, or point to them, wherever the eval counts depend on them.
- Add the shared complexity formula and the skill and agent hard gates that the scorecard rubrics cite from this file, or repoint those rubrics to wherever the formula and gates actually live.
- Give the tier folders it names (`rules/01_standards/`, `02_conduct/`, `03_workflows/`, `_path_scoped_rules/`) an existing home in `src/claude/rules/`, or mark them as created on install.
- Record the incident, PR or repeated failure that justifies this page, which is what its own "Evidence" bullet asks every addition to do.
- Split the two-point bullets in the parent ("One concept") and in `_authoring_skills.md` ("Description").
- Add a check that each path named in a pointer exists.

| Dimension | Score | Date Updated | Notes |
|---|---|---|---|
| **Clarity** | 7/10 | 2026-11-05 | • 🔍 **Clear body:** the opening says what it covers and when to read each child, and the guidance is actionable.<br>• ⚠️ **Undefined term:** "run a lean session on a matching task" (`_authoring_rules.md`) is never explained.<br>• ⚠️ **Outside context:** "match the count to its maturity" (`_authoring_skills.md`, `_authoring_agents.md`) never defines or links the maturity levels, and "the next review" (`_authoring_rules.md`) has no cadence. |
| **Complexity** | 5/10 | 2026-11-05 | • 🧮 **Raw complexity 5:** Concepts 2 (before-you-start checks, quality gates, rules, skills, agents), Scope 2 (guidance spans `rules/`, `skills/`, `agents/` and `_templates/`), Dependencies 1 (`make` and `pre-commit`), Prerequisites 0.<br>• ⚠️ **Several jobs:** this matches the ~5 anchor ("several jobs, several folders"), although the parent-and-children split keeps each file small. |
| **Evidence of Need** | 6/10 | 2026-11-05 | • 🔗 **Lineage:** `src/claude_old/rules/_rules_on_demand/claude_config/authoring_guidelines.md` (v2.1.0, created 2026-08-28) shows the page has existed since August, and commit a791956 (#87) restored it.<br>• 🔗 **Depended on:** `guiding_principles.md` points here, and the rules, hooks, agents and tests scorecard rubrics all cite it.<br>• ⚠️ **No incident:** no file records a dated failure it fixes, `docs/maintenance/task_log.md` has no authoring entries, and the page doesn't meet its own "Evidence" bullet. |
| **Token Cost Justification** | N/A | 2026-11-05 | • 🎯 **Lazy:** it lives in `_rules_on_demand/` with `loading: lazy` and `miss_cost: medium`, so a pointer is enough and it adds nothing to the always-on budget. |
| **Structural Compliance** | 8/10 | 2026-11-05 | • ✅ **Gates met:** all four files have the 3-line header, an emoji H1, a Purpose line and emoji `##` headings, with no list over 5 bullets and no Related section, and all are under 40 lines.<br>• ✅ **Split correctly:** the entry point has `applies_to`, `miss_cost` and `loading` lines, and it names each of its 3 children.<br>• ⚠️ **Packed bullets:** "One concept" (parent) and "Description" (`_authoring_skills.md`) each carry two points. |
| **Currency** | 6/10 | 2026-11-05 | • ✅ **Most paths exist:** `_templates/` files, `portable_paths.md`, `claude_naming_patterns.md`, the scorecard READMEs, the PR template's Evaluation criteria, `task_log.md`, the always-on budget hook and `test_rules_structure.py` all exist.<br>• ⚠️ **Missing folders:** `rules/01_standards/`, `02_conduct/`, `03_workflows/` and `rules/_path_scoped_rules/` don't exist under `src/claude/rules/` today.<br>• ⚠️ **Drifted content:** the rules, hooks, agents and tests rubrics cite this file for "the shared complexity formula", and `scoring_anchors.md` and the agents rubric cite its "hard gates", but neither appears in the parent or its children. |
| **Test Coverage** | 8/10 | 2026-11-05 | • 🧪 **Structure test:** `tests/src/claude/test_rules_structure.py` covers all four files, including `test_child_is_named_by_its_parent`.<br>• ✅ **No incident:** none is recorded, so no content-regression test is needed.<br>• ⚠️ **Gaps:** nothing checks that named paths exist or records a result for the pointer's lean-session check. |
| **Overall** | **6.7/10** | 2026-11-05 | • 💪 **Lean and well split:** a short entry point with three focused children, each passing the structural gates.<br>• ⚠️ **Stale against its dependants:** other rubrics expect a complexity formula and hard gates that this page doesn't hold, and it names tier folders absent from the repo. |

## 🔗 Related files

- `src/claude/rules/_rules_on_demand/claude_config/authoring_guidelines.md` — the rule being scored
- `src/claude/rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_rules.md` — child; Clarity, Currency
- `src/claude/rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_skills.md` — child; Clarity, Structural Compliance
- `src/claude/rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_agents.md` — child; Clarity
- `src/claude_old/rules/_rules_on_demand/claude_config/authoring_guidelines.md` — Evidence of Need (lineage)
- `src/claude/rules/_rules_on_demand/claude_config/guiding_principles.md` — Evidence of Need (inbound pointer)
- `docs/maintenance/task_log.md` — Evidence of Need (no authoring entries)
- `docs/maintenance/quality/themes/quality_scorecards/rules/README.md` — Currency (cites the missing complexity formula)
- `docs/maintenance/quality/themes/quality_scorecards/agents/README.md` — Currency (cites the missing hard gates)
- `docs/maintenance/quality/themes/quality_scorecards/scoring_anchors.md` — Currency (cites skill hard gates)
- `tests/src/claude/test_rules_structure.py` — Test Coverage, Structural Compliance
