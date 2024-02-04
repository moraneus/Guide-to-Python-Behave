@shopping_cart
Feature: Shopping Cart
  As an online shopper
  I want to manage my shopping cart
  So that I can order my desired products

  Scenario Outline: Add a product to the shopping cart
    Given I am on the product page
    When I add "<product>" to the cart
    Then I should see "<product>" in the cart

    Examples:
      | product    |
      | Book       |
      | Smartphone |