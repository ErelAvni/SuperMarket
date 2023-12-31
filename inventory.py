from product import Product
from product_manager import ProductManager


class Inventory(ProductManager):
    def __init__(self):
        super().__init__()
        self.__products = super().get_products()

    def get_products(self):
        return super().get_products()

    def find_product_index(self, prod):
        return super().find_product_index(prod)

    def find_product(self, prod):
        return super().find_product(prod)

    def add_product(self, prod):
        super().add_product(prod)

    def remove_product(self, prod):
        super().remove_product(prod)

    def __str__(self):
        return "Supermarket inventory contains: \n" + super().__str__()
