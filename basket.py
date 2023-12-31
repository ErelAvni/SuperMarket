from inventory import Inventory
from product_manager import ProductManager


class Basket(ProductManager):
    sm_inv = Inventory()
    def __init__(self):
        super().__init__()

    def get_products(self):
        return super().get_products()

    def find_product(self, product):
        if product not in Basket.sm_inv:
            return False
        return super().find_product(product)

    def add_new_product(self, product):
        if product not in Basket.sm_inv:
            return
        if Basket.sm_inv[product.get_id()].get_amount() == 0:
            return
        super().add_new_product(product)

    def change_product_amount(self, product, amount):
        super().change_product_amount(product, Basket.sm_inv[product.get_item().get_id()].amount - amount)
        if Basket.sm_inv[product.get_item().get_id()].set_amount() is not None: #check if its negative. if its not - it wont enter the if statement and wont reset a bunch of unwanted things
            super().change_product_amount(product, amount - Basket.sm_inv[product.get_item().get_id()].get_amount())
            Basket.sm_inv[product.get_item().get_id()].set_amount(0)
        else:
            super().change_product_amount(product, amount)

    def remove_product(self, product):
        super().change_product_amount(product, product.get_amount())
        super().remove_product(product)

    def check_out(self):
        total = 0
        for i in range(len(self.get_products())):
            total += self.get_products()[i].calc_price()
        return total
