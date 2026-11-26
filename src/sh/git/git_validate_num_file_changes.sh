#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Fail a PR that changes more than the max number of files, unless it's on a release/ branch
# Usage: src/sh/git/git_validate_num_file_changes.sh <git branch name> "<changed files, one per line>" (run from the repo
#        root, with the list from GitHub's PR files API, so no checkout of the PR is needed)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/../shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/../shell_utils.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

GIT_BRANCH_NAME="${1:?Required: git branch name (arg 1)}"
# the PR's changed files, one per line
CHANGED_FILES="${2-}"
# maximum number of files a PR can change; override via the MAX_FILES_ALLOWED env var
MAX_FILES_CHANGED="${MAX_FILES_ALLOWED:-20}"
# how many changed files to list before summarising the rest
MAX_FILES_LISTED=50

#=======================================================================
# Functions
#=======================================================================

# Check whether the branch is a release/ branch
is_release_branch() {
    [[ "${GIT_BRANCH_NAME}" == release/* ]]
}

# Normalise the file limit to a whole number, or exit 1
validate_max_files_changed() {
    # the limit must be a whole number (checked after the release skip, which never uses it)
    if ! MAX_FILES_CHANGED="$(to_whole_number "${MAX_FILES_CHANGED}")"; then
        print_section_header "${ERROR}" "ERROR: MAX_FILES_ALLOWED must be a whole number of up to 9 digits, got '${MAX_FILES_ALLOWED}'."
        exit 1
    fi
}

# Set FILE_COUNT from the changed files
count_changed_files() {
    # count non-empty lines; grep exits 1 when there are none, so don't let set -e stop the script
    FILE_COUNT=$(grep -c . <<< "${CHANGED_FILES}" || true)
}

# Print the changed files, summarising any beyond the listing limit
print_changed_files() {
    log_message "${DEBUG_DETAILS}" "Files changed (${FILE_COUNT}):"
    # list the first files only, so a very large PR doesn't flood the log
    head -n "${MAX_FILES_LISTED}" <<< "${CHANGED_FILES}"
    if [[ "${FILE_COUNT}" -gt "${MAX_FILES_LISTED}" ]]; then
        echo "... and $((FILE_COUNT - MAX_FILES_LISTED)) more"
    fi
}

# Compare the file count with the limit, exiting 1 when it's over
check_file_count() {
    if [[ "${FILE_COUNT}" -gt "${MAX_FILES_CHANGED}" ]]; then
        print_section_header "${ERROR}" "ERROR: number of files changed in PR (${FILE_COUNT}) exceeds the max (${MAX_FILES_CHANGED})."
        echo -e "Split the PR by logical area, or use a release/ branch for one bulk change (see docs/guides/git_branching_strategy.md)."
        exit 1
    fi
    print_section_header "${INFO}" "SUCCESS: number of changed files (${FILE_COUNT}) is within the max (${MAX_FILES_CHANGED})."
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

# release branches are for large bulk changes (see docs/guides/git_branching_strategy.md), so they skip the check
if is_release_branch; then
    print_section_header "${INFO}" "Release branch - skip file count check." && echo
    exit 0
fi

validate_max_files_changed
count_changed_files
print_changed_files
check_file_count

print_section_header "${DEBUG}" "Script execution completed." && echo
