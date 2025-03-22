Feature: Main page UI test

  Scenario: Verify header links has at lest 1 link
    Given Open target main page
    Then Verify at least 1 link shown


  Scenario: Verify all header links are shown
    Given Open target main page
    Then Verify 6 links shown