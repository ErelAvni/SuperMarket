from item import Item


class UnitItem(Item):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_price(self):
        return super().get_price()

    def get_id(self):
        return super().get_id()

    def __str__(self):
        return super().__str__()