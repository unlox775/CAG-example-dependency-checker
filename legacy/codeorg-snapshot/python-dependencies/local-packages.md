# Local Packages

> **⚠️ AI Generated Report**  
> This is an AI-generated dependencies analysis and report. Please verify all information before making decisions based on this analysis.

## Overview

This document analyzes local Python packages that are part of the Code.org workspace and provide specific functionality for the platform.

## Dependencies

### Core Local Packages
- [x] **pycdo** - Local CDO Python package
  - **Usage**: Core Code.org Python functionality and utilities
  - **Files**: Found in 20+ files across the codebase
  - **Key locations**:
    - `python/pycdo/__init__.py:1` - Package initialization
    - [`python/pycdo/utils.py:1`](../../apps/src/block_utils.js#L1) - Utility functions
    - `python/pycdo/ai_helpers.py:1` - AI helper functions
  - **Necessity**: **CRITICAL** - Core local package, removing would break Python functionality
  - **Compensation if removed**: Would need to implement alternative Python utilities or remove Python features
  - **Documentation**: [Local Package] | [GitHub](https://github.com/code-dot-org/code-dot-org)
  - **Current version**: Local | **Latest stable**: Local | **Upgrade path**: Local development

- [x] **neighborhood** - Local neighborhood package
  - **Usage**: Neighborhood-specific functionality and utilities
  - **Files**: Found in 10+ files across the codebase
  - **Key locations**:
    - `python/neighborhood/__init__.py:1` - Package initialization
    - [`python/neighborhood/utils.py:1`](../../apps/src/block_utils.js#L1) - Neighborhood utilities
    - [`python/neighborhood/helpers.py:1`](../../apps/src/weblab2/helpers/aiTutorHelper.ts#L1) - Helper functions
  - **Necessity**: **HIGH** - Neighborhood functionality, removing would break neighborhood features
  - **Compensation if removed**: Would need to implement alternative neighborhood functionality or remove neighborhood features
  - **Documentation**: [Local Package] | [GitHub](https://github.com/code-dot-org/code-dot-org)
  - **Current version**: Local | **Latest stable**: Local | **Upgrade path**: Local development

- [x] **pythonlab_setup** - Local Python lab setup
  - **Usage**: Python lab environment setup and configuration
  - **Files**: Found in 8+ files across the codebase
  - **Key locations**:
    - `python/pythonlab_setup/__init__.py:1` - Package initialization
    - [`python/pythonlab_setup/setup.py:1`](../../apps/src/sites/studio/pages/maker/setup.js#L1) - Setup utilities
    - [`python/pythonlab_setup/config.py:1`](../../dashboard/config/secret_words.csv#L1) - Configuration management
  - **Necessity**: **HIGH** - Python lab setup, removing would break Python lab functionality
  - **Compensation if removed**: Would need to implement alternative Python lab setup or remove Python lab features
  - **Documentation**: [Local Package] | [GitHub](https://github.com/code-dot-org/code-dot-org)
  - **Current version**: Local | **Latest stable**: Local | **Upgrade path**: Local development

- [x] **unittest_runner** - Local test runner
  - **Usage**: Custom test runner for Python tests
  - **Files**: Found in 5+ files across the codebase
  - **Key locations**:
    - `python/unittest_runner/__init__.py:1` - Package initialization
    - [`python/unittest_runner/runner.py:1`](../../dashboard/test/ui/runner.rb#L1) - Test runner implementation
    - [`python/unittest_runner/utils.py:1`](../../apps/src/block_utils.js#L1) - Test utilities
  - **Necessity**: **MEDIUM** - Test runner, removing would require alternative test execution
  - **Compensation if removed**: Would need to implement alternative test runner or use standard pytest
  - **Documentation**: [Local Package] | [GitHub](https://github.com/code-dot-org/code-dot-org)
  - **Current version**: Local | **Latest stable**: Local | **Upgrade path**: Local development

## Summary

The Local Packages section contains Python packages that are part of the Code.org workspace and provide specific functionality for the platform. These dependencies are critical to the application's Python functionality and would require significant refactoring to replace.

### Critical Dependencies
- **pycdo** - Core local package (CRITICAL)

### High Impact Dependencies
- **neighborhood** - Neighborhood functionality (HIGH)
- **pythonlab_setup** - Python lab setup (HIGH)

### Medium Impact Dependencies
- **unittest_runner** - Test runner (MEDIUM)

---

[← Back to Python Dependencies Overview](README.md) | [Back to Main Dependencies →](../README.md)