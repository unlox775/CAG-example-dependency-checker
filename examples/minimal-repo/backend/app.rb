# frozen_string_literal: true

require 'sinatra/base'
require 'json'
require 'multi_json'
require 'oj'
require_relative 'models/contact'
require_relative 'services/notification_service'

class App < Sinatra::Base
  configure do
    set :protection, except: [:path_traversal]
  end

  before do
    content_type :json
  end

  post '/api/contact' do
    body = JSON.parse(request.body.read)
    contact = Models::Contact.create_from_params(body)
    Services::NotificationService.notify_new_contact(contact)
    { id: contact.id, status: 'received' }.to_json
  end

  get '/api/contact/:id' do
    contact = Models::Contact.find(params[:id])
    halt 404 unless contact
    contact.to_h.to_json
  end

  get '/api/health' do
    { status: 'ok', service: 'backend' }.to_json
  end
end
