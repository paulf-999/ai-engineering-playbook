# 🧭 Anthropic: The AI-native SDLC Playbook

**Purpose:** what Anthropic's course on the AI-native software development lifecycle (SDLC) recommends, where its limits are, and which parts fit this repo.

## 📋 Executive Summary

- 🧭 **What it is:** a course of short recommended practices, which it calls plays, for using Claude Code from planning to maintenance.
- 💡 **Core idea:** each stage leaves a versioned file for the next, from `intent.md` to `spec.md` to `plan.md`, and people stay accountable for judgement calls.
- 🎛️ **Controls:** skills are advisory, while hooks and required CI checks enforce what must hold.
- 📏 **Evidence:** every play suggests an early and a later measure of success, but the course reports no measured results.
- 🎯 **For this repo:** the relevance section below records which plays to adopt, adapt, defer or leave out.

## 🔗 Source

- 📚 **Course:** [The AI-native SDLC playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook), from Anthropic's Claude Academy, about an hour of reading.
- 📅 **Version:** the course gives no date or version, so cite the lesson and the 2026-11-02 access date.
- 🗓️ **Captured:** 2026-11-02, after reading every lesson in full.
- 📚 **Further reading:** the [closing lesson](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-thoughts-and-resources) lists the Claude Code documentation a platform team needs to set up these controls.
- 🔎 **Reviewed:** 2026-11-11, with each quote, figure and measure checked against its lesson.

## 📋 Overview

How Anthropic's SDLC course is structured, and where it suggests starting. The course is built from plays: short recommended practices, each with prerequisites, steps and two measures of success.

### 🔑 Key points

The course's structure comes down to these points:

- 🧩 **Stages:** the plays are grouped by stage: plan, design, build, test, deploy and maintain.
- 📈 **Measures:** each play names a leading indicator, an early sign it's working, and a lagging indicator, a later measure of its outcome.
- 🧵 **Thread:** read across the lessons, each stage commits a file the next one uses, from `intent.md` to `spec.md` to `plan.md`. This is the repo's synthesis, since no lesson states it.
- 🙋 **Accountability:** "Humans remain accountable for every decision that requires judgment" ([Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction)).
- 🚦 **Where to start:** with the six plays that have no prerequisites: capturing intent, plan mode, `CLAUDE.md`, skills, the feedback loop and hooks as approval gates ([Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction)).
  - **Later plays:** the rest build on these, as the introduction's dependency graph shows. Subagents need `CLAUDE.md`, evals need `CLAUDE.md` and the feedback loop, PR review needs evals and subagents, CI/CD needs PR review and hooks, and closing the loop on metrics needs CI/CD and captured intent ([Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction)).
  - **Plan mode:** Claude proposes a plan before changing anything.

## 🔄 Plays by stage

Each of the course's plays, grouped by stage, with its core practice and how to tell it's working. Each play pairs an early signal that it's working with a later result to measure:

