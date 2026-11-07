<!-- version: 1.0.0 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-05 -->
# Quality Scorecard — datetime.md

**Date Created:** 2026-11-05
**Date Updated:** 2026-11-05

**Overall score:** 6.5/10

**Recommended improvements:**

- Add a `**Read on demand:**` pointer to this guide from an always-on rule in `src/claude/`, or change the `loading:` reason to name a pointer that exists.
- Add a reachability test that fails when nothing in `src/claude/` points to a lazy rule.
- Say whether repo markdown docs, such as READMEs, count as technical or human-facing.
- Record a dated incident or usage evidence that shows dates drifting between formats.
- Give each table body row an emoji, and turn the hard-wrapped prose under the H1 and in Timezone into one-sentence bullets.

| Dimension | Score | Date Updated | Notes |
|---|---|---|---|
| **Clarity** | 7/10 | 2026-11-05 | • 🔍 **Formats:** the format table and the UTC `Z` rule can each be read only one way.<br>• ⚠️ **Boundary:** line 48 "Code files and technical documentation" overlaps with human-facing content, so a README or a technical Confluence page could go either way. |
| **Complexity** | 8/10 | 2026-11-05 | • 🧮 **Raw complexity 2:** Concepts 2 (ISO dates, UTC/`Z`, filename underscores, sentence-style human dates, no retroactive edits) + Scope 0 + Dependencies 0 + Prerequisites 0. |
| **Evidence of Need** | 5/10 | 2026-11-05 | • 🔗 **Lineage only:** the rule dates from `created: 2026-04-11` and is at version 2.0.4, and it was ported from `src/claude_old/` in commit 7b2a23e.<br>• 🔗 **Old pointer:** `src/claude_old/rules/01_standards/naming_standards.md` line 14 pointed to it.<br>• 📏 **Cost known:** `docs/maintenance/context_cost.md` lists it at about 463 tokens.<br>• ⚠️ **No incident:** no file records a date-format mistake or any repeat use, and `miss_cost: low` says the same. |
| **Token Cost Justification** | N/A | 2026-11-05 | • 🎯 **Lazy:** it sits in `_rules_on_demand/`, so it costs nothing until Claude reads it. |
| **Structural Compliance** | 7/10 | 2026-11-05 | • ✅ **Gates met:** 68 lines, a full 6-line header with `loading: lazy` matching its folder, an emoji H1, a Purpose line and emoji `##` headings.<br>• ⚠️ **Style slips:** the format table rows have no emoji.<br>• ⚠️ **Prose:** lines 11–13 and 36–37 are hard-wrapped, multi-sentence prose, not bullets.<br>• ⚠️ **Maintenance:** the Contents list is kept by hand, and both lists sit at the 5-item ceiling. |
| **Currency** | 5/10 | 2026-11-05 | • 🍂 **Dangling pointer:** line 6 says Claude arrives via "naming_standards.md's date pointer", but no `naming_standards.md` exists in `src/claude/`.<br>• 🍂 **Orphaned:** a search finds no file in `src/claude/` that names `style_guides/utilities/datetime.md`, so nothing in the new config sends Claude here. |
| **Test Coverage** | 7/10 | 2026-11-05 | • 🧪 **Structural:** `tests/src/claude/test_rules_structure.py` covers this file's header, H1, Purpose, headings, lists and usage lines.<br>• ⚠️ **Unrecorded run:** the test file is new and uncommitted, and no file records a passing run.<br>• ⚠️ **No reachability check:** no test catches the missing pointer above.<br>• ✅ **No incident test needed:** the rule records no incident, so it needs no content-regression test. |
| **Overall** | **6.5/10** | 2026-11-05 | • 💪 **Simple:** a short, single-topic guide with an exact format table and a clear filename exception.<br>• ⚠️ **Unreachable:** in the new config nothing points to it, and nothing records a need for it. |

## 🔗 Related files

- `src/claude/rules/_rules_on_demand/style_guides/utilities/datetime.md`: the rule being scored.
- `src/claude_old/rules/_rules_on_demand/style_guides/utilities/datetime.md`: the version it was ported from (Evidence of Need).
- `src/claude_old/rules/01_standards/naming_standards.md`: the old pointer, which has no counterpart in `src/claude/` yet (Evidence of Need, Currency).
- `docs/maintenance/context_cost.md`: the token size estimate (Evidence of Need).
- `tests/src/claude/test_rules_structure.py`: the structural coverage (Structural Compliance, Test Coverage).
