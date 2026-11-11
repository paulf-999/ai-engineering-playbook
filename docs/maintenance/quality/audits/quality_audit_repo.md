<!-- version: 1.0.17 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-11 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

## 💬 Component feedback

How each Claude config component fared in the session transcripts, kept across reviews on the [component feedback page](quality_audit_repo/component_feedback.md).

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-11 | ✅ 2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | **8/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-11 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | 🟡 1 | **7/10** |

## 🔍 Why the latest scores

The blind run of `main` at #165, with each theme below ✅ and what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 3 duplicates: "Right mechanism" in `authoring_guidelines.md` and `guiding_principles.md`, the 110-line limit in `authoring_guidelines.md` and the tests, and the `claude_naming_patterns.md` pointer in `naming_standards.md` and `authoring_guidelines.md` | Finding 3 |
| 📦 **Always-on headroom** | About 2,265 of 3,000 tokens, or 75.5%, just over the 75% line | Trim about 15 tokens |
| 🔗 **Cross-file consistency** | 2 contradictions: `test_maintenance.md` re-scores each test at the regular review where CONTRIBUTING uses a follow-up PR, and `authoring_guidelines.md` restates the line cap and header rules that checks enforce | Findings 4 and 5 |
| 🔁 **Upkeep cost** | 16 of the last 50 commits, or 32% | Leave `docs/maintenance/` alone outside reviews |
| 🔮 **Built for today** | 2 cases: the `applies_to` and `miss_cost` usage lines that nothing reads, and the "Per-turn overhead" red flag while no hook fires every turn | Findings 2 and 5 |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🧪 **Unread style guides:** the run proposed retiring the on-demand style guides no transcript read. This repo holds the intended setup rather than one project's usage, so this one is left as information.
2. 🧾 **Unread usage lines:** drop the `applies_to` and `miss_cost` lines from 38 rules, with their check in `test_rules_structure.py` and their mentions in `_authoring_rules.md`, `file_headers.md` and `rule.md.template`.
3. 🎯 **One checklist:** keep "Right mechanism" and "No duplicate" once, and drop the duplicate naming pointer from `authoring_guidelines.md`.
4. 🧪 **No restated checks:** drop the 110-line and Header gates from `authoring_guidelines.md`, leaving the tests and `file_headers.md` as their homes.
5. ✂️ **Small cuts:** delete the "Rescore" bullet in `test_maintenance.md`, and the "Per-turn overhead" red flag row in `02_evaluation_criteria.md`.
