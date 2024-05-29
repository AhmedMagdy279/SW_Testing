Feature: Checkout process

  Scenario: Checkout an item as a registered user
    Given I am on the homepage
    When I add an item to the cart
    And I go to the cart
    And I click on checkout
    And I log in with valid credentials
    Then I should be able to complete the checkout process