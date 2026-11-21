# 📏 Measured: do the Azure DevOps rules change Claude's output?

**Purpose:** what 24 scripted runs showed about whether the Azure DevOps rules make Claude follow them, on 4 common Azure Pipelines tasks in a sparse sample project.

> [!NOTE]
> Run on 2026-11-20 with Claude Opus 5.5. It measures whether Claude follows the written rules, using checks the rules' author wrote, not whether the result is a better pipeline, which needs people to judge. It's 3 runs per task, on one model, so treat the figures as a signal, not a precise rate.

## 📊 Results

Each task ran 3 times without the rules and 3 times with them, in a fresh copy of a sparse sample: a small Python package with a `requirements.txt` and one plain `azure-pipelines.yml` that runs ruff, so the conventions come only from the rules. A script checked each output against the rules.

| Task | Without | With |
|---|---|---|
| 🔍 **PR:** lint the Python files with ruff on every PR to `main` | 26% | 84% |
| 🔐 **Secret:** fetch a Key Vault secret and publish the package with it | 28% | 84% |
| 🚀 **Deploy:** a prod pipeline that reuses a shared deploy template | 32% | 90% |
| ✏️ **Edit:** run the pytest tests in a separate job of `azure-pipelines.yml` | 26% | 71% |
| **All checks**, the mean of the 4 task figures | **28%** | **82%** |

Split by [kind of rule](../../guides/authoring_guide/_rule_classification.md):

| Checks | Without | With |
|---|---|---|
| 🧰 **Standards:** pinned task versions, job timeouts, `displayName`s, short inline scripts, narrow triggers, explicit `dependsOn`, secrets through `env:`, deployment jobs with `environment:`, `extends:` with typed parameters, no persisted checkout credentials | 61% | 96% |
| 🏢 **Team conventions:** `src/cicd/` layout for pipelines, templates and scripts, the `---` opener, 4-space indents, commented variables, the shared variables template, camelCase job IDs, quoted `displayName`s, `Bash@3` with `filePath`, the venv preparation script, the PR and deploy trigger patterns, the `Release-` run name, `AzureKeyVault@2` with `RunAsPreJob` | 5% | 78% |

## 🔍 What changed

- 🔐 **Security basics came without the rules:** every task a run used was pinned to its major version, and every secret run passed the token through `env:` and fetched only `api-token` from Key Vault.
- ⏱️ **Timeouts and names came only with the rules:** no run without them set `timeoutInMinutes`, and 7 of 12 left a stage, job or step without a `displayName`.
- 🚀 **Deploys:** with the rules, every deploy pipeline used `extends:`, excluded PR builds and set the `Release-` run name. Without them, all 3 pulled the template in with `- template:` and none did either of the other two.
- 📁 **Layout was the weakest convention:** 4 of 6 PR and secret runs with the rules put the pipeline at the repo root, not under `src/cicd/`, though every deploy run used it. The rerun below shows the fix.
- 🐍 **The Python child was read but not applied:** the edit runs with the rules named the venv preparation script, then used plain `pip`, since the sample has no such script, and kept their test steps inline. The rerun below shows the fix.
- ⚠️ **A claim that didn't hold:** 1 edit run with the rules said it had added the `---` opener and 4-space indents, but its file kept neither.

## 🔁 Rerun after tightening the conventions

[#460](https://github.com/paulf-999/ai-engineering-playbook/pull/460) made two team conventions stricter: entry pipelines go under `src/cicd/`, never the repo root, and every shell command lives in a script file, with no inline `script:` steps. On 2026-11-21, the 3 tasks they affect ran 3 more times each with the rules, scored the same way:

| Task | With, before #460 | With, after #460 |
|---|---|---|
| 🔍 **PR** | 84% | 98% |
| 🔐 **Secret** | 84% | 88% |
| ✏️ **Edit** | 71% | 93% |

- 📁 **Layout fixed:** all 6 PR and secret runs put their pipeline and scripts under `src/cicd/`.
- 🐚 **Scripts fixed:** every new step ran a script file, and 2 of 3 edit runs also moved the existing ruff step out of the YAML.
- 📊 **By kind:** across these 3 tasks, standards held at 95% to 96%, and team conventions rose from 73% to 92%.
- ❌ **Still missed:** all 3 secret runs and 1 PR run skipped the shared variables template, 2 secret runs left the `main` trigger without a `paths:` filter, and 2 of 3 edit runs skipped the venv preparation script.
- 💰 **Cost:** $1.91 for the 9 runs, up from $1.02 for the same 9 before #460, since each run now writes scripts too.

## 🧪 How it was run

- 🗂️ **Sample project:** the sparse sample above, whose `azure-pipelines.yml` has a bare `main` trigger, 2-space indents and no timeout or `displayName`.
- 🤖 **Each run:** a separate `claude -p --safe-mode` session, so nothing else loaded, with read and write tools only and the same prompt in both conditions, ending "Go ahead without asking me questions."
- 📦 **With the rules:** the session's system prompt held what a default install loads when Claude works on an Azure Pipelines file: `CLAUDE.md`, the always-on rules, and the Azure DevOps guide with its team conventions. The on-demand files sat in a config folder for Claude to read when a rule pointed there. That matches an install closely, but isn't one, since the installer won't run inside Claude Code.
- ✅ **Scoring:** a script parsed each run's new or changed YAML and checked it, scoring only the new job in the edit, and skipping file-wide formatting there. It can tell whether a rule was followed, but not whether the pipeline runs.
- 🔧 **Scorer fixes after the runs:** after reading the outputs, a task's `inputs:` block stopped counting as a step of its own, and the shared variables check now applies only where a pipeline declares `variables:`. The figures above use the fixed scorer.
- 💰 **Cost:** $2.50 for the 24 runs, $1.56 with the rules and $0.94 without.
