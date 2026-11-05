<!-- version: 1.0.0 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-05 -->
# Quality Scorecard — jira.md

**Date Created:** 2026-11-05
**Date Updated:** 2026-11-05

**Overall score:** 5.8/10

**Recommended improvements:**

- Make the required fields match across the files: either move Sprint and Priority into the Blocking table in `_definition_of_ready.md`, or mark them "Recommended" in `_field_standards.md` and in the parent's Completeness bullet.
- Make the component rule match too: `_definition_of_ready.md` #7 says "at least one", while `_field_standards.md` says every component `jira_values.md` lists.
- Define "hygiene checks", "ADF", "Triage" and "BAU" where each first appears, or swap them for plain words.
- Add a `**Read on demand:**` pointer to `jira.md` in an always-on rule under `src/claude/rules/`, or rewrite the `loading:` reason to name a trigger that exists.
- Record the evidence of need, such as dated tickets written with the guide or rows in `docs/maintenance/task_log.md`.
- Give each table body row and each labelled top-level bullet its emoji, and split the multi-sentence paragraphs into one sentence per bullet.
- Add a reachability test that fails when an on-demand rule has no inbound pointer.

| Dimension | Score | Date Updated | Notes |
|---|---|---|---|
| **Clarity** | 6/10 | 2026-11-05 | • 💪 **Clear opening:** the Purpose line and the four Core principles say what the guide covers in seconds.<br>• ⚠️ **Contradiction:** `_field_standards.md` lists Sprint and Priority as "Required: Yes" before sprint entry, and so does the parent's Completeness bullet, but `_definition_of_ready.md` #11–12 puts them under "Recommended (should pass)".<br>• ⚠️ **Undefined terms:** "hygiene checks" (parent), "ADF" and "Triage" (`_field_standards.md`) and "BAU" (`_sprint_planning.md`) are never explained. |
| **Complexity** | 4/10 | 2026-11-05 | • 🧮 **Raw complexity 6:** Concepts 3 (six aspects: ticket shape, fields, business value, readiness, sprint planning, values) + Scope 1 (one folder) + Dependencies 1 (Jira MCP tools such as `getJiraIssue`) + Prerequisites 1 (a filled `_local/jira_values.md`).<br>• ⚠️ **Wide for one rule:** past the ~5 anchor's "several jobs … and one external service", though it is split cleanly into children. |
| **Evidence of Need** | 6/10 | 2026-11-05 | • 🔗 **Ported, not new:** `src/claude_old/rules/_rules_on_demand/style_guides/jira.md` and its children carry `created: 2026-05-20`, and the old `src/claude_old/rules/02_conduct/writing_style.md` pointed to it "before writing or changing a Jira ticket".<br>• 🔗 **Signs of real use:** the worked examples read like real tickets, and the user's always-on `writing_style.md` still points to the guide.<br>• ⚠️ **Nothing recorded:** no dated incident, ticket log or usage row, and `docs/maintenance/task_log.md` doesn't mention Jira, so it sits between the 5 and 7 anchors. |
| **Token Cost Justification** | N/A | 2026-11-05 | • 🎯 **On demand:** it lives in `_rules_on_demand/` with `loading: lazy`, so it costs nothing until read, and the dimension doesn't apply. |
| **Structural Compliance** | 7/10 | 2026-11-05 | • ✅ **Gates met on reading:** the metadata and usage headers, emoji H1s and headings, Purpose lines, length under 110 lines, Contents only where 3+ headings exist, and every child named in the parent.<br>• ⚠️ **Table rows lack emojis:** in the field, issue-type, readiness and values tables, against `_markdown_layout.md`.<br>• ⚠️ **Multi-sentence paragraphs:** `_ticket_conventions.md` line 83 and `_sprint_planning.md` line 46.<br>• ⚠️ **Bullet labels differ:** some files open bullets with an emoji, others don't, for example `_field_standards.md` "**IDs:**" and `_business_value.md` "**Acceptable:**". |
| **Currency** | 5/10 | 2026-11-05 | • 🍂 **Dead trigger:** the `loading:` line says "read when writing_style.md's Jira pointer sends Claude here", but no `writing_style.md` exists under `src/claude/` yet.<br>• 🍂 **Unreachable:** nothing in the new config points to `jira.md`, so Claude reaches it only by chance.<br>• 🔍 **Checked and current:** the six child paths exist, and `make install` copies files without touching `_local/`. |
| **Test Coverage** | 7/10 | 2026-11-05 | • 🧪 **Structural test exists:** `tests/src/claude/test_rules_structure.py` covers all seven files, including the child-is-named check, with each check shown able to fail.<br>• 🧪 **No incident record:** none to pin, so no content-regression test is needed.<br>• ⚠️ **No inbound check:** nothing fails when an on-demand rule has no inbound pointer, which is the gap that left this guide unreachable. |
| **Overall** | **5.8/10** | 2026-11-05 | • 💪 **Well split:** a lean parent with six focused children, and site-specific values kept in a local template rather than the repo.<br>• ⚠️ **Gaps:** an unreachable trigger, required fields that disagree between files, and no recorded evidence of use. |

## 🔗 Related files

- `src/claude/rules/_rules_on_demand/style_guides/jira.md` — the rule being scored
- `src/claude/rules/_rules_on_demand/style_guides/jira/_ticket_conventions.md` — Clarity, Structural Compliance
- `src/claude/rules/_rules_on_demand/style_guides/jira/_field_standards.md` — Clarity contradiction, Structural Compliance
- `src/claude/rules/_rules_on_demand/style_guides/jira/_definition_of_ready.md` — Clarity contradiction
- `src/claude/rules/_rules_on_demand/style_guides/jira/_sprint_planning.md` — Clarity, Structural Compliance
- `src/claude/rules/_rules_on_demand/style_guides/jira/_business_value.md` — Structural Compliance
- `src/claude/rules/_rules_on_demand/style_guides/jira/_jira_values_template.md` — Complexity (prerequisite), Currency
- `src/claude_old/rules/_rules_on_demand/style_guides/jira.md` — Evidence of Need (earlier version, created 2026-05-20)
- `src/claude_old/rules/02_conduct/writing_style.md` — Evidence of Need and Currency (the only inbound pointer, in the old config)
- `tests/src/claude/test_rules_structure.py` — Test Coverage
- `docs/maintenance/task_log.md` — Evidence of Need (no Jira entries)
