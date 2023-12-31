from weightItem import WeightItem, WeightUnit
from unitItem import UnitItem
from product import Product
from inventory import Inventory
from basket import Basket


def get_inventory_items(file_name, path):
    sm = Inventory()
    inputs = open(f"{path}\\{file_name}.txt", 'r', encoding='utf-8-sig')
    for line in inputs:
        sep_list = line.strip().split(",")
        if len(sep_list) == 3:
            prod = Product(UnitItem(sep_list[0], float(sep_list[1])), int(sep_list[2]))
        if len(sep_list) == 4:
            prod = Product(WeightItem(sep_list[0], float(sep_list[1]), sep_list[3]), float(sep_list[2]))
        sm.add_product(prod)
    return sm


if __name__ == '__main__':
    inv = get_inventory_items("supermarket inv", "C:\\Users\\משתמש\\Documents")
    bask = Basket()
    inpt = input("type smt and type pay to pay")
    while (inpt.lower() != "pay"):
        inpt = input("type smt and type pay to pay")
        if inpt.lower() == "add_product":
            inpt = input("add a product")
            bask.add_product(inpt)#out of time if had more time would have written down an enum of every possible action and print them out
