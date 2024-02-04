from features.models.browser import Browser
from features.models.cart import Cart


def before_all(context):
    context.browser = Browser()
    context.cart = Cart()


def after_all(context):
    # Clean up and close the browser window after tests are done
    context.browser.quit()
