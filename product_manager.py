from abc import ABC, abstractmethod
from product import Product
from item import Item


class ProductManager(ABC):
    @abstractmethod
    def __init__(self):
        self.__products = []

    def get_products(self):
        return self.__products

    def find_product_index(self, prod):
        id = prod.get_item().get_id()
        for i in range(len(self.__products)):
            if id == self.__products[i].get_item().get_id():
                return i
        return -1

    def find_product(self, prod):
        low, high = 0, len(self.__products) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_value = self.__products[mid].get_item().get_id()

            if mid_value == prod.get_item().get_id():
                return mid
            elif mid_value < prod.get_item().get_id():
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def add_product(self, prod):
        if self.find_product(prod) != -1:
            return
        self.__products.append(prod)

    def remove_product(self, prod):
        if self.find_product_index(prod) == -1:
            return
        del self.__products[self.find_product_index(prod)]

    def __str__(self):
        msg = ""
        for i in range(len(self.__products)):
            msg += self.__products[i].__str__() + "\n"
        return msg
