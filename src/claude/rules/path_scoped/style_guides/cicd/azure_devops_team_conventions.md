---
paths:
  - "**/azure_pipeline*.yml"
  - "**/azure_pipeline*.yaml"
  - "**/azure-pipelines*.yml"
  - "**/azure-pipelines*.yaml"
  - "**/cicd/pipelines/**/*.yml"
  - "**/cicd/pipelines/**/*.yaml"
---
# 🔷 Azure DevOps team conventions

**Purpose:** this team's pipeline layout, triggers, names and values. Another team can replace them with its own, while the standards stay in `azure_devops.md`.

## 🧱 Basics

- 📁 **Entry pipelines:** `src/cicd/azure_pipeline_<purpose>[_<env>].yml`, such as `azure_pipeline_pr.yml` or `azure_pipeline_code_deployment_prod.yml`, never at the repo root, creating `src/cicd/` if the repo has none.
- 🗂️ **Templates:** under `src/cicd/pipelines/`, in `pr_pipelines/`, `code_deployment_pipelines/` and `template_pipelines/`.
- 🐚 **Scripts and tests:** scripts in `src/cicd/scripts/<area>/`, with their bats tests in `tests/cicd/<area>/`.
- 📐 **Formatting:** every file opens with `---` and uses 4-space indents.
- 🏷️ **Names:** camelCase job IDs, such as `validateGit`, and quoted `displayName`s, such as `'Prep step: render the config file'`.
- 🖥️ **Pools:** PR and deploy pipelines run on separate agent pools, and a pytest consistency check fails if a pipeline uses the wrong one.

## 🎯 Triggers

- 🔍 **PR pipeline:** `pr:` with `autoCancel: true`, `branches` of `main` and a `paths.include` filter, and each stage gated on `eq(variables['Build.Reason'], 'PullRequest')`.
- 🚀 **Deploy pipelines:** `pr: branches: exclude: ['*']`, a `trigger:` on the environment's branch, and `name: Release-$(Date:yyyyMMdd).$(Rev:r)`.
- 🧩 **Shared deploy:** each deploy pipeline `extends:` the shared deploy template, passing its environment as parameters.

## 🔑 Variables

- 📄 **Shared values:** non-secret values live in `template_pipelines/template_cicd_variables.yml`, pulled in with `- template:` under `variables:`.
- 🔐 **Secrets:** an `AzureKeyVault@2` step with `RunAsPreJob: true` fetches them, and each step maps the ones it needs in `env:`.
- 💬 **Comments:** every variable has a comment saying what it holds.

## 🔧 Steps

- 🐚 **Scripts:** every shell command lives in a script file, run by `Bash@3` with `filePath: $(CICD_SCRIPTS_DIR)/<area>/<script>.sh` and its inputs in `arguments` or `env:`.
- 🚫 **No inline shell:** never use `script:`, `bash:` or an inline `targetType`, however short, and move any inline step out when editing its job.
- ☁️ **Azure resources:** `AzureCLI@2` with `azureSubscription: <service-connection>` and `scriptLocation: scriptPath`.
- 🌿 **Branch diffs:** `checkout: self` with `clean: true` and `fetchDepth: 0`, so a job can compare the PR branch with `main`.
- 📣 **Notifications:** a notify job with `condition: always()` reads the build's result through `dependencies.<job>.outputs['<step>.<VAR>']`, or `stageDependencies.<stage>.<job>.outputs[...]` from a later stage, which the script sets with `isOutput=true`.

## 📋 Standard PR pipeline boilerplate

```yaml
---
variables:
    # Shared non-secret values
    - template: pipelines/template_pipelines/template_cicd_variables.yml

    # Where the CI/CD scripts live in the repo
    - name: CICD_SCRIPTS_DIR
      value: src/cicd/scripts

pr:
    autoCancel: true  # cancel the run when a newer commit is pushed
    branches:
        include:
            - main
    paths:
        include:  # only run when these change
            - src/*

pool: <pr-agent-pool>

stages:
    - stage: Lint
      displayName: 'Lint: check the changed files'
      condition: eq(variables['Build.Reason'], 'PullRequest')  # only run on a PR
      jobs:
          - job: lintChangedFiles
            displayName: '- Lint the changed files'
            timeoutInMinutes: 30
            steps:
                - template: pipelines/pr_pipelines/lint_pipeline.yml
```

## 📚 Read on demand

- [`on_demand/style_guides/cicd/azure_devops/_python_jobs_team_conventions.md`](../../../on_demand/style_guides/cicd/azure_devops/_python_jobs_team_conventions.md), in your Claude config directory, when a job sets up Python or installs packages.
