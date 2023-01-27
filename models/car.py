from utils import Assert

class Car:

    def __init__(self, brand, cost, origin_country):
        Assert.is_not_empty(brand)
        Assert.is_positive(cost)
        Assert.is_not_empty(origin_country)
        self._brand = brand
        self._cost = cost
        self._origin_country = origin_country

    @property
    def brand(self):
        return self._brand

    @property
    def cost(self):
        return self._cost

    @property
    def origin_country(self):
        return self._origin_country