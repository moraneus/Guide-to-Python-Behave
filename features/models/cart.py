class Cart:
    def __init__(self):
        self.__m_cart = []

    @property
    def cart(self) -> list:
        return self.__m_cart

    def add_product_to_cart(self, product: str):
        self.__m_cart.append(product)

