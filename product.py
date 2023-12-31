from weightItem import WeightItem
from unitItem import UnitItem


class Product:
    def __init__(self, item, amount):
        self.__item = item
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        if amount <= 0:
            return 0
            self.__amount = 0
        self.__amount = amount
        return None

    def get_item(self):
        return self.__item

    def calc_price(self):
        if self.item == UnitItem(self.item):
            return self.item.get_price() * self.amount
        elif self.item == WeightItem(self.item):
            if self.item.get_weight_unit() == "kg":
                return self.item.get_price() * self.amount / 1000
            return self.item.get_price() * self.amount / 1000
