# 📊 DORA: AI Capabilities Model

**Purpose:** what the AI Capabilities Model from DORA (DevOps Research and Assessment) found, where its limits are, and how far it applies to this repo's design.

## 📋 Executive Summary

- 📊 **What it is:** DORA's 2025 research, drawing on nearly 5,000 technology professionals, naming seven capabilities that shape how much teams gain from AI (p. 3).
- 🔊 **Core idea:** "AI's primary role in software development is to amplify", magnifying an organisation's strengths and dysfunctions alike (p. 3).
- ⚠️ **Caution:** the evidence comes from surveys and shows correlation, so treat each finding as a hypothesis to test.
- 🎯 **Direct fit:** curated internal context, strong version control, and small, frequent changes apply directly to a personal setup.
- 🏢 **Organisational:** the other capabilities depend mainly on an organisation, so they apply here only indirectly or not at all.

## 🔗 Source

The report and how to cite it:

- 📄 **Report:** [*DORA AI Capabilities Model*](https://dora.dev/ai/capabilities-model/report/), v. 2025.1, Google LLC, with citations retrieved October 2025 (p. 1).
- ⚖️ **Licence:** CC BY-NC-SA 4.0, so it can be quoted with attribution for non-commercial use.
- 🗓️ **Captured:** 2026-11-02, after reading in full the PDF the report page links to.
- 🔢 **Page numbers:** "p." means the report's printed page number, which is one less than the PDF page.
- 🔎 **Reviewed:** 2026-11-11, with each quote, figure and page number checked against the PDF.
- 🧪 **Methods:** the report defers to [*State of AI-assisted Software Development 2025*](https://dora.dev/research/2025/dora-report/) for how it was run (p. 94).

## 📋 Overview

The evidence behind DORA's AI Capabilities Model, its central claim, and how the report means it to be used.

### 🔑 Key points

The report rests on these points:

- 👥 **Evidence base:** survey responses from nearly 5,000 technology professionals, plus over 100 hours of qualitative data (p. 3).
- 🔊 **Central claim:** "AI's primary role in software development is to amplify. It magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones" (p. 3).
- 📈 **Adoption:** 90% of respondents use AI as part of their work (p. 7).
- 🧩 **Model:** seven capabilities that change how strongly AI adoption is linked to outcomes (p. 7).
  - **Alongside:** they add to the DORA Core Model, DORA's long-standing model of what drives delivery performance, rather than replacing it (p. 7).
- 🧪 **Intended use:** "form hypotheses, run experiments, and measure the results" in your own context (p. 5).

## 🧩 The seven capabilities

What each of DORA's seven capabilities means, what it strengthens, and where the report covers it. Each capability changes how much a team gains from AI:

| Capability | What it means, paraphrased | Strengthens AI's effect on | Pages |
|---|---|---|---|
| 📣 Clear and communicated AI stance | An official position on AI use that everyone knows and understands | Individual effectiveness, organisational performance and throughput, and it reduces friction | 14–19 |
| 🗄️ Healthy data ecosystems | High-quality, easily accessible, unified internal data | Organisational performance | 20–25 |
| 🔌 AI-accessible internal data | AI securely connected to internal code and docs, which the report calls context engineering | Individual effectiveness and code quality | 26–35 |
| 🌿 Strong version control practices | Everything versioned, with small frequent commits and confident rollback | Individual effectiveness, from frequent commits, and team performance, from rollback | 36–43 |
| 📦 Working in small batches | Work split into the smallest chunks that can be delivered on their own | Product performance, and it reduces friction, though it slightly lowers individual effectiveness | 44–51 |
| 👤 User-centric focus | Team priorities set by what users need | Team performance, which falls when user focus is low | 52–57 |
| 🏗️ Quality internal platforms | Shared tools, services and docs, run as an internal product | Organisational performance, but only when the platform is good | 58–65 |

## 🔎 Findings worth carrying forward

Specific findings from DORA's report that are worth using in this repo's design. This section uses these terms:

- 🥇 **Gold-standard code:** the repositories and branches that best show current conventions.

### 📦 Small batches and version control

The report recommends these habits:

- 📏 **Batch size:** "Any batch of code that takes longer than a week to complete is too big", with a daily commit to trunk (p. 48).
- ⚖️ **Trade-off:** small batches slightly reduce how effective people feel, which the report judges worth it for product performance (pp. 46–48).
- 🤖 **Agent files:** keep files such as `CLAUDE.md` and AI prompts in version control, as about 21% of respondents do for prompts (pp. 39–40).
- ✍️ **Commit messages:** explain why, for example with Conventional Commits (p. 40).

### 🤖 AI context

These findings cover what to give AI:

- 🧠 **Curate it:** give AI relevant context rather than volume, since irrelevant context degrades its answers (pp. 32–33).
  - **Code:** index only gold-standard code (p. 32).
  - **Size:** "a 20-page standards document is often too much for a model" to attend to while solving a task (p. 32).
- 📚 **Distil it:** have AI summarise a key source, then have a human expert check the summary (p. 32).

### 🏢 Stance, users and planning

These findings sit beyond the code itself:

- 🚦 **AI stance:** sort uses into prohibited, permitted with guardrails, and allowed (p. 18).
- 📝 **Spec-driven development:** writing requirements before code, named as an emerging way to keep AI-written code aligned with users (p. 55).
- 🗺️ **Value stream mapping:** drawing every step from idea to production to find where work waits, which strengthens AI's effect on organisational performance (p. 74).
- 🔐 **Tool access:** connect AI to internal data through a "least privilege" model, using only vetted tools (p. 33).
- ✍️ **Agent commits:** decide whether AI may commit changes directly, and commit each change as a distinct, atomic unit (pp. 38–40).
- 🎯 **Prioritisation:** the report's guide to choosing what to improve first weighs what a team can change by itself (p. 90), which in a one-person repo is almost everything.

## ⚠️ Limitations

What DORA's evidence can and can't show.

### 📏 Strength of the evidence

These limits come from how the data was gathered. The first two bullets and "Not stages" are this repo's reading, not the report's own words:

- 🔗 **Correlation, not cause:** the report's single survey can show that a capability goes with better results, but not that it causes them.
  - **Estimates:** effects are shown with 89% credible intervals, the range the true effect most likely falls in (p. 10).
- 📢 **Strong wording:** the report calls the capabilities "proven to amplify" (p. 4), which goes further than such a survey can show.
- 🙋 **Self-report:** outcomes such as individual effectiveness and code quality are respondents' own judgements (p. 9).
- 🌱 **First version:** DORA calls this its first such model, and says it will keep validating and revising it (p. 7).
- 📉 **Weak at low levels:** at low levels of a capability, the report finds AI's added effect "Unsubstantiated" (p. 16 onwards).
- 🌪️ **Instability:** AI-assisted coding is also "associated with increased software delivery instability" (p. 38).

### 🧭 Scope and source

These limits affect how far the findings transfer here:

- 🪜 **Not stages:** the seven capabilities sit side by side, rather than forming a ladder to climb in order.
- 👥 **Teams and organisations:** respondents rate their own work as well as their team's and organisation's, but most capabilities describe a team or organisation, so they don't transfer directly to one person's setup (p. 9).
- 🏢 **Publisher:** Google Cloud runs DORA, and some examples use its own tools, though it names "GEMINI.md or CLAUDE.md" side by side (p. 40).

## 🎯 Applicability to this playbook

How far each of DORA's capabilities applies to this repo's personal Claude setup, as decided at the maintainer's review. The table uses these terms:

- 🗄️ **DataOps:** applying software delivery practices to data pipelines.
- 🛤️ **Golden path:** a ready-made, supported way to do a common task.

| Capability | Applies here | Why |
|---|---|---|
| 📣 Clear and communicated AI stance | Indirect | `security.md` sets this config's guarded uses, but workplace policy belongs to the employer |
| 🗄️ Healthy data ecosystems | Out of scope (organisational) | Data quality sits with the organisation, though DataOps work touches it |
| 🔌 AI-accessible internal data | Direct | `CLAUDE.md` and rules are context engineering at personal scale, curated by the always-on budget and on-demand rules |
| 🌿 Strong version control practices | Direct | Config and prompts are versioned here, with commit messages checked by a hook, though plans sit outside git in the Claude config directory |
| 📦 Working in small batches | Direct | The PR size limit in the [contributing guidelines](../../../../.github/CONTRIBUTING.md), and splitting plans into small PRs, already support it |
| 👤 User-centric focus | Indirect | The maintainer is the main user, and each plan's Intent and Spec sections write requirements first |
| 🏗️ Quality internal platforms | Indirect | This repo acts as a small golden path, but an organisation's platform is out of reach |
