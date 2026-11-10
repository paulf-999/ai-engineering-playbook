<!-- version: 1.0.0 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-04 -->
# 📦 TOGAF: Architecture content and the Enterprise Continuum

**Purpose:** what an architecture effort produces, how the TOGAF Standard classifies architectures for reuse, and where the results are kept.

This page is part of the [summary of the TOGAF Standard](../togaf_standards.md), and building blocks are defined on the [core concepts page](01_core_concepts.md).

## 📐 The Architecture Content Framework

The framework sorts what the ADM produces into three kinds of output:

| Output | What it is | Example |
|---|---|---|
| 📄 **Deliverable** | A formally agreed work product, reviewed and signed off by stakeholders. | Architecture Definition Document |
| 📊 **Artefact** | A single description of one aspect of the architecture, as a catalogue, matrix or diagram. | An application-to-process matrix |
| 🧱 **Building block** | A reusable component of capability, described by artefacts. | A customer data service |

- 🪆 **How they nest:** deliverables contain artefacts, and artefacts describe building blocks.
- 🧬 **Content Metamodel:** a model of the entities, such as actors, services and applications, and how they relate, so content stays consistent.

## 🌐 The Enterprise Continuum

The Enterprise Continuum classifies architectures and solutions from generic to specific, so teams can reuse what already exists:

| Level | Meaning |
|---|---|
| 🌍 **Foundation** | Generic building blocks that apply to almost any organisation. |
| 🧰 **Common Systems** | Patterns for common systems, such as security or networking. |
| 🏭 **Industry** | Patterns specific to one industry, such as banking or retail. |
| 🏢 **Organisation-Specific** | The organisation's own architectures, built from the levels above. |

- ↔️ **Two parallel continua:** the Architecture Continuum holds these levels for architectures, and the Solutions Continuum holds them for the solutions that deliver them.

## 🗄️ The Architecture Repository

The repository is where architecture work is stored, in these main parts:

- 🧬 **Architecture Metamodel:** the tailored framework and content metamodel the organisation uses.
- 🛠️ **Architecture Capability:** how the architecture function itself is organised and run.
- 🗺️ **Architecture Landscape:** the architectures themselves, at strategic, segment and capability levels.
- 📚 **Standards and reference:** the Standards Library, of standards to follow, and the Reference Library, of reusable patterns.
- 🧾 **Governance Log:** the record of decisions, compliance assessments and dispensations.
