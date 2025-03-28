# Created by happyfiredev at 3/27/25
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: # Enter scenario name here
    Given Open target main page
    When Click on sign-in button
    When Click on sign-in for right side navigation menu
    Then Verify Sign In form opened
    Then Input email and password on SignIn page
    And Click sign in btn on sign in
    And Open target user account page
    And Verify user is signed by url
