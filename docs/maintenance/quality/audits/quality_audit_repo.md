<!-- version: 1.0.10 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-10 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ✅ 2 | ❌ 0 | ❌ 0 | ✅ 2 | ✅ 2 | **6/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ❌ 0 | ❌ 0 | ✅ 2 | 🟡 1 | ❌ 0 | **3/10** |

## 🔍 Why the latest scores

Each theme below ✅, with what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🧾 **Evidence of need** | 10 further-reading summaries under `reference_material/further_reading/`, which their own README says nothing in the design links to yet | Finding 1 |
| 🎯 **Single source** | 7 duplicates, among them the 20-file PR limit in five files, the 110-line limit in three, and the parent and child repeats in `airflow.md`, `ansible.md` and the `code_complexity` family | Finding 4 |
| 🔗 **Cross-file consistency** | 5 contradictions: the PR template names a `code_reviewer` agent that doesn't exist, `target_architecture.md` and `01_principles.md` leave always-on rules out of the required core, `test_maintenance.md` says "every few months" against the regular review, the budget script's env var raises the ceiling without a PR, and `01_principles.md` says the repo review checks outcomes it no longer records | Finding 5 |
| 🔁 **Upkeep cost** | 28 of the last 50 commits touch `docs/maintenance/` other than to record a review | Fewer audit edits per PR |
| 🪜 **Simplest mechanism** | 3 heavier than needed: rule scoring, the PR evaluation table, whose author rows repeat checked numbers, and the version-header machinery | Findings 2 and 3 |
| 🔮 **Built for today** | 5 unused: the budget script's `.claude/` root, the hook row in the PR criteria, the `applies_to` and `miss_cost` header lines, `MAX_FILES_ALLOWED`, and the PR template's UAT checkbox | Finding 3 |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 📚 **Further reading:** cut the 10 summaries under `reference_material/further_reading/`, or link them from the design.
2. 🏷️ **Version headers:** replace `bump_file_headers.sh`, its test, `test_file_metadata_headers.py` and `file_headers.md` with git history.
3. 🧮 **PR evaluation table:** drop the author rows the budget check already covers, merge Cost into Always-on weight, and drop the hook row and UAT checkbox.
4. 🎯 **One place per fact:** keep the 20-file and 110-line limits in one place each, and trim the parent and child repeats.
5. 🔗 **Contradictions:** fix the reviewer name, the required core, the review timing, the budget override and the outcomes claim.
