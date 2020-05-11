Feature: Cucumber Basket

  @cucumber-basket
  Scenario Outline: Add cucumbers
    Given the basket has “<initial>” cucumbers
    When "<more>" cucumbers are added to the basket
    Then the basket contains "<total>" cucumbers

    Examples: Cucumber Counts
      | initial | more | total |
      |    0    |   1  |   1   |
      |    1    |   2  |   3   |
      |    5    |   4  |   9   |
