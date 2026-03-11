# frozen_string_literal: true

require 'minitest/autorun'
require_relative '../models/contact'

class ContactTest < Minitest::Test
  def test_create_from_params
    c = Models::Contact.create_from_params(
      'id' => 'abc', 'name' => 'Jane', 'email' => 'j@x.com', 'message' => 'Hi'
    )
    assert_equal 'abc', c.id
    assert_equal 'Jane', c.name
  end
end
