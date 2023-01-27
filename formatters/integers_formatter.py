from utils import Integers

class IntegersFormatter():

    @staticmethod
    def format_even_or_odd(integer):
        return 'even' if Integers.is_even(integer) else 'odd'