<!-- version: 1.0.0 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-09 -->
# 📏 Rule Quality Rubric

**Purpose:** how a reviewer scores each Claude rule out of 10 for whether it earns its place, which the markdown rubric, judging only how it's written, doesn't cover.

The themes apply the [evaluation criteria](../../../target_architecture/design_principles/02_evaluation_criteria.md) to one rule at a time. A rule here means an entry-point rule in `src/claude/rules/` together with its children, the `_`-prefixed files it points to.

## 🏷️ Themes

Each theme scores ✅ 2, 🟡 1 or ❌ 0, and the totals map to grades: A for 9 or more, B for 8, C for 7, D for 6, and F below 6.

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| 🧾 **Evidence of need** | It answers a real, recurring problem, such as a correction or a task-log row | Plausible, but no evidence is cited or found | Speculative |
| 🧭 **Right mechanism** | Prose guidance is the right form for what it asks | Part of it would fit a skill, `CLAUDE.md` or a check better | Mostly the wrong form |
| 🎚️ **Right tier** | It loads only for the tasks that need it | Loads somewhat wider than needed, such as broad `paths:` globs | Loads every session, though only some tasks need it |
| 🔁 **No duplicate** | Nothing else covers it: no other rule, check or default Claude behaviour | One point repeats another source | Mostly repeats another source |
| 🛡️ **Enforced** | Anything that must always hold is also checked by a hook, test or CI | One must-hold point is prose only | Several are prose only |

## 📏 How to score

- 📍 **Cite it:** each 🟡 or ❌ names the line or file that costs the mark.
- 👨‍👧 **Families:** score a rule with its children, since they load together, and leave the children without rows.
- 🔁 **Defaults count:** a point Claude follows without being told is a duplicate, since it costs context for nothing.
- 🕳️ **Gaps:** name every theme below ✅ in the audit's Gaps column, starting with the theme's name.

## 🕵️ Reviewer brief

A PR that changes a rule refreshes that rule's row. One fresh-context reviewer on Sonnet gets only this brief, since a primed brief inflates scores:

```text
Score each rule below against docs/maintenance/quality/themes/quality_themes_rules.md.
Read each rule with its children, and search the repo for evidence and duplicates.
Return one audit row per rule: the five theme scores, the grade and total, and Gaps.
```

## 📊 Where scores live

The [audit](../audits/quality_audit_rules.md) holds each rule's row.
