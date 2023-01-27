import unittest
from models import Age, InvalidAgeException

class TestAge(unittest.TestCase):

    def test_should_raise_invalid_age_exception_if_age_is_negative(self):
        self.assertRaises(InvalidAgeException, lambda: Age(-20))

    def test_should_raise_invalid_age_exception_if_age_is_too_high(self):
        self.assertRaises(InvalidAgeException, lambda: Age(160))

    def test_zero_is_a_valid_age(self):
        Age(0)    

    def test_is_younger_than_returns_true_if_age_is_younger_than_other_age(self):
        self.assertTrue(Age(9).is_younger_than(Age(10)))
    
    def test_is_younger_than_returns_false_if_age_is_not_younger_than_other_age(self):
        self.assertFalse(Age(10).is_younger_than(Age(9)))

    def test_should_raise_type_error_when_constructor_argument_is_not_an_integer(self):
        self.assertRaises(TypeError, lambda: Age(10.20))
        self.assertRaises(TypeError, lambda: Age('string'))
        self.assertRaises(TypeError, lambda: Age([]))
        self.assertRaises(TypeError, lambda: Age({}))
