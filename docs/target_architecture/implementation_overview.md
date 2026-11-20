# 🧩 Implementation overview

**Purpose:** how each claim in the [README](../../README.md) intro is built, with links to the files that deliver it.

## 🛠️ One-command setup

What `make install` does:

- 📦 **Copy:** it copies [`src/claude/`](../../src/claude/README.md) into `~/.claude`, or into one repo's `.claude/` folder with `PROJECT=<path>`.
- 🪄 **Guide:** the [getting-started guide](../guides/getting_started.md) covers which install to choose.

## ⚡ Selective loading

Each rule's top folder decides when it loads, per the [rules README](../../src/claude/rules/README.md) and the [tiers](architecture/_tiers.md):

- 🌱 **Always on:** [`rules/always_on/`](../../src/claude/rules/always_on/) loads in every session.
- 📍 **Path scoped:** [`rules/path_scoped/`](../../src/claude/rules/path_scoped/) loads only when Claude touches a file matching the rule's `paths:` frontmatter.
- 💤 **On demand:** [`on_demand/`](../../src/claude/rules/on_demand/) installs beside `rules/`, so it loads only when a rule's "Read on demand" pointer sends Claude there.
- 🛠️ **Skills and agents:** [skills](../../src/claude/skills/) and [agents](../../src/claude/agents/) load only when called by name or matched by their description.

## 🔄 Spec-led workflow

Claude agrees a plan before coding, and hooks enforce the key steps, as the [workflow](architecture/_workflow.md) explains:

- 📝 **Rule:** [`ai_sdlc_workflow.md`](../../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) sets the stages: Intent, Spec, Plan, Feedback loop and Review.
- 📋 **Plan check:** [`hook_enforcement_plan_sections.sh`](../../src/claude/hooks/hook_enforcement_plan_sections.sh) blocks a plan of 15 or more lines with no Intent or Spec heading.
- ✅ **Done check:** [`hook_enforcement_done_checks.sh`](../../src/claude/hooks/hook_enforcement_done_checks.sh) sends Claude back once to run the repo's done checks before it stops.
- 🪝 **All hooks:** the [hooks README](../../src/claude/hooks/README.md) lists each hook and the rule it enforces.

## 📏 Evidence

The rules are backed by checks and measured runs:

- 💰 **Budget:** a pre-commit check, [`claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh), caps the always-on text, and `make context_cost` writes the token report to [`maintenance/context_cost.md`](../../maintenance/context_cost.md), per [budget and guards](architecture/_budget_and_guards.md).
- 🔍 **Measured runs:** the [dbt](../examples/dbt/dbt_rules_measured.md), [Airflow](../examples/airflow/airflow_rules_measured.md), [SQL and Snowflake](../examples/sql/snowflake_rules_measured.md), [Terraform](../examples/infra/terraform_rules_measured.md), [Ansible](../examples/infra/ansible_rules_measured.md), [GitHub Actions](../examples/cicd/cicd_rules_measured.md) and [Azure DevOps](../examples/cicd/azure_devops_rules_measured.md) runs compare Claude with and without the rules.
- 🧪 **Evals:** [`evals.yaml`](../../src/claude/rules/evals.yaml) holds rule cases, and `make evals RULES=1` runs each with and without its rule.
- 📏 **Reviews:** each regular review records which parts helped, per the [measures](architecture/_measures.md).
