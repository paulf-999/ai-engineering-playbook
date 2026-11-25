#!/bin/bash

# Description: Copy files into the target, and back up, remove and restore the ones already there
# Usage: source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_file_changes.sh",
#        from claude_install_config.sh, which sets the paths and inputs these functions read

#=======================================================================
# Variables
#=======================================================================

# no variables of its own

#=======================================================================
# Functions
#=======================================================================

# Create the folder a file path sits in, skipping mkdir when it's already there, since most files share a folder
make_parent_folder() {
    [[ -d "${1%/*}" ]] || mkdir -p "${1%/*}"
}

# Copy an installed path into a backup folder
back_up_file() {
    make_parent_folder "${1}/${2}"
    cp -p "${TARGET_DIR}/${2}" "${1}/${2}"
}

# Copy an installed path into a backup folder, then remove it from the target
back_up_and_remove() {
    back_up_file "${1}" "${2}"
    rm "${TARGET_DIR}/${2}"
}

# Print where to back up an installed path: the upgrade folder for a copy an earlier install wrote, else the usual one
backup_dir_for() {
    if file_exists "${MANIFEST}" && grep -Fxq -- "${1}" "${MANIFEST}"; then
        echo "${UPGRADE_BACKUP_DIR}"
    else
        echo "${BACKUP_DIR}"
    fi
}

# Succeed if a source file is already installed as it would be now
is_up_to_date() {
    file_exists "${2}" || return 1
    # a file with no links or, in a project, pointers to rewrite is compared as it stands, with no render
    if [[ -z "${PROJECT}" ]] && ! has_links "${1}"; then
        cmp -s "${SOURCE_DIR}/${1}" "${2}"
    else
        cmp -s <(render "${1}") "${2}"
    fi
}

# Copy each file over the target, backing up any existing copy that differs, and skipping identical ones
install_files() {
    local file relative target copied=0 backed_up=0
    for file in "${SOURCE_FILES[@]}"; do
        target_path "${file}"
        relative="${TARGET_PATH}"
        target="${TARGET_DIR}/${relative}"
        is_up_to_date "${file}" "${target}" && continue
        if file_exists "${target}"; then
            back_up_file "$(backup_dir_for "${relative}")" "${relative}"
            backed_up=$((backed_up + 1))
        fi
        make_parent_folder "${target}"
        render "${file}" > "${target}"
        copied=$((copied + 1))
    done
    log_message "${INFO}" "Installed ${copied} changed file(s), backing up ${backed_up}, into ${TARGET_DIR}."
}

# Back up and remove each file the repo no longer has, then record what this install wrote
remove_old_files() {
    local file
    # each removed file is one the manifest lists, so an earlier install wrote it
    for file in "${REMOVED_FILES[@]+"${REMOVED_FILES[@]}"}"; do
        back_up_and_remove "${UPGRADE_BACKUP_DIR}" "${file}"
    done
    remove_emptied_folders
    log_message "${INFO}" "Removed ${#REMOVED_FILES[@]} file(s) an earlier install added." false
    printf '%s' "${TARGET_PATHS}" > "${MANIFEST}"
}

# Remove the folders that removing REMOVED_FILES left empty, walking up from each file, so other empty folders stay
remove_emptied_folders() {
    local file folder
    for file in "${REMOVED_FILES[@]+"${REMOVED_FILES[@]}"}"; do
        # the leading ./ lets each step trim one folder in place, without a dirname subprocess, until only . is left
        folder="./${file}"
        folder="${folder%/*}"
        # rmdir only removes an empty folder, so the walk stops at the first one that still holds something
        while [[ "${folder}" != "." ]] && rmdir "${TARGET_DIR}/${folder}" 2> /dev/null; do
            folder="${folder%/*}"
        done
    done
    return 0
}

# Print the oldest backup of an installed path, or nothing if there's none, trying a project's hashed folders before the
# unhashed ones, which could be another repo's with the same name
oldest_backup() {
    local prefix backup
    for prefix in "${BACKUP_PREFIX}" ${OLD_BACKUP_PREFIX:+"${OLD_BACKUP_PREFIX}"}; do
        # the globs expand in date order, and matching the whole date skips uninstall and upgrade backups
        for backup in "${prefix}"[0-9][0-9][0-9][0-9]_[0-9][0-9]_[0-9][0-9]_[0-9][0-9][0-9][0-9][0-9][0-9]/"${1}"; do
            if file_exists "${backup}"; then
                echo "${backup}"
                return 0
            fi
        done
    done
}

# Back up and remove each installed file, restoring its oldest backup, which holds the user's own file,
# since an upgrade backs up the playbook's own previous version to the upgrade folder instead
uninstall_files() {
    local file original restored=0
    for file in "${REMOVED_FILES[@]}"; do
        back_up_and_remove "${BACKUP_DIR}" "${file}"
        original="$(oldest_backup "${file}")"
        if [[ -n "${original}" ]]; then
            cp -p "${original}" "${TARGET_DIR}/${file}"
            restored=$((restored + 1))
        fi
    done
    rm -f "${MANIFEST}"
    remove_emptied_folders
    log_message "${INFO}" "Removed ${#REMOVED_FILES[@]} file(s), restoring ${restored} from backups."
}
