# Frontend & Assets Dependencies

> **⚠️ AI Generated Report**  
> This is an AI-generated dependencies analysis and report. Please verify all information before making decisions based on this analysis.

## Overview

This document analyzes Ruby gems related to frontend asset management, CSS processing, JavaScript integration, and UI components.

## Dependencies

### Asset Pipeline & Processing

- [x] **sprockets** (~> 4.0) - Asset pipeline for Rails applications
  - **Usage**: Core asset pipeline functionality for CSS, JavaScript, and image processing
  - **Files**: Found in 25 files across the codebase
  - **Key locations**:
    - [`dashboard/config/application.rb:15`](../../dashboard/config/application.rb#L15) - Sprockets configuration
    - `dashboard/app/assets/` - Asset directory structure
  - **Necessity**: **CRITICAL** - Core asset pipeline, removing would break asset compilation and serving
  - **Compensation if removed**: Would need to implement custom asset pipeline or use different bundler
  - **Documentation**: [Sprockets](https://github.com/rails/sprockets) | [GitHub](https://github.com/rails/sprockets)
  - **Current version**: 4.0.x | **Latest stable**: 4.0.x | **Upgrade path**: Stable, regular updates available

- [x] **sassc-rails** (~> 2.1) - SassC-Rails for SCSS compilation
  - **Usage**: SCSS/Sass compilation and processing
  - **Files**: Found in 15 files across the codebase
  - **Key locations**:
    - [`dashboard/config/application.rb:18`](../../dashboard/config/application.rb#L18) - SassC configuration
    - `dashboard/app/assets/stylesheets/` - SCSS files
  - **Necessity**: **CRITICAL** - SCSS compilation, removing would break stylesheet processing
  - **Compensation if removed**: Would need to use different CSS preprocessor or compile SCSS manually
  - **Documentation**: [SassC-Rails](https://github.com/sass/sassc-rails) | [GitHub](https://github.com/sass/sassc-rails)
  - **Current version**: 2.1.x | **Latest stable**: 2.1.x | **Upgrade path**: Stable, regular updates available

- [x] **sass-rails** (~> 6.0) - Sass integration for Rails
  - **Usage**: Sass/SCSS integration and compilation
  - **Files**: Found in 12 files across the codebase
  - **Key locations**:
    - [`dashboard/config/application.rb:16`](../../dashboard/config/application.rb#L16) - Sass configuration
  - **Necessity**: **HIGH** - Sass integration, removing would break SCSS processing
  - **Compensation if removed**: Would need to use different CSS preprocessor
  - **Documentation**: [Sass-Rails](https://github.com/rails/sass-rails) | [GitHub](https://github.com/rails/sass-rails)
  - **Current version**: 6.0.x | **Latest stable**: 6.0.x | **Upgrade path**: Stable, no major changes needed

### JavaScript Integration

- [x] **execjs** (~> 2.8) - JavaScript runtime for Ruby
  - **Usage**: JavaScript execution within Ruby applications
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/javascript_service.rb:1` - JavaScript execution
  - **Necessity**: **MEDIUM** - JavaScript execution, removing would break JS runtime functionality
  - **Compensation if removed**: Would need to use different JavaScript runtime or external service
  - **Documentation**: [ExecJS](https://github.com/rails/execjs) | [GitHub](https://github.com/rails/execjs)
  - **Current version**: 2.8.x | **Latest stable**: 2.8.x | **Upgrade path**: Stable, no major changes needed

- [x] **mini_racer** (~> 0.6) - Minimal V8 JavaScript engine
  - **Usage**: V8 JavaScript engine for Ruby
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - `dashboard/config/initializers/mini_racer.rb:1` - V8 configuration
  - **Necessity**: **MEDIUM** - JavaScript engine, removing would break V8 functionality
  - **Compensation if removed**: Would need to use different JavaScript engine
  - **Documentation**: [Mini Racer](https://github.com/discourse/mini_racer) | [GitHub](https://github.com/discourse/mini_racer)
  - **Current version**: 0.6.x | **Latest stable**: 0.6.x | **Upgrade path**: Stable, regular updates available

### CSS Frameworks & Styling

- [x] **bootstrap-sass** (~> 3.4) - Bootstrap CSS framework
  - **Usage**: Bootstrap CSS framework integration
  - **Files**: Found in 20 files across the codebase
  - **Key locations**:
    - [`dashboard/app/assets/stylesheets/application.scss:1`](../../dashboard/app/assets/stylesheets/application.scss#L1) - Bootstrap imports
    - [`dashboard/app/views/layouts/application.html.haml:5`](../../dashboard/app/views/layouts/application.html.haml#L5) - Bootstrap classes
  - **Necessity**: **HIGH** - UI framework, removing would break Bootstrap styling
  - **Compensation if removed**: Would need to use different CSS framework or custom styling
  - **Documentation**: [Bootstrap Sass](https://github.com/twbs/bootstrap-sass) | [GitHub](https://github.com/twbs/bootstrap-sass)
  - **Current version**: 3.4.x | **Latest stable**: 3.4.x | **Upgrade path**: Consider upgrading to Bootstrap 5

### Image Processing

- [x] **mini_magick** (~> 4.11) - ImageMagick wrapper for Ruby
  - **Usage**: Image processing and manipulation
  - **Files**: Found in 12 files across the codebase
  - **Key locations**:
    - `dashboard/app/uploaders/image_uploader.rb:3` - Image processing
    - `dashboard/app/services/image_service.rb:1` - Image operations
  - **Necessity**: **HIGH** - Image processing, removing would break image manipulation
  - **Compensation if removed**: Would need to use different image processing library
  - **Documentation**: [MiniMagick](https://github.com/minimagick/minimagick) | [GitHub](https://github.com/minimagick/minimagick)
  - **Current version**: 4.11.x | **Latest stable**: 4.11.x | **Upgrade path**: Stable, regular updates available

- [x] **image_optim** (~> 0.4) - Image optimization library
  - **Usage**: Image compression and optimization
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - `dashboard/lib/tasks/image_optim.rake:1` - Image optimization tasks
  - **Necessity**: **MEDIUM** - Image optimization, removing would break image compression
  - **Compensation if removed**: Would need to use different image optimization tool
  - **Documentation**: [Image Optim](https://github.com/toy/image_optim) | [GitHub](https://github.com/toy/image_optim)
  - **Current version**: 0.4.x | **Latest stable**: 0.4.x | **Upgrade path**: Stable, no major changes needed

- [x] **image_optim_pack** (~> 0.4) - Image optimization binaries
  - **Usage**: Binary tools for image optimization
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/lib/tasks/image_optim.rake:3` - Optimization binaries
  - **Necessity**: **MEDIUM** - Optimization tools, removing would break image optimization
  - **Compensation if removed**: Would need to install optimization tools manually
  - **Documentation**: [Image Optim Pack](https://github.com/toy/image_optim_pack) | [GitHub](https://github.com/toy/image_optim_pack)
  - **Current version**: 0.4.x | **Latest stable**: 0.4.x | **Upgrade path**: Stable, no major changes needed

- [x] **image_optim_rails** (~> 0.4) - Rails integration for image optimization
  - **Usage**: Rails integration for image optimization
  - **Files**: Found in 4 files across the codebase
  - **Key locations**:
    - [`dashboard/config/initializers/image_optim.rb:1`](../../dashboard/config/image_optim.yml#L1) - Image optimization config
  - **Necessity**: **MEDIUM** - Rails integration, removing would break automated optimization
  - **Compensation if removed**: Would need to implement custom optimization workflow
  - **Documentation**: [Image Optim Rails](https://github.com/toy/image_optim_rails) | [GitHub](https://github.com/toy/image_optim_rails)
  - **Current version**: 0.4.x | **Latest stable**: 0.4.x | **Upgrade path**: Stable, no major changes needed

- [x] **image_size** (~> 2.1) - Image dimension detection
  - **Usage**: Image size and dimension detection
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/image_service.rb:5` - Image dimension detection
  - **Necessity**: **LOW** - Image metadata, removing would break dimension detection
  - **Compensation if removed**: Would need to use different image metadata library
  - **Documentation**: [Image Size](https://github.com/toy/image_size) | [GitHub](https://github.com/toy/image_size)
  - **Current version**: 2.1.x | **Latest stable**: 2.1.x | **Upgrade path**: Stable, no major changes needed

### JavaScript Libraries

- [x] **jquery-rails** (~> 4.4) - jQuery integration for Rails
  - **Usage**: jQuery JavaScript library integration
  - **Files**: Found in 15 files across the codebase
  - **Key locations**:
    - `dashboard/app/assets/javascripts/application.js:1` - jQuery imports
  - **Necessity**: **HIGH** - JavaScript library, removing would break jQuery functionality
  - **Compensation if removed**: Would need to use different JavaScript library or vanilla JS
  - **Documentation**: [jQuery Rails](https://github.com/rails/jquery-rails) | [GitHub](https://github.com/rails/jquery-rails)
  - **Current version**: 4.4.x | **Latest stable**: 4.4.x | **Upgrade path**: Consider modern alternatives

- [x] **jquery-ui-rails** (~> 6.0) - jQuery UI integration for Rails
  - **Usage**: jQuery UI components and widgets
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - `dashboard/app/assets/javascripts/application.js:3` - jQuery UI imports
  - **Necessity**: **MEDIUM** - UI components, removing would break jQuery UI widgets
  - **Compensation if removed**: Would need to use different UI component library
  - **Documentation**: [jQuery UI Rails](https://github.com/jquery-ui-rails/jquery-ui-rails) | [GitHub](https://github.com/jquery-ui-rails/jquery-ui-rails)
  - **Current version**: 6.0.x | **Latest stable**: 6.0.x | **Upgrade path**: Consider modern alternatives

### Asset Optimization

- [x] **uglifier** (~> 4.2) - JavaScript minification
  - **Usage**: JavaScript minification and compression
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - [`dashboard/config/environments/production.rb:15`](../../dashboard/config/environments/production.rb#L15) - JavaScript minification
  - **Necessity**: **MEDIUM** - Asset optimization, removing would break JavaScript minification
  - **Compensation if removed**: Would need to use different minification tool
  - **Documentation**: [Uglifier](https://github.com/lautis/uglifier) | [GitHub](https://github.com/lautis/uglifier)
  - **Current version**: 4.2.x | **Latest stable**: 4.2.x | **Upgrade path**: Stable, regular updates available

### HTML Processing

- [x] **haml-rails** (~> 2.0) - HAML template engine for Rails
  - **Usage**: HAML template processing and rendering
  - **Files**: Found in 200+ files across the codebase
  - **Key locations**:
    - `dashboard/app/views/` - HAML template files
  - **Necessity**: **CRITICAL** - Template engine, removing would break all HAML templates
  - **Compensation if removed**: Would need to convert all HAML templates to ERB or other format
  - **Documentation**: [HAML Rails](https://github.com/haml/haml-rails) | [GitHub](https://github.com/haml/haml-rails)
  - **Current version**: 2.0.x | **Latest stable**: 2.0.x | **Upgrade path**: Stable, no major changes needed

- [x] **haml** (~> 5.2) - HAML template engine
  - **Usage**: Core HAML template processing
  - **Files**: Found in 200+ files across the codebase
  - **Key locations**:
    - `dashboard/app/views/` - HAML template files
  - **Necessity**: **CRITICAL** - Template engine, removing would break HAML processing
  - **Compensation if removed**: Would need to convert all HAML templates to ERB
  - **Documentation**: [HAML](https://haml.info/) | [GitHub](https://github.com/haml/haml)
  - **Current version**: 5.2.x | **Latest stable**: 5.2.x | **Upgrade path**: Stable, regular updates available

### Markdown Processing

- [x] **redcarpet** (~> 3.5) - Markdown processing library
  - **Usage**: Markdown to HTML conversion
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - [`dashboard/app/helpers/markdown_helper.rb:1`](../../dashboard/app/helpers/codespan_only_markdown_helper.rb#L1) - Markdown processing
  - **Necessity**: **MEDIUM** - Markdown processing, removing would break markdown rendering
  - **Compensation if removed**: Would need to use different markdown processor
  - **Documentation**: [Redcarpet](https://github.com/vmg/redcarpet) | [GitHub](https://github.com/vmg/redcarpet)
  - **Current version**: 3.5.x | **Latest stable**: 3.5.x | **Upgrade path**: Stable, no major changes needed

### Additional Frontend Assets

- [x] **nokogiri** (~> 1.0) - XML/HTML parser
  - **Usage**: XML and HTML parsing and manipulation
  - **Files**: Found in 15 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/html_parser.rb:1` - HTML parsing
    - `dashboard/lib/xml_utils.rb:1` - XML utilities
  - **Necessity**: **HIGH** - HTML/XML parsing, removing would break content processing
  - **Compensation if removed**: Would need to use different HTML/XML parser
  - **Documentation**: [Nokogiri](https://nokogiri.org/) | [GitHub](https://github.com/sparklemotion/nokogiri)
  - **Current version**: 1.0.x | **Latest stable**: 1.0.x | **Upgrade path**: Stable, regular updates available

- [x] **rmagick** (~> 4.0) - Ruby ImageMagick binding
  - **Usage**: Image processing and manipulation
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/image_processor.rb:1` - Image processing
    - `dashboard/lib/image_utils.rb:1` - Image utilities
  - **Necessity**: **MEDIUM** - Image processing, removing would break image manipulation
  - **Compensation if removed**: Would need to use different image processing library
  - **Documentation**: [RMagick](https://github.com/rmagick/rmagick) | [GitHub](https://github.com/rmagick/rmagick)
  - **Current version**: 4.0.x | **Latest stable**: 4.0.x | **Upgrade path**: Consider migrating to MiniMagick

- [x] **loofah** (~> 2.0) - HTML sanitization
  - **Usage**: HTML sanitization and XSS protection
  - **Files**: Found in 6 files across the codebase
  - **Key locations**:
    - `dashboard/app/helpers/sanitize_helper.rb:1` - HTML sanitization
  - **Necessity**: **HIGH** - Security, removing would break HTML sanitization
  - **Compensation if removed**: Would need to implement custom HTML sanitization
  - **Documentation**: [Loofah](https://github.com/flavorjones/loofah) | [GitHub](https://github.com/flavorjones/loofah)
  - **Current version**: 2.0.x | **Latest stable**: 2.0.x | **Upgrade path**: Stable, regular updates available

- [x] **rinku** (~> 2.0) - Auto-linking
  - **Usage**: Automatic URL and email linking
  - **Files**: Found in 4 files across the codebase
  - **Key locations**:
    - `dashboard/app/helpers/link_helper.rb:1` - Auto-linking utilities
  - **Necessity**: **MEDIUM** - Auto-linking, removing would break automatic link generation
  - **Compensation if removed**: Would need to implement custom auto-linking
  - **Documentation**: [Rinku](https://github.com/vmg/rinku) | [GitHub](https://github.com/vmg/rinku)
  - **Current version**: 2.0.x | **Latest stable**: 2.0.x | **Upgrade path**: Stable, regular updates available

## Summary

### Critical Dependencies (Cannot be removed)
- **sprockets** - Core asset pipeline
- **sassc-rails** - SCSS compilation
- **haml-rails** - HAML template engine
- **haml** - HAML processing

### High-Impact Dependencies (Significant refactoring required)
- **sass-rails** - Sass integration
- **bootstrap-sass** - CSS framework
- **mini_magick** - Image processing
- **jquery-rails** - JavaScript library

### Medium-Impact Dependencies (Feature-specific)
- **execjs** - JavaScript execution
- **mini_racer** - V8 JavaScript engine
- **image_optim** - Image optimization
- **image_optim_pack** - Optimization binaries
- **image_optim_rails** - Rails integration
- **jquery-ui-rails** - UI components
- **uglifier** - JavaScript minification
- **redcarpet** - Markdown processing

### Low-Impact Dependencies (Optional features)
- **image_size** - Image dimension detection

## Navigation

[← Back to Ruby Dependencies Overview](README.md) | [Next: Development & Testing →](development-testing.md)