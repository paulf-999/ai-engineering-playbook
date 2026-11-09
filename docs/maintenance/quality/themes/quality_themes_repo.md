<!-- version: 1.0.1 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-09 -->
# 🏗️ Repo Quality Rubric

**Purpose:** how a reviewer gives the whole repo a bloat score and an over-engineering score, each out of 10, which per-file scores can't see.

A per-file score rates how well a file is written, not whether it should exist. This rubric looks across files instead.

## 🏷️ Themes

Each theme scores ✅ 2, 🟡 1 or ❌ 0. The themes add up to two scores, where 10 means none of the problem:

- 🎈 **Bloat:** Proportionality, Evidence of need and Single source, out of 6.
- 🏗️ **Over-engineering:** Cross-file consistency and Upkeep cost, out of 4.
- 🔢 **Scaled:** each score is scaled to 10 and rounded to the nearest whole number, with halves rounded up.

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| ⚖️ **Proportionality** | Support files are no more than product files | Up to double | More than double |
| 🧾 **Evidence of need** | Every component has a current user, inbound link or task-log row | One component has none | Several have none |
| 🎯 **Single source** | Each fact, rule or check lives in one place | One duplicate | Several duplicates |
| 🔗 **Cross-file consistency** | No file contradicts another | One contradiction | Several contradictions |
| 🔁 **Upkeep cost** | 20% or fewer of the last 50 commits touch `docs/maintenance/` | Up to 40% | Over 40% |

## 📏 How to score

- 📐 **Anchored themes:** Proportionality and Upkeep cost come from the measures below, not judgement, so they can't drift upwards.
- 📍 **Judged themes:** each 🟡 or ❌ for the other three must cite a path.
- 🗓️ **Planned folders:** a folder its README marks "planned" doesn't count against Evidence of need.
- 🔢 **Product and support:** product is `src/claude/` and `docs/target_architecture/`, and support is `tests/`, `src/sh/`, `docs/maintenance/` and `.github/`.

## 🔢 Measures

Run these from the repo root on `main`, and record each result:

```bash
# product and support file counts
git ls-files src/claude docs/target_architecture | wc -l
git ls-files tests src/sh docs/maintenance .github | wc -l
# files and KB by area
for area in src/claude docs tests src/sh; do echo "${area}: $(git ls-files "${area}" | wc -l) files, $(git ls-files -z "${area}" | xargs -0 cat | wc -c | awk '{print int($1 / 1024)}') KB"; done
# commits of the last 50 that touch docs/maintenance/
for commit in $(git log --first-parent -50 --format=%h); do git show --name-only --format= "${commit}" | grep -q '^docs/maintenance/' && echo "${commit}"; done | wc -l
# always-on tokens
src/sh/claude_validate_always_on_budget.sh
```

## 🕵️ Reviewer brief

At each [regular review](../../../target_architecture/design_principles/01_principles.md#-numbers-and-tests), one fresh-context Explore agent gets only this brief, since a primed brief inflates scores:

```text
Score this repo against docs/maintenance/quality/themes/quality_themes_repo.md.
Run its measures, score each theme, and cite a path for each judged 🟡 or ❌.
Return the measures, the five theme scores with a reason each, the two scores,
and up to 5 findings
ranked by how much they would cut, each naming the files involved.
```

## 📊 Where scores live

The [audit](../audits/quality_audit_repo.md) holds one row per run and the current findings.
