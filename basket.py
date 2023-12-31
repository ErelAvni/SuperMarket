from inventory import Inventory
from product_manager import ProductManager
from product import Product


class Basket(ProductManager):
    sm_inv = Inventory()

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
        if Basket.sm_inv.find_product(prod) == -1:
            return
        if Basket.sm_inv.get_products()[Basket.sm_inv.find_product_index(prod)].get_amount() == 0:
            return
        if Basket.sm_inv.get_products()[Basket.sm_inv.find_product_index(prod)].get_amount() < prod.get_amount():
            max_prod = Product(prod.get_item(), Basket.sm_inv.get_products()[Basket.sm_inv.find_product_index(prod)].get_amount())
            self.__products.append(max_prod)
            Basket.sm_inv.remove_product(prod)
            return
        super().add_product(prod)
        Basket.sm_inv.get_products()[Basket.sm_inv.find_product(prod)].set_amount(Basket.sm_inv.get_products()[Basket.sm_inv.find_product(prod)].get_amount() - prod.get_amount())

    def remove_product(self, prod):
        super().remove_product(prod)
        if Basket.sm_inv.find_product == -1:
            sm.add_product(prod)
            return
        num = Basket.sm_inv.get_products()[find_product_index(prod)].get_amount()
        Basket.sm_inv.get_products()[find_product_index(prod)].set_amount(num + prod.get_amount())

    def calc_total_price(self):
        total = 0
        for i in range(len(self.__products)):
            total += self.__products[i].calc_price()
        return total

    def __str__(self):
        return "basket contains: \n" + super().__str__()
