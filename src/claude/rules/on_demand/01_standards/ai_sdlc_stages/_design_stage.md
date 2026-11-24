# 📐 Design stage

**Purpose:** how to turn an accepted intent into a spec that an engineer can plan against, applying policy while drafting rather than in a late review.

## 🪜 Steps

1. Read the accepted intent, the codebase it touches, and every rule, skill and policy that applies.
2. Draft the Spec section, as [Plan layout](../../../always_on/01_standards/ai_sdlc_workflow.md#️-plan-layout) sets out, with each policy as a constraint.
3. List the concerns first, such as policies that can't both be met, then the rest of the spec.
4. Answer each open question from the intent, or carry it forward with its owner.
5. Check the spec solves the stated problem and adds nothing the intent didn't ask for.
6. Stop for approval before building.

## 🚩 Flagging concerns

Flag a concern rather than choose silently:

| Concern | Flag it with |
|---|---|
| ⚔️ Two policies conflict | Both requirements, why they clash, and the options |
| 🕳️ A policy is missing or unclear | What it should decide, and who owns it |
| 🚧 A policy can't be met | The gap, the risk and a possible workaround |
| 🔐 Security or personal data | The data and route exposed, as the [security rule](../../../always_on/01_standards/security.md) sets out |

- 👤 **Route:** name each concern's policy owner, so the product owner can settle it before engineering sees the spec.

## ❓ Open questions

- ✅ **Answered:** record the answer and the reason beside it.
- ➡️ **Carried forward:** say why it can wait, who decides and by when.

## 🖼️ Mock-ups

- 🎨 **Front-end work:** mock up the screen from the accepted intent, iterate with the product owner, then build from the agreed version.
- 🔗 **Link it:** name the agreed mock-up in the spec, so the [Test stage](_test_stage.md#-screenshot-loop) can compare against it.
- 🧰 **If a design tool is available:** export its mock-up to the build session.

## 🧾 Example prompt

```text
Read the accepted intent and draft the spec for our codebase.
Apply every policy available to you.
List concerns first, above all policies that contradict each other.
Answer the intent's open questions, or carry them forward with an owner.
```

## ⚖️ Governance

- ✍️ **Approval:** a person decides whether the spec moves to build, and consults a technical lead on higher-risk work.
- 🗃️ **Evidence:** keep the spec beside its intent, so one shows what was asked for and the other what was decided.
- 🔖 **If policies are versioned:** record the prompt and the skill versions the spec was drafted under.

## 📏 Measures

- ⏱️ **Early sign:** time from a saved intent to a saved spec.
- 🔁 **Later result:** spec edits made after the first `plan.md`, which show requirements rework.

## 📞 Called by

This rule is invoked by [`rules/on_demand/01_standards/ai_sdlc_stages.md`](../ai_sdlc_stages.md), when turning an intent into a spec or mock-up.
