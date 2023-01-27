from utils import Assert

class Income:

    def __init__(self, amount):
        Assert.is_positive(amount)
        self._amount = amount

    def is_lower_than(self, other_income):
        if (not isinstance(other_income, Income)):
            raise TypeError(f'Expected Income object, was: {type(other_income).__name__}')
        return self.amount < other_income.amount
    
    @property
    def amount(self):
        return self._amount