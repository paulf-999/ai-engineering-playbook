<!-- version: 1.0.0 -->
<!-- created: 2026-11-10 -->
<!-- updated: 2026-11-10 -->
# 💰 SQL: Cost guardrails

**Purpose:** the warehouse settings and query checks that keep Snowflake spend down.

- **`AUTO_SUSPEND = 60`:** set on all pipeline warehouses (idle warehouses are the largest spend leak)
- **Match warehouse size to query complexity:**
  - XS: Simple aggregations, tests, dbt runs in dev
  - S: Standard dbt runs in CI/prod
  - M+: Complex transformations, join-heavy queries (should be rare)

- **Validate query scans:** check query profile before merging large refactors
  - Increased scans = increased cost; flag in the PR if bytes scanned rise by more than 20%
