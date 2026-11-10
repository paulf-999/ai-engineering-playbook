<!-- version: 1.0.12 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-10 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

## 💬 Component feedback

How each Claude config component fared in the session transcripts since the last review, as the [target architecture](../../../target_architecture/target_architecture.md#-measures) asks:

| Component | Effect | Evidence |
|---|---|---|
| `02_conduct/behaviour.md` | Helped | "Ask before big changes" and "Present options" led to plans and naming choices confirmed before multi-file edits |
| `_rules_on_demand/03_workflows/git.md` | Helped | "Clean index" and "Unfamiliar changes" kept other sessions' branches and files out of this session's commits |
| `_rules_on_demand/02_conduct/reporting.md`, Checkpoints | Unused | "Checkpoints" never fired, though one session spanned more than 15 PRs |

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ✅ 2 | ✅ 2 | ❌ 0 | ✅ 2 | ✅ 2 | **8/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ❌ 0 | ❌ 0 | ✅ 2 | ✅ 2 | 🟡 1 | **5/10** |

## 🔍 Why the latest scores

Each theme below ✅, with what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 5 duplicates: the token estimate coded in both `shell_utils.sh` and `test_rules_structure.py`, the answer format in both `02_evaluation_criteria.md` and the PR template, the on-demand install location in three files, the grade bands in both per-file rubrics and `_audit_tables.py`, and the 3,000 and 1,200 token limits hard-coded in the PR template | Finding 3 |
| 🔗 **Cross-file consistency** | 4 contradictions: where `TODO.md` lives (`todo_logging.md` against `TODO.md.template`), who measures outcomes (`01_principles.md` and `target_architecture.md` against the repo rubric), where to edit templates (`_templates/README.md` against `src/claude/README.md`), and `CONTRIBUTING.md`'s snake_case against hyphenated skill and agent names | Finding 3 |
| 🔁 **Upkeep cost** | 30 of the last 50 commits touch `docs/maintenance/` other than to record a review | Fewer audit edits per PR |
| 🔮 **Built for today** | 3 unused: the budget script's `.claude/` root, skill and agent parsing and `@` import code, the TODO template's archiving and extra columns, and the PR criteria's hook row | Findings 1 and 2 |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🧮 **PR author rows:** drop the rows that copy numbers CI already checks, and the hook row, and keep the answer format in one file.
2. 🔧 **Budget script:** remove the `.claude/` root, the skill and agent parsing and the `@` import code until they're needed, and share one token estimator with `test_rules_structure.py`.
3. 🔗 **Contradictions and repeats:** settle where `TODO.md` lives and trim its template, drop the backport advice, square the outcome measures with the rubric, and keep the install location in one place.
