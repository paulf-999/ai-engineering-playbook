#!/bin/bash
# version: 1.0.0
# created: 2026-11-04
# updated: 2026-11-04
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Copy the repo's Claude config (src/claude/) into your Claude config directory, backing up each file it overwrites
# Usage: src/sh/claude_install_config.sh (run from the repo root, at your own terminal; make install calls it)

# Load reusable shell script vars & functions
source src/sh/shell_utils.sh

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

# mirrors the config directory's layout, so each file is copied to the same relative path
SOURCE_DIR="src/claude"
TARGET_DIR="${CLAUDE_CONFIG_DIR:-${HOME}/.claude}"
BACKUP_DIR="${TARGET_DIR}/backups/install_$(date +%Y_%m_%d_%H%M%S)"
# the tracked files under SOURCE_DIR, set by list_source_files
SOURCE_FILES=()

#=======================================================================
# Functions
#=======================================================================

# Collect the files git tracks under SOURCE_DIR, so untracked drafts and caches are never installed
list_source_files() {
    local file
    while IFS= read -r -d '' file; do
        SOURCE_FILES+=("${file#"${SOURCE_DIR}"/}")
    done < <(git ls-files -z -- "${SOURCE_DIR}")
    if [[ "${#SOURCE_FILES[@]}" -eq 0 ]]; then
        log_message "${ERROR}" "No tracked files found under ${SOURCE_DIR} - nothing to install."
        exit 1
    fi
}

# Show what will change and require 'install' typed at a real terminal, so Claude's Bash tool can't run it unattended
confirm_install() {
    local answer file
    if [[ ! -t 0 ]]; then
        log_message "${ERROR}" "Run make install from your own terminal - nothing changed."
        exit 1
    fi
    log_message "${INFO}" "Installing ${#SOURCE_FILES[@]} file(s) into ${TARGET_DIR}:"
    for file in "${SOURCE_FILES[@]}"; do
        echo "  ${file}"
    done
    echo "Each file it overwrites is backed up to ${BACKUP_DIR} first, and nothing is deleted."
    read -r -p "Type 'install' to continue: " answer || true
    if [[ "${answer}" != "install" ]]; then
        log_message "${WARNING}" "Install cancelled - nothing changed."
        exit 1
    fi
}

# Copy each file over the target, backing up any existing copy that differs, and skipping identical ones
install_files() {
    local file target copied=0 backed_up=0
    for file in "${SOURCE_FILES[@]}"; do
        target="${TARGET_DIR}/${file}"
        if file_exists "${target}" && cmp -s "${SOURCE_DIR}/${file}" "${target}"; then
            continue
        fi
        if file_exists "${target}"; then
            mkdir -p "$(dirname "${BACKUP_DIR}/${file}")"
            cp -p "${target}" "${BACKUP_DIR}/${file}"
            backed_up=$((backed_up + 1))
        fi
        mkdir -p "$(dirname "${target}")"
        cp "${SOURCE_DIR}/${file}" "${target}"
        copied=$((copied + 1))
    done
    log_message "${INFO}" "Installed ${copied} changed file(s), backing up ${backed_up}, into ${TARGET_DIR}."
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

list_source_files
confirm_install
install_files

print_section_header "${DEBUG}" "Script execution completed." && echo
