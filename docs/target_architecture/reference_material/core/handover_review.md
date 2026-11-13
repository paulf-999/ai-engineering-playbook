# 📝 Handover review

**Purpose:** two sections of an outside review of the maintainer's old Claude setup, written as a handover, which shaped this repo's design.

This page is part of the [reference material](../README.md). It quotes both sections word for word and adds nothing to them.

## ⚠️ Section 4: The biggest risk

> **4. The biggest risk: overengineering the AI experience**
>
> This is where I'd challenge your approach.
>
> You mentioned a colleague who uses almost no skills, one or two MCPs, no dedicated AI code review and relatively little prompting after the initial architecture and design.
>
> That approach could be just as successful as yours, or even more successful.
>
> The important distinction is:
>
> - Your approach: Encode engineering knowledge, standards and repeatable processes into a shared framework.
> - Their approach: Rely more heavily on initial design, the model's capabilities and post-build testing.
>
> Neither is inherently superior.
>
> Your framework is most valuable if it helps engineers achieve comparable or better outcomes with less total effort and less variation in quality.
>
> I'd be particularly careful about mandatory agent orchestration, excessive context loading and rules that duplicate existing CI/CD checks.
>
> The best configuration may be a small mandatory foundation, with specialised skills and agents activated only when relevant.

## 🎯 Section 6: What to prioritise next

> **6. What I would prioritise next**
>
> Rather than expanding the number of skills or agents, I'd prioritise three improvements.
>
> 1. Define a minimal baseline. Identify which rules and controls are genuinely necessary for every engineer, and which should be optional or task-specific.
> 2. Introduce evaluation and observability. Establish whether the framework improves accepted delivery time, quality and human effort. Measure the overhead introduced by the framework itself.
> 3. Establish a feedback loop. When engineers find a skill ineffective, a rule overly restrictive or a workflow redundant, make it easy to improve or retire it.

## 🔗 Where it's used

The two sections shaped these pages:

- 🧭 **Stance:** the [design principles](../../design_principles.md) take their small required core, and their warnings, from section 4.
- 📏 **Priorities:** the [target architecture](../../target_architecture.md) follows section 6, with its tiers, measures and regular reviews.
