# 📏 Measured: do the Terraform rules change Claude's output?

**Purpose:** what 24 scripted runs showed about whether the Terraform rules make Claude follow them, on 4 common Terraform tasks weighted towards the team's layout, CI and tooling.

> [!NOTE]
> Run on 2026-11-20 with Claude Opus 5.5. It measures whether Claude follows the written rules, using checks the rules' author wrote, not whether the result is better Terraform, which needs people to judge. It's 3 runs per task, on one model and one sparse sample project, so treat the figures as a signal, not a precise rate. The pre-commit task is scored from the config each run printed, since the sessions couldn't write the file, and one run with the rules printed none.

## 📊 Results

Each task ran 3 times without the rules and 3 times with them, in a fresh copy of a sparse sample: one flat `terraform/main.tf` with a provider pinned to `>= 2.0`, password login and one warehouse, so the conventions come only from the rules. A script checked each output against the rules:

| Task | Without the rules | With the rules |
|---|---|---|
| 🧩 **Module:** a warehouse with USAGE granted to a list of roles | 63% | 100% |
| 🌍 **Environment:** a UAT warehouse for the reporting team | 21% | 98% |
| 🚀 **CI/CD:** check every PR and deploy on merge to `main` | 30% | 70% |
| 🪝 **Pre-commit hooks** for the repo | 50% | 100%, from 2 runs |
| **All checks**, the mean of the 4 task figures | **41%** | **92%** |

Split by [kind of rule](../../guides/authoring_guide/_rule_classification.md):

| Checks | Without the rules | With the rules |
|---|---|---|
| 🧰 **Standards:** `main.tf`, `variables.tf`, `outputs.tf` and `README.md`, a description and type on every variable, `validation` blocks, `for_each` over `count`, a primary resource named `this`, key-pair login, no hardcoded credentials, `.env` and state in `.gitignore`, remote state, validate and plan on PRs, apply in sequence, secrets from a secret store, the `terraform_fmt` and `detect-private-key` hooks | 61% | 92% |
| 🏢 **Team conventions:** the `terraform/environments/` and `terraform/modules/` layout, `provider.tf`, `.env_template` and `local_terraform_dev.sh`, an exact provider pin, `SCREAMING_SNAKE_CASE` provider variables, `_WH` warehouse names, ownership then usage grants, Azure Pipelines at the team's template paths with Azure Key Vault, all 5 environments with `dependsOn`, the team's hook list and a 120-character `.yamllint` | 26% | 92% |

## 🔍 What changed

- 🌍 **Environments copied the sample without the rules:** all 3 UAT runs kept the `>= 2.0` pin, password login and untyped variables, and none wrote `provider.tf` or `.env_template`.
- 📁 **The team's files only came with the rules:** every environment and module run with them wrote `provider.tf`, and every environment run wrote `.env_template` and `local_terraform_dev.sh`.
- 🧩 **Modules were already close:** without the rules, they used `terraform/modules/`, typed variables, `for_each` and `this`, but none added an ownership grant or a `_WH` name check.
- 🚀 **CI picked the team's tool only with the rules:** all 3 runs without them wrote GitHub Actions, and all 3 with them wrote Azure Pipelines at the team's two template paths, with Azure Key Vault.
- 🪝 **Hooks without the rules were generic:** all 3 had the common hooks, but none had `no-commit-to-branch`, `yamllint`, `yamlfmt` or the 120-character line limit.
- ❌ **Still missed:** all 3 CI runs with the rules deployed the sample's one root, not the 5 environments in sequence, and said so in their reply. One environment run had no remote state backend.

## 🧪 How it was run

- 🗂️ **Sample project:** a `README.md` and the flat `terraform/main.tf` described above.
- 🤖 **Each run:** a separate `claude -p --safe-mode` session, so nothing else loaded, with read and write tools only and the same prompt in both conditions, ending "Go ahead without asking me questions."
- 📦 **With the rules:** the session's system prompt held what a default install loads when Claude works on a `.tf` file: `CLAUDE.md`, the always-on rules, and the Terraform rules with their team conventions. The on-demand files sat in a config folder for Claude to read when a rule pointed there. That matches an install closely, but isn't one, since the installer won't run inside Claude Code.
- 🔒 **Pre-commit config:** Claude Code treats `.pre-commit-config.yaml` as a sensitive file, so every hooks run was blocked from writing it, even with an explicit allow rule. Each run's reply was scored instead, and the one that listed its hooks without printing the file was left out.
- ✅ **Scoring:** a script read each run's new or changed files and checked them. It can tell whether a rule was followed, but not whether `terraform plan` passes.
- 💰 **Cost:** $7.03 for the 24 runs, $4.60 with the rules and $2.43 without, since runs with them wrote more files.
