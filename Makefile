SHELL = /bin/sh

#================================================================
# Usage
#================================================================
# make help		# list the available targets
# make deps		# install the dependencies and git hooks
# make install		# copy src/claude/ into your Claude config directory
# make test		# run the tests (pytest)
# make context_cost	# rewrite docs/maintenance/context_cost.md from src/claude/
# make clean		# delete the pytest, ruff and Python caches

#=======================================================================
# Variables
#=======================================================================
.EXPORT_ALL_VARIABLES:

# load variables from separate file
include src/make/variables.mk # load variables from a separate makefile file

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
	@echo "${INFO}\nCalled makefile target 'install'. Copy the Claude config into $${CLAUDE_CONFIG_DIR:-$$HOME/.claude}.${COLOUR_OFF}"
	@bash src/sh/claude_install_config.sh

context_cost:
	@bash src/sh/claude_report_context_cost.sh

test:
	@echo "${INFO}\nCalled makefile target 'test'. Perform any required tests.${COLOUR_OFF}\n"
	@pytest

clean:
	@rm -rf .pytest_cache .ruff_cache
	@find src tests -name __pycache__ -type d -prune -exec rm -rf {} +

# Phony targets
.PHONY: all help deps install test clean context_cost

# .PHONY tells Make that these targets don't represent files
# This prevents conflicts with any files named "all" or "clean"
