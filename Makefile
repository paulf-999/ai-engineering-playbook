SHELL = /bin/sh

#================================================================
# Usage
#================================================================
# make help		# list the available targets
# make all		# run deps then install, the default target the Makefile linter requires
# make deps		# install the dependencies and git hooks
# make install		# copy src/claude/ into your Claude config directory, or PROJECT=<repo>'s .claude/ folder
# make uninstall	# remove what make install added, restoring the files it replaced
# make install YES=1	# install without the typed confirmation, for provisioning scripts outside Claude Code
# make install STYLE=0	# install without the personal reply-format and writing-style rules
# make test		# run the tests (pytest)
# make context_cost	# rewrite maintenance/context_cost.md from src/claude/
# make clean		# delete the pytest, ruff and Python caches

#=======================================================================
# Variables
#=======================================================================
.EXPORT_ALL_VARIABLES:

# ANSI colour codes for the target messages: green, then reset
INFO := \033[0;32m
COLOUR_OFF := \033[0m

#=======================================================================
# Targets
#=======================================================================
all: deps install

help:
	@echo "${INFO}\nAvailable targets:${COLOUR_OFF}\n"
	@sed -n 's/^# make /make /p' Makefile

deps:
	@echo "${INFO}\nCalled makefile target 'deps'. Download any required libraries.${COLOUR_OFF}\n"
	@test -n "$$VIRTUAL_ENV" || { echo "Activate the virtualenv first: see docs/guides/virtualenv_setup.md"; exit 1; }
	@python -m pip install -r requirements.txt
	@python -m pre_commit install

install:
	@echo "${INFO}\nCalled makefile target 'install'. Copy the Claude config into $${PROJECT:+$$PROJECT/.claude}$$([ -n "$${PROJECT:-}" ] || echo "$${CLAUDE_CONFIG_DIR:-$$HOME/.claude}").${COLOUR_OFF}"
	@bash src/sh/claude_install_config.sh

uninstall:
	@echo "${INFO}\nCalled makefile target 'uninstall'. Remove the Claude config that make install added.${COLOUR_OFF}"
	@UNINSTALL=1 bash src/sh/claude_install_config.sh

context_cost:
	@bash src/sh/claude_report_context_cost.sh

test:
	@echo "${INFO}\nCalled makefile target 'test'. Perform any required tests.${COLOUR_OFF}\n"
	@pytest

clean:
	@rm -rf .pytest_cache .ruff_cache
	@find src tests -name __pycache__ -type d -prune -exec rm -rf {} +

# Phony targets
.PHONY: all help deps install uninstall test clean context_cost

# .PHONY tells Make that these targets don't represent files
# This prevents conflicts with any files named "all" or "clean"
