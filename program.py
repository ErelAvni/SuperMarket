from weightItem import WeightItem, WeightUnit
from unitItem import UnitItem

if __name__ == '__main__':
    a = WeightItem("Milki", 5, WeightUnit.kg)
    b = UnitItem("Bamba", 7.99)
    print(a, b)
