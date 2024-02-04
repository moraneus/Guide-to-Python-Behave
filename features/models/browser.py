from features.models.cart import Cart


class Browser:
    def __init__(self):
        self.__m_cart = Cart()
        print("Browser started")

    def visit_product_page(self):
        print("In product page")

    def add_product_to_cart(self, product: str):
        self.__m_cart.add_product_to_cart(product)

    def get_cart_contents(self) -> list:
        return self.__m_cart.cart

    def quit(self):
        print("Exit browser")




