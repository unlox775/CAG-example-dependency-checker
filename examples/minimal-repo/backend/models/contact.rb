# frozen_string_literal: true

require 'sequel'

module Models
  class Contact
    def self.create_from_params(params)
      new(
        id: params['id'],
        name: params['name'],
        email: params['email'],
        message: params['message'],
        submitted_at: params['submittedAt']
      )
    end

    def self.find(id)
      # Stub: would query Sequel DB
      nil
    end

    attr_reader :id, :name, :email, :message, :submitted_at

    def initialize(id:, name:, email:, message:, submitted_at: nil)
      @id = id
      @name = name
      @email = email
      @message = message
      @submitted_at = submitted_at
    end

    def to_h
      { id: id, name: name, email: email, message: message, submitted_at: submitted_at }
    end
  end
end
