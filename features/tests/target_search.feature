# Created by Apollo at 3/8/25
Feature: Testing Target shopping cart and logged out


  Scenario: Testing is the user cart is e
    Given Open target main page
    When Click on shopping cart icon
    Then Verify cart is empty

  Scenario: verify that a logged out user can navigate to Sign In
    Given Open target main page
    When Click on sign-in button
    And Click on sign-in for right side navigation menu
    Then Verify Sign In form opened