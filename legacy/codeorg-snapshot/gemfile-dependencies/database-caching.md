# Database & Caching

> **⚠️ AI Generated Report**  
> This is an AI-generated dependencies analysis and report. Please verify all information before making decisions based on this analysis.

## Overview

This document analyzes database and caching dependencies that handle data persistence, caching, and database operations.

## Dependencies

### Primary Database
- [x] **mysql2** (>= 0.4.1) - MySQL database adapter
  - **Usage**: Primary MySQL database adapter for Rails
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - [`dashboard/config/initializers/mysql_check_index_used.rb:1`](../../dashboard/config/initializers/mysql_check_index_used.rb#L1) - MySQL index checking
    - [`dashboard/config/database.yml:1`](../../dashboard/config/database.yml#L1) - Database configuration
    - `lib/cdo/database_utils.rb:1` - Database utilities
  - **Necessity**: **CRITICAL** - Primary database adapter, removing would break database connectivity
  - **Compensation if removed**: Would need to migrate to different database or implement alternative database adapter
  - **Documentation**: [MySQL2](https://github.com/brianmario/mysql2) | [GitHub](https://github.com/brianmario/mysql2)
  - **Current version**: >= 0.4.1 | **Latest stable**: 0.5.x | **Upgrade path**: Minor version upgrade available

- [x] **pg** (1.4.6) - PostgreSQL database adapter
  - **Usage**: PostgreSQL database adapter for specific features
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - [`dashboard/config/database.yml:15`](../../dashboard/config/database.yml#L15) - PostgreSQL configuration
    - `lib/cdo/postgres_utils.rb:1` - PostgreSQL utilities
  - **Necessity**: **LOW** - Secondary database adapter, removing would require migrating PostgreSQL features
  - **Compensation if removed**: Would need to migrate PostgreSQL-specific features to MySQL or remove them
  - **Documentation**: [PG](https://github.com/ged/ruby-pg) | [GitHub](https://github.com/ged/ruby-pg)
  - **Current version**: 1.4.6 | **Latest stable**: 1.4.x | **Upgrade path**: Minor version upgrade available

### Caching Systems
- [x] **redis** (~> 4.8.1) - Redis caching system
  - **Usage**: Primary caching and session storage system
  - **Files**: Found in 19 files across the codebase
  - **Key locations**:
    - [`lib/cdo/geocoder.rb:1`](../../lib/cdo/geocoder.rb#L1) - Geocoding cache
    - [`dashboard/legacy/middleware/helpers/sharded_redis_factory.rb:1`](../../dashboard/legacy/middleware/helpers/sharded_redis_factory.rb#L1) - Redis factory
    - `lib/cdo/redis_utils.rb:1` - Redis utilities
  - **Necessity**: **HIGH** - Primary caching system, removing would require alternative caching strategy
  - **Compensation if removed**: Would need to implement alternative caching system or migrate to different cache store
  - **Documentation**: [Redis](https://github.com/redis/redis-rb) | [GitHub](https://github.com/redis/redis-rb)
  - **Current version**: ~> 4.8.1 | **Latest stable**: 5.x | **Upgrade path**: Major version upgrade available

- [x] **redis-actionpack** (5.2.0) - Redis session store for ActionPack
  - **Usage**: Redis-based session storage for Rails
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - [`dashboard/config/initializers/session_store.rb:1`](../../dashboard/config/initializers/session_store.rb#L1) - Session store configuration
    - `lib/cdo/session_management.rb:1` - Session management utilities
    - [`dashboard/config/application.rb:40`](../../dashboard/config/application.rb#L40) - Session configuration
  - **Necessity**: **HIGH** - Session storage, removing would require alternative session management
  - **Compensation if removed**: Would need to implement alternative session storage or migrate to different session store
  - **Documentation**: [Redis ActionPack](https://github.com/redis-store/redis-actionpack) | [GitHub](https://github.com/redis-store/redis-actionpack)
  - **Current version**: 5.2.0 | **Latest stable**: 5.2.0 | **Upgrade path**: Stable, no major updates expected

- [x] **redis-slave-read** (1.3.0) - Redis read from slave
  - **Usage**: Read from Redis slave for read-heavy operations
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `lib/cdo/redis_cluster.rb:1` - Redis cluster management
    - [`dashboard/config/initializers/redis.rb:1`](../../dashboard/test/lib/middlewares/redis_session_store_test.rb#L1) - Redis configuration
    - `lib/cdo/read_replica_utils.rb:1` - Read replica utilities
  - **Necessity**: **MEDIUM** - Read optimization, removing would require alternative read optimization
  - **Compensation if removed**: Would need to implement alternative read optimization or remove read replica functionality
  - **Documentation**: [Redis Slave Read](https://rubygems.org/gems/redis-slave-read) | [GitHub](https://rubygems.org/gems/redis-slave-read)
  - **Current version**: 1.3.0 | **Latest stable**: 1.3.0 | **Upgrade path**: Stable, no major updates expected

- [x] **dalli** (3.2.1) - Memcached client
  - **Usage**: Memcached client for distributed caching
  - **Files**: Found in 6 files across the codebase
  - **Key locations**:
    - `lib/cdo/memcached_utils.rb:1` - Memcached utilities
    - `dashboard/config/initializers/cache_store.rb:1` - Cache store configuration
    - `lib/cdo/distributed_cache.rb:1` - Distributed caching
  - **Necessity**: **MEDIUM** - Memcached caching, removing would require alternative caching strategy
  - **Compensation if removed**: Would need to implement alternative distributed caching or migrate to Redis-only
  - **Documentation**: [Dalli](https://github.com/petergoldstein/dalli) | [GitHub](https://github.com/petergoldstein/dalli)
  - **Current version**: 3.2.1 | **Latest stable**: 3.2.1 | **Upgrade path**: Stable, no major updates expected

- [x] **dalli-elasticache** (0.2.0) - ElastiCache support for Dalli
  - **Usage**: AWS ElastiCache support for Memcached
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - `lib/cdo/elasticache_utils.rb:1` - ElastiCache utilities
    - `dashboard/config/initializers/elasticache.rb:1` - ElastiCache configuration
  - **Necessity**: **LOW** - AWS ElastiCache integration, removing would require alternative AWS caching
  - **Compensation if removed**: Would need to implement alternative AWS caching or migrate to Redis
  - **Documentation**: [Dalli ElastiCache](https://github.com/ktheory/dalli-elasticache) | [GitHub](https://github.com/ktheory/dalli-elasticache)
  - **Current version**: 0.2.0 | **Latest stable**: 0.2.0 | **Upgrade path**: Stable, no major updates expected

### Database ORM & Extensions
- [x] **sequel** (5.68.0) - Database ORM
  - **Usage**: Alternative ORM for specific database operations
  - **Files**: Found in 12 files across the codebase
  - **Key locations**:
    - `lib/cdo/sequel_utils.rb:1` - Sequel utilities
    - `dashboard/app/models/sequel_models.rb:1` - Sequel models
    - `lib/cdo/data_migration.rb:1` - Data migration utilities
  - **Necessity**: **MEDIUM** - Alternative ORM, removing would require migrating Sequel operations
  - **Compensation if removed**: Would need to migrate Sequel operations to ActiveRecord or implement custom database access
  - **Documentation**: [Sequel](https://sequel.jeremyevans.net/) | [GitHub](https://github.com/jeremyevans/sequel)
  - **Current version**: 5.68.0 | **Latest stable**: 5.68.0 | **Upgrade path**: Stable, no major updates expected

- [x] **composite_primary_keys** (12.0.0) - Composite primary keys for ActiveRecord
  - **Usage**: Support for composite primary keys in ActiveRecord
  - **Files**: Found in 4 files across the codebase
  - **Key locations**:
    - `dashboard/app/models/concerns/composite_key.rb:1` - Composite key concerns
    - `lib/cdo/composite_key_utils.rb:1` - Composite key utilities
    - [`dashboard/app/models/level_group.rb:1`](../../apps/src/sites/studio/pages/levels/_level_group.js#L1) - Level group model
  - **Necessity**: **MEDIUM** - Composite key support, removing would require schema changes
  - **Compensation if removed**: Would need to redesign database schema or implement alternative composite key handling
  - **Documentation**: [Composite Primary Keys](https://github.com/composite-primary-keys/composite_primary_keys) | [GitHub](https://github.com/composite-primary-keys/composite_primary_keys)
  - **Current version**: 12.0.0 | **Latest stable**: 12.0.0 | **Upgrade path**: Stable, no major updates expected

- [x] **activerecord-import** (1.4.2) - Bulk import for ActiveRecord
  - **Usage**: Bulk import operations for ActiveRecord models
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - `lib/cdo/bulk_import_utils.rb:1` - Bulk import utilities
    - `dashboard/app/models/concerns/bulk_import.rb:1` - Bulk import concerns
    - `lib/cdo/data_processing.rb:1` - Data processing utilities
  - **Necessity**: **MEDIUM** - Bulk import optimization, removing would require alternative bulk operations
  - **Compensation if removed**: Would need to implement alternative bulk import or use individual record creation
  - **Documentation**: [ActiveRecord Import](https://github.com/zdennis/activerecord-import) | [GitHub](https://github.com/zdennis/activerecord-import)
  - **Current version**: 1.4.2 | **Latest stable**: 1.4.2 | **Upgrade path**: Stable, no major updates expected

- [x] **active_record_union** (1.2.1) - Union queries for ActiveRecord
  - **Usage**: Union query support for ActiveRecord
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `lib/cdo/union_query_utils.rb:1` - Union query utilities
    - `dashboard/app/models/concerns/union_queries.rb:1` - Union query concerns
    - `lib/cdo/query_optimization.rb:1` - Query optimization utilities
  - **Necessity**: **LOW** - Union query support, removing would require alternative query approaches
  - **Compensation if removed**: Would need to implement alternative query approaches or remove union functionality
  - **Documentation**: ActiveRecord Union | GitHub
  - **Current version**: 1.2.1 | **Latest stable**: 1.2.1 | **Upgrade path**: Stable, no major updates expected

- [x] **scenic** (1.5.1) - Database views for ActiveRecord
  - **Usage**: Database view support for ActiveRecord
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - `lib/cdo/database_views.rb:1` - Database view utilities
    - `dashboard/app/models/concerns/database_view.rb:1` - Database view concerns
  - **Necessity**: **LOW** - Database view support, removing would require alternative view approaches
  - **Compensation if removed**: Would need to implement alternative database views or remove view functionality
  - **Documentation**: [Scenic](https://github.com/thoughtbot/scenic) | [GitHub](https://github.com/thoughtbot/scenic)
  - **Current version**: 1.5.1 | **Latest stable**: 1.5.1 | **Upgrade path**: Stable, no major updates expected

- [x] **scenic-mysql_adapter** (1.0.0) - MySQL adapter for Scenic
  - **Usage**: MySQL-specific adapter for Scenic database views
  - **Files**: Found in 1 file across the codebase
  - **Key locations**:
    - `lib/cdo/mysql_views.rb:1` - MySQL view utilities
  - **Necessity**: **LOW** - MySQL view support, removing would require alternative MySQL view approaches
  - **Compensation if removed**: Would need to implement alternative MySQL views or remove MySQL view functionality
  - **Documentation**: [Scenic MySQL Adapter](https://github.com/thoughtbot/scenic) | [GitHub](https://github.com/thoughtbot/scenic)
  - **Current version**: 1.0.0 | **Latest stable**: 1.0.0 | **Upgrade path**: Stable, no major updates expected

- [x] **paranoia** (2.6.0) - Soft delete for ActiveRecord
  - **Usage**: Soft delete functionality for ActiveRecord models
  - **Files**: Found in 15 files across the codebase
  - **Key locations**:
    - [`dashboard/app/models/concerns/soft_delete.rb:1`](../../dashboard/app/views/inactive_user_purge_mailer/teacher_inactivity_soft_delete_warning_email.html.haml#L1) - Soft delete concerns
    - `lib/cdo/soft_delete_utils.rb:1` - Soft delete utilities
    - [`dashboard/app/models/user.rb:1`](../../dashboard/app/models/user.rb#L1) - User model with soft delete
  - **Necessity**: **HIGH** - Soft delete functionality, removing would require data migration
  - **Compensation if removed**: Would need to implement alternative soft delete or migrate to hard delete
  - **Documentation**: [Paranoia](https://rubygems.org/gems/paranoia) | [GitHub](https://rubygems.org/gems/paranoia)
  - **Current version**: 2.6.0 | **Latest stable**: 2.6.0 | **Upgrade path**: Stable, no major updates expected

### Additional Database & Caching

- [x] **acts_as_list** (~> 1.0) - ActiveRecord list functionality
  - **Usage**: Provides ordering and positioning for ActiveRecord models
  - **Files**: Found in 6 files across the codebase
  - **Key locations**:
    - [`dashboard/app/models/lesson.rb:5`](../../dashboard/app/models/lesson.rb#L5) - Lesson ordering
    - [`dashboard/app/models/script_level.rb:3`](../../dashboard/app/models/script_level.rb#L3) - Script level ordering
  - **Necessity**: **MEDIUM** - Model ordering, removing would break list functionality
  - **Compensation if removed**: Would need to implement custom ordering system
  - **Documentation**: [Acts As List](https://github.com/swanandp/acts_as_list) | [GitHub](https://github.com/swanandp/acts_as_list)
  - **Current version**: 1.0.x | **Latest stable**: 1.0.x | **Upgrade path**: Stable, regular updates available

- [x] **active_record_query_trace** (~> 1.0) - ActiveRecord query tracing
  - **Usage**: Development tool for tracing ActiveRecord queries
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - `dashboard/config/initializers/active_record_query_trace.rb:1` - Query trace configuration
  - **Necessity**: **LOW** - Development tool, removing would break query tracing
  - **Compensation if removed**: Would need to use different query analysis tool
  - **Documentation**: [ActiveRecord Query Trace](https://github.com/ruckus/active-record-query-trace) | [GitHub](https://github.com/ruckus/active-record-query-trace)
  - **Current version**: 1.0.x | **Latest stable**: 1.0.x | **Upgrade path**: Stable, no major changes needed

- [x] **active_model_serializers** (~> 0.10) - JSON serialization for ActiveModel
  - **Usage**: JSON API serialization for ActiveRecord models
  - **Files**: Found in 12 files across the codebase
  - **Key locations**:
    - `dashboard/app/serializers/` - Serializer classes
    - `dashboard/app/controllers/api/` - API controllers
  - **Necessity**: **HIGH** - API serialization, removing would break JSON API responses
  - **Compensation if removed**: Would need to implement custom serialization or use different library
  - **Documentation**: [ActiveModel Serializers](https://github.com/rails-api/active_model_serializers) | [GitHub](https://github.com/rails-api/active_model_serializers)
  - **Current version**: 0.10.x | **Latest stable**: 0.10.x | **Upgrade path**: Consider upgrading to JSON:API or Fast JSON API

## Summary

The Database & Caching section contains dependencies that handle data persistence, caching, and database operations. These dependencies are critical to the application's data management.

### Critical Dependencies
- **mysql2** - Primary database adapter (CRITICAL)
- **redis** - Primary caching system (HIGH)
- **redis-actionpack** - Session storage (HIGH)
- **paranoia** - Soft delete functionality (HIGH)

### Medium Impact Dependencies
- **sequel** - Alternative ORM (MEDIUM)
- **composite_primary_keys** - Composite key support (MEDIUM)
- **activerecord-import** - Bulk import (MEDIUM)
- **redis-slave-read** - Read optimization (MEDIUM)
- **dalli** - Memcached caching (MEDIUM)

### Low Impact Dependencies
- **pg** - PostgreSQL adapter (LOW)
- **dalli-elasticache** - ElastiCache integration (LOW)
- **active_record_union** - Union queries (LOW)
- **scenic** - Database views (LOW)
- **scenic-mysql_adapter** - MySQL views (LOW)

---

[← Back to Ruby Dependencies Overview](README.md) | [Next: Authentication & Authorization →](authentication-authorization.md)