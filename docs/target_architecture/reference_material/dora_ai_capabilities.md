<!-- version: 1.1.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 📊 DORA: AI Capabilities Model

For anyone shaping the target architecture: what DORA's (DevOps Research and Assessment) AI Capabilities Model found and measured, where its limits are, and how far each capability applies to a personal playbook.

- **Source:** *DORA AI Capabilities Model*, v. 2025.1, Google LLC, licensed CC BY-NC-SA 4.0, with citations retrieved October 2025 (p. 1).
- **Read:** in full on 2026-11-02, from a local copy of the PDF.
- **Page numbers:** "p." means the report's printed page number, which is one less than the PDF page.
- **Methodology:** this report defers to the *State of AI-assisted Software Development 2025* report for its methods and models (p. 94).
- **Moderates:** DORA's term for a capability that changes how strongly AI adoption is linked to an outcome.
- **Labels:** "The report says" and "Limitations" report the source, while "Applicability" is this playbook's interpretation.

## 📋 The report says: overview

- **Evidence base:** survey responses from nearly 5,000 technology professionals plus more than 100 hours of qualitative data (p. 3).
- **Central claim:** "AI's primary role in software development is to amplify. It magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones" (p. 3).
- **Adoption:** 90% of survey respondents use AI as part of their work (p. 7).
- **Model:** seven capabilities that moderate how AI adoption affects outcomes, complementing rather than replacing the DORA Core Model (p. 7).
- **Intended use:** "form hypotheses, run experiments, and measure the results" in your own context (p. 5).

## 🧩 The report says: the seven capabilities

| Capability | DORA's definition, paraphrased | Amplifies AI's effect on | Pages |
|---|---|---|---|
| Clear and communicated AI stance | An official position on AI use that is comprehensible and widely known, covering expectation, support, permission and applicability | Individual effectiveness, organisational performance and throughput, and it reduces friction | 14–19 |
| Healthy data ecosystems | Internal data that is high-quality, easily accessible and unified | Organisational performance | 20–25 |
| AI-accessible internal data | AI securely connected to internal code, docs and current external docs, which the report calls context engineering | Individual effectiveness and code quality | 26–35 |
| Strong version control practices | Everything in version control, frequent small commits and confident use of rollback | Individual effectiveness (commit frequency) and team performance (rollback) | 36–43 |
| Working in small batches | Work split into the smallest chunks that can be completed and delivered independently | Product performance, and it reduces friction | 44–51 |
| User-centric focus | Team priorities aligned to what users need | Team performance, which falls when user focus is low | 52–57 |
| Quality internal platforms | Shared tools, services, docs and golden paths (ready-made, supported ways to do common tasks), run as an internal product | Organisational performance, with negligible effect when platform quality is low | 58–65 |

## 🔎 The report says: findings worth carrying forward

- **Batch size:** "Any batch of code that takes longer than a week to complete is too big", with a daily commit to trunk (p. 48).
- **Small-batch trade-off:** small batches slightly reduce perceived individual effectiveness, which the report argues is worth it for product performance and less friction (pp. 46–48).
- **Agent configuration:** store agent files such as `CLAUDE.md` and AI prompts in version control, which about 21% of respondents already do for prompts (pp. 39–40).
- **Commit messages:** explain the why, for example with Conventional Commits (p. 40).
- **Context rot:** give AI relevant, curated context rather than volume, and index only gold-standard code (pp. 32–33).
- **Distilled sources:** have AI summarise a key source, then a human expert validates it (p. 32).
- **AI stance:** sort uses into prohibited, permitted with guardrails, and allowed (p. 18).
- **Spec-driven development:** named as an emerging way to keep AI-generated code aligned with user needs (p. 55).
- **Value stream mapping:** it also amplifies AI's effect on organisational performance (p. 74).
- **Assessment:** seven team archetypes from a cluster analysis (pp. 67–70), a 90-minute prioritisation workshop (pp. 82–87) and a rubric that includes locus of control, meaning what a team can change by itself (p. 90).

## ⚠️ Limitations

- **Correlation, not cause:** the effects are survey-based estimates of how each capability moderates AI's effect, shown with 89% credible intervals, the range the true effect most likely falls in (p. 10).
- **Strong wording:** the report calls the capabilities "proven to amplify" (p. 4), which goes further than a cross-sectional survey can show.
- **Not stages:** the seven are parallel capabilities, not a maturity ladder.
- **Unit of analysis:** respondents describe their teams and organisations, so findings don't transfer directly to one person's configuration.
- **Self-report:** outcomes such as individual effectiveness and code quality are respondents' own assessments.
- **Publisher:** Google Cloud runs DORA, and some examples use its own tools, such as `GEMINI.md`.

## 🎯 Applicability to this playbook (proposed, not yet adopted)

| Capability | Applicability | Why |
|---|---|---|
| Clear and communicated AI stance | Indirect | The playbook can state its own allowed, guarded and prohibited uses, but workplace policy belongs to the employer |
| Healthy data ecosystems | Out of scope (organisational) | Data quality and unification sit with the organisation, though DataOps work touches it |
| AI-accessible internal data | Direct | `CLAUDE.md`, rules and curated context are context engineering at personal scale |
| Strong version control practices | Direct | Versioned config, small commits, and storing prompts and plans are all in reach |
| Working in small batches | Direct | The 20-file PR limit and plan slicing already support it |
| User-centric focus | Indirect | The users are the maintainer and consumers of their data products, and spec-first work helps |
| Quality internal platforms | Indirect | The playbook acts as a small golden path, but an organisation's platform is out of reach |
