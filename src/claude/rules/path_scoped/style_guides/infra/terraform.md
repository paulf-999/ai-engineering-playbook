---
paths:
  - "**/*.tf"
---
<!-- version: 1.5.5 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-13 -->
<!-- applies_to: Terraform files -->
<!-- miss_cost: medium — infrastructure code drifts from the team's layout and needs reworking -->
# 🏗️ Terraform Style Guide & Standards

**Purpose:** Define the team's standards for the Terraform that manages Snowflake infrastructure and deploys through Azure Pipelines.

## 🏗️ Core principles

- **Separation by environment:** each environment (`dev`, `uat`, `cicd`, `prod`, `global`) is an independent Terraform root module with its own state.
- **Modules for reuse:** shared resource patterns (roles, warehouses, grants) live in `terraform/modules/` and are called from environment configurations.
- **Config-driven:** no credentials or environment-specific values are hardcoded; use `.env_template` to guide local setup.
- **Validation-first:** variable inputs are validated with `validation` blocks; naming conventions for Snowflake objects are enforced at the variable level.
- **Infrastructure only:** Terraform manages Snowflake infrastructure (roles, warehouses, databases, grants), not application logic.

## 📚 Read on demand

- `on_demand/style_guides/infra/terraform/_structure.md`, in your Claude config directory, when adding a module or environment, or deciding what to commit.
- `on_demand/style_guides/infra/terraform/_conventions.md`, when naming a Snowflake object, resource, module, variable or output.
- `on_demand/style_guides/infra/terraform/_declarations.md`, when declaring a variable or output, or adding a validation block.
- `on_demand/style_guides/infra/terraform/_modules.md`, when composing modules, using `for_each` or adding a `lifecycle` block.
- `on_demand/style_guides/infra/terraform/_providers.md`, when pinning, authenticating or configuring the Snowflake provider.
- `on_demand/style_guides/infra/terraform/_ci_and_tooling.md`, when a pre-commit hook or pipeline stage fails.
