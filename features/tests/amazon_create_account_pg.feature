# Created by Apollo at 3/8/25
Feature: This feature tests the functionality and display of elements on the Amazon create account page


  Scenario: Testing that elements are displaying correctly
    Given Open Amazon creation account page
    When Enter valid data into the name and email fields
    Then Verify using amazon create page
    And Check Amazon logo
    And Check name field
    And Check email field
    And Password field
    And Password field check
    And Continue button
    And Conditions of use link
    And Privacy notice link
    And Sign-In link