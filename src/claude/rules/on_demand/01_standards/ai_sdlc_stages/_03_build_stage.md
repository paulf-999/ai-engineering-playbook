# 🔨 Build stage

**Purpose:** how to plan an implementation, build it and keep the plan true, with guidance on the files and checks that steer Claude.

## 🗺️ Implementation plan

1. Work in plan mode, from the approved intent and spec.
2. Name the files that change, the order of work, the risks, and the proof each step worked.
3. Challenge it: what could break, which step is riskiest, and which options were rejected and why?
4. Refine it until a stranger to the conversation could build from the plan alone.
5. Get the plan approved before editing, then keep it outside every repo.

Place each of these in the sections that [Plan layout](../../../always_on/01_standards/ai_sdlc_workflow.md#️-plan-layout) allows, such as rejected options under **Why** in the Spec, rather than adding headings.

- 🔀 **Departures:** when work departs from the plan, update the saved plan in the same turn, and ask first if the choice is material.

## ✋ When to edit without per-edit prompts

The user chooses the permission mode. Suggest accepting edits automatically only when all of these hold:

- 📐 **Tight spec:** the approved plan leaves no material choice open.
- 💥 **Small blast radius:** a mistake is contained and easy to reverse.
- 🧪 **Covered code:** tests Claude can run already check the behaviour.
- 🛡️ **Guardrails:** hooks or permissions block the unsafe actions.

Review then moves from each edit to the finished artefacts.

## 📌 Source of truth

For each artefact, such as a requirement or design, name one authoritative system, and have the rest link to it:

| Choice | How it works |
|---|---|
| 🌿 Repo | Files are the record, and other tools link to them |
| 🎫 Existing tool, such as Jira | Read the record first, then write the outcome back once approved |
| 🔗 Linkage, the minimum | The file names the record ID, and the record names the file or commit |

## 🧠 Guidance and guardrails

- 📘 **`CLAUDE.md`:** hold what a new joiner needs, under a page, and propose a correction once Claude makes a mistake twice.
- 🧰 **Skills:** write one for knowledge that must be applied consistently, with a policy owner, and test several phrasings trigger it.
- 🪝 **Hooks:** back a policy that must always hold, such as protected paths or formatting, since a skill only advises.
- ⚡ **Hook speed:** keep them fast and scoped to the changed file, leaving full test runs to the commit or PR.
- 🚦 **Approval prompts:** keep these for [Deploy stage](_05_deploy_stage.md#-approval-gates) gates, so parallel sessions aren't held up.

Read the [guiding principles](../claude_config/guiding_principles.md) before changing any of these.

## 🔀 Parallel work

- 🧩 **Split:** run tasks in parallel only when they touch different files, and run the rest in order.
- 🌳 **Isolate:** give each session its own worktree, as [`git.md`](../git.md) sets out.
- 👀 **Limit:** start with two or three, and add sessions only while review keeps up.
- 🤖 **Subagents:** use one for a repeated, scoped job, such as research or a final check, with only the tools it needs.

## ⚖️ Governance

- ✍️ **Approval:** an engineer approves routine plans, and a technical lead or architect approves higher-risk ones.
- 🗃️ **Evidence:** keep the approved plan and its updates, then check the diff against the Spec.
- 📜 **Config changes:** review `CLAUDE.md`, skill and hook changes as code, with the policy owner's sign-off.

## 📏 Measures

- ⏱️ **Early signs:** changes merged from the first pass, repeated mistakes, and time for a policy change to reach its skill.
- 🔁 **Later results:** rework per change, whether the merged diff matches the plan, and time to a new joiner's first merged PR.
- 🔀 **Parallel work:** sessions per engineer while review quality holds, then changes merged per week beside rework.

## 📞 Called by

This rule is invoked by [`rules/on_demand/01_standards/ai_sdlc_stages.md`](../ai_sdlc_stages.md), when writing an implementation plan, building from one or running parallel sessions.
