from behave import register_type
import parse

from features.models.product import Product


@parse.with_pattern(r"[^\"].+")
def parse_product(text):
    return Product(text)


register_type(Product=parse_product)
