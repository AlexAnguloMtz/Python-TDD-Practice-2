from abc import ABC, abstractmethod

class TaxStrategy(ABC):

    @abstractmethod
    def should_pay_taxes(self, age, monthly_income):
        pass