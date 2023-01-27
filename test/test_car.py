import unittest
from models import Car

class TestCar(unittest.TestCase):

    def test_cannot_create_car_with_empty_brand(self):
        self.assertRaises(ValueError, lambda: Car('', 5000, 'Germany'))

    def test_cannot_create_car_with_negative_cost(self):
        self.assertRaises(ValueError, lambda: Car('Ford', -5000, 'Germany'))

    def test_cannot_create_car_with_cost_zero(self):
        self.assertRaises(ValueError, lambda: Car('Ford', 0, 'Germany'))

    def test_cannot_create_car_with_empty_origin_country(self):
        self.assertRaises(ValueError, lambda: Car('Ford', 5000, ''))
    
    def test_cost_can_be_an_integer(self):
        Car('Ford', 5000, 'Germany')

    def test_cost_can_be_a_float(self):
        Car('Ford', 5000.5555, 'Germany')

    def test_raises_type_error_when_brand_is_not_a_string(self):
        invalid_brands = [100, 100.100, [], {}]
        for invalid_brand in invalid_brands:
            self.assertRaises(TypeError, lambda: Car(invalid_brand, 5000, 'Germany'))

    def test_raises_type_error_when_cost_is_not_a_number(self):
        invalid_costs = ['string', [], {}]
        for invalid_cost in invalid_costs:
            self.assertRaises(TypeError, lambda: Car('Ford', invalid_cost, 'Germany'))

    def test_raises_type_error_when_origin_country_is_not_a_string(self):
        invalid_origin_countries = [100, 100.100, [], {}]
        for invalid_origin_country in invalid_origin_countries:
            self.assertRaises(TypeError, lambda: Car('Ford', 5000, invalid_origin_country))


