from abc import ABC, abstractmethod


class ProductManager(ABC):
    @abstractmethod
    def __init__(self):
        self.__products = {}

    def get_products(self):
        return self.__products

    def find_product(self, product):
        keys = sorted(self.__products.keys())
        low, high = 0, len(keys) - 1
        key = product.get_id()

        while low <= high:
            mid = (low + high) // 2
            mid_key = keys[mid]

            if mid_key == key:
                return key
            elif mid_key < key:
                low = mid + 1
            else:
                high = mid - 1
        return

    def add_new_product(self, product):
        if self.find_product(product):
            return
        self.__products[product.get_item().get_id()] = product

    def change_product_amount(self, product, amount):
        if product.get_item().get_id() not in self.__products:
            return
        self.__products[product.get_item().get_id()].set_amount(amount)

    def remove_product(self, product):
        if product.get_item().get_id() not in self.__products:
            return
