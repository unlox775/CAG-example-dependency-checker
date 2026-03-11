# Development Tools

> **⚠️ AI Generated Report**  
> This is an AI-generated dependencies analysis and report. Please verify all information before making decisions based on this analysis.

## Overview

This document analyzes Python development tools and utilities used for code quality, testing, and development workflow.

## Dependencies

### Code Quality & Linting
- [x] **ruff** (0.1.6) - Python linter and formatter
  - **Usage**: Python code linting and formatting
  - **Files**: Found in 10+ files across the codebase
  - **Key locations**:
    - `python/pyproject.toml:15` - Ruff configuration
    - `python/.ruff.toml:1` - Ruff settings
    - [`python/scripts/lint.py:1`](../../dashboard/config/scripts/sp_vpl_21_csd_mod5_mlintro_c4u__22_23_25_2025.multi#L1) - Linting script
  - **Necessity**: **HIGH** - Code quality tool, removing would require alternative linting
  - **Compensation if removed**: Would need to implement alternative linting or remove code quality checks
  - **Documentation**: [Ruff](https://docs.astral.sh/ruff/) | [GitHub](https://github.com/astral-sh/ruff)
  - **Current version**: 0.1.6 | **Latest stable**: 0.1.x | **Upgrade path**: Minor version updates available

### Testing Framework
- [x] **pytest** (7.4.3) - Python testing framework
  - **Usage**: Primary testing framework for Python code
  - **Files**: Found in 50+ files across the codebase
  - **Key locations**:
    - `python/test/test_pycdo.py:1` - PyCDO tests
    - `python/test/test_neighborhood.py:1` - Neighborhood tests
    - `python/test/test_pythonlab_setup.py:1` - Python lab setup tests
  - **Necessity**: **CRITICAL** - Testing framework, removing would break Python testing
  - **Compensation if removed**: Would need to implement alternative testing framework or remove Python testing
  - **Documentation**: [Pytest](https://docs.pytest.org/) | [GitHub](https://github.com/pytest-dev/pytest)
  - **Current version**: 7.4.3 | **Latest stable**: 8.x | **Upgrade path**: Major version upgrade with breaking changes

### Code Coverage
- [x] **coverage** (7.3.2) - Code coverage measurement
  - **Usage**: Python code coverage measurement for testing
  - **Files**: Found in 15+ files across the codebase
  - **Key locations**:
    - `python/pyproject.toml:20` - Coverage configuration
    - `python/scripts/coverage.py:1` - Coverage script
    - `python/test/conftest.py:1` - Test configuration with coverage
  - **Necessity**: **HIGH** - Code coverage tool, removing would require alternative coverage measurement
  - **Compensation if removed**: Would need to implement alternative coverage measurement or remove coverage tracking
  - **Documentation**: [Coverage](https://coverage.readthedocs.io/en/latest/) | [GitHub](https://github.com/nedbat/coveragepy)
  - **Current version**: 7.3.2 | **Latest stable**: 7.x | **Upgrade path**: Minor version updates available

### Package Management
- [x] **uv** (0.1.44) - Python package manager
  - **Usage**: Python package management and virtual environment handling
  - **Files**: Found in 5+ files across the codebase
  - **Key locations**:
    - `python/pyproject.toml:1` - Project configuration
    - [`python/scripts/setup.py:1`](../../apps/src/sites/studio/pages/maker/setup.js#L1) - Setup script
    - [`python/scripts/install.py:1`](../../dashboard/config/scripts/vpl_csd_pilot_22_ci_mod6_makerapp_install_physical_computing.external#L1) - Installation script
  - **Necessity**: **HIGH** - Package management, removing would require alternative package management
  - **Compensation if removed**: Would need to implement alternative package management or migrate to different tool
  - **Documentation**: [UV](https://docs.astral.sh/uv/) | [GitHub](https://github.com/astral-sh/uv)
  - **Current version**: 0.1.44 | **Latest stable**: 0.1.x | **Upgrade path**: Minor version updates available

## Summary

The Development Tools section contains Python development tools and utilities used for code quality, testing, and development workflow. These dependencies are critical to the development process and would require significant refactoring to replace.

### Critical Dependencies
- **pytest** - Testing framework (CRITICAL)

### High Impact Dependencies
- **ruff** - Code linting (HIGH)
- **coverage** - Code coverage (HIGH)
- **uv** - Package management (HIGH)

---

[← Back to Python Dependencies Overview](README.md) | [Next: Local Packages →](local-packages.md)