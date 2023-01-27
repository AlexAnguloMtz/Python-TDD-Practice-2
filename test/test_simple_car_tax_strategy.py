import unittest
from models import Car, SimpleCarTaxStrategy

class TestSimpleCarTaxStrategy(unittest.TestCase):

    def test_calculates_taxes_correctly(self):
        
        countries_taxes_dictionary = {
            'Germany': 20,
            'Japan': 30,
            'Italy': 15,
            'USA': 8
        }

        car_tax_strategy = SimpleCarTaxStrategy(countries_taxes_dictionary)

        self.assertEqual(120, car_tax_strategy.total_cost_with_taxes(Car('Ford', 100, 'Germany')))
        self.assertEqual(130, car_tax_strategy.total_cost_with_taxes(Car('Ford', 100, 'Japan')))
        self.assertEqual(115, car_tax_strategy.total_cost_with_taxes(Car('Ford', 100, 'Italy')))
        self.assertEqual(108, car_tax_strategy.total_cost_with_taxes(Car('Ford', 100, 'USA')))




