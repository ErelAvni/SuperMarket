from item import Item
from enum import Enum


class WeightUnit(Enum):
    kg = "kg"
    g = "g"


class WeightItem(Item):
    def __init__(self, name, price, weight_unit):
        super().__init__(name, price)
        self.__weight_unit = WeightUnit(weight_unit)

    def get_price(self):
        return super().get_price()

    def get_id(self):
        return super().get_id()

    def get_weight_unit(self):
        return self.__weight_unit.value

    def __str__(self):
        return super().__str__() + f" | weight units: {self.__weight_unit.value}"
