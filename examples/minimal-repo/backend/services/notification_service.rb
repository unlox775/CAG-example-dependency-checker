# frozen_string_literal: true

require 'faraday'
require 'nokogiri'

module Services
  class NotificationService
    def self.notify_new_contact(contact)
      # Stub: would POST to webhook or enqueue job
      # Faraday.get(...) or Faraday.post(...)
      # Nokogiri used for parsing HTML in email templates
      nil
    end
  end
end
