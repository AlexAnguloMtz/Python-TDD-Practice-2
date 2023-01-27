from abc import ABC, abstractmethod

class CarTaxStrategy(ABC):

    @abstractmethod
    def total_cost_with_taxes(self, car):
        pass