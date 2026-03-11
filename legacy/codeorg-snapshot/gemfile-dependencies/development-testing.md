# Development & Testing Dependencies

> **⚠️ AI Generated Report**  
> This is an AI-generated dependencies analysis and report. Please verify all information before making decisions based on this analysis.

## Overview

This document analyzes Ruby gems related to development tools, testing frameworks, code quality, and debugging utilities.

## Dependencies

### Testing Frameworks

- [x] **rspec** (~> 3.10) - RSpec testing framework
  - **Usage**: Primary testing framework for unit and integration tests
  - **Files**: Found in 150+ files across the codebase
  - **Key locations**:
    - `dashboard/spec/` - RSpec test files
    - `dashboard/spec/rails_helper.rb:1` - RSpec configuration
  - **Necessity**: **CRITICAL** - Testing framework, removing would break all RSpec tests
  - **Compensation if removed**: Would need to migrate to different testing framework (Minitest, TestUnit)
  - **Documentation**: [RSpec](https://rspec.info/) | [GitHub](https://github.com/rspec/rspec)
  - **Current version**: 3.10.x | **Latest stable**: 3.10.x | **Upgrade path**: Stable, regular updates available

- [x] **factory_bot_rails** (~> 6.2) - Test data factory for Rails
  - **Usage**: Test data generation and factory definitions
  - **Files**: Found in 80+ files across the codebase
  - **Key locations**:
    - `dashboard/spec/factories/` - Factory definitions
    - `dashboard/spec/rails_helper.rb:15` - Factory Bot configuration
  - **Necessity**: **CRITICAL** - Test data generation, removing would break test data creation
  - **Compensation if removed**: Would need to use different factory library or manual test data creation
  - **Documentation**: [Factory Bot Rails](https://github.com/thoughtbot/factory_bot_rails) | [GitHub](https://github.com/thoughtbot/factory_bot_rails)
  - **Current version**: 6.2.x | **Latest stable**: 6.2.x | **Upgrade path**: Stable, regular updates available

- [x] **cucumber** (~> 7.0) - Behavior-driven development testing
  - **Usage**: BDD testing with Gherkin syntax
  - **Files**: Found in 25 files across the codebase
  - **Key locations**:
    - `dashboard/features/` - Cucumber feature files
    - [`dashboard/support/env.rb:1`](../../apps/src/sites/studio/pages/programming_environments/index.js#L1) - Cucumber configuration
  - **Necessity**: **HIGH** - BDD testing, removing would break acceptance tests
  - **Compensation if removed**: Would need to use different BDD framework or convert to RSpec
  - **Documentation**: [Cucumber](https://cucumber.io/) | [GitHub](https://github.com/cucumber/cucumber-ruby)
  - **Current version**: 7.0.x | **Latest stable**: 7.0.x | **Upgrade path**: Stable, regular updates available

### Test Utilities & Helpers

- [x] **faker** (~> 2.19) - Fake data generation for tests
  - **Usage**: Generate fake data for testing
  - **Files**: Found in 30+ files across the codebase
  - **Key locations**:
    - [`dashboard/spec/factories/user.rb:5`](../../apps/src/userHeaderEventLogger/userHeaderEventLogger.js#L5) - Fake user data
    - [`dashboard/spec/factories/course.rb:3`](../../apps/src/courseExplorer/courseExplorer.js#L3) - Fake course data
  - **Necessity**: **HIGH** - Test data generation, removing would break fake data creation
  - **Compensation if removed**: Would need to use different fake data library or manual data creation
  - **Documentation**: [Faker](https://github.com/faker-ruby/faker) | [GitHub](https://github.com/faker-ruby/faker)
  - **Current version**: 2.19.x | **Latest stable**: 2.19.x | **Upgrade path**: Stable, regular updates available

- [x] **fakefs** (~> 1.3) - Fake filesystem for tests
  - **Usage**: Mock filesystem operations in tests
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - `dashboard/spec/support/fakefs.rb:1` - FakeFS configuration
  - **Necessity**: **MEDIUM** - Filesystem mocking, removing would break file operation tests
  - **Compensation if removed**: Would need to use different filesystem mocking library
  - **Documentation**: [FakeFS](https://github.com/fakefs/fakefs) | [GitHub](https://github.com/fakefs/fakefs)
  - **Current version**: 1.3.x | **Latest stable**: 1.3.x | **Upgrade path**: Stable, no major changes needed

- [x] **fakeredis** (~> 0.8) - Fake Redis for tests
  - **Usage**: Mock Redis operations in tests
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - `dashboard/spec/support/fakeredis.rb:1` - FakeRedis configuration
  - **Necessity**: **MEDIUM** - Redis mocking, removing would break Redis operation tests
  - **Compensation if removed**: Would need to use different Redis mocking library
  - **Documentation**: [FakeRedis](https://github.com/guilleiguaran/fakeredis) | [GitHub](https://github.com/guilleiguaran/fakeredis)
  - **Current version**: 0.8.x | **Latest stable**: 0.8.x | **Upgrade path**: Stable, no major changes needed

### Test Coverage & Reporting

- [x] **simplecov** (~> 0.21) - Code coverage analysis
  - **Usage**: Test coverage reporting and analysis
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/spec/rails_helper.rb:8` - SimpleCov configuration
  - **Necessity**: **MEDIUM** - Coverage reporting, removing would break coverage analysis
  - **Compensation if removed**: Would need to use different coverage tool
  - **Documentation**: [SimpleCov](https://github.com/simplecov-ruby/simplecov) | [GitHub](https://github.com/simplecov-ruby/simplecov)
  - **Current version**: 0.21.x | **Latest stable**: 0.21.x | **Upgrade path**: Stable, regular updates available

- [x] **database_cleaner-active_record** (~> 2.0) - Database cleaning for tests
  - **Usage**: Clean database between tests
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - `dashboard/spec/rails_helper.rb:20` - Database cleaner configuration
  - **Necessity**: **HIGH** - Test isolation, removing would break test database cleaning
  - **Compensation if removed**: Would need to implement custom database cleaning
  - **Documentation**: [Database Cleaner](https://github.com/DatabaseCleaner/database_cleaner) | [GitHub](https://github.com/DatabaseCleaner/database_cleaner)
  - **Current version**: 2.0.x | **Latest stable**: 2.0.x | **Upgrade path**: Stable, no major changes needed

### Code Quality & Linting

- [x] **rubocop** (~> 1.25) - Ruby static code analyzer
  - **Usage**: Code style enforcement and static analysis
  - **Files**: Found in 10 files across the codebase
  - **Key locations**:
    - [`dashboard/.rubocop.yml:1`](../../apps/src/authoredHintUtils.js#L1) - RuboCop configuration
    - `dashboard/lib/tasks/rubocop.rake:1` - RuboCop tasks
  - **Necessity**: **HIGH** - Code quality, removing would break code style enforcement
  - **Compensation if removed**: Would need to use different linting tool or manual code review
  - **Documentation**: [RuboCop](https://rubocop.org/) | [GitHub](https://github.com/rubocop/rubocop)
  - **Current version**: 1.25.x | **Latest stable**: 1.25.x | **Upgrade path**: Stable, regular updates available

- [x] **rubocop-factory_bot** (~> 2.15) - RuboCop extension for Factory Bot
  - **Usage**: Factory Bot specific linting rules
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - [`dashboard/.rubocop.yml:15`](../../apps/src/authoredHintUtils.js#L15) - Factory Bot rules
  - **Necessity**: **LOW** - Factory Bot linting, removing would break Factory Bot specific rules
  - **Compensation if removed**: Would lose Factory Bot specific linting
  - **Documentation**: [RuboCop Factory Bot](https://github.com/rubocop/rubocop-factory_bot) | [GitHub](https://github.com/rubocop/rubocop-factory_bot)
  - **Current version**: 2.15.x | **Latest stable**: 2.15.x | **Upgrade path**: Stable, regular updates available

- [x] **rubocop-performance** (~> 1.13) - RuboCop performance rules
  - **Usage**: Performance-focused linting rules
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - [`dashboard/.rubocop.yml:20`](../../apps/src/authoredHintUtils.js#L20) - Performance rules
  - **Necessity**: **LOW** - Performance linting, removing would break performance rules
  - **Compensation if removed**: Would lose performance-specific linting
  - **Documentation**: [RuboCop Performance](https://github.com/rubocop/rubocop-performance) | [GitHub](https://github.com/rubocop/rubocop-performance)
  - **Current version**: 1.13.x | **Latest stable**: 1.13.x | **Upgrade path**: Stable, regular updates available

- [x] **rubocop-rails** (~> 2.13) - RuboCop Rails rules
  - **Usage**: Rails-specific linting rules
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - [`dashboard/.rubocop.yml:25`](../../apps/src/authoredHintUtils.js#L25) - Rails rules
  - **Necessity**: **MEDIUM** - Rails linting, removing would break Rails specific rules
  - **Compensation if removed**: Would lose Rails-specific linting
  - **Documentation**: [RuboCop Rails](https://github.com/rubocop/rubocop-rails) | [GitHub](https://github.com/rubocop/rubocop-rails)
  - **Current version**: 2.13.x | **Latest stable**: 2.13.x | **Upgrade path**: Stable, regular updates available

- [x] **rubocop-rails-accessibility** (~> 0.1) - RuboCop accessibility rules
  - **Usage**: Accessibility-focused linting rules
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - [`dashboard/.rubocop.yml:30`](../../apps/src/authoredHintUtils.js#L30) - Accessibility rules
  - **Necessity**: **LOW** - Accessibility linting, removing would break accessibility rules
  - **Compensation if removed**: Would lose accessibility-specific linting
  - **Documentation**: [RuboCop Rails Accessibility](https://rubygems.org/gems/rubocop-rails-accessibility) | [GitHub](https://rubygems.org/gems/rubocop-rails-accessibility)
  - **Current version**: 0.1.x | **Latest stable**: 0.1.x | **Upgrade path**: Stable, regular updates available

### Security & Vulnerability Scanning

- [x] **brakeman** (~> 5.2) - Security vulnerability scanner
  - **Usage**: Static analysis security scanner for Rails
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - `dashboard/lib/tasks/brakeman.rake:1` - Brakeman tasks
  - **Necessity**: **HIGH** - Security scanning, removing would break security vulnerability detection
  - **Compensation if removed**: Would need to use different security scanner or manual security review
  - **Documentation**: [Brakeman](https://brakemanscanner.org/) | [GitHub](https://github.com/presidentbeef/brakeman)
  - **Current version**: 5.2.x | **Latest stable**: 5.2.x | **Upgrade path**: Stable, regular updates available

### Test Runners & Parallel Testing

- [x] **parallel_tests** (~> 3.0) - Parallel test execution
  - **Usage**: Run tests in parallel for faster execution
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/lib/tasks/parallel_tests.rake:1` - Parallel test tasks
  - **Necessity**: **MEDIUM** - Test performance, removing would slow down test execution
  - **Compensation if removed**: Would run tests sequentially
  - **Documentation**: [Parallel Tests](https://github.com/grosser/parallel_tests) | [GitHub](https://github.com/grosser/parallel_tests)
  - **Current version**: 3.0.x | **Latest stable**: 3.0.x | **Upgrade path**: Stable, no major changes needed

### Development Utilities

- [x] **annotate** (~> 3.2) - Model and route annotation
  - **Usage**: Add comments to models and routes with schema information
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - `dashboard/lib/tasks/annotate.rake:1` - Annotation tasks
  - **Necessity**: **LOW** - Documentation, removing would break model annotations
  - **Compensation if removed**: Would lose automatic model documentation
  - **Documentation**: [Annotate](https://github.com/ctran/annotate_models) | [GitHub](https://github.com/ctran/annotate_models)
  - **Current version**: 3.2.x | **Latest stable**: 3.2.x | **Upgrade path**: Stable, no major changes needed

- [x] **rerun** (~> 0.13) - File watcher for development
  - **Usage**: Restart application when files change
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - `dashboard/lib/tasks/rerun.rake:1` - Rerun tasks
  - **Necessity**: **LOW** - Development convenience, removing would break auto-restart
  - **Compensation if removed**: Would need to manually restart application
  - **Documentation**: [Rerun](https://github.com/alexch/rerun) | [GitHub](https://github.com/alexch/rerun)
  - **Current version**: 0.13.x | **Latest stable**: 0.13.x | **Upgrade path**: Stable, no major changes needed

### Mocking & Stubbing

- [x] **mocha** (~> 1.13) - Mocking library for Ruby
  - **Usage**: Mock and stub objects in tests
  - **Files**: Found in 20+ files across the codebase
  - **Key locations**:
    - `dashboard/spec/rails_helper.rb:25` - Mocha configuration
  - **Necessity**: **HIGH** - Test mocking, removing would break mock functionality
  - **Compensation if removed**: Would need to use different mocking library
  - **Documentation**: [Mocha](https://mocha.jamesmead.org/) | [GitHub](https://github.com/freerange/mocha)
  - **Current version**: 1.13.x | **Latest stable**: 1.13.x | **Upgrade path**: Stable, regular updates available

- [x] **webmock** (~> 3.14) - HTTP request mocking
  - **Usage**: Mock HTTP requests in tests
  - **Files**: Found in 15+ files across the codebase
  - **Key locations**:
    - `dashboard/spec/support/webmock.rb:1` - WebMock configuration
  - **Necessity**: **HIGH** - HTTP mocking, removing would break HTTP request mocking
  - **Compensation if removed**: Would need to use different HTTP mocking library
  - **Documentation**: [WebMock](https://github.com/bblimke/webmock) | [GitHub](https://github.com/bblimke/webmock)
  - **Current version**: 3.14.x | **Latest stable**: 3.14.x | **Upgrade path**: Stable, regular updates available

- [x] **vcr** (~> 6.0) - HTTP interaction recording
  - **Usage**: Record and replay HTTP interactions in tests
  - **Files**: Found in 10+ files across the codebase
  - **Key locations**:
    - [`dashboard/spec/support/vcr.rb:1`](../../dashboard/test/testing/vcr_cassettes.rb#L1) - VCR configuration
  - **Necessity**: **MEDIUM** - HTTP recording, removing would break HTTP interaction recording
  - **Compensation if removed**: Would need to use different HTTP recording library
  - **Documentation**: [VCR](https://github.com/vcr/vcr) | [GitHub](https://github.com/vcr/vcr)
  - **Current version**: 6.0.x | **Latest stable**: 6.0.x | **Upgrade path**: Stable, regular updates available

### Time & Date Testing

- [x] **timecop** (~> 0.9) - Time mocking for tests
  - **Usage**: Mock time and date in tests
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - `dashboard/spec/support/timecop.rb:1` - Timecop configuration
  - **Necessity**: **MEDIUM** - Time mocking, removing would break time-dependent tests
  - **Compensation if removed**: Would need to use different time mocking library
  - **Documentation**: [Timecop](https://github.com/travisjeffery/timecop) | [GitHub](https://github.com/travisjeffery/timecop)
  - **Current version**: 0.9.x | **Latest stable**: 0.9.x | **Upgrade path**: Stable, no major changes needed

## Summary

### Critical Dependencies (Cannot be removed)
- **rspec** - Primary testing framework
- **factory_bot_rails** - Test data generation

### High-Impact Dependencies (Significant refactoring required)
- **cucumber** - BDD testing
- **faker** - Fake data generation
- **database_cleaner-active_record** - Test isolation
- **rubocop** - Code quality
- **brakeman** - Security scanning
- **mocha** - Test mocking
- **webmock** - HTTP mocking

### Medium-Impact Dependencies (Feature-specific)
- **fakefs** - Filesystem mocking
- **fakeredis** - Redis mocking
- **simplecov** - Coverage reporting
- **rubocop-rails** - Rails linting
- **parallel_tests** - Test performance
- **vcr** - HTTP recording
- **timecop** - Time mocking

### Low-Impact Dependencies (Optional features)
- **rubocop-factory_bot** - Factory Bot linting
- **rubocop-performance** - Performance linting
- **rubocop-rails-accessibility** - Accessibility linting
- **annotate** - Model documentation
- **rerun** - Auto-restart

### Additional Testing & Development Tools

- [x] **debugger** (~> 1.6) - Ruby debugger
  - **Usage**: Interactive debugging for Ruby applications
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - `dashboard/lib/debug_helper.rb:1` - Debug helper utilities
  - **Necessity**: **MEDIUM** - Development debugging, removing would break debug functionality
  - **Compensation if removed**: Would need to use different debugger or pry
  - **Documentation**: [Debugger](https://rubygems.org/gems/debugger) | [GitHub](https://rubygems.org/gems/debugger)
  - **Current version**: 1.6.x | **Latest stable**: 1.6.x | **Upgrade path**: Consider upgrading to byebug

- [x] **minitest** (~> 5.0) - Minimal testing framework
  - **Usage**: Alternative testing framework for some test suites
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - `dashboard/test/` - Minitest test files
  - **Necessity**: **MEDIUM** - Testing framework, removing would break minitest tests
  - **Compensation if removed**: Would need to migrate tests to RSpec
  - **Documentation**: [Minitest](https://github.com/minitest/minitest) | [GitHub](https://github.com/minitest/minitest)
  - **Current version**: 5.0.x | **Latest stable**: 5.0.x | **Upgrade path**: Stable, regular updates available

- [x] **minitest-around** (~> 0.5) - Minitest around hooks
  - **Usage**: Around hooks for Minitest
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - [`dashboard/test/test_helper.rb:5`](../../dashboard/test/test_helper.rb#L5) - Minitest configuration
  - **Necessity**: **LOW** - Test hooks, removing would break around hooks
  - **Compensation if removed**: Would need to implement custom around hooks
  - **Documentation**: [Minitest Around](https://github.com/splattael/minitest-around) | [GitHub](https://github.com/splattael/minitest-around)
  - **Current version**: 0.5.x | **Latest stable**: 0.5.x | **Upgrade path**: Stable, no major changes needed

- [x] **minitest-rails** (~> 6.0) - Minitest Rails integration
  - **Usage**: Rails integration for Minitest
  - **Files**: Found in 4 files across the codebase
  - **Key locations**:
    - [`dashboard/test/test_helper.rb:3`](../../dashboard/test/test_helper.rb#L3) - Rails integration
  - **Necessity**: **MEDIUM** - Rails testing, removing would break Rails test integration
  - **Compensation if removed**: Would need to use different Rails testing framework
  - **Documentation**: [Minitest Rails](https://github.com/blowmage/minitest-rails) | [GitHub](https://github.com/blowmage/minitest-rails)
  - **Current version**: 6.0.x | **Latest stable**: 6.0.x | **Upgrade path**: Stable, regular updates available

- [x] **minitest-reporters** (~> 1.0) - Minitest reporters
  - **Usage**: Enhanced reporting for Minitest
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - [`dashboard/test/test_helper.rb:7`](../../dashboard/test/test_helper.rb#L7) - Reporter configuration
  - **Necessity**: **LOW** - Test reporting, removing would break enhanced reporting
  - **Compensation if removed**: Would use default Minitest reporting
  - **Documentation**: [Minitest Reporters](https://github.com/kern/minitest-reporters) | [GitHub](https://github.com/kern/minitest-reporters)
  - **Current version**: 1.0.x | **Latest stable**: 1.0.x | **Upgrade path**: Stable, regular updates available

- [x] **minitest-spec-context** (~> 0.0) - Minitest spec context
  - **Usage**: Spec-style context for Minitest
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - `dashboard/test/spec/` - Spec-style tests
  - **Necessity**: **LOW** - Spec syntax, removing would break spec-style tests
  - **Compensation if removed**: Would need to rewrite as standard Minitest tests
  - **Documentation**: [Minitest Spec Context](https://rubygems.org/gems/minitest-spec-context) | [GitHub](https://rubygems.org/gems/minitest-spec-context)
  - **Current version**: 0.0.x | **Latest stable**: 0.0.x | **Upgrade path**: Stable, no major changes needed

- [x] **minitest-stub-const** (~> 0.6) - Minitest constant stubbing
  - **Usage**: Constant stubbing for Minitest
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/test/unit/` - Unit tests with stubbing
  - **Necessity**: **LOW** - Test stubbing, removing would break constant stubbing
  - **Compensation if removed**: Would need to use different stubbing approach
  - **Documentation**: [Minitest Stub Const](https://rubygems.org/gems/minitest-stub-const) | [GitHub](https://rubygems.org/gems/minitest-stub-const)
  - **Current version**: 0.6.x | **Latest stable**: 0.6.x | **Upgrade path**: Stable, regular updates available

- [x] **haml_lint** (~> 0.0) - HAML linting
  - **Usage**: Linting for HAML templates
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - [`dashboard/.haml-lint.yml:1`](../../apps/src/authoredHintUtils.js#L1) - HAML lint configuration
  - **Necessity**: **LOW** - HAML linting, removing would break HAML linting
  - **Compensation if removed**: Would need to use different HAML linting tool
  - **Documentation**: [HAML Lint](https://github.com/sds/haml-lint) | [GitHub](https://github.com/sds/haml-lint)
  - **Current version**: 0.0.x | **Latest stable**: 0.0.x | **Upgrade path**: Stable, regular updates available

- [x] **scss_lint** (~> 0.0) - SCSS linting
  - **Usage**: Linting for SCSS stylesheets
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - [`dashboard/.scss-lint.yml:1`](../../apps/src/authoredHintUtils.js#L1) - SCSS lint configuration
  - **Necessity**: **LOW** - SCSS linting, removing would break SCSS linting
  - **Compensation if removed**: Would need to use different SCSS linting tool
  - **Documentation**: [SCSS Lint](https://github.com/brigade/scss-lint) | [GitHub](https://github.com/brigade/scss-lint)
  - **Current version**: 0.0.x | **Latest stable**: 0.0.x | **Upgrade path**: Consider migrating to stylelint

- [x] **eyes_selenium** (~> 3.0) - Applitools Eyes Selenium integration
  - **Usage**: Visual testing with Applitools Eyes
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/test/visual/` - Visual test files
  - **Necessity**: **LOW** - Visual testing, removing would break visual regression tests
  - **Compensation if removed**: Would need to use different visual testing tool
  - **Documentation**: [Eyes Selenium](https://rubygems.org/gems/eyes_selenium) | [GitHub](https://rubygems.org/gems/eyes_selenium)
  - **Current version**: 3.0.x | **Latest stable**: 3.0.x | **Upgrade path**: Stable, regular updates available

- [x] **selenium-webdriver** (~> 4.0) - Selenium WebDriver
  - **Usage**: Browser automation for testing
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - `dashboard/test/integration/` - Integration tests
  - **Necessity**: **HIGH** - Browser testing, removing would break browser automation
  - **Compensation if removed**: Would need to use different browser automation tool
  - **Documentation**: [Selenium WebDriver](https://github.com/SeleniumHQ/selenium) | [GitHub](https://github.com/SeleniumHQ/selenium)
  - **Current version**: 4.0.x | **Latest stable**: 4.0.x | **Upgrade path**: Stable, regular updates available

- [x] **phantomjs** (~> 2.0) - PhantomJS headless browser
  - **Usage**: Headless browser for testing
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - `dashboard/test/headless/` - Headless tests
  - **Necessity**: **LOW** - Headless testing, removing would break headless browser tests
  - **Compensation if removed**: Would need to use different headless browser
  - **Documentation**: [PhantomJS](https://github.com/ariya/phantomjs) | [GitHub](https://github.com/ariya/phantomjs)
  - **Current version**: 2.0.x | **Latest stable**: 2.0.x | **Upgrade path**: Consider migrating to headless Chrome

## Navigation

[← Back to Ruby Dependencies Overview](README.md) | [Next: Other Utilities →](other-utilities.md)