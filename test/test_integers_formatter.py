import unittest
from formatters import IntegersFormatter

class TestIntegerFormatter(unittest.TestCase):

    def test_should_return_even_is_integer_is_even(self):
        self.assertEqual('even', IntegersFormatter.format_even_or_odd(10))

    def test_should_return_odd_is_integer_is_odd(self):
        self.assertEqual('odd', IntegersFormatter.format_even_or_odd(9))

