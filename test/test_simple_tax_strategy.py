import unittest
from models import SimpleTaxStrategy, Age, Income

class TestSimpleTaxStrategy(unittest.TestCase):

    def test_taxes_should_not_be_paid_by_people_under_18_years_old(self):
        self.assertFalse(SimpleTaxStrategy().should_pay_taxes(Age(17), Income(999999999)))

    def test_taxes_should_not_be_paid_by_people_who_make_less_than_15000_per_month(self):
        self.assertFalse(SimpleTaxStrategy().should_pay_taxes(Age(18), Income(14999)))

    def test_taxes_should_be_paid_by_people_over_age_18_who_also_make_15000_or_more_per_month(self):
        self.assertTrue(SimpleTaxStrategy().should_pay_taxes(Age(18), Income(15000)))


