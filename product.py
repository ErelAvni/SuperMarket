from weightItem import WeightItem
from unitItem import UnitItem


class Product:
    def __init__(self, item, amount):
        self.__item = item
        self.__amount = amount

    def get_item(self):
        return self.__item

    def get_amount(self):
        return self.__amount

    def set_item(self, item):
        self.__item = item

    def set_amount(self, amount):
        if amount <= 0:
            return 0
            self.__amount = 0
        self.__amount = amount
        return None

    def get_item(self):
        return self.__item

    def calc_price(self):
        if type(self.__item) == UnitItem:
            return self.__item.get_price() * self.__amount
        elif type(self.__item) == WeightItem:
            if self.__item.get_weight_unit() == "kg":
                return (self.__item.get_price() * self.__amount) / 1000
            if self.__item.get_weight_unit() == "g":
                return self.__item.get_price() * self.__amount * 10

    def __str__(self):
        return f"{self.__amount} {self.__item.get_name()}'s. Price: {self.calc_price()}₪"
