from abc import ABC, abstractmethod


class Item(ABC):
    total_id = 0

    @abstractmethod
    def __init__(self, name, base_price):
        self.__id = Item.total_id + 1
        self.__name = name
        self.__base_price = base_price
        Item.total_id += 1

    def get_price(self):
        return self.__base_price

    def get_id(self):
        return self.__id

    def __str__(self):
        return f"id: {self.__id} | name: {self.__name} | price: {self.__base_price}"
