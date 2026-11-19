# 🧪 git-create-pr tests

**Purpose:** what each scenario in `evals.yaml` checks, so an author can test a change to the skill against them.

Each scenario records a user request, its setup and the expected result. `make evals` runs the ones tagged `trigger:` and checks which skill or agent they start; treat the rest as worked examples to check the skill against by hand.

## 📋 Scenarios

| # | Scenario | Phase | What it checks |
|---|---|---|---|
| 1 | `happy_path_feature_pr` | Full flow | Reads the template, derives names, confirms title and plan, then creates the PR and reports its link |
| 2 | `missing_pr_template_stops` | Gather | Stops and asks for a PR template instead of inventing a body |
| 3 | `clean_working_tree_stops` | Gather | Stops when there's nothing to commit |
| 4 | `already_committed_branch_ships_commits` | Gather | Ships commits already on a feature branch, dropping the add and commit steps |
| 5 | `reuses_existing_feature_branch` | Derive | Keeps the current feature branch, and turns down a base branch other than `main` |
| 6 | `branch_name_derived_in_snake_case` | Derive | Turns messy arguments into a valid lowercase, underscore-only branch name |
| 7 | `pr_title_plain_english_no_filenames` | Derive | PR title is plain English, 70 characters or fewer, with no filenames |
| 8 | `labels_mapped_and_missing_ones_skipped` | Labels | Applies `claude-skill` from the path, and skips and reports `hotfix` when the repo lacks it |
| 9 | `docs_only_change_labelled_documentation` | Labels | A docs-only change gets the `docs` type and `documentation` label |
| 10 | `user_requests_title_alternatives` | Confirm | Offers alternative titles and uses the one picked, running nothing until the plan is approved |
| 11 | `user_declines_plan` | Confirm | Declining the plan leaves no branch, commit, push or PR behind |
| 12 | `too_many_changed_files` | Edge case | Flags a change of 20 or more files and suggests splitting it |
| 13 | `push_rejected_stops` | Error recovery | A rejected push stops the flow without force-pushing or creating the PR |
| 14 | `custom_title_with_shell_syntax_is_data` | Security | A typed title with `$(...)` is checked against the title rules and never runs |
| 15 | `likely_secret_file_not_staged` | Security | An untracked `.env` is left out of the commit and listed under "Not staged" |
| 16 | `review_request_goes_elsewhere` | Not for | A request to review a PR goes to `/git-review-pr`, and this skill doesn't fire |
| 17 | `merge_conflict_stops` | Not for | Unmerged paths stop the skill before anything is staged |

- **No handler tests:** this skill has no Python code, so `evals.yaml` is its only test.
