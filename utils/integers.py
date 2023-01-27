from .assertions import Assert

class Integers:
    
    @staticmethod
    def is_even(integer):
        Assert.is_integer(integer)
        return integer % 2 == 0