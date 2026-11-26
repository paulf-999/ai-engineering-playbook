#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Fail a PR whose author has more than the max number of PRs ready for review, counting only this PR and
#              older ones, so the oldest can always merge, and leaving out drafts and Dependabot
# Usage: src/sh/git/git_validate_open_prs.sh "<pr author>" "<owner/repo>" "<pr number>" (needs gh and a token that can read PRs)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/../shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/../shell_utils.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

PR_AUTHOR="${1:?Required: login of the PR author (arg 1)}"
REPO="${2:?Required: owner/repo (arg 2)}"
PR_NUMBER="${3:?Required: number of this PR (arg 3)}"
# maximum number of PRs an author can have ready for review, counting this one and older ones
MAX_OPEN_PRS=6

#=======================================================================
# Functions
#=======================================================================

# Print how many of the author's open PRs ready for review are this one or older, or 0 if this one is a draft, or fail
# if GitHub can't be read
count_open_prs() {
    local open_prs
    open_prs="$(gh api --paginate "repos/${REPO}/pulls?state=open&per_page=100" --jq '.[] | "\(.user.login) \(.number) \(.draft)"')" || return 1
    # GitHub numbers PRs in the order they're opened, so a lower number is older; a draft can't merge, so it never counts
    awk -v author="${PR_AUTHOR}" -v number="${PR_NUMBER}" '
        $1 == author && $2 == number && $3 == "true" { draft = 1 }
        $1 == author && $2 <= number && $3 != "true" { count++ }
        END { print draft ? 0 : count + 0 }
    ' <<< "${open_prs}"
}

# Exit 1 if the author has too many PRs open, or they can't be counted
check_open_prs() {
    local open_prs
    if ! open_prs="$(count_open_prs)"; then
        print_section_header "${ERROR}" "ERROR: couldn't list the open PRs in ${REPO}."
        exit 1
    fi
    if [[ "${open_prs}" -gt "${MAX_OPEN_PRS}" ]]; then
        print_section_header "${ERROR}" "ERROR: ${PR_AUTHOR} has ${open_prs} PRs ready for review, over the limit of ${MAX_OPEN_PRS}."
        echo "Merge or close some of them, then re-run this check."
        exit 1
    fi
    print_section_header "${INFO}" "SUCCESS: ${PR_AUTHOR} has ${open_prs} PRs ready for review (limit ${MAX_OPEN_PRS})."
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

if [[ "${PR_AUTHOR}" == "dependabot[bot]" ]]; then
    print_section_header "${INFO}" "SUCCESS: Dependabot's open PRs aren't limited"
    exit 0
fi

check_open_prs

print_section_header "${DEBUG}" "Script execution completed." && echo
