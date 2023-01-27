import unittest
from models import Income

class TestIncome(unittest.TestCase):

    def test_should_recognize_incomes_higher_than_self(self):
        self.assertTrue(Income(99).is_lower_than(Income(100)))

    def test_should_raise_value_error_when_receiving_negative_amount_in_constructor(self):
        self.assertRaises(ValueError, lambda: Income(-10))
    
    def test_should_raise_type_error_when_receiving_non_numeric_argument_in_constructor(self):
        self.assertRaises(TypeError, lambda: Income('string'))
        self.assertRaises(TypeError, lambda: Income([]))
        self.assertRaises(TypeError, lambda: Income({}))