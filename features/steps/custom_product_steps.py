from behave import given, when, then

from type_definitions import Product


@given('I add a product "{product_name:Product}" to the cart')
def step_impl(context, product_name):
    context.cart.add_product_to_cart(product_name)


@then('the product should be recognized as a Product')
def step_impl(context):
    # Check the last added product in the cart
    last_added_product = context.cart.cart[-1]
    assert isinstance(last_added_product, Product), "The object is not an instance of Product"
