<!-- version: 1.0.12 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-10 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ✅ 2 | ✅ 2 | ❌ 0 | ✅ 2 | ✅ 2 | **8/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ❌ 0 | ❌ 0 | ✅ 2 | 🟡 1 | 🟡 1 | **4/10** |

## 🔍 Why the latest scores

Each theme below ✅, with what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 5 duplicates: the token estimate coded in both `shell_utils.sh` and `test_rules_structure.py`, the evaluation standards in both `02_evaluation_criteria.md` and the PR template, the 20-file PR limit in five files, the install location in six, and principles restated in `05_proposed_changes.md` | Findings 1, 2 and 4 |
| 🔗 **Cross-file consistency** | 6 contradictions: component feedback said to be recorded but never measured, a CI warning pointing to a tests reviewer brief that doesn't exist, an evidence-of-need row the PR template lacks, per-file red flags against a per-standard table, `05_proposed_changes.md` calling adopted changes unadopted, and `CLAUDE.md` leaving out `src/claude/` | Findings 1, 2 and 5 |
| 🔁 **Upkeep cost** | 32 of the last 50 commits touch `docs/maintenance/` other than to record a review, many retuning the rubric itself | Finding 3 |
| 🪜 **Simplest mechanism** | 2 heavier than needed: a reviewer agent for every config PR on top of the tests, and the `loading:` header line that repeats its folder | Findings 1 and 4 |
| 🔮 **Built for today** | 3 unused: the `ALWAYS_ON_TOKEN_BUDGET` and `MAX_FILES_ALLOWED` overrides, the per-turn overhead red flag with no hooks, and the six further-reading sources nothing links to | Findings 2 and 5 |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. ⚖️ **One home for the evaluation criteria:** keep the table in the PR template, link to it from `02_evaluation_criteria.md`, settle the per-file red flags and evidence-of-need row, and cut the restated instruction in `CONTRIBUTING.md`.
2. 🗑️ **Old proposals and further reading:** retire `current_architecture/05_proposed_changes.md`, and decide whether the six further-reading sources stay in `reference_material/README.md`.
3. 🧊 **Rubric churn:** freeze the repo rubric between regular reviews, and point the CI warning only to rubrics that have a reviewer brief.
4. 🧮 **One token estimator:** share the comment-stripping and ÷ 4 logic between `shell_utils.sh` and `test_rules_structure.py`, and drop the `loading:` line that repeats the folder.
5. 🔗 **Measures and restatements:** square the component-feedback claim with the rubric, state the 20-file limit and install path once, drop the unused env overrides, and add `src/claude/` to `CLAUDE.md`'s project line.
