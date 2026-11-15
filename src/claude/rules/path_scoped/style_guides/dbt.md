---
paths:
  - "**/models/**/*.sql"
  - "**/models/**/*.yml"
  - "**/dbt_project.yml"
---
# 🔵 dbt Style Guide & Standards

**Purpose:** the dbt project's standards for lineage, documentation, tests and materialisation. They adapt [dbt Labs' style guide](https://docs.getdbt.com/best-practices/how-we-style/0-how-we-style-our-dbt-projects) but use their own layers, prefixes and team macros, so edit those to fit your project.

## 🎯 Core principles

- **Lineage:** reference every table with `{{ ref('model') }}` or `{{ source('raw', 'table') }}`, never `schema.table`, so the lineage graph stays correct.
- **Documentation:** give every model and column a `description:` in YAML, since descriptions are the source of truth for downstream teams.
- **Tests:** put `unique` and `not_null` on every model's surrogate key, or an aggregate's grain columns, `relationships` on foreign keys, and `freshness` on every source with a loaded-at column.
- **Materialisation:** start from each layer's default and justify any change, since the wrong choice wastes compute or leaves data stale.
- **Before a PR:** `dbt parse` and `dbt test` pass, as no hook runs them.

## 📚 Read on demand

- `on_demand/style_guides/dbt/_model_organisation.md`, in your Claude config directory, when adding a model or choosing its layer, prefix or materialisation.
- `on_demand/style_guides/dbt/_naming_conventions.md`, when naming a model, column, key or CTE.
- `on_demand/style_guides/dbt/_yaml_resource_properties.md`, when writing model or source YAML.
- `on_demand/style_guides/dbt/_team_conventions.md`, before writing logic a team macro or package may already cover, or using the team's key column, audit fields or folders.
- `on_demand/style_guides/dbt/_snapshots.md`, when adding or changing a snapshot.
