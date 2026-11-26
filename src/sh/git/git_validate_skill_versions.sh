#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Fail a PR that changes a skill's files without bumping the version in its skill.contract.yaml
# Usage: src/sh/git/git_validate_skill_versions.sh "<owner/repo>" "<base sha>" "<head sha>" "<changed files, one per line>"
#        (needs gh and a token that can read the repo; reads contracts through GitHub's API, so no checkout of the PR
#        is needed)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/../shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/../shell_utils.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

REPO="${1:?Required: owner/repo (arg 1)}"
BASE_SHA="${2:?Required: base commit (arg 2)}"
HEAD_SHA="${3:?Required: head commit (arg 3)}"
# the PR's changed files, one per line
CHANGED_FILES="${4-}"

#=======================================================================
# Functions
#=======================================================================

# Print the version line of the contract at path $2 in commit $1, nothing when it doesn't exist there, or fail if
# GitHub can't be read
contract_version() {
    local contract
    if ! contract="$(gh api "repos/${REPO}/contents/${2}?ref=${1}" -H "Accept: application/vnd.github.raw+json" 2>&1)"; then
        # a 404 means the contract isn't there, so the skill is new or deleted; anything else is a failed lookup
        [[ "${contract}" == *"HTTP 404"* ]] && return 0
        return 1
    fi
    grep -m 1 '^version:' <<< "${contract}" || true
}

# Print the commit where the PR's branch left the base, or fail if GitHub can't be read
merge_base() {
    gh api "repos/${REPO}/compare/${BASE_SHA}...${HEAD_SHA}" --jq '.merge_base_commit.sha'
}

# List each skill folder, as src/claude/skills/<group>/<skill>, that has a changed file
changed_skills() {
    awk -F/ '/^src\/claude\/skills\// && NF > 5 { print $1 "/" $2 "/" $3 "/" $4 "/" $5 }' <<< "${CHANGED_FILES}" | sort -u
}

# Exit 1, saying GitHub couldn't be read
lookup_failed() {
    print_section_header "${ERROR}" "ERROR: couldn't read the skill contracts from ${REPO}."
    exit 1
}

# Exit 1, naming each existing skill that changed while its contract version stayed the same
check_versions() {
    local skill contract base base_version head_version stale=()
    while read -r skill; do
        [[ -n "${skill}" ]] || continue
        contract="${skill}/skill.contract.yaml"
        [[ -n "${base:-}" ]] || base="$(merge_base)" || lookup_failed
        base_version="$(contract_version "${base}" "${contract}")" || lookup_failed
        # a skill new in this PR, or one it deletes, has no earlier version to compare
        [[ -n "${base_version}" ]] || continue
        head_version="$(contract_version "${HEAD_SHA}" "${contract}")" || lookup_failed
        [[ "${head_version}" == "${base_version}" ]] && stale+=("${skill##*/}")
    done <<< "$(changed_skills)"
    if [[ "${#stale[@]}" -gt 0 ]]; then
        print_section_header "${ERROR}" "ERROR: these skills changed without a version bump in skill.contract.yaml: ${stale[*]}."
        echo -e "Bump each one's version, such as 1.1.0 to 1.2.0 for a behaviour change, or 1.1.1 for a fix."
        exit 1
    fi
    print_section_header "${INFO}" "SUCCESS: every changed skill has a new contract version."
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

check_versions

print_section_header "${DEBUG}" "Script execution completed." && echo
