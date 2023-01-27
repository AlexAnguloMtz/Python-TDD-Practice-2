from utils import Range
from utils import Assert

class Age:

    _MINIMUM_AGE = 0
    _MAXIMUM_AGE = 150
    _VALID_AGE_RANGE = Range(_MINIMUM_AGE, _MAXIMUM_AGE)

    def __init__(self, age_years):
        Assert.is_integer(age_years)
        if (not self.is_valid_age(age_years)):
            raise InvalidAgeException(f'Invalid age: {age_years}')    
        self._value = age_years        

    def is_valid_age(self, age_years):
        return Age._VALID_AGE_RANGE.contains(age_years)

    def is_younger_than(self, other_age):
        if (not isinstance(other_age, Age)):
            raise TypeError(f'Expected an Age, was: {type(other_age).__name__}')
        return self.value < other_age.value
        
    @property
    def value(self):
        return self._value

class InvalidAgeException(Exception):
    pass
