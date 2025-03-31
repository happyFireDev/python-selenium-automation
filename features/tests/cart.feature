Feature: Cart test

  Scenario: 'Your cart is empty' message is show for empty
    Given Open target main page
    When Click on shopping cart icon
    Then Verify 'Your cart is empty' message is shown
    And Verify cart page opens

  Scenario: verify that a logged out user can navigate to sign-in
    Given Open target main page
    When Click on sign-in button
    And Click on sign-in for right side navigation menu
    Then Verify Sign In form opened
