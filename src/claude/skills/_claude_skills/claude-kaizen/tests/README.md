# 🧪 claude-kaizen tests

**Purpose:** what each scenario in `evals.yaml` checks, so an author can test a change to the skill against them.

Each scenario records a user request, its setup and the expected result. `make evals` runs the ones tagged `trigger:` and checks which skill or agent they start. Treat the rest as worked examples to check the skill against by hand, since their setups need feedback notes or a set verdict.

## 📋 Scenarios

| # | Scenario | Phase | What it checks |
|---|---|---|---|
| 1 | `plain_request_doesnt_fire` | Trigger | "Run kaizen" doesn't start the slash-only skill |
| 2 | `slash_command_starts_it` | Trigger | `/claude-kaizen` reads the notes before proposing anything |
| 3 | `drafts_shown_before_any_edit` | Draft | Each rule comes with its case as a diff, and a "no" edits nothing |
| 4 | `no_effect_verdict_undone` | Prove | A **no effect** verdict undoes the skill's own edits |
| 5 | `repo_specific_note_stays_in_memory` | Select | A note about one repo's layout isn't proposed as a rule |
| 6 | `never_commits` | Report | Kept rules stay in the working tree, for `/git-create-pr` |
| 7 | `single_correction_saved_to_memory` | Not for | A one-off correction goes to memory, not kaizen |
| 8 | `rule_review_goes_elsewhere` | Not for | Reviewing existing rules doesn't fire the skill |

- **Runner tests:** `tests/src/py/test_claude_run_rule_evals.py` checks the `CASE` filter the skill relies on.
