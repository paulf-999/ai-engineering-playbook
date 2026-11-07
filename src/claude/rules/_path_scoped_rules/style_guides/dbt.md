---
<!-- version: 1.5.1 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-07 -->
<!-- applies_to: **/models/**/*.sql, **/dbt_project.yml -->
<!-- miss_cost: medium — models drift from the project's layout and need reworking -->
<!-- loading: path-scoped — loads with dbt files -->
paths:
  - "**/models/**/*.sql"
  - "**/dbt_project.yml"
---

# 🔵 dbt Style Guide & Standards

**Purpose:** Define the dbt project's standards for model organisation, naming, YAML properties, testing, snapshots and macros, so every model is consistent, maintainable and correct.

**Scope:** all models, macros and YAML in the dbt project, building on [dbt Labs' style guide](https://docs.getdbt.com/best-practices/how-we-style/0-how-we-style-our-dbt-projects).

---

## 🎯 Core Principles

**dbt excellence rests on these four pillars:**

1. **Lineage clarity** — use `ref()` and `source()` everywhere; never hardcoded table references
   - **Why:** builds the lineage graph shown in the docs site from `dbt docs generate`, and allows safe refactoring
   - **How:** every table reference is `{{ ref('model') }}` or `{{ source('raw', 'table') }}`
   - **Test:** does the lineage graph in the generated docs show the correct upstream and downstream models?

2. **Documentation completeness** — every model and column has a description
   - **Why:** undocumented models create confusion, and descriptions are the source of truth for downstream teams
   - **How:** add a `description:` field for every model and column in YAML
   - **Test:** do the docs from `dbt docs generate` explain what each model and column contains and who owns it?

3. **Testing discipline** — every model's key and every source has tests
   - **Why:** broken lineage silently corrupts downstream data, and tests catch schema changes immediately
   - **How:** apply `unique` and `not_null` to every model's `KEY`, a `freshness` check, run by `dbt source freshness`, to every source with a loaded-at column, and `relationships` tests on foreign keys
   - **Test:** do CI checks block PRs with missing tests?

4. **Selective materialisation** — choose materialisation strategically, not by default
   - **Why:** the wrong materialisation wastes Snowflake compute or creates stale data
   - **How:** start from each layer's default in the model organisation page listed under Read on demand, and justify any change
   - **Test:** is each materialisation choice justified by query frequency and data volume?

---

## 📂 Model Layers (Architecture)

- **Four layers:** Staging → Base → Mart → Publication.
- **Prefixes:** `staging_`, `mart_` and `pub_`, with no prefix for base models.

---

## ⚠️ Common Mistakes & Recovery

| Mistake | Impact | How to fix |
|---------|--------|-----------|
| Missing `ref()` relationships | Lineage broken; schema changes undetected | Replace `schema.table` with `{{ ref('model_name') }}` |
| No documentation on new columns | BI users confused about column meaning | Add `description:` for every column in YAML |
| Materialised as table when should be view | Data goes stale between scheduled dbt runs | Change `materialized: view` and re-run dbt |
| Missing uniqueness test on key | Duplicate fact rows silently accumulated | Add `unique` and `not_null` tests on `KEY` in the model's YAML |
| No incremental logic in large models | Full model rebuilds waste Snowflake compute | Use `is_incremental()` block with `unique_key` |

---

## ✅ Model Acceptance Checklist

Before marking a model PR as ready:

- [ ] All tables referenced via `{{ ref() }}` or `{{ source() }}`
- [ ] Model and all columns have descriptions in YAML
- [ ] Every source with a loaded-at column has a `freshness` check
- [ ] `KEY` has `unique` and `not_null` tests, and foreign keys have `relationships` tests
- [ ] SQL passes SQLFluff validation, and `dbt parse` and `dbt test` pass
- [ ] Lineage graph in the generated docs shows correct upstream/downstream
- [ ] Materialisation choice justified (view/table/incremental)
- [ ] Documentation generated and reviewed (`dbt docs generate`)

## 📚 Read on demand

- **Read on demand:** `_rules_on_demand/style_guides/dbt/_model_organisation.md`, in your Claude config directory, when adding a model or choosing its layer or materialisation.
- **Read on demand:** `_rules_on_demand/style_guides/dbt/_naming_conventions.md`, when naming a model, column, key or CTE.
- **Read on demand:** `_rules_on_demand/style_guides/dbt/_yaml_resource_properties.md`, when writing model or source YAML.
- **Read on demand:** `_rules_on_demand/style_guides/dbt/_macros.md`, before writing logic a team macro or package may already cover.
- **Read on demand:** `_rules_on_demand/style_guides/dbt/_snapshots.md`, when adding or changing a snapshot.
