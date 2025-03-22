Feature: Target search test cases

#  Scenario: User can search for a tea on Target
#    Given Open target main page
#    When Search for tea
#    Then Verify correct search results shown for tea

#  Scenario: User can search for a iPhone on Target
#    Given Open target main page
#    When Search for iPhone
#    Then Verify correct search results shown for iPhone
#
#  Scenario: User can search for a dress on Target
#    Given Open target main page
#    When Search for dress
#    Then Verify correct search results shown for dress

#  Scenario Outline: User can search for a product on Target
#    Given Open target main page
#    When Search for <search_word>
#    Then Verify correct search results shown for <expected_text>
#    Examples:
#    |search_word  |expected_text  |
#    |tea          |tea            |
#    |iPhone       |iPhone         |
#    |dress        |dress          |

   Scenario: Adding target product into cart

      Given Open target main page
      When Search for tea
      Then Click on first product on search results page
      And Click add to cart in side-menu pop-up
      Given Open target shopping cart page
      Then Verify cart has 1 product(s)
