<!-- version: 1.0.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🎯 DORA report: Applicability to this playbook (proposed, not yet adopted)

For anyone shaping the target architecture: how far each capability applies to a personal playbook, as a proposal.

- **Part of:** [DORA: AI Capabilities Model](../dora_ai_capabilities.md).
- 🔬 **DORA:** DevOps Research and Assessment, a Google Cloud research programme on software delivery performance.
- 🗄️ **DataOps:** applying software delivery practices to data pipelines.
- 🛤️ **Golden path:** a ready-made, supported way to do a common task.
- 📦 **Data products:** datasets or pipelines built and maintained for others to use.

| Capability | Applicability | Why |
|---|---|---|
| 📣 Clear and communicated AI stance | Indirect | The playbook can state its own allowed, guarded and prohibited uses, but workplace policy belongs to the employer |
| 🗄️ Healthy data ecosystems | Out of scope (organisational) | Data quality and unification sit with the organisation, though DataOps work touches it |
| 🔌 AI-accessible internal data | Direct | `CLAUDE.md`, rules and curated context are context engineering at personal scale |
| 🌿 Strong version control practices | Direct | Versioned config, small commits, and storing prompts and plans are all in reach |
| 📦 Working in small batches | Direct | The repo's PR size limit in [`CONTRIBUTING.md`](../../../../.github/CONTRIBUTING.md) and plan slicing already support it |
| 👤 User-centric focus | Indirect | The users are the maintainer and consumers of their data products, and spec-first work helps |
| 🏗️ Quality internal platforms | Indirect | The playbook acts as a small golden path, but an organisation's platform is out of reach |
