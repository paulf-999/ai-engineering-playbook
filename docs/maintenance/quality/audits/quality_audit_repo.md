<!-- version: 1.0.15 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-11 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

## 💬 Component feedback

How each Claude config component fared in the session transcripts since the last review, as the [target architecture](../../../target_architecture/target_architecture.md#-measures) asks:

| Component | Effect | Evidence |
|---|---|---|
| `hooks/hook_enforcement_plan_sections.sh` | Helped | Blocked 16 plans that lacked Intent or Spec, each sent to `sdlc_workflow.md`, at one resubmit each |
| `_rules_on_demand/03_workflows/sdlc_workflow.md` and `saving_plans.md` | Helped | Read about 6 and 12 times, through the hook and after plan approval |
| `_rules_on_demand/03_workflows/git.md`, `reporting.md` and `portable_paths.md` | Helped | Read about 16, 6 and 5 times |
| `_path_scoped_rules/testing.md`, `code_security.md` and `python.md` | Helped | Loaded in 13 or 14 sessions each, where matching files were open |
| Other stacks' path-scoped and on-demand rules | Unused | Never loaded, since almost all sessions were in this repo |

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-11 | ✅ 2 | ✅ 2 | ❌ 0 | 🟡 1 | ✅ 2 | **7/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-11 | 🟡 1 | ❌ 0 | ✅ 2 | ✅ 2 | ✅ 2 | **7/10** |

## 🔍 Why the latest scores

Each theme below ✅, with what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 4 duplicates: the 110-line limit in `guiding_principles.md`, `authoring_guidelines.md` and `rule.md.template`, the config-change checklist in those 2 rules and `02_evaluation_criteria.md`, the naming rule in `naming_standards.md` and `CONTRIBUTING.md`, and the rule-loading tiers in `src/claude/README.md`, `target_architecture.md` and `_authoring_rules.md` | Finding 4 |
| 📦 **Always-on headroom** | About 2,265 of 3,000 tokens, or 75.5%, about 15 tokens over the 75% line | Finding 5 |
| 🔗 **Cross-file consistency** | 2 contradictions: `target_architecture.md` red-flags porting any hook where `02_evaluation_criteria.md` flags only every-prompt hooks, and `quality_themes_rules.md` and `quality_themes_test_files.md` re-score inside the PR where `CONTRIBUTING.md` uses a follow-up audit-only PR | Fix both lines |
| 🔁 **Upkeep cost** | 25 of the last 50 commits, or 50%, of which 12 edit this rubric and 9 count only because a product commit also re-scored an audit row | Finding 3 |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 📚 **Merge split reference docs:** fold the numbered pages under `reference_material/core/anthropic_ai_native_sdlc/`, `reference_material/core/dora_ai_capabilities/` and `current_architecture/` into their parent pages, about 14 files.
2. 🧾 **Unread usage lines:** drop the `applies_to` and `miss_cost` lines from 36 rules, with their check in `test_rules_structure.py` and their mentions in `file_headers.md`, `_authoring_rules.md` and `rule.md.template`.
3. 🔁 **Upkeep measure:** count only commits that change `docs/maintenance/` outside `quality/audits/`, so a product commit that also re-scores an audit row doesn't count.
4. 🎯 **One home per fact:** keep the 110-line limit, the config-change checklist, the naming rule and the rule-loading tiers in one place each, and link to them.
5. ✂️ **Trim always-on text:** cut about 20 tokens where `behaviour.md` overlaps `src/claude/CLAUDE.md` and `claude_plans.md`.
