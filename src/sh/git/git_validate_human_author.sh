#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Fail a bot's PR that has no human assignee, so a person is always named on it
# Usage: src/sh/git/git_validate_human_author.sh "<author type>" ["<assignee types, separated by spaces>"] (types as GitHub gives them, such as User or Bot)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/../shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/../shell_utils.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

AUTHOR_TYPE="${1:?Required: account type of the PR author (arg 1)}"
ASSIGNEE_TYPES="${2-}"

#=======================================================================
# Functions
#=======================================================================

# Succeed if the author or an assignee is a person, which GitHub calls a User
has_human() {
    [[ " ${AUTHOR_TYPE} ${ASSIGNEE_TYPES} " == *" User "* ]]
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

if ! has_human; then
    print_section_header "${ERROR}" "ERROR: this PR's author is a ${AUTHOR_TYPE}, and no person is assigned to it."
    echo "Assign the person who answers for this PR."
    exit 1
fi
print_section_header "${INFO}" "SUCCESS: a person is named on this PR"

print_section_header "${DEBUG}" "Script execution completed." && echo
