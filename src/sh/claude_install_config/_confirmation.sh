#!/bin/bash

# Description: Show what an install or uninstall will change, and require a typed confirmation
# Usage: source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_confirmation.sh",
#        from claude_install_config.sh, which sets the paths and inputs these functions read

#=======================================================================
# Variables
#=======================================================================

# what a project install says about preferences, which only go into your own config
PROJECT_PREFERENCES_NOTE="Preferences don't install into a project; add them to your own config with make install"

#=======================================================================
# Functions
#=======================================================================

# Stop unless run at a real terminal, so Claude's Bash tool can't run the make target $1 unattended
require_terminal() {
    [[ -t 0 ]] && return 0
    log_message "${ERROR}" "Run make ${1} from your own terminal - nothing changed."
    exit 1
}

# Show the prompt $2, and stop unless the word $1 is typed, saying that $3 was cancelled
require_typed() {
    local answer
    read -r -p "${2}" answer || true
    if [[ "${answer}" != "${1}" ]]; then
        log_message "${WARNING}" "${3} cancelled - nothing changed."
        exit 1
    fi
}

# Say how to keep the preferences an install is removing, if it's removing any
print_opt_in_note() {
    local file
    [[ "${PREFERENCES}" == 1 ]] && return 0
    for file in "${REMOVED_FILES[@]}"; do
        if is_preference "${file}"; then
            if [[ -n "${PROJECT}" ]]; then
                log_message "${WARNING}" "${PROJECT_PREFERENCES_NOTE}."
            else
                log_message "${WARNING}" "PREFERENCES=0 removes the preferences: rerun with a plain make install to keep them."
            fi
            return 0
        fi
    done
}

# List the files an install removes and why
print_removals() {
    local file
    [[ "${#REMOVED_FILES[@]}" -gt 0 ]] || return 0
    log_message "${WARNING}" "Removing ${#REMOVED_FILES[@]} file(s) an earlier install added:"
    for file in "${REMOVED_FILES[@]}"; do
        if [[ "${PREFERENCES}" != 1 ]] && is_preference "${file}"; then
            echo "  ${file} (holds preferences, left out)"
        else
            echo "  ${file} (no longer in the repo)"
        fi
    done
    print_opt_in_note
}

# Show what will change and require 'install' typed at a real terminal,
# unless YES=1 opts out outside Claude Code, which sets CLAUDECODE in its Bash tool
confirm_install() {
    if [[ "${ASSUME_YES}" == 1 && -n "${CLAUDECODE:-}" ]]; then
        log_message "${ERROR}" "YES=1 can't be used from Claude Code - run make install from your own terminal."
        exit 1
    fi
    [[ "${ASSUME_YES}" == 1 ]] || require_terminal install
    log_message "${INFO}" "Installing ${#SOURCE_FILES[@]} file(s) into ${TARGET_DIR}."
    print_removals
    echo
    echo "It also updates settings.json, backing up anything it changes to $(dirname "${BACKUP_DIR}")."
    if [[ "${PREFERENCES}" == 1 ]]; then
        echo "It then files saved plans by their status, and archives drafts and plan mode's own plans unchanged for 14 days."
    fi
    [[ "${ASSUME_YES}" == 1 ]] && return 0
    echo
    require_typed install "$(echo -e "${DEBUG}Type 'install' to continue:${COLOUR_OFF} ")" Install
}

# Show what uninstall removes and require 'uninstall' typed at a real terminal
confirm_uninstall() {
    local file
    require_terminal uninstall
    if [[ "${#REMOVED_FILES[@]}" -eq 0 ]]; then
        log_message "${WARNING}" "No install manifest lists files in ${TARGET_DIR} - nothing to uninstall."
        exit 1
    fi
    log_message "${WARNING}" "Removing ${#REMOVED_FILES[@]} file(s) the last install added to ${TARGET_DIR}:"
    for file in "${REMOVED_FILES[@]}"; do
        echo "  ${file}"
    done
    echo "Each is backed up to ${BACKUP_DIR} first, and any file an install replaced is restored from its oldest backup."
    echo "It also removes the config's hooks and deny rules from ${SETTINGS}, keeping every other setting."
    require_typed uninstall "Type 'uninstall' to continue: " Uninstall
}
