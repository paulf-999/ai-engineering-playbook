---
<!-- version: 1.7.0 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-10 -->
<!-- applies_to: dbt models and project files -->
<!-- miss_cost: medium — models drift from the project's layout and need reworking -->
<!-- loading: path-scoped — loads with dbt files -->
paths:
  - "**/models/**/*.sql"
  - "**/models/**/*.yml"
  - "**/dbt_project.yml"
---

# 🔵 dbt Style Guide & Standards

**Purpose:** the dbt project's standards for lineage, documentation, tests and materialisation, building on [dbt Labs' style guide](https://docs.getdbt.com/best-practices/how-we-style/0-how-we-style-our-dbt-projects).

## 🎯 Core principles

- **Lineage:** reference every table with `{{ ref('model') }}` or `{{ source('raw', 'table') }}`, never `schema.table`, so the lineage graph stays correct.
- **Documentation:** give every model and column a `description:` in YAML, since descriptions are the source of truth for downstream teams.
- **Tests:** put `unique` and `not_null` on every model's `KEY`, its surrogate key column, `relationships` on foreign keys, and `freshness` on every source with a loaded-at column.
- **Materialisation:** start from each layer's default and justify any change, since the wrong choice wastes compute or leaves data stale.
- **Before a PR:** `dbt parse` and `dbt test` pass, as no hook runs them.

## 📚 Read on demand

- **Read on demand:** `_rules_on_demand/style_guides/dbt/_model_organisation.md`, in your Claude config directory, when adding a model or choosing its layer, prefix or materialisation.
- **Read on demand:** `_rules_on_demand/style_guides/dbt/_naming_conventions.md`, when naming a model, column, key or CTE.
- **Read on demand:** `_rules_on_demand/style_guides/dbt/_yaml_resource_properties.md`, when writing model or source YAML.
- **Read on demand:** `_rules_on_demand/style_guides/dbt/_macros.md`, before writing logic a team macro or package may already cover.
- **Read on demand:** `_rules_on_demand/style_guides/dbt/_snapshots.md`, when adding or changing a snapshot.
