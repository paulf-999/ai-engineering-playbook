<!-- version: 1.0.0 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-05 -->
# Quality Scorecard — claude_naming_patterns.md

**Date Created:** 2026-11-05
**Date Updated:** 2026-11-05

**Overall score:** 7.0/10

**Recommended improvements:**

- Replace example names that don't exist in `src/claude/`, or label them "examples from the earlier config".
- Say in one clause what each hook type (`enforcement`, `style_guide`, `session_start`) is for.
- State the agent `<name>` format so it matches `_authoring_agents.md`'s `<domain>_<purpose>`.
- Point to where valid skill domains are listed, or say none are fixed yet.
- Say whether on-demand child files take the `_` prefix.

| Dimension | Score | Date Updated | Notes |
|---|---|---|---|
| **Clarity** | 7/10 | 2026-11-05 | • 🔍 **Clear table:** one row per artefact, each with a pattern and an example, so it's quick to apply<br>• ⚠️ **Hook types undefined:** line 15 lists `enforcement`, `style_guide` and `session_start` without saying when each applies<br>• ⚠️ **Agent name format missing:** line 16 gives only `<name>`, while `_authoring_agents.md` line 14 requires `<domain>_<purpose>`<br>• ⚠️ **Domain undefined:** line 14 says "a domain" but names no list of valid domains, and no `skill_domains.yaml` exists in `src/claude/`<br>• ⚠️ **Children unclear:** line 19 says "name them the same way" without covering the `_<aspect>.md` child convention |
| **Complexity** | 7/10 | 2026-11-05 | • 🧮 **Raw complexity 3:** Concepts 2 (4 artefact patterns plus 2 placement bullets), Scope 1 (governs naming across the config folders), Dependencies 0, Prerequisites 0 |
| **Evidence of Need** | 6/10 | 2026-11-05 | • 🔗 **Lineage:** the file has existed since 2026-08-28 (`created` header), and an earlier copy is in `src/claude_old/rules/_rules_on_demand/claude_config/claude_naming_patterns.md`<br>• 🔗 **Indirect evidence:** `docs/target_architecture/current_architecture/01_snapshot.md` line 19 records that the earlier config enforced naming with a hook, which suggests names drifted often enough to automate<br>• 🔗 **Two pointers:** `authoring_guidelines.md` line 34 points here, and so did `src/claude_old/rules/01_standards/naming_standards.md` line 13<br>• ⚠️ **No dated incident:** no file records a specific badly named artefact or a usage count, so it doesn't reach the "one real use" anchor<br>• ⚠️ **Git history not checked:** this review had no git access, so commit history wasn't checked |
| **Token Cost Justification** | N/A | 2026-11-05 | • 🎯 **Lazy:** it sits in `_rules_on_demand/`, loads only through the pointer in `authoring_guidelines.md`, and costs about 197 tokens (`docs/maintenance/context_cost.md` line 37) |
| **Structural Compliance** | 8/10 | 2026-11-05 | • ✅ **Header and usage lines:** version, created and updated, plus `applies_to`, `miss_cost` and `loading: lazy`, which matches its folder<br>• ✅ **Opening and length:** an emoji H1, a one-line Purpose and 13 counted lines, with emoji-led rows and bold-keyword single-sentence bullets<br>• ⚠️ **Not shown run:** it appears to pass `test_rules_structure.py` on reading, but this review had no run result to confirm it<br>• ⚠️ **Minor layout slips:** the table and the bullet list have no lead-in sentence, and the Hook pattern cell holds both a pattern and a list of types |
| **Currency** | 6/10 | 2026-11-05 | • 🍂 **Examples missing:** none of `naming_standards.md`, `style_guides/sql.md`, `hook_enforcement_naming_convention.sh`, `agents/core/technical_writer/AGENT.md` or a `confluence_create_page` skill exists under `src/claude/`<br>• 🍂 **Unverifiable hook types:** `src/claude/` has no `hooks/` folder, so the three hook types can't be checked against real hooks<br>• ⚠️ **Drift from sibling:** the Agent row doesn't carry the `<domain>_<purpose>` name rule set in `_authoring_agents.md`<br>• ✅ **Fixed path:** line 18 now says `style_guides/` where the `src/claude_old` copy said `style_guide_standards/` |
| **Test Coverage** | 8/10 | 2026-11-05 | • 🧪 **Structural test exists:** `tests/src/claude/test_rules_structure.py` scans every rule, including this one, and includes can-fail checks<br>• ✅ **No incident test needed:** the rule records no incident, so no content-regression test is due<br>• ⚠️ **Not shown run:** the test is newly staged and this review had no result showing it passed for this file |
| **Overall** | **7.0/10** | 2026-11-05 | • 💪 **Compact and lazy:** a 13-line table that loads only when naming something new<br>• ⚠️ **Examples and gaps:** most example names don't exist in this repo, and hook types, agent names and skill domains are left undefined |

## 🔗 Related files

- `src/claude/rules/_rules_on_demand/claude_config/claude_naming_patterns.md` — the rule being scored
- `src/claude/rules/_rules_on_demand/claude_config/authoring_guidelines.md` — the pointer that loads it (Evidence of Need, Token Cost)
- `src/claude/rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_agents.md` — the agent naming rule it doesn't match (Clarity, Currency)
- `src/claude_old/rules/_rules_on_demand/claude_config/claude_naming_patterns.md` — the earlier version (Evidence of Need, Currency)
- `src/claude_old/rules/01_standards/naming_standards.md` — the earlier pointer here (Evidence of Need)
- `docs/target_architecture/current_architecture/01_snapshot.md` — the record of the naming hook (Evidence of Need)
- `docs/maintenance/context_cost.md` — its token cost (Token Cost Justification)
- `tests/src/claude/test_rules_structure.py` — the structural test (Structural Compliance, Test Coverage)
