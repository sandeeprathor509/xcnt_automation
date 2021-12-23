@web
Feature: This is an XCNT web ui automation
  Basic scenarios will be covered like creation, deletion and verification of the user

  Scenario: Verify the user home screen before user creation
    Given Launch the browser
    Then Validate the page title
    And Verify the visibility of elements on the user home screen before user creation

  Scenario: Verify the create new user flow and user home screen after creating a user
    Given Launch the browser
    Then Click on the create user button
    And Enter the details of the user
    Then Click on the submit button
    And Verify the visibility of elements on the user home screen
    And Click on the delete button

  Scenario: Verify the details created for a user
    Given Launch the browser
    Then Click on the create user button
    And Enter the details of the user
    Then Click on the submit button
    Then Validate the created user detail on the home screen
    And Click on the delete button

  Scenario: Validate the error messages on the user creation page
    Given Launch the browser
    Then Click on the create user button
    Then Click on the submit button
    And Verify the validation message on the user creation page

  Scenario: Verify the user creation screen
    Given Launch the browser
    Then Click on the create user button
    And Verify the visibility of the elements on the user creation screen

  Scenario Outline: Validate the email creation with wrong input
    Given Launch the browser
    Then Click on the create user button
    And Validate the user info as <firstname>, <lastname> and <email>
    Then Validate the invalid email error

    Examples:
      | firstname | lastname | email        |
      | 1         | 2        | invalid      |
      | .         | .        | invalid@.com |