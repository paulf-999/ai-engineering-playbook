<!-- version: 1.6.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# 📚 Reference Material

**Purpose:** the outside sources behind this repo's target architecture, the design for its new Claude configuration, and how to use and cite them.

## 📋 Source register

Each summarised or quoted source links to its page from the Source column, the Access column says which sources were read in full, and Captured gives the date each summary or quoted page was written, so an old date flags a summary to recheck.

| # | Source | Publisher | Version or date | Access | Captured | Used for |
|---|---|---|---|---|---|---|
| 1️⃣ | [The AI-native SDLC playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook) · [summary](anthropic_ai_native_sdlc.md) | Anthropic (Claude Academy) | Not stated, © 2026 | Public, sign-in optional, read in full | 2026-11-02 | Lifecycle and workflow guidance |
| 2️⃣ | [DORA AI Capabilities Model report](https://dora.dev/ai/capabilities-model/report/) · [summary](dora_ai_capabilities.md) | DORA (DevOps Research and Assessment), a Google Cloud programme | Report v. 2025.1, CC BY-NC-SA 4.0 | Full report from [Google Cloud](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report), read in full | 2026-11-02 | The seven capabilities and how to build them |
| 3️⃣ | [State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/) | Google Cloud, with IT Revolution, GitHub, GitLab, SkillBench and Workhelix | 2025, exact date not stated | Full report from [cloud.google.com/dora](https://cloud.google.com/dora), not yet read | No summary | Survey evidence on AI adoption and outcomes |
| 4️⃣ | [DORA AI Capabilities Model survey questions](https://dora.dev/ai/capabilities-model/questions/) | DORA, a Google Cloud programme | Page last updated 2025-11-25 | Public | No summary | How each capability and outcome was measured |
| 5️⃣ | [Handover review](handover_review.md), sections 4 and 6 | An outside reviewer of the [old Claude configuration](../current_architecture.md) | Not dated | Quoted in this repo | 2026-11-03 | The design's stance and priorities |
| 6️⃣ | [How Claude remembers your project](https://code.claude.com/docs/en/memory) · [summary](claude_code_memory_docs.md) | Anthropic (Claude Code docs) | Live docs, no version or date | Public, read in full | 2026-11-03 | What loading context into every session costs, and how imports and path-scoped rules load |
| 7️⃣ | [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) · [summary](bockeler_harness_engineering.md) | Birgitta Böckeler, on martinfowler.com | 2026-04-02 | Public, read in full | 2026-11-03 | When to guide Claude and when to enforce, from outside Anthropic |
| 8️⃣ | [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) · [summary](anthropic_agent_evals.md) | Anthropic (Engineering blog) | 2026-01-09 | Public, read in full | 2026-11-03 | Testing whether each part of this repo's configuration still helps |
| 9️⃣ | [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) · [summary](metr_developer_productivity_trial.md) | METR (Model Evaluation & Threat Research): Becker, Rush, Barnes and Rein, on arXiv | v2, 2025-07-25, CC BY 4.0 | Public, main text and key appendices read | 2026-11-03 | Trial evidence that felt speed-ups can hide real slowdowns |
| 🔟 | [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) · [summary](claude_code_best_practices.md) | Anthropic (Claude Code docs) | Live docs, no version or date | Public, read in full | 2026-11-03 | Anthropic's split between guidance Claude may follow and rules that always hold |

## 🧭 How to use these sources

Each source plays a different role, so weigh its claims by what kind of source it is.

### 🛠️ Guidance

These sources say what to do, but none shows that a practice works:

- 🎓 **Anthropic's SDLC course:** practical guidance for each stage of the software development lifecycle.
- 📘 **Claude Code docs:** how Claude Code behaves today, so recheck the live page before relying on an old summary.
- 🧰 **Böckeler's harness engineering:** a practitioner's view, from outside Anthropic, of the controls a user builds around a coding agent, useful as a check on vendor advice.
- 🧪 **Anthropic's evals article:** a method for testing agents, not evidence about this repo.
- 🧑‍💼 **Handover review:** one reviewer's judgement on the old configuration, which sets the design's direction rather than proving it works.

### 🔬 Evidence

These sources measure outcomes:

- 📊 **DORA:** a long-running research programme whose surveys show correlation rather than cause.
- ⚖️ **METR's trial:** a randomised controlled trial, so it shows cause rather than correlation, but on 16 developers in early 2025.

### 📝 Every source

- 🚫 **Not a specification:** this repo takes ideas from every source, but needn't implement any of them.
- 📝 **Citations:** record the page or section, and the version or access date, for every claim taken from a source.
