# 🎯 DORA report: Applicability to this playbook

**Purpose:** how far each of DORA's capabilities applies to this repo's personal Claude setup, as decided at the maintainer's review.

This page is part of the [summary of DORA's AI Capabilities Model](../dora_ai_capabilities.md). The table uses these terms:

- 🗄️ **DataOps:** applying software delivery practices to data pipelines.
- 🛤️ **Golden path:** a ready-made, supported way to do a common task.

| Capability | Applies here | Why |
|---|---|---|
| 📣 Clear and communicated AI stance | Indirect | `security.md` sets this config's guarded uses, but workplace policy belongs to the employer |
| 🗄️ Healthy data ecosystems | Out of scope (organisational) | Data quality sits with the organisation, though DataOps work touches it |
| 🔌 AI-accessible internal data | Direct | `CLAUDE.md` and rules are context engineering at personal scale, curated by the always-on budget and on-demand rules |
| 🌿 Strong version control practices | Direct | Config and prompts are versioned here, with commit messages checked by a hook, though plans sit outside git in the Claude config directory |
| 📦 Working in small batches | Direct | The PR size limit in the [contributing guidelines](../../../../../.github/CONTRIBUTING.md), and splitting plans into small PRs, already support it |
| 👤 User-centric focus | Indirect | The maintainer is the main user, and each plan's Intent and Spec sections write requirements first |
| 🏗️ Quality internal platforms | Indirect | This repo acts as a small golden path, but an organisation's platform is out of reach |
