# Ruby Dependencies

Backend API (Sinatra) for contact form submissions and health checks.

## Web Framework

- [x] **sinatra**
  - **Necessity**: **CRITICAL**
  - Web framework. Used in `backend/app.rb`, routes.

- [x] **puma**
  - **Necessity**: **CRITICAL**
  - Application server. Runs via `puma -C config.ru` or `rackup`.

- [x] **rack**
  - **Necessity**: **CRITICAL**
  - Rack interface. Required by Sinatra.

- [x] **rack-protection**
  - **Necessity**: **HIGH**
  - CSRF, XSS protection. Loaded by Sinatra.

## JSON and Serialization

- [x] **json**
  - **Necessity**: **HIGH**
  - JSON parsing. Used in `backend/app.rb` for `JSON.parse(request.body.read)`.

- [x] **multi_json**
  - **Necessity**: **MEDIUM**
  - JSON adapter abstraction. Required by some Sinatra extensions.

- [x] **oj**
  - **Necessity**: **MEDIUM**
  - Fast JSON parser. Used in `backend/app.rb`.

## Database and HTTP

- [x] **sequel**
  - **Necessity**: **HIGH**
  - ORM for database access. Used in `backend/models/contact.rb`, `db/init.rb`.

- [x] **sqlite3**
  - **Necessity**: **HIGH**
  - SQLite adapter for Sequel. Used in `backend/db/init.rb`.

- [x] **faraday**
  - **Necessity**: **MEDIUM**
  - HTTP client for notification webhooks. Used in `backend/services/notification_service.rb`.

## Utilities

- [x] **dotenv**
  - **Necessity**: **MEDIUM**
  - Load `.env` for config. Used in `backend/config.ru`.

- [x] **nokogiri**
  - **Necessity**: **LOW**
  - XML/HTML parsing for email templates. Used in `backend/services/notification_service.rb`.

## Dev and Test

- [x] **rake**
  - **Necessity**: **LOW**
  - Task runner. Used in `backend/Rakefile`.

- [x] **minitest**
  - **Necessity**: **MEDIUM**
  - Test framework. Used in `backend/test/contact_test.rb`.
