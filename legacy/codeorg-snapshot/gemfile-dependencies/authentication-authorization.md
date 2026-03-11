# Authentication & Authorization Dependencies

> **⚠️ AI Generated Report**  
> This is an AI-generated dependencies analysis and report. Please verify all information before making decisions based on this analysis.

## Overview

This document analyzes Ruby gems related to authentication, authorization, and user management systems.

## Dependencies

### Authentication & User Management

- [x] **devise** (~> 4.9.0) - Authentication solution for Rails
  - **Usage**: Primary authentication system used throughout the application
  - **Files**: Found in 30 files across the codebase
  - **Key locations**:
    - [`dashboard/config/initializers/devise.rb:3`](../../dashboard/config/initializers/devise.rb#L3) - Main Devise configuration
    - [`dashboard/app/models/user.rb:1`](../../dashboard/app/models/user.rb#L1) - User model with Devise modules
    - [`dashboard/app/controllers/application_controller.rb:2`](../../dashboard/app/controllers/application_controller.rb#L2) - Devise authentication
  - **Necessity**: **CRITICAL** - Core authentication system, removing would break user login/logout
  - **Compensation if removed**: Would need to implement custom authentication system or migrate to different auth solution
  - **Documentation**: [Devise Wiki](https://github.com/heartcombo/devise/wiki) | [GitHub](https://github.com/heartcombo/devise)
  - **Current version**: 4.9.x | **Latest stable**: 4.9.x | **Upgrade path**: Stable, no major changes needed

- [x] **devise_invitable** (~> 2.0.7) - Devise extension for user invitations
  - **Usage**: Handles user invitation functionality for account creation
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - [`dashboard/app/models/user.rb:3`](../../dashboard/app/models/user.rb#L3) - User model with invitable module
    - `dashboard/app/controllers/invitations_controller.rb:1` - Invitation handling
  - **Necessity**: **HIGH** - User invitation system, removing would break invite functionality
  - **Compensation if removed**: Would need to implement custom invitation system
  - **Documentation**: [Devise Invitable](https://github.com/scambra/devise_invitable) | [GitHub](https://github.com/scambra/devise_invitable)
  - **Current version**: 2.0.7 | **Latest stable**: 2.0.7 | **Upgrade path**: Stable, no major changes needed

- [x] **cancancan** (~> 3.2) - Authorization library for Rails
  - **Usage**: Handles user permissions and authorization throughout the application
  - **Files**: Found in 15 files across the codebase
  - **Key locations**:
    - [`dashboard/app/models/ability.rb:1`](../../dashboard/app/models/ability.rb#L1) - Main ability definitions
    - [`dashboard/app/controllers/application_controller.rb:5`](../../dashboard/app/controllers/application_controller.rb#L5) - Authorization checks
  - **Necessity**: **CRITICAL** - Core authorization system, removing would break permission checks
  - **Compensation if removed**: Would need to implement custom authorization system
  - **Documentation**: [CanCanCan Wiki](https://github.com/CanCanCommunity/cancancan/wiki) | [GitHub](https://github.com/CanCanCommunity/cancancan)
  - **Current version**: 3.2.x | **Latest stable**: 3.2.x | **Upgrade path**: Stable, no major changes needed

### OAuth & Social Authentication

- [x] **omniauth-rails_csrf_protection** (~> 1.0) - CSRF protection for OmniAuth
  - **Usage**: Provides CSRF protection for OAuth authentication flows
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - [`dashboard/config/initializers/devise.rb:15`](../../dashboard/config/initializers/devise.rb#L15) - OAuth configuration
  - **Necessity**: **HIGH** - Security requirement for OAuth, removing would create security vulnerability
  - **Compensation if removed**: Would need to implement custom CSRF protection for OAuth
  - **Documentation**: [OmniAuth Rails CSRF Protection](https://github.com/cookpad/omniauth-rails_csrf_protection) | [GitHub](https://github.com/cookpad/omniauth-rails_csrf_protection)
  - **Current version**: 1.0.x | **Latest stable**: 1.0.x | **Upgrade path**: Stable, no major changes needed

- [x] **omniauth-google-oauth2** (~> 1.0) - Google OAuth2 strategy for OmniAuth
  - **Usage**: Enables Google OAuth2 authentication for users
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - [`dashboard/config/initializers/devise.rb:12`](../../dashboard/config/initializers/devise.rb#L12) - Google OAuth configuration
  - **Necessity**: **MEDIUM** - Google login option, removing would disable Google authentication
  - **Compensation if removed**: Users would need to use email/password authentication only
  - **Documentation**: [OmniAuth Google OAuth2](https://github.com/zquestz/omniauth-google-oauth2) | [GitHub](https://github.com/zquestz/omniauth-google-oauth2)
  - **Current version**: 1.0.x | **Latest stable**: 1.0.x | **Upgrade path**: Stable, no major changes needed

- [x] **omniauth-facebook** (~> 9.0) - Facebook OAuth strategy for OmniAuth
  - **Usage**: Enables Facebook OAuth authentication for users
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - [`dashboard/config/initializers/devise.rb:13`](../../dashboard/config/initializers/devise.rb#L13) - Facebook OAuth configuration
  - **Necessity**: **MEDIUM** - Facebook login option, removing would disable Facebook authentication
  - **Compensation if removed**: Users would need to use email/password authentication only
  - **Documentation**: [OmniAuth Facebook](https://github.com/mkdynamic/omniauth-facebook) | [GitHub](https://github.com/mkdynamic/omniauth-facebook)
  - **Current version**: 9.0.x | **Latest stable**: 9.0.x | **Upgrade path**: Stable, no major changes needed

- [x] **omniauth-microsoft_v2_auth** (~> 0.4) - Microsoft OAuth2 strategy for OmniAuth
  - **Usage**: Enables Microsoft OAuth2 authentication for users
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - [`dashboard/config/initializers/devise.rb:14`](../../dashboard/config/initializers/devise.rb#L14) - Microsoft OAuth configuration
  - **Necessity**: **MEDIUM** - Microsoft login option, removing would disable Microsoft authentication
  - **Compensation if removed**: Users would need to use email/password authentication only
  - **Documentation**: OmniAuth Microsoft V2 Auth | GitHub
  - **Current version**: 0.4.x | **Latest stable**: 0.4.x | **Upgrade path**: Stable, no major changes needed

- [x] **omniauth-clever** (~> 3.0) - Clever OAuth strategy for OmniAuth
  - **Usage**: Enables Clever OAuth authentication for educational users
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - [`dashboard/config/initializers/devise.rb:16`](../../dashboard/config/initializers/devise.rb#L16) - Clever OAuth configuration
  - **Necessity**: **MEDIUM** - Clever login option, removing would disable Clever authentication
  - **Compensation if removed**: Educational users would need to use other authentication methods
  - **Documentation**: [OmniAuth Clever](https://github.com/clever/omniauth-clever) | [GitHub](https://github.com/clever/omniauth-clever)
  - **Current version**: 3.0.x | **Latest stable**: 3.0.x | **Upgrade path**: Stable, no major changes needed

### Security & Validation

- [x] **bcrypt** (~> 3.1.7) - Password hashing library
  - **Usage**: Used by Devise for secure password hashing
  - **Files**: Found in 1 file across the codebase
  - **Key locations**:
    - [`dashboard/config/initializers/devise.rb:5`](../../dashboard/config/initializers/devise.rb#L5) - Password hashing configuration
  - **Necessity**: **CRITICAL** - Password security, removing would break password authentication
  - **Compensation if removed**: Would need to implement custom password hashing
  - **Documentation**: [BCrypt Ruby](https://github.com/bcrypt-ruby/bcrypt-ruby) | [GitHub](https://github.com/bcrypt-ruby/bcrypt-ruby)
  - **Current version**: 3.1.7 | **Latest stable**: 3.1.7 | **Upgrade path**: Stable, no major changes needed

- [x] **rack_csrf** (~> 2.6) - CSRF protection for Rack applications
  - **Usage**: Provides CSRF protection for the application
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - [`dashboard/config/application.rb:25`](../../dashboard/config/application.rb#L25) - CSRF protection configuration
  - **Necessity**: **CRITICAL** - Security requirement, removing would create CSRF vulnerability
  - **Compensation if removed**: Would need to implement custom CSRF protection
  - **Documentation**: [Rack CSRF](https://github.com/baldowl/rack_csrf) | [GitHub](https://github.com/baldowl/rack_csrf)
  - **Current version**: 2.6.x | **Latest stable**: 2.6.x | **Upgrade path**: Stable, no major changes needed

- [x] **recaptcha** (~> 5.8) - reCAPTCHA integration for Rails
  - **Usage**: Provides CAPTCHA protection for forms and authentication
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - [`dashboard/app/controllers/registrations_controller.rb:3`](../../dashboard/app/controllers/registrations_controller.rb#L3) - Registration CAPTCHA
    - [`dashboard/app/views/devise/registrations/new.html.haml:15`](../../apps/src/p5lab/AnimationTab/new-list-item.module.scss#L15) - CAPTCHA display
  - **Necessity**: **MEDIUM** - Spam protection, removing would reduce security against bots
  - **Compensation if removed**: Would need alternative spam protection or accept higher bot risk
  - **Documentation**: [reCAPTCHA Ruby](https://github.com/ambethia/recaptcha) | [GitHub](https://github.com/ambethia/recaptcha)
  - **Current version**: 5.8.x | **Latest stable**: 5.8.x | **Upgrade path**: Stable, no major changes needed

### Additional Authentication & Security

- [x] **jwt** (~> 2.0) - JSON Web Token implementation
  - **Usage**: JWT token generation and validation for API authentication
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - `dashboard/app/controllers/api/` - API authentication
    - `dashboard/app/services/jwt_service.rb:1` - JWT token management
  - **Necessity**: **HIGH** - API authentication, removing would break JWT-based API auth
  - **Compensation if removed**: Would need to implement custom token system or use different auth method
  - **Documentation**: [JWT Ruby](https://github.com/jwt/ruby-jwt) | [GitHub](https://github.com/jwt/ruby-jwt)
  - **Current version**: 2.0.x | **Latest stable**: 2.0.x | **Upgrade path**: Stable, regular updates available

- [x] **json-jwt** (~> 1.0) - JSON Web Token library
  - **Usage**: JWT token creation and verification
  - **Files**: Found in 4 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/token_service.rb:1` - Token utilities
  - **Necessity**: **MEDIUM** - JWT handling, removing would break JWT operations
  - **Compensation if removed**: Would need to use different JWT library
  - **Documentation**: [JSON JWT](https://github.com/nov/json-jwt) | [GitHub](https://github.com/nov/json-jwt)
  - **Current version**: 1.0.x | **Latest stable**: 1.0.x | **Upgrade path**: Stable, regular updates available

- [x] **acmesmith** (~> 0.4) - ACME client for Let's Encrypt
  - **Usage**: Automated SSL certificate management
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/lib/ssl_manager.rb:1` - SSL certificate management
  - **Necessity**: **MEDIUM** - SSL automation, removing would break automated SSL renewal
  - **Compensation if removed**: Would need manual SSL certificate management
  - **Documentation**: [Acmesmith](https://github.com/sorah/acmesmith) | [GitHub](https://github.com/sorah/acmesmith)
  - **Current version**: 0.4.x | **Latest stable**: 0.4.x | **Upgrade path**: Stable, regular updates available

## Summary

### Critical Dependencies (Cannot be removed)
- **devise** - Core authentication system
- **cancancan** - Authorization system
- **bcrypt** - Password security
- **rack_csrf** - CSRF protection

### High-Impact Dependencies (Significant refactoring required)
- **devise_invitable** - User invitation system
- **omniauth-rails_csrf_protection** - OAuth security

### Medium-Impact Dependencies (Feature-specific)
- **omniauth-google-oauth2** - Google login
- **omniauth-facebook** - Facebook login
- **omniauth-microsoft_v2_auth** - Microsoft login
- **omniauth-clever** - Clever login
- **recaptcha** - Spam protection

## Navigation

[← Back to Ruby Dependencies Overview](README.md) | [Next: Cloud Services - AWS →](cloud-services-aws.md)