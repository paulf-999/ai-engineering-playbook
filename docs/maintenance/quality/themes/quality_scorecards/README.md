<!-- version: 1.0.1 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-05 -->
# 📊 Quality Scorecards

**Purpose:** One home for the quality scorecards that review this config's artefacts — kept apart from rules and skills, since they're review records Claude never reads while working.

This page is part of the maintainers' quality docs described in the [docs folder guide](../../../../README.md), beside the [markdown rubric](../quality_themes_markdown_files.md). It lives in the playbook repo, not in the installed config.

---

## 📁 Where each scorecard lives

| Folder | Scores | File pattern |
|---|---|---|
| `agents/` | Agents in `agents/`, one flat folder | `agents/scorecard_<agent_name>.md` |
| `hooks/` | Hooks in `hooks/`, one flat folder | `hooks/scorecard_<hook_name>.md` |
| `rules/` | Rules in `rules/`, mirroring the rule's current tier, with `_rules_on_demand/` for on-demand rules and `_path_scoped_rules/` for path-scoped rules, style guides included | `rules/<tier>/scorecard_<rule_name>.md` |
| `skills/` | Skills in `skills/`, one flat folder | `skills/scorecard_<skill_name>.md` |
| `tests/` | Tests in this repo's `tests/`, mirroring the `tests/` path | `tests/<subpath>/scorecard_<test_file_stem>.md` |

- **Summaries:** each folder has a `<type>_scorecards_summary.md` rollup (e.g. [`skills/skill_scorecards_summary.md`](skills/skill_scorecards_summary.md)) — update it in the same commit as any scorecard change.
  - **Top-level rollup:** [`quality_scorecards_summary.md`](quality_scorecards_summary.md) compares all five types and ranks the next actions.
  - **Template:** all six summaries follow [`_templates/scorecard/scorecard_summary.md.template`](../../../../../src/claude/_templates/scorecard/scorecard_summary.md.template).
- **Templates:** rules use the template in [`rules/README.md`](rules/README.md), and skills use [`_templates/skills/_quality_scorecard_template.md`](../../../../../src/claude/_templates/skills/_quality_scorecard_template.md).
- **Never `@import`:** these files are for review and audit only, so they cost no session tokens.
- **Audits:** cross-cutting audits of whole areas live in the playbook repo under [`docs/maintenance/quality/audits/`](../../audits/), not here.

---

## 🔍 Independent review

Skills, rules and agents are scored by a reviewer that didn't write them, so the author never marks their own work.

### 📏 Rules: one review per PR

1. **Free checks:** `make test` passes, including [the rule structure test](../../../../../tests/src/claude/test_rules_structure.py), which checks layout, usage lines, inbound pointers and pointer paths.
2. **Author's table:** the PR's evaluation table is filled in, including each rule's evidence of need.
3. **One review:** a single fresh-context Agent call on Sonnet scores Clarity, Evidence of Need and Currency for every rule the PR adds or changes, reading only those rules, their pointer targets, [the rules rubric](rules/README.md) and [`scoring_anchors.md`](scoring_anchors.md).
4. **Record:** each rule gets a row in [`rule_scorecards_summary.md`](rules/rule_scorecards_summary.md) and in [`score_history.csv`](score_history.csv), and the findings go in the PR, with no per-file scorecard.
5. **Skip:** a PR that only moves or renames rules needs no review.

- **Baseline:** the 7 scorecard files under `rules/` are the first full review, kept for reference rather than updated.

### 🧩 Skills and agents

1. **Deterministic checks:** `make test` and `pre-commit run --all-files` pass before any scoring.
2. **Evals:** the artefact's evals exist at the count its maturity needs.
   - **Agents:** run `python3 src/claude/scripts/_audit_scripts/audit_agent_evals.py <agent>` (not built yet) and give the reviewer its pass rate, which costs one Claude call per runnable eval.
3. **Fresh-context review:** call the Agent tool with `subagent_type: quality_scorecard_reviewer` (not built yet), passing only the artefact's path and its type.
   - **Its inputs:** the artefact, its contract, its evals, the type's rubric and [`scoring_anchors.md`](scoring_anchors.md).
   - **Never pass:** the authoring conversation or the current scorecard's scores, since either would anchor the result.
4. **History row:** append the row it returns to [`score_history.csv`](score_history.csv) as the next attempt, then copy the scores into the scorecard and its summaries.
   - **Enforced by:** `test_score_history.py` (not built yet), which fails when attempts skip or the latest row doesn't match the scorecard.
5. **Human review:** a [CODEOWNERS](../../../../../.github/CODEOWNERS) reviewer approves the scorecard change in the PR.

- **Anchors:** [`scoring_anchors.md`](scoring_anchors.md) shows what a 5, a 7 and a 9 look like for each type.
- **Seed rows:** attempt 1 for every scorecard that existed before this flow says `reviewer=author`, since those scores were self-assessed.
- **Not yet covered:** hooks and tests keep author scoring for now.

---

## 🚀 Top 5 recommended actions

The five lowest-scoring artefacts, each with the first recommended improvement from its scorecard.

| # | Artefact | Score | Action | Scorecard |
|---|---|---|---|---|
| — | — | — | Nothing is scored yet | — |

- **Upkeep:** refresh this list whenever a scorecard is re-scored.
- **Full ranking:** see [`quality_scorecards_summary.md`](quality_scorecards_summary.md).
