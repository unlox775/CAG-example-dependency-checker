# frozen_string_literal: true

require 'sequel'
require 'sqlite3'

DB = Sequel.sqlite(ENV.fetch('DATABASE_URL', 'db/contacts.sqlite3'))
