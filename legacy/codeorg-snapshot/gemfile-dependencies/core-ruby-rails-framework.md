# Core Ruby & Rails Framework

> **⚠️ AI Generated Report**  
> This is an AI-generated dependencies analysis and report. Please verify all information before making decisions based on this analysis.

## Overview

This document analyzes the core Ruby and Rails framework dependencies that form the foundation of the Code.org web application.

## Dependencies

### Core Framework
- [x] **rails** (~> 6.1) - Main web framework
  - **Usage**: Core web framework used throughout the application
  - **Files**: Found in 104 files across the codebase
  - **Key locations**:
    - [`dashboard/config/application.rb:3`](../../dashboard/config/application.rb#L3) - Main application configuration
    - `dashboard/bin/rails:1` - Rails executable
    - [`dashboard/config/initializers/devise.rb:3`](../../dashboard/config/initializers/devise.rb#L3) - Devise configuration
  - **Necessity**: **CRITICAL** - Core framework, removing would break entire application
  - **Compensation if removed**: Would need to rewrite entire web application using different framework
  - **Documentation**: [Rails Guides](https://guides.rubyonrails.org/) | [GitHub](https://github.com/rails/rails)
  - **Current version**: 6.1.x | **Latest stable**: 7.1.x | **Upgrade path**: Major version upgrade with breaking changes

- [x] **rails-controller-testing** (1.0.5) - Controller testing utilities
  - **Usage**: Testing utilities for Rails controllers
  - **Files**: Found in 15 files across the codebase
  - **Key locations**:
    - [`dashboard/test/controllers/registrations_controller_test.rb:1`](../../dashboard/test/controllers/registrations_controller_test.rb#L1) - Registration controller tests
    - [`dashboard/test/controllers/omniauth_callbacks_controller_test.rb:1`](../../dashboard/test/controllers/omniauth_callbacks_controller_test.rb#L1) - OAuth callback tests
    - [`dashboard/test/controllers/sections_controller_test.rb:1`](../../dashboard/test/controllers/sections_controller_test.rb#L1) - Sections controller tests
  - **Necessity**: **MEDIUM** - Testing utility, removing would require rewriting controller tests
  - **Compensation if removed**: Would need to rewrite controller tests using alternative testing approaches
  - **Documentation**: [Rails Controller Testing](https://github.com/rails/rails-controller-testing) | [GitHub](https://github.com/rails/rails-controller-testing)
  - **Current version**: 1.0.5 | **Latest stable**: 1.0.5 | **Upgrade path**: Stable, no major updates expected

### Asset Pipeline
- [x] **sprockets** (4.0.3) - Asset pipeline (custom fork)
  - **Usage**: Asset compilation and serving system
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - [`dashboard/config/application.rb:15`](../../dashboard/config/application.rb#L15) - Asset pipeline configuration
    - [`dashboard/config/initializers/assets.rb:1`](../../dashboard/config/initializers/assets.rb#L1) - Asset precompilation settings
    - [`dashboard/app/assets/config/manifest.js:1`](../../apps/src/sites/studio/pages/datasets/edit_manifest.js#L1) - Asset manifest
  - **Necessity**: **HIGH** - Core asset pipeline, removing would break asset compilation
  - **Compensation if removed**: Would need to implement alternative asset pipeline or migrate to different asset system
  - **Documentation**: [Sprockets](https://github.com/rails/sprockets) | [GitHub](https://github.com/rails/sprockets)
  - **Current version**: 4.0.3 (custom fork) | **Latest stable**: 4.0.3 | **Upgrade path**: Custom fork, updates depend on Code.org development

- [x] **sassc-rails** (2.1.2) - Sass compilation (custom fork)
  - **Usage**: Sass/SCSS compilation for stylesheets
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - [`dashboard/config/application.rb:16`](../../dashboard/config/application.rb#L16) - Sass configuration
    - [`dashboard/app/assets/stylesheets/application.scss:1`](../../dashboard/app/assets/stylesheets/application.scss#L1) - Main stylesheet
    - [`dashboard/app/assets/stylesheets/cdo.scss:1`](../../apps/src/dcdo.js#L1) - CDO specific styles
  - **Necessity**: **HIGH** - Stylesheet compilation, removing would break CSS processing
  - **Compensation if removed**: Would need to implement alternative Sass compilation or migrate to different CSS preprocessor
  - **Documentation**: [SassC Rails](https://github.com/sass/sassc-rails) | [GitHub](https://github.com/sass/sassc-rails)
  - **Current version**: 2.1.2 (custom fork) | **Latest stable**: 2.1.2 | **Upgrade path**: Custom fork, updates depend on Code.org development

### Response Handling
- [x] **responders** (3.0.1) - Response handling utilities
  - **Usage**: Standardized response handling for controllers
  - **Files**: Found in 12 files across the codebase
  - **Key locations**:
    - [`dashboard/app/controllers/application_controller.rb:3`](../../dashboard/app/controllers/application_controller.rb#L3) - Base controller
    - [`dashboard/app/controllers/sections_controller.rb:1`](../../dashboard/app/controllers/sections_controller.rb#L1) - Sections controller
    - [`dashboard/app/controllers/levels_controller.rb:1`](../../dashboard/app/controllers/levels_controller.rb#L1) - Levels controller
  - **Necessity**: **MEDIUM** - Response handling utility, removing would require updating controller responses
  - **Compensation if removed**: Would need to rewrite controller response handling or implement custom response logic
  - **Documentation**: [Responders](https://github.com/heartcombo/responders) | [GitHub](https://github.com/heartcombo/responders)
  - **Current version**: 3.0.1 | **Latest stable**: 3.0.1 | **Upgrade path**: Stable, no major updates expected

## Summary

The Core Ruby & Rails Framework section contains the essential dependencies that form the foundation of the Code.org web application. These dependencies are critical to the application's operation and would require significant refactoring to replace.

### Critical Dependencies
- **rails** - Core web framework (CRITICAL)
- **sprockets** - Asset pipeline (HIGH)
- **sassc-rails** - Stylesheet compilation (HIGH)

### Medium Impact Dependencies
- **rails-controller-testing** - Testing utilities (MEDIUM)
- **responders** - Response handling (MEDIUM)

---

[← Back to Ruby Dependencies Overview](README.md) | [Next: Ruby Version Compatibility →](ruby-version-compatibility.md)