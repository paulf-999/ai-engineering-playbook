#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Fail a PR whose author has more than the max number of PRs open, leaving out Dependabot
# Usage: src/sh/git/git_validate_open_prs.sh "<pr author>" "<owner/repo>" (needs gh and a token that can read PRs)

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
# maximum number of PRs an author can have open, including this one
MAX_OPEN_PRS=3

#=======================================================================
# Functions
#=======================================================================

# Print how many PRs the author has open, or fail if GitHub can't be read
count_open_prs() {
    local authors
    authors="$(gh api --paginate "repos/${REPO}/pulls?state=open&per_page=100" --jq '.[].user.login')" || return 1
    # a whole-line match, as one login can be part of another; grep exits 1 on a count of 0
    grep -cxF -- "${PR_AUTHOR}" <<< "${authors}" || true
}

# Exit 1 if the author has too many PRs open, or they can't be counted
check_open_prs() {
    local open_prs
    if ! open_prs="$(count_open_prs)"; then
        print_section_header "${ERROR}" "ERROR: couldn't list the open PRs in ${REPO}."
        exit 1
    fi
    if [[ "${open_prs}" -gt "${MAX_OPEN_PRS}" ]]; then
        print_section_header "${ERROR}" "ERROR: ${PR_AUTHOR} has ${open_prs} PRs open, over the limit of ${MAX_OPEN_PRS}."
        echo "Merge or close some of them, then re-run this check."
        exit 1
    fi
    print_section_header "${INFO}" "SUCCESS: ${PR_AUTHOR} has ${open_prs} PRs open (limit ${MAX_OPEN_PRS})."
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
