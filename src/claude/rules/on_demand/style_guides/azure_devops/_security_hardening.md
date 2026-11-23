# 🛡️ Security hardening

**Purpose:** the Azure Pipelines practices that keep secrets, service connections and agents from being abused, following Microsoft's "Secure Azure Pipelines" guidance. This team's pools, triggers and Key Vault steps are in [`azure_devops_team_conventions.md`](../../../path_scoped/style_guides/azure_devops_team_conventions.md).

## 🔑 Secrets and service connections

- **Key Vault:** link secrets from Azure Key Vault, through a variable group or an `AzureKeyVault@2` step, rather than storing them in pipeline settings.
- **Narrow filters:** set the Key Vault step's `SecretsFilter` to the secrets the job needs where it can, so a job fetches no more than it uses.
- **Workload identity:** create Azure service connections with workload identity federation, not a client secret that expires and can leak.
- **Pipeline permissions:** grant each service connection, variable group and environment to the pipelines that need it, never to all pipelines.

## 🚪 Untrusted input

- **Fork builds:** leave "Make secrets available to builds of forks" off, so a fork's PR runs without secrets.
- **Queue-time variables:** turn on "Limit variables that can be set at queue time", and list any that may change under `settableVariables`.
- **Shell arguments:** turn on "Enable shell tasks arguments validation", so a crafted value can't add commands through a task's `arguments`.
- **Untrusted values:** treat `System.PullRequest.*`, `Build.SourceBranch` and any commit message or PR title as untrusted input.

## 🔒 Templates and environments

- **Required templates:** add a "Required template" check on production environments and service connections, so only pipelines that extend the approved template can use them.
- **Approvals:** put approvals and branch control checks on each production environment, allowing only the release branch.
- **Job scope:** keep "Limit job authorization scope to current project" on, so the job token can't reach other projects.

## 🖥️ Agents

- **Separate pools:** run PR builds and deploys on different agent pools, so untrusted PR code never runs where deploy credentials live.
- **Clean workspaces:** set `workspace: clean: all` or `checkout: clean: true` on self-hosted agents, so one run can't leave files for the next.

## 📝 Logs and artifacts

- **No secret output:** never `echo`, run `set -x` or dump `env` in a step that holds a secret, since masking misses transformed values.
- **Derived secrets:** register any value built from a secret with `##vso[task.setvariable variable=NAME;issecret=true]`, so the logs mask it.
- **Artifacts:** never publish a folder holding credentials, such as `.git/` or a rendered config file, as a pipeline artifact.

## 📞 Called by

This rule is invoked by [`rules/path_scoped/style_guides/azure_devops.md`](../../../path_scoped/style_guides/azure_devops.md), before adding a secret, a service connection, a deploy stage or a third-party task.
