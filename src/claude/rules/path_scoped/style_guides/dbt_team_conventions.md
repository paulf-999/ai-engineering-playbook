---
paths:
  - "**/models/**/*.sql"
  - "**/models/**/*.yml"
  - "**/dbt_project.yml"
---
# 🔵 dbt team conventions

**Purpose:** this team's own dbt choices: its layers, names, snapshot settings and YAML patterns. Another team can replace them with its own, while the standards stay in `dbt.md`.

## 🏛️ Model layers

The project uses a four-layer architecture. Each layer has a distinct responsibility and source of truth:

| Layer | Purpose | Selects from | Materialisation |
|-------|---------|-------------|-----------------|
| **Staging** | Cleans and standardises raw source data. One model per source entity. Light transformations only — rename, recast, deduplicate. | `source()` | Incremental |
| **Base** | Thin interface layer between staging and marts. Applies final column selection and aliasing before business logic. | `ref(staging_*)` | View or table |
| **Mart** | Business logic and transformation. Domain-organised. Combines base models into business-facing datasets. | `ref()` on base models, or `ref(mart_*)` | Table |
| **Publication** | Exposed layer for downstream consumers and reporting. Minimal transformation — selects from mart. | `ref(mart_*)` | Table or view |

## 🏷️ Names

| What | Pattern | Example |
|------|---------|---------|
| Staging model | `staging_<source>_<entity>.sql` | `staging_crm_customer_list.sql` |
| Base model | `<source>_<entity>.sql` | `crm_customer_list.sql` |
| Mart model | `mart_<domain>_<entity>.sql` | `mart_commerce_payouts.sql` |
| Publication model | `pub_<domain>_<entity>.sql` | `pub_commerce_payouts.sql` |
| Snapshot | `dim_<entity>_history.sql` | `dim_merchant_history.sql`, `dim_merchant_all_history.sql` |
| Date-dimension join column | `<event>_KEY` | `SNAPSHOT_DATE_KEY` |
| Staging source YAML | `_staging_src.yml` | `staging/<source>/_staging_src.yml` |
| Base model YAML | `_src_base.yml` | `base/<source>/_src_base.yml` |

## 📸 Snapshots

- 🔍 **Strategy:** `check`, with an explicit `check_cols` list.
- 🗄️ **Schema:** `WAREHOUSE`.
- 📥 **Source:** select from `ref()` on the matching `dim_` warehouse model, not from `source()`.
- 📅 **Date spines:** use the `dbt_date` package.

## 📄 YAML

- 📏 **Line length:** 120 characters, matching the project's SQLFluff config.
- 🗃️ **Database routing:** a Jinja block picks the database from `target.name`, and a `&db_name` anchor reuses it across the source's tables.
- 🔠 **Source names:** source and table names are `UPPER_CASE`, matching Snowflake object names.
- 🔒 **Sensitive data:** flag PII with `meta: {sensitive: true}` on the column.

## 📚 Read on demand

- `on_demand/style_guides/dbt_team_conventions/_macros_and_keys.md`, in your Claude config directory, before writing logic a team macro or package may already cover, or using the team's key column or audit fields.
- `on_demand/style_guides/dbt_team_conventions/_layout.md`, when adding a folder or placing a model or YAML file.
