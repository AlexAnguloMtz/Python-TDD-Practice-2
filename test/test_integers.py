import unittest
from utils import Integers

class TestIntegers(unittest.TestCase):

    def test_is_even_should_return_true_if_integer_is_even(self):
        self.assertTrue(Integers.is_even(10))

    def test_is_even_should_return_false_if_integer_is_odd(self):
        self.assertFalse(Integers.is_even(9))

    def test_should_raise_type_error_if_input_is_not_an_integer(self):
        invalid_inputs = [10.5, 'string', [], {}]
        for element in invalid_inputs:
            self.assertRaises(TypeError, lambda: Integers.is_even(element))


