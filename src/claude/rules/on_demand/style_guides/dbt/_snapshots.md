# 📸 dbt Snapshots

**Purpose:** Cover naming conventions, configuration standards, best practices, and guidance on building downstream models on top of snapshots.

## 🏷️ Naming

Snapshots follow the team's naming pattern, in [`dbt_team_conventions.md`](../../../path_scoped/style_guides/dbt_team_conventions.md).

## 📋 Contents

- [🔧 Configuration](#-configuration)
- [✅ Best practices](#-best-practices)
- [📐 Building models on top of snapshots](#-building-models-on-top-of-snapshots)

---

## 🔧 Configuration

Use the team's strategy and schema, in [`dbt_team_conventions.md`](../../../path_scoped/style_guides/dbt_team_conventions.md). With the `check` strategy, dbt compares a defined list of columns on each run and creates a new snapshot record when any of them change.

| Setting | Value |
|---------|-------|
| `strategy` | The team's |
| `unique_key` | The surrogate key of the source model |
| `target_schema` | The team's, set as `schema` in dbt 1.9 and later |
| `check_cols` | Explicit list of columns to watch — do not use `'all'` in production |

---

## ✅ Best practices

| Category | Guideline |
|----------|-----------|
| **Source** | Snapshot the model the team names, per [`dbt_team_conventions.md`](../../../path_scoped/style_guides/dbt_team_conventions.md) |
| **Transformations** | Avoid transformations inside snapshots — clean data in the upstream dim model |
| **Row limiting** | Include the team's row-limiting macro, per [`_macros_and_keys_team_conventions.md`](_macros_and_keys_team_conventions.md) |
| **Column list** | Define `check_cols` explicitly — avoids unintended snapshot triggers from irrelevant column changes |
| **Idempotency** | Snapshots must be safe to re-run without duplicating or corrupting history |

---

## 📐 Building models on top of snapshots

When a record-per-day view is needed rather than a record-per-change, use a **date spine** — join the snapshot model to a date spine based on `dbt_valid_from` and `dbt_valid_to`. The team's date package provides utilities for this.

If the date spine produces high row counts, materialise the downstream model as incremental so only new `snapshot_date` records are appended on each run.

## 📞 Called by

This rule is invoked by [`rules/path_scoped/style_guides/dbt.md`](../../../path_scoped/style_guides/dbt.md), when adding or changing a snapshot.
