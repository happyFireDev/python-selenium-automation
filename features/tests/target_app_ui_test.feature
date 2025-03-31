Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store app page from original window
    When Click Privacy Policy link
    And Switch to app page new window
    Then Verify Privacy Policy page opened
    And Close pp current active page
    And Return to main app window
