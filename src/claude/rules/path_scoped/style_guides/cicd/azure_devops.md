---
paths:
  - "**/azure_pipeline*.yml"
  - "**/azure_pipeline*.yaml"
  - "**/azure-pipelines*.yml"
  - "**/azure-pipelines*.yaml"
  - "**/cicd/pipelines/**/*.yml"
  - "**/cicd/pipelines/**/*.yaml"
---
# 🔷 Azure DevOps Style Guide & Standards

**Purpose:** the principles every Azure Pipelines YAML file follows, so CI/CD stays secure, fast and easy to debug. This team's layout, triggers, names and values are in [`azure_devops_team_conventions.md`](azure_devops_team_conventions.md), which loads with this guide.

## 🔐 Security

- **Pinned versions:** pin every task to its major version, such as `Bash@3`, and every container image to a tag or digest, never `latest`.
- **Secrets:** take secrets only from Azure Key Vault or a secret variable group, never from a plain `variables:` value or the YAML itself.
- **Secrets through env:** pass each secret to a step through its `env:` block, since Azure Pipelines doesn't map secret variables to environment variables.
- **No injection:** never put untrusted values, such as `System.PullRequest.SourceBranch` or a PR title, inside `script:`, and pass them through `env:` as quoted `"${VAR}"`.
- **No secret output:** never `echo` a secret, and mark any value derived from one with `issecret=true` when setting it as a variable.
- **Checkout credentials:** leave `persistCredentials` off unless a later step pushes, so the job's token isn't left in `.git/config`.

## ⏱️ Reliability

- **Timeouts:** set `timeoutInMinutes` on every job, sized to the work, since the default is 60 minutes on Microsoft-hosted agents and no limit on self-hosted ones.
- **Narrow triggers:** limit `pr:` and `trigger:` with `branches` and `paths` filters, so a pipeline runs only when its inputs change.
- **Superseded runs:** keep `autoCancel` on for PR triggers, so a new push cancels the older run.
- **Azure Repos PRs:** `pr:` applies only to GitHub and Bitbucket repos, so an Azure Repos PR build comes from a build validation branch policy instead.
- **Deploy gates:** deploy through a deployment job with `environment:`, so the environment's approvals and checks guard it.
- **Explicit order:** give every stage and job that depends on another a `dependsOn`, and any non-default run rule a `condition:`.

## 🧾 Reuse and readability

- **Templates:** reuse logic through templates with typed `parameters:`, and make deploy pipelines `extends:` a shared template.
- **Expression syntax:** use `${{ }}` for compile-time values such as parameters, `$( )` for variables in task inputs, `$[ ]` for runtime values in `variables:`, and bare expressions, such as `eq(...)`, in `condition:`.
- **Names:** give every stage, job and step a `displayName` that says what it checks or does.
- **Scripts:** move a script longer than about 5 lines into a script file in the repo, so it can be linted and tested.
- **Comments:** explain each non-obvious trigger, condition or variable in a comment beside it.

## 📚 Read on demand

[`on_demand/style_guides/cicd/azure_devops/_security_hardening.md`](../../../on_demand/style_guides/cicd/azure_devops/_security_hardening.md), in your Claude config directory, before adding a secret, a service connection, a deploy stage or a third-party task.
