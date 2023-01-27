'''
Ask the user a number and print if 
the received number is even or odd
'''
from formatters import IntegersFormatter

def final_message(integer):
    return f'The integer {integer} is {IntegersFormatter.format_even_or_odd(integer)}'

def main():
    print(final_message(int(input('Enter an integer: '))))

try:
    main()
except Exception as exception:
    print(exception)