Feature: Testing that all the UI elements on the help page are present

  Scenario: Verifying UI elements on the help page
    Given Open target help page
    Then Verify title tile is present
    And Verify search bar is present
    And Verify search bar button is present
    And Verify help boxes is present
    And Verify manage my grid boxes are present
    And Verify 2 lower grid boxes are present
    And Verify browse all Help pages text title are present