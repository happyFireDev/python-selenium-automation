Feature: User to sign in

  Scenario: Test user account signing in
    Given Open target main page
    When Click on sign-in button
    When Click on sign-in for right side navigation menu
    Then Verify Sign In form opened
    Then Input email and password on SignIn page
    And Click sign in btn on sign in
    Given Open target user account page
    Then Verify user is signed by url

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    When Click on sign-in button
    When Click on sign-in for right side navigation menu
    Then Verify Sign In form opened
    Given Store signin page from original window
    When Click on Target terms and conditions link
    And Switch to terms new window
    Then Verify Terms and Conditions page is opened
    And Close terms and conditions window
    And Switch back to signin original window