class Assert:
    
    @staticmethod
    def is_integer(tested):
        if (not isinstance(tested, int)):
            raise TypeError(f'Expected an integer, was: {type(tested).__name__}')

    @staticmethod
    def is_number(tested):
        if (not (isinstance(tested, int) or isinstance(tested, float))):
            raise TypeError(f'Expected a number, was: {tested}')

    @staticmethod
    def is_positive(tested):
        Assert.is_number(tested)
        if (tested <= 0):
            raise ValueError(f'Expected positive number, was: {tested}')

    @staticmethod
    def is_string(tested):
        if (not isinstance(tested, str)):
            raise TypeError(f'Expected string, was: {type(tested).__name__}')

    @staticmethod
    def is_not_empty(tested):
        Assert.is_string(tested)
        if (not tested.strip()):
            raise ValueError('Expected non empty string')

