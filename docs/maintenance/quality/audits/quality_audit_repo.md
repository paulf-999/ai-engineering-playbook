<!-- version: 1.0.9 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-10 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ✅ 2 | ✅ 2 | ❌ 0 | 🟡 1 | ✅ 2 | **7/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ❌ 0 | ❌ 0 | ✅ 2 | 🟡 1 | 🟡 1 | **4/10** |

## 🔍 Why the latest scores

Each theme below ✅, with what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 4 duplicates: `authoring_guidelines.md` repeats three `guiding_principles.md` points, the 110-line limit is written in four files, `naming_standards.md` "Offer options" repeats `behaviour.md` "Present options", and the skill and agent name patterns sit in `claude_naming_patterns.md`, `_authoring_skills.md`, `_authoring_agents.md` and the templates | Finding 3 |
| 📦 **Always-on headroom** | ~2,278 tokens is 76% of the budget, just over the 75% line | Trim about 30 tokens (finding 2) |
| 🔗 **Cross-file consistency** | 4 contradictions: `target_architecture.md`'s tiers have no place for always-on rules, `behaviour.md` "several files" against its `reporting.md` pointer's "many files or turns", `reporting.md` writes to `~/_sessions/` against `portable_paths.md`, and `authoring_guidelines.md` points to a hook pattern that `claude_naming_patterns.md` no longer has | Finding 5 |
| 🔁 **Upkeep cost** | 26 of the last 50 commits touch `docs/maintenance/` other than to record a review | Finding 1 |
| 🪜 **Simplest mechanism** | 2 heavier than needed: the rules and test audits each keep a hand-scored table and checker, where `test_rules_structure.py` and the MoSCoW grep already cover most of it | Finding 1 |
| 🔮 **Built for today** | 3 unused: five of the seven colours in `variables.mk`, `dir_exists` in `shell_utils.sh`, and the untracked `.claude/` root in `claude_validate_always_on_budget.sh` | Finding 4 |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🗑️ **Per-file audits:** retire `quality_audit_rules.md`, `quality_audit_test_files.md`, their rubrics, checkers and `_audit_tables.py`, keeping the MoSCoW grep and test in `test_maintenance.md`.
2. 📦 **Always-on trim:** move `naming_standards.md` on demand, or at least drop its "Offer options", which `behaviour.md` "Present options" covers.
3. 🎯 **One place per point:** cut the `authoring_guidelines.md` bullets that repeat `guiding_principles.md`, and keep name patterns only in `claude_naming_patterns.md`.
4. 🔮 **Unused capacity:** drop the five unused colours in `variables.mk`, `dir_exists` and its test, and the `.claude/` root in `claude_validate_always_on_budget.sh`.
5. 🔗 **Contradictions:** give always-on rules a tier in `target_architecture.md`, give `behaviour.md` and `reporting.md` one threshold, move the `reporting.md` checkpoints into the config directory, and drop "hook" from the naming pointer in `authoring_guidelines.md`.
