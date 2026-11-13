# ⚠️ AI-native SDLC course: Caveats

**Purpose:** the limits of Anthropic's SDLC course: who it's for, how strong its evidence is, and what it assumes.

This page is part of the [summary of Anthropic's SDLC course](../anthropic_ai_native_sdlc.md). These points are this repo's assessment, not the course's own words.

## ⚠️ Limits

These limits matter here:

- 👥 **Audience:** the course names none, but it writes for a platform team and closes on the governance needs of large enterprises ([Closing thoughts](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-thoughts-and-resources)).
- 📏 **Evidence:** the measures it suggests are untested proposals.
  - **Its figures:** expectations, not results, such as capturing intent shrinking "a multi-week elicitation and refinement cycle to hours" ([Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent)).
- 🏢 **Vendor source:** Anthropic publishes both the course and the tools it recommends.
  - **Basis:** it calls the course the practice of Anthropic's Applied AI team, without saying how that was gathered ([Closing thoughts](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-thoughts-and-resources)).
- 🔐 **Organisation features:** several plays work best with features an organisation runs.
  - **Examples:** managed settings for hooks no one may switch off, a managed code review service, which `claude-code-action` in your own CI can replace, and an OpenTelemetry usage export for some measures.
