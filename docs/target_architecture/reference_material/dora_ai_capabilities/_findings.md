<!-- version: 1.0.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🔎 DORA report: Findings worth carrying forward

For anyone shaping the target architecture: specific findings worth carrying into the target architecture.

- **Part of:** [DORA: AI Capabilities Model](../dora_ai_capabilities.md).
- **Page numbers:** "p." is the report's printed page number, one less than the PDF page.
- **Trunk:** the main branch that everyone merges into.
- **Context rot:** AI answers getting worse when its context is overloaded with irrelevant material.
- **Gold-standard code:** the repositories and branches that best show current conventions.
- **Value stream mapping:** drawing every step from idea to production to find where work waits.

- **Batch size:** "Any batch of code that takes longer than a week to complete is too big", with a daily commit to trunk (p. 48).
- **Small-batch trade-off:** small batches slightly reduce perceived individual effectiveness, which the report argues is worth it for product performance and less friction (pp. 46–48).
- **Agent configuration:** store agent files such as `CLAUDE.md` and AI prompts in version control, which about 21% of respondents already do for prompts (pp. 39–40).
- **Commit messages:** explain the why, for example with Conventional Commits (p. 40).
- **Context rot:** give AI relevant, curated context rather than volume, and index only gold-standard code (pp. 32–33).
- **Distilled sources:** have AI summarise a key source, then a human expert validates it (p. 32).
- **AI stance:** sort uses into prohibited, permitted with guardrails, and allowed (p. 18).
- **Spec-driven development:** named as an emerging way to keep AI-generated code aligned with user needs (p. 55).
- **Value stream mapping:** it also amplifies AI's effect on organisational performance (p. 74).
- **Prioritisation:** the rubric includes locus of control, meaning what a team can change by itself (p. 90).
