# 🚧 Build progress

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** which parts of the [target architecture](../docs/target_architecture/README.md) are still outstanding, and the effort each needs.

## 📋 Executive Summary

Of the design's 18 components, 13 are built, 1 is partly built, 2 are not built, 1 is deferred and 1 is out of scope. The largest gap is skills and agents, since none has been ported yet.

## 📊 Outstanding components

Status is 🟡 Partly, ❌ Not built, ⏸️ Deferred or 🚫 Out of scope, and every other component is built. Effort is S (a few hours), M (about a day, in one PR) or L (several PRs). Each component links to the section that describes it:

| Component | Status | Evidence | Outstanding | Effort |
|---|---|---|---|---|
| 🧰 **[Skills and agents](../docs/target_architecture/README.md#️-tiers)** | ❌ Not built | Only the templates in [`src/claude/_templates/`](../src/claude/_templates/) | Review each old-config file, then port, slim or drop it ([#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7), [#85](https://github.com/paulf-999/ai-engineering-playbook/issues/85)) | L |
| 👀 **[PR review loop](../docs/target_architecture/README.md#-workflow)** | 🟡 Partly | The [PR template](../.github/pull_request_template.md)'s Plan Spec and criteria sections, checked by [`pr_description.yml`](../.github/workflows/pr_description.yml) | Port the reviewer agent ([#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7)) | M |
| 🧪 **[Evals](../docs/target_architecture/README.md#-workflow)** | ⏸️ Deferred | — | — | — |
| 🚀 **[CI/CD metrics](../docs/target_architecture/README.md#-workflow)** | 🚫 Out of scope | — | — | — |
| 🔪 **[Halving test](../docs/target_architecture/README.md#-measures)** | ❌ Not built | No review records running it | Run it at the next review and record the answer | S |
