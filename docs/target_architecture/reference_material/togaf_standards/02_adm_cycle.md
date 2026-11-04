<!-- version: 1.0.0 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-04 -->
# 🔁 TOGAF: The ADM cycle

**Purpose:** what each phase of the Architecture Development Method (ADM) is for, what it needs and what it produces.

This page is part of the [summary of the TOGAF Standard](../togaf_standards.md), and its terms are defined on the [core concepts page](01_core_concepts.md).

## 🔑 Key points

The ADM works in these ways:

- 🔁 **A cycle:** each pass through the phases refines the last.
- 🎯 **Baseline to target:** each architecture phase describes the current state, the target and the gaps between them.
- 📋 **Requirements at the centre:** Requirements Management feeds every phase and takes changes from each.

## 🧭 The phases

| Phase | Purpose | Key inputs | Key outputs |
|---|---|---|---|
| 🛠️ **Preliminary** | Set up the organisation's ability to do architecture work. | The organisation's goals, existing frameworks and principles | Tailored framework, architecture principles, team and governance set-up |
| 🔭 **A. Architecture Vision** | Agree scope, stakeholders and a high-level view of the target. | Request for Architecture Work | Architecture Vision, and an approved Statement of Architecture Work |
| 💼 **B. Business Architecture** | Describe the baseline and target business, and the gaps. | Architecture Vision, principles | Draft Architecture Definition Document and Architecture Requirements Specification |
| 🗄️ **C. Information Systems Architectures** | Do the same for data and applications. | Business Architecture | Updated phase B outputs |
| ⚙️ **D. Technology Architecture** | Do the same for the technology that supports them. | Information Systems Architectures | Updated phase B outputs |
| 🧩 **E. Opportunities and Solutions** | Group the gaps into work packages and decide how to deliver them. | Gaps from phases B to D | Architecture Roadmap, Transition Architectures, draft migration plan |
| 🗺️ **F. Migration Planning** | Order and cost the work packages into a final plan. | Roadmap and draft migration plan | Final Implementation and Migration Plan |
| 🏛️ **G. Implementation Governance** | Make sure delivery projects build what the architecture says. | Implementation and Migration Plan | Architecture Contracts, compliance assessments |
| 🔄 **H. Architecture Change Management** | Keep the architecture fit for purpose as things change. | Change requests, new technology, business changes | Architecture updates, or a new Request for Architecture Work |
| 📋 **Requirements Management** | Track requirements and their changes across every phase. | Requirements from any phase | Requirements Impact Assessment, updated Architecture Requirements Specification |

## 📄 Key deliverables

The phase table names these deliverables:

- 📝 **Statement of Architecture Work:** the agreed scope, plan and approach for one architecture effort.
- 📘 **Architecture Definition Document:** the description of the baseline and target architectures across the domains.
- 📋 **Architecture Requirements Specification:** the measurable requirements a solution must meet to follow the architecture.
- 🪜 **Transition Architecture:** an interim state between baseline and target, used when the change is too big for one step.

## 🔂 Iteration

The ADM groups its phases into four kinds of iteration, each able to repeat on its own:

- 🛠️ **Architecture Capability:** the Preliminary phase and phase A, to set up or change how architecture is done.
- 🏗️ **Architecture Development:** phases B to D, to build up the architecture content.
- 🗺️ **Transition Planning:** phases E and F, to turn the target into a delivery plan.
- 🏛️ **Architecture Governance:** phases G and H, to oversee delivery and manage change.
