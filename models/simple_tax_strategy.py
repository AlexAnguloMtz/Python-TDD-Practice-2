from models import Age, Income
from .tax_strategy import TaxStrategy

class SimpleTaxStrategy(TaxStrategy):

    _MINIMUM_AGE_TO_PAY_TAX = Age(18)
    _MINIMUM_INCOME_TO_PAY_TAX = Income(15000)

    def should_pay_taxes(self, age, monthly_income):
        if (not isinstance(age, Age)):
            raise TypeError(f'Expected Age object, was {type(age).__name__}')
        if (not isinstance(monthly_income, Income)):
            raise TypeError(f'Expected Income object, was {type(income).__name__}')
        
        return not age.is_younger_than(SimpleTaxStrategy._MINIMUM_AGE_TO_PAY_TAX) \
            and not monthly_income.is_lower_than(SimpleTaxStrategy._MINIMUM_INCOME_TO_PAY_TAX) 