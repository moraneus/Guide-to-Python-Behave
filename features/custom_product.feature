@custom_product
Feature: Custom Product

  Scenario: Adding a product with custom type
    Given I add a product "Laptop" to the cart
    Then the product should be recognized as a Product