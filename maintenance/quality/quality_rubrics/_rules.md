# 📏 Rules

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the checklist a reviewer runs on each changed rule at a regular review, as part of the [quality rubrics](../quality_rubrics.md).

Right place and No duplicate apply the [evaluation criteria](../../../docs/target_architecture/design_principles/02_evaluation_criteria.md) to one rule at a time. A rule here means an entry-point rule in `src/claude/rules/` together with its children, the `_`-prefixed files it points to.

## ✅ Checklist

| Check | What passing looks like |
|---|---|
| 🎯 **Changes behaviour** | Every point tells Claude something it wouldn't do by default |
| 🧭 **Right place** | Prose is the right form, it loads only for tasks that need it, and must-hold points are also checked |
| 🔁 **No duplicate** | No other rule, doc, hook, test or CI check covers it |
| 📖 **Clarity** | Key point first, every term explained, and Claude can act on it without other pages |
| 🔍 **Accuracy** | Every path, command, link and claim checks out, including any check it says exists |

## 📏 How to check

- 📍 **Cite it:** each finding names the line or file that fails the check.
- 🌐 **Other repos:** a path-scoped rule written for another repo's layout, such as its folders or hooks, isn't inaccurate for naming things this repo lacks.
- 👨‍👧 **Families:** check a rule with its children, since they load together.
- 🧾 **Need at review time:** whether a rule gets used is checked at each regular review, by the evaluation criteria's Trial check, not here.

## 🕵️ Reviewer brief

Each regular review checks every rule changed since the last one. One fresh-context reviewer on Sonnet gets only this brief, since a primed brief goes easier on the work:

```text
Check each rule below against maintenance/quality/quality_rubrics/_rules.md.
Read each rule with its children, and search the repo for duplicates and to check its claims.
Return one finding per failed check: the rule, the check, the line, and the fix.
```

## 🎫 Where findings go

Open a GitHub issue for each finding the review doesn't fix in its own PR, so the fixes are tracked rather than recorded as scores.
