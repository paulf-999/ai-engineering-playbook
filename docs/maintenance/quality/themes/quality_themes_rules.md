<!-- version: 2.0.3 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-13 -->
# 📏 Rule Quality Rubric

**Purpose:** how a reviewer scores each Claude rule out of 10 for whether it earns its place and reads correctly, so each rule has one score.

Right place and No duplicate apply the [evaluation criteria](../../../target_architecture/design_principles/02_evaluation_criteria.md) to one rule at a time. A rule here means an entry-point rule in `src/claude/rules/` together with its children, the `_`-prefixed files it points to.

## 🏷️ Themes

Each theme scores ✅ 2, 🟡 1 or ❌ 0, and the totals map to grades: A for 9 or more, B for 8, C for 7, D for 6, and F below 6.

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| 🎯 **Changes behaviour** | Every point tells Claude something it wouldn't do by default | One or two points restate default behaviour | Mostly default behaviour |
| 🧭 **Right place** | Prose is the right form, it loads only for tasks that need it, and must-hold points are also checked | One lapse, such as broad `paths:` globs or a must-hold point left as prose only | Two or more lapses |
| 🔁 **No duplicate** | No other rule, doc, hook, test or CI check covers it | One point repeats another source | Mostly repeats another source |
| 📖 **Clarity** | Key point first, every term explained, and Claude can act on it without other pages | One lapse, such as an undefined term or a buried point | Hard to follow |
| 🔍 **Accuracy** | Every path, command, link and claim checks out, including any check it says exists | One wrong path, link or claim | Several errors |

## 📏 How to score

- 📍 **Cite it:** each 🟡 or ❌ names the line or file that costs the mark.
- 🌐 **Other repos:** a path-scoped rule written for another repo's layout, such as its folders or hooks, isn't inaccurate for naming things this repo lacks.
- 👨‍👧 **Families:** score a rule with its children, since they load together, and leave the children without rows.
- 🧾 **Need at review time:** whether a rule gets used is checked at each regular review, by the evaluation criteria's Trial check, not here.
- 🕳️ **Gaps:** name every theme below ✅ in the audit's Gaps column, starting with the theme's name.

## 🕵️ Reviewer brief

Each regular review refreshes the row of every rule changed since the last one, in one PR. One fresh-context reviewer on Sonnet gets only this brief, since a primed brief inflates scores:

```text
Score each rule below against docs/maintenance/quality/themes/quality_themes_rules.md.
Read each rule with its children, and search the repo for duplicates and to check its claims.
Return one audit row per rule: the five theme scores, the grade and total, and Gaps.
```

## 📊 Where scores live

The [audit](../audits/quality_audit_rules.md) holds each rule's row.
