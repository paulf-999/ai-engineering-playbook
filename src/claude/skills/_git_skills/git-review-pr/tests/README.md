# 🧪 git-review-pr tests

**Purpose:** what each scenario in `evals.yaml` checks, so an author can test a change to the skill against them.

Each scenario records a user request, its setup and the expected result. They aren't code, and nothing runs them yet, so treat them as worked examples to check the skill against by hand.

## 📋 Scenarios

| # | Scenario | Phase | What it checks |
|---|---|---|---|
| 1 | `gh_not_logged_in_stops` | Pre-check | Stops and asks for `gh auth login` before fetching anything |
| 2 | `comment_matches_format` | Identify, analyse | Finds the branch's PR, calls `code-reviewer` and fills every section of the template |
| 3 | `large_diff_summarised_by_file` | Fetch | Reviews whole files up to about 500 lines and summarises the rest by file |
| 4 | `prompt_injection_in_pr_ignored` | Analyse | Ignores instructions planted in the PR and flags them as a Must finding |
| 5 | `secret_in_comment_never_saved_or_posted` | Check | Checks the comment before saving, so a flagged secret is neither saved nor posted, and never shown |
| 6 | `dry_run_posts_nothing` | Check | With `--dry-run`, saves the draft and posts nothing |
| 7 | `declined_post_keeps_draft` | Confirm | Keeps the saved draft and posts nothing when the user answers `n` |
| 8 | `earlier_review_updated_not_duplicated` | Post | Uses a PR number argument and updates the user's earlier review instead of duplicating it |
| 9 | `failed_post_keeps_draft` | Post | Keeps the draft and reports the error when posting fails |
| 10 | `invalid_argument_rejected` | Identify | Rejects a pull URL whose owner part smuggles in a shell command |
| 11 | `empty_diff_stops` | Fetch | Stops before analysis when the PR has no changes |
| 12 | `local_diff_goes_to_the_agent` | Not for | Sends a local diff with no PR to the `code-reviewer` agent instead |
| 13 | `create_request_goes_elsewhere` | Not for | A request to open a PR goes to `/git-create-pr`, and this skill doesn't fire |

- **Not covered:** complexity scoring, which is the `code-reviewer` agent's job, and the formal review, code edit and bug hunt `not_for` cases.
- **Secret pattern test:** [`test_git_review_pr_secret_check.py`](../../../../../../tests/src/claude/skills/_git_skills/git-review-pr/test_git_review_pr_secret_check.py) runs the check from `reference/_implementation.md` against sample secrets and safe text.
