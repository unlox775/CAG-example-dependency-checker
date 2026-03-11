.PHONY: help install check-dependencies check-all clean

DEPENDENCY_CHECKER_CONFIG ?= dependency-checker.config.json
VENV_DIR ?= .venv
PYTHON ?= $(VENV_DIR)/bin/python3
PIP ?= $(VENV_DIR)/bin/pip

help:
	@echo "Standalone Dependency Checker (CAG Example)"
	@echo "==========================================="
	@echo "install              Create local venv and install requirements"
	@echo "check-dependencies   Run dependency documentation gate"
	@echo "check-all            Alias for check-dependencies"
	@echo "clean                Remove local run artifacts"

install:
	python3 -m venv "$(VENV_DIR)"
	"$(PIP)" install -r requirements.txt

check-dependencies:
	@if [ -x "$(PYTHON)" ]; then \
		"$(PYTHON)" dependency_checker.py --config "$(DEPENDENCY_CHECKER_CONFIG)"; \
	else \
		python3 dependency_checker.py --config "$(DEPENDENCY_CHECKER_CONFIG)"; \
	fi

check-all: check-dependencies

clean:
	rm -rf __pycache__ .pytest_cache "$(VENV_DIR)"
	rm -f results/dependency-checker-last-run-*.txt
