Feature: Testing a product with multi-option

  Scenario: User will select colors
    Given Open multi-option product page on target for A-91511634
    #    https://www.target.com/p/A-91511634
#    When Product name Levi's Mens Carson Synthetic Leather Casual Lace Up Sneaker Shoe
    When Product name
    Then Verify user can click through colors

#  Scenario: User will select colors
#    Given Open multi-option product page on target for A-54551690
##    https://www.target.com/p/A-54551690
#    When Product name
#    Then Verify user can click through colors