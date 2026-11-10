<!-- version: 1.1.5 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-10 -->
# 🏗️ Repo Quality Rubric

**Purpose:** how a reviewer gives the whole repo a bloat score and an over-engineering score, each out of 10, which per-file scores can't see.

A per-file score rates how well a file is written, not whether it should exist. This rubric looks across files instead.

## 🏷️ Themes

Each theme scores ✅ 2, 🟡 1 or ❌ 0, and each score adds up its 5 themes, so 10 out of 10 means none of the problem.

### 🎈 Bloat

Files and text the repo doesn't need:

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| ⚖️ **Proportionality** | Support files are no more than product files | Up to double | More than double |
| 🧾 **Evidence of need** | At most 1 file has no current user or inbound link | 2 or 3 have none | 4 or more have none |
| 🎯 **Single source** | At most 1 fact, rule or check lives in more than one place | 2 or 3 duplicates | 4 or more duplicates |
| 📦 **Always-on headroom** | Always-on tokens are 75% of the budget or less | Up to 90% | Over 90% |
| 🚧 **Placeholders** | No "not built yet" or "Nothing scored yet" text | 1 to 5 | More than 5 |

### 🏗️ Over-engineering

Process and machinery heavier than the repo needs:

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| 🔗 **Cross-file consistency** | At most 1 contradiction between files | 2 or 3 contradictions | 4 or more contradictions |
| 🔁 **Upkeep cost** | 20% or fewer of the last 50 commits touch `docs/maintenance/`, other than to record a review | Up to 40% | Over 40% |
| 🗃️ **Process weight** | `docs/maintenance/` files are a tenth of product files or fewer | Up to a quarter | More than a quarter |
| 🪜 **Simplest mechanism** | At most 1 check or process is heavier than the simplest that works, such as a scored rubric where a test would do | 2 or 3 | 4 or more |
| 🔮 **Built for today** | At most 1 level, stage or extension point for a need that hasn't arisen | 2 or 3 | 4 or more |

## 📏 How to score

- 📐 **Measured themes:** Proportionality, Always-on headroom, Placeholders, Upkeep cost and Process weight come from the measures below, not judgement, so they can't drift upwards.
- 📍 **Judged themes:** each 🟡 or ❌ for the other five must cite a path.
- 🔢 **Count issues:** score a judged theme by how many distinct issues it has, since a fresh reviewer always finds one or two.
- 🧮 **No double count:** Evidence of need counts whole files nothing uses, and Built for today counts unused capacity inside files that are used.
- 🤝 **Kept by choice:** don't mark down a folder or file that its README or parent rule marks "planned", the separate `shell_utils.sh` copies, the [tests audit](../audits/quality_audit_test_files.md) and [rules audit](../audits/quality_audit_rules.md) with their rubrics and checkers, the per-file version headers and `bump_file_headers.sh`, the budget script's scanning of skills, agents, `@` imports and a project `.claude/`, kept for the planned skills and agents, or the token report, `docs/maintenance/context_cost.md`, whose commits the upkeep measure leaves out.
- 🔢 **Product and support:** product is `src/claude/` and `docs/target_architecture/`, and support is `tests/`, `src/sh/`, `docs/maintenance/` and `.github/`.

## 🔢 Measures

Run these from the repo root on `main` under `bash`, since another shell's `grep` wrapper can change the counts, and score the measured themes from them:

```bash
# product and support file counts
git ls-files src/claude docs/target_architecture | wc -l
git ls-files tests src/sh docs/maintenance .github | wc -l
# files and KB by area
for area in src/claude docs tests src/sh; do echo "${area}: $(git ls-files "${area}" | wc -l) files, $(git ls-files -z "${area}" | xargs -0 cat | wc -c | awk '{print int($1 / 1024)}') KB"; done
# commits of the last 50 on main that touch docs/maintenance/, other than the kept token report,
# leaving out commits that only record a review, by changing nothing outside quality/audits/
git log --first-parent -50 --format=%h origin/main | while read -r commit; do files=$(git show --name-only --format= "${commit}" | grep -v '^docs/maintenance/context_cost\.md$'); grep -q '^docs/maintenance/' <<< "${files}" && grep -qv '^docs/maintenance/quality/audits/' <<< "${files}" && echo "${commit}"; done | wc -l
# docs/maintenance/ files
git ls-files docs/maintenance | wc -l
# placeholder phrases, leaving out this rubric and its audit
git grep -ciE 'not built yet|nothing scored yet' -- '*.md' ':!docs/maintenance/quality/*/quality_*_repo.md' | awk -F: '{sum += $2} END {print sum + 0}'
# always-on tokens, against the 3,000-token budget
src/sh/claude_validate_always_on_budget.sh
```

## 🕵️ Reviewer brief

At each [regular review](../../../target_architecture/design_principles/01_principles.md#-numbers-and-tests), one fresh-context Explore agent gets only this brief, since a primed brief inflates scores:

```text
Score this repo against docs/maintenance/quality/themes/quality_themes_repo.md.
Run its measures, score each theme, and cite a path for each judged 🟡 or ❌.
Return the measures, the ten theme scores with a reason each,
the Bloat and Over-engineering totals, and up to 5 findings ranked by how much
they would cut, each naming the files involved.
Don't open docs/maintenance/quality/audits/quality_audit_repo.md, which holds
the last run's scores.
```

## 📊 Where scores live

The [audit](../audits/quality_audit_repo.md) holds the latest run's scores and the current findings.