| Stage | Play | Core practice | Early signal | Later result |
|---|---|---|---|---|
| 📝 Plan | [Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent) | Claude interviews the requester and drafts `intent.md`, which the product owner corrects | Time to a committed `intent.md` | Share of intent files accepted into design |
| 📐 Design | [Requirements and design](https://academy.claude.com/courses/ai-native-sdlc-playbook/requirements-and-design) | Claude drafts `spec.md` from the approved intent, and a person decides whether to proceed | Time from intent to spec | Spec edits after the first `plan.md` |
| 🗺️ Build | [Plan mode as the default](https://academy.claude.com/courses/ai-native-sdlc-playbook/plan-mode) | Refine the plan until a stranger could build from it, then commit it as `plan.md` | Changes merged from the first pass | Rework per change, and how often the merged diff still matches `plan.md` |
| 📘 Build | [The CLAUDE.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/claude-md) | Keep it under a page, and add a correction "when Claude makes a mistake twice" | How often a mistake repeats | Time to a new joiner's first merged PR |
| 🧠 Build | [Skills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge) | Write a skill for knowledge that must be applied consistently, and back must-hold policies with a hook or PR check | Time from a policy's approval to its skill update | PR findings that cite the policy |
| 🔀 Build | [Parallel sessions and subagents](https://academy.claude.com/courses/ai-native-sdlc-playbook/parallel-sessions-and-subagents) | One separate checkout per task, adding sessions "only while review is keeping up" | Sessions per engineer while review quality holds | Changes merged per engineer per week, read with the rework rate |
| 🔁 Test | [Give Claude a feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop) | One command that fails loudly, and a failing test before each bug fix | First-pass CI success for agent-written changes | Review time and change failure rate |
| 🧪 Test | [Continuous evals in CI](https://academy.claude.com/courses/ai-native-sdlc-playbook/continuous-evals-in-ci) | Rerun 20 to 50 real tasks, called evals, on a schedule and whenever `CLAUDE.md`, skills or hooks change | Eval pass rate, and time for an incident to become an eval | Regressions caught in CI rather than in production |
| 👀 Deploy | [AI in the PR review loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop) | Automated review applies a `REVIEW.md` checklist, but can't approve its own code | Time to first review | Defects caught before merge |
| 🚧 Deploy | [Hooks as approval gates](https://academy.claude.com/courses/ai-native-sdlc-playbook/hooks-as-approval-gates) | Each required approval becomes a hook that allows, asks or blocks an action | Time spent waiting at gates | Gate breaches reaching production |
| 🚀 Deploy | [CI/CD integration and deployment](https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment) | Run Claude unattended and sandboxed, starting with read-only steps and adding write steps behind the existing gates, while a person authorises each release | Pipeline failures triaged without paging a person | DORA measures |
| 📉 Maintain | [Closing the loop on metrics](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-the-loop-on-metrics) | Tested code flags unusual readings, then Claude diagnoses them and, for the largest, may open a PR | Time from a flagged reading to an `intent.md` in the triage queue | Repeat incidents, and findings that become merged fixes |

## ⚠️ Caveats

The limits of Anthropic's SDLC course: who it's for, how strong its evidence is, and what it assumes. These points are this repo's assessment, not the course's own words.

### ⚠️ Limits

These limits matter here:

- 👥 **Audience:** the course names none, but it writes for a platform team and closes on the governance needs of large enterprises ([Closing thoughts](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-thoughts-and-resources)).
- 📏 **Evidence:** the measures it suggests are untested proposals.
  - **Its figures:** expectations, not results, such as capturing intent shrinking "a multi-week elicitation and refinement cycle to hours" ([Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent)).
- 🏢 **Vendor source:** Anthropic publishes both the course and the tools it recommends.
  - **Basis:** it calls the course the practice of Anthropic's Applied AI team, without saying how that was gathered ([Closing thoughts](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-thoughts-and-resources)).
- 🔐 **Organisation features:** several plays work best with features an organisation runs.
  - **Examples:** managed settings for hooks no one may switch off, a managed code review service, which `claude-code-action` in your own CI can replace, and an OpenTelemetry usage export for some measures.

## 🔍 Our reading

What Anthropic's SDLC course means for the design of this repo's Claude configuration. This section gives this repo's view rather than the course's.

### 🔑 Key points

These ideas carry over:

- 🦴 **Core sequence:** specify, plan, then check the work against versioned files, which needs none of the admin-run features that some plays assume.
- ⚖️ **Advice versus enforcement:** the course calls skills advisory, and this repo treats `CLAUDE.md` the same way, while hooks and required CI checks enforce.
  - **Use here:** the [review of the old configuration](../../legacy_architecture.md#-where-complexity-outran-evidence) applies this split to its safeguards.
- 📏 **Measurement:** each play's early signal and later result are ready candidates for checking whether a change helped.
  - **Use here:** the [target architecture's workflow](../../README.md#-workflow) names the signal each regular review reads for every play it adopts.

## 🎯 Relevance to this playbook

Which of the course's plays suit this repo, as decided at the maintainer's review, with the ones it has adopted recorded in the [target architecture's workflow](../../README.md#-workflow). Each row adopts a play as it is, adapts it, defers it or leaves it out:

| Play | Decision | Why |
|---|---|---|
| 📝 Capture intent, requirements and design | Adapt | Intent and Spec sections at the top of each plan, saved as `intent.md` and `spec.md` once it is approved, suit a single maintainer, who also acts as product owner |
| 🗺️ Plan mode and `plan.md` | Adapt | Plans stay in the Claude config directory, since this repo's config is installed there rather than worked on in each repo |
| 📘 `CLAUDE.md` | Adapt | The always-on token budget replaces the one-page limit, and a fix still goes in once Claude repeats a mistake |
| 🧠 Skills | Adopt | Only for knowledge that must be applied consistently, backed by a hook or CI check, as the course advises, though none ship yet |
| 🔀 Parallel sessions and subagents | Adapt | Separate checkouts fit, but one reviewer limits how many sessions help |
| 🔁 Feedback loop | Adopt | `make test` and `pre-commit run --all-files` already give one command each |
| 🧪 Continuous evals | Deferred | A small set of repeatable test tasks is feasible, once API cost and upkeep are weighed |
| 👀 PR review loop | Adapt | A fresh-context reviewer agent fills each config PR's evaluation criteria in place of a `REVIEW.md`, though a solo maintainer can't separate author and approver |
| 🚧 Hooks as approval gates | Adapt | User-level hooks that `make install` registers and keeps in step, such as the plan sections hook, since a personal setup has no managed settings |
| 🚀 CI/CD integration, closing the loop on metrics | Out of scope for now | Both need a deployed service, which this repo doesn't have |
