<!-- version: 1.0.0 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-04 -->
# 🏛️ TOGAF: Governance and tailoring

**Purpose:** how the TOGAF Standard keeps delivery in line with the architecture, and how an organisation adapts the method to fit itself.

This page is part of the [summary of the TOGAF Standard](../togaf_standards.md), and governance happens mainly in phases G and H of the [ADM cycle](02_adm_cycle.md).

## 🏛️ Architecture governance

Governance makes sure architecture decisions are made, followed and recorded, through these parts:

- 👥 **Architecture Board:** a group of senior stakeholders that oversees the architecture, settles disputes and approves exceptions.
- 📝 **Architecture Contract:** an agreement between the architecture function and a delivery team on what will be built and to what standard.
- 🔍 **Compliance review:** a check, at set points in a project, that the solution matches the architecture.
- 🎫 **Dispensation:** a time-limited, approved exception for a solution that can't comply yet.

## 📏 Levels of compliance

A compliance review rates how far a solution matches the architecture:

| Level | Meaning |
|---|---|
| ⚪ **Irrelevant** | The solution and the architecture have nothing in common. |
| 🔵 **Consistent** | The overlap follows the architecture, but parts of it aren't built and the solution adds features it doesn't cover. |
| 🟢 **Compliant** | Parts of the architecture aren't built, but everything that is built follows it, and nothing goes beyond it. |
| ✅ **Conformant** | All of the architecture is built as specified, plus extra features it doesn't cover. |
| 🏆 **Fully conformant** | The solution and the architecture match exactly. |
| ❌ **Non-conformant** | Some of what is built goes against the architecture. |

## ✂️ Tailoring the ADM

The standard expects the ADM to be adapted rather than followed as written:

- 🔤 **Terms:** swap TOGAF's terms for those the organisation already uses.
- 🔀 **Process:** reorder, merge or skip phases, or run them in parallel, to suit the organisation's maturity and pace.
- 📦 **Content:** produce only the deliverables and artefacts stakeholders actually need.
- 🔗 **Other frameworks:** fit the ADM alongside methods already in use, such as agile delivery or a project management method.
- 🎯 **Where it's set:** tailoring is decided in the Preliminary phase and revisited as the organisation changes.

## 🎚️ Scope and partitioning

Large enterprises can't be described in one architecture, so the standard splits the work by subject, time and maturity, and by these levels of detail:

- 🗺️ **Strategic:** a long-term, organisation-wide view, used to set direction.
- 🧩 **Segment:** a single area of the business, used to plan programmes.
- 🔧 **Capability:** one capability in detail, used to guide delivery projects.
