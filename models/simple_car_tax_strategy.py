from .car_tax_strategy import CarTaxStrategy
from .car import Car

class SimpleCarTaxStrategy(CarTaxStrategy):

    def __init__(self, countries_taxes_dictionary):
        if (not isinstance(countries_taxes_dictionary, dict)):
            raise TypeError(f'Expected dictionary, was: {type(countries_taxes_dictionary).__name__}')

        self._countries_taxes_dictionary = countries_taxes_dictionary

    def total_cost_with_taxes(self, car):
        if (not isinstance(car, Car)):
            raise TypeError(f'Expected a Car, was a: {type(car).__name__}')
        
        return self._tax_amount(car) + car.cost

    def _tax_amount(self, car):
        return (self._tax_percentage(car) / 100) * car.cost 

    def _tax_percentage(self, car):
        return self._countries_taxes_dictionary[car.origin_country]
