<!-- version: 1.1.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# 🎯 DORA report: Applicability to this playbook

**Purpose:** how far each of DORA's capabilities applies to this repo's personal Claude setup, as a proposal not yet adopted.

This page is part of the [summary of DORA's AI Capabilities Model](../dora_ai_capabilities.md). The table uses these terms:

- 🗄️ **DataOps:** applying software delivery practices to data pipelines.
- 🛤️ **Golden path:** a ready-made, supported way to do a common task.
- 📦 **Data products:** datasets or pipelines built and maintained for others to use.

| Capability | Applies here | Why |
|---|---|---|
| 📣 Clear and communicated AI stance | Indirect | This repo can state its own banned, guarded and allowed uses, but workplace policy belongs to the employer |
| 🗄️ Healthy data ecosystems | Out of scope (organisational) | Data quality sits with the organisation, though DataOps work touches it |
| 🔌 AI-accessible internal data | Direct | `CLAUDE.md`, rules and curated context are context engineering at personal scale |
| 🌿 Strong version control practices | Direct | Versioned config, small commits, and storing prompts and plans are all in reach |
| 📦 Working in small batches | Direct | The PR size limit in the [contributing guidelines](../../../../.github/CONTRIBUTING.md), and splitting plans into small PRs, already support it |
| 👤 User-centric focus | Indirect | The users are the maintainer and the people who use the maintainer's data products, and writing requirements first helps |
| 🏗️ Quality internal platforms | Indirect | This repo acts as a small golden path, but an organisation's platform is out of reach |
