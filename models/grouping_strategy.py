from abc import ABC, abstractmethod

class GroupingStrategy(ABC):

    @abstractmethod
    def group_for(self, student):
        pass