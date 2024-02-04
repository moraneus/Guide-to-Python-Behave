from behave import given, when, then


@given('I am on the product page')
def step_impl(context):
    context.browser.visit_product_page()


@when('I add "{product}" to the cart')
def step_impl(context, product: str):
    context.browser.add_product_to_cart(product)


@then('I should see "{product}" in the cart')
def step_impl(context, product: str):
    assert product in context.browser.get_cart_contents()

