# 🚀 Deploy stage

**Purpose:** how to review a change, hold it at approval gates and release it safely, with Claude acting up to the production gate and never past it.

## 👀 Review passes

Run the same passes on every PR, and tag each finding with its pass:

| Pass | Looks for |
|---|---|
| 🐞 Bugs | Logic errors, broken edge cases and subtle regressions |
| 🔐 Security | What the [security rule](../../../always_on/01_standards/security.md) covers, injection, authentication gaps and personal data in logs |
| 📋 Compliance | Differences from the spec, the plan and the design principles |

- 🚩 **Important:** a finding that would break behaviour, leak data or breach a policy.
- ✏️ **Minor:** style and naming, capped at five per review, with the rest given as a count.
- ⏭️ **Skip:** generated files, and anything CI already enforces.

## 🔁 After review

1. Address each comment, push the fix if that's authorised, and record what changed in the PR thread.
2. Repeat until checks are green and no findings are open.
3. For a finding flagged a second time, propose a correction to `CLAUDE.md` or the relevant rule.
4. Say when the change has made that guidance out of date.

- 🎚️ **Tuning:** rate findings regularly, such as monthly, to cut noise.
- 🏢 **If a review service or CI action is set up:** it can run the passes from a `REVIEW.md`, and severity counts can feed a merge check.

## ✍️ Separate approval

- 🙅 **No self-approval:** the agent that wrote a change never approves it, and a finding neither approves nor blocks by itself.
- 🙋 **Person:** a human approves, through branch protection where the repo has it.
- 👤 **Solo maintainer:** follow the repo's own merge rules, and use an independent review where separation isn't possible.

## 🚦 Approval gates

- 📋 **List first:** write down the approvals that must stay human, such as release sign-off and protected-path edits.
- 🪝 **Enforce:** each becomes a hook or CI check that allows, asks or blocks.
- 💬 **Explain:** a block states its reason and the route to approval.
- 🏢 **If settings are managed:** keep mandatory gates there, where no one can switch them off.

## 🔑 Credentials and autonomy

Use short-lived credentials scoped to the job, in a sandbox, with no production access by default.

| Environment | Claude may |
|---|---|
| 🛠️ Development | Deploy freely, within the user's permissions |
| 🧪 Staging | Deploy only as far as the team has agreed |
| 🏭 Production | Prepare the release, which a named person authorises |

- 🪜 **In pipelines:** start with read-only jobs, such as failure triage, then add writes that arrive as PRs.
- 🧰 **If deployment tools are exposed to Claude:** allowlist deploy, status and rollback per environment.
- 🪪 **Identity:** run unattended jobs under the agent's own identity, so logs separate its actions.

## ↩️ Rollback

- 🔘 **One command:** name it before release, and confirm what it restores.
- 🏋️ **Rehearse:** exercise it regularly in staging, before any automation depends on it.
- 🛑 **Authority:** run it in production only through a pre-approved runbook or a person's approval.

## ⚖️ Governance

- 🗃️ **Evidence:** the PR holds findings, fixes and approvals, and hook logs hold gate decisions.
- 🚧 **Boundary:** agent changes reach `main` only through a PR, and production only past the gate.

## 📏 Measures

- ⏱️ **Early signs:** time to first review, wait at each gate, and pipeline failures triaged without paging a person.
- 📉 **Later results:** defects caught before merge against those escaping, gate breaches, and DORA's delivery measures.

## 📞 Called by

This rule is invoked by [`rules/on_demand/01_standards/ai_sdlc_stages.md`](../ai_sdlc_stages.md), when reviewing a change, setting an approval gate, or releasing or rolling back.
