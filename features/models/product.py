class Product(object):
    def __init__(self, i_product_name):
        self.__m_product_name = i_product_name

    @property
    def name(self) -> str:
        return self.__m_product_name
