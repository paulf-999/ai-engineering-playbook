# 🛠️ Authoring skills

**Purpose:** how to lay out, describe and test a new skill, as part of the [authoring guide](../authoring_guide.md).

- 📄 **SKILL.md:** about 60 lines from `_templates/skills/SKILL.md.template`, leaving longer detail to `reference/`.
- 📜 **Contract:** a `skill.contract.yaml` from its template, written before `SKILL.md`, since it sets the scope.
- 📚 **Folders:** `reference/` for the files Claude reads while running the skill, starting with `_implementation.md`, and `tests/` for `evals.yaml` and a plain-language `README.md`, with nothing else apart from one script at the root if it runs code.
- 🏷️ **Name:** `<domain>-<action>`, a domain then an imperative verb, such as `git-create-pr`, matching the folder name, per the [Agent Skills spec](https://agentskills.io/specification).
- 🚧 **Not for:** list in the contract's `not_for` what the skill doesn't do, since that boundary matters most.
- 🗣️ **Description:** use the phrases people type to ask for it, and keep it short, since every description loads in every session.
- 🔇 **Slash-only:** set `disable-model-invocation: true` for a skill people run on purpose, such as a periodic review, since its description then costs no always-on context.
- ✋ **Confirm first:** set `confirmation_required: true` for anything irreversible or visible to others, such as a push.
- 🔐 **Safety:** read secrets from the environment, validate input before it reaches a shell or API, and hard-code no paths.

## 🏁 Before merging

- 🧪 **Evals:** add evals that cover its main triggers and one case where it shouldn't fire, tagging each with `trigger: <skill-or-agent>` or `trigger: none` so `make evals` checks it. Tag a scenario `behaviour: true` too when its setup is local git state, so `make evals BEHAVIOUR=1` grades its assertions.
- 📋 **Evaluation criteria:** a skill loads on demand, so its PR needs no Evaluation criteria section unless the [evaluation criteria](../../target_architecture/design_principles/02_evaluation_criteria.md) say so.
- 🏅 **Review:** have a fresh-context reviewer check it against a checklist for its type, modelled on the [rules checklist](../../../maintenance/quality/quality_rubrics/_repo.md#-rules-and-tests-checklists).
