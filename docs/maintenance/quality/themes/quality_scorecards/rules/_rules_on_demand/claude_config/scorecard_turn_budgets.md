<!-- version: 1.0.0 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-05 -->
# Quality Scorecard — turn_budgets.md

**Date Created:** 2026-11-05
**Date Updated:** 2026-11-05

**Overall score:** 7.7/10

**Recommended improvements:**

- Record evidence of need in the rule or its scorecard: a dated runaway or overspent unattended run, or a script, skill or CI job in this repo that runs `claude -p --max-turns`.
- Add a row for read-only CI checks such as review or lint-in-CI, and make the cap ranges stop overlapping so each run fits exactly one row.
- Add a second entry point for scripts, skills and CI jobs, since the only pointer covers "testing a config change".
- Run `tests/src/claude/test_rules_structure.py` and commit it, so the structural pass is on record.

| Dimension | Score | Date Updated | Notes |
|---|---|---|---|
| **Clarity** | 8/10 | 2026-11-05 | • 🎯 **Actionable:** "pass `--max-turns N` on every non-interactive run, such as `claude -p`" leaves no room for two readings.<br>• ⚠️ **Overlapping bands:** the ranges "15 to 20", "20 to 30" and "25 to 50" overlap, so a cap of 20 or 25 fits two rows.<br>• ⚠️ **Missing common case:** no row covers read-only CI checks such as a PR review, which is the most likely unattended run. |
| **Complexity** | 9/10 | 2026-11-05 | • 🧮 **Raw complexity 1:** Concepts 1 (cap, default, table, red flag), Scope 0 (one file), Dependencies 0 (Claude Code's own flag), Prerequisites 0. |
| **Evidence of Need** | 4/10 | 2026-11-05 | • ❓ **No incident recorded:** the rule names no dated runaway run or overspend, and `miss_cost` only says "an unattended run loops and overspends".<br>• 🔍 **Repo search:** no script, workflow or skill in the repo runs `claude -p` or `--max-turns`, and `docs/` never mentions a turn cap, runaway or overspend.<br>• 🗂️ **`src/claude_old/`:** holds the same rule (v2.0.0) plus a second pointer from `automation_controls.md`, which shows it was kept on purpose but gives no usage record.<br>• ⚠️ **Git history not checked:** this reviewer has no shell, so the commit log wasn't read for an originating incident. |
| **Token Cost Justification** | N/A | 2026-11-05 | • 🎯 **Lazy:** it sits in `_rules_on_demand/`, so it costs nothing until `guiding_principles.md` points to it, and a medium miss cost makes a pointer enough. |
| **Structural Compliance** | 8/10 | 2026-11-05 | • ✅ **Clean by inspection:** 6-line header, emoji H1, Purpose line, emoji first cells, short lists, one sentence per bullet, 22 lines.<br>• ⚠️ **Pass not on record:** `test_rules_structure.py` is staged but uncommitted, and no run of it was recorded, so the anchor-9 "passes" needs proof first. |
| **Currency** | 9/10 | 2026-11-05 | • ✅ **Current:** `--max-turns`, `claude -p` and the `guiding_principles.md` pointer named in `loading:` all exist today.<br>• 🔍 **Narrow entry point:** the `automation_controls.md` pointer from `src/claude_old/` wasn't ported, so the only trigger is "before testing a config change with `claude -p`", which is narrower than the rule's "script, skill or CI job". |
| **Test Coverage** | 8/10 | 2026-11-05 | • 🧪 **Structural only, as required:** an instructional rule with no incident record needs no content-regression test.<br>• ⚠️ **Unrun:** structural coverage comes from a new, uncommitted test with no recorded run. |
| **Overall** | **7.7/10** | 2026-11-05 | • 💪 **Tight and actionable:** one concept in 22 lines, with a clear default and an escape valve.<br>• ⚠️ **Need unproven:** no recorded incident or use, and no unattended Claude run in the repo yet. |

## 🔗 Related files

- `src/claude/rules/_rules_on_demand/claude_config/turn_budgets.md`: the rule being scored.
- `src/claude/rules/_rules_on_demand/claude_config/guiding_principles.md`: its only current entry point (Currency, Token Cost).
- `src/claude_old/rules/_rules_on_demand/claude_config/turn_budgets.md`: the earlier version (Evidence of Need).
- `src/claude_old/rules/_rules_on_demand/02_conduct/automation_controls.md`: a second pointer that wasn't ported yet (Evidence of Need, Currency).
- `tests/src/claude/test_rules_structure.py`: the structural test (Structural Compliance, Test Coverage).
