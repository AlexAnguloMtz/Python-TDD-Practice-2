class Range:

    def __init__(self, low, high):
        if (high <= low):
            raise ValueError(f'Cannot create range with low value: {low} and high value: {high}')
        self._low = low
        self._high = high

    def contains(self, number):
        return number >= self._low and number <= self._high 