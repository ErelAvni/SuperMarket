from product import Product
from product_manager import ProductManager


class Inventory(ProductManager):
    def __init__(self):
        super().__init__()

    def get_products(self):
        return super().get_products()

    def find_product(self, product):
        return super().find_product(product)

    def add_new_product(self, product):
        super().add_new_product(product)

    def change_product_amount(self, product, amount):
        super().change_product_amount(product, amount)

    def remove_product(self, product):
        super().remove_product(product)
        super().change_product_amount(product, 0)
