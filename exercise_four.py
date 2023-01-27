"""
Write a program to ask the user the properties of 
a car (brand, origin and cost). Print the taxes that 
the buyer should pay and the final price (taxes included).

The countries and taxes to use are the following:

Country       Tax
------------------
Germany ----- 20%
Japan ------- 30%
Italy ------- 15%
USA --------- 8%
"""
from models import Car, SimpleCarTaxStrategy

def ask_car_brand():
    return input('Enter the brand of the car: ')

def ask_car_origin():
    return input('''
        Which number matches the country of your car?
        1) Germany
        2) Japan
        3) Italy
        4) USA
        '''
    )

def ask_car_cost():
    return float(input('Enter the base cost of the car: '))

def taxes_dictionary():
    return {
        'Germany': 20,
        'Japan': 30,
        'Italy': 15,
        'USA': 8
    }

def countries_input_dictionary():
    return {
        '1': 'Germany',
        '2': 'Japan',
        '3': 'Italy',
        '4': 'USA'
    }

def countries_options():
    return countries_input_dictionary().keys()
    
def validate_country_input(origin_country_input):
    if (not origin_country_input in countries_options()):
        raise ValueError('Invalid country option. Please restart the program.')
    return origin_country_input

def country_from_input(country_input):
    return countries_input_dictionary()[country_input]

def create_car():
    return Car(
        ask_car_brand(),
        ask_car_cost(),
        country_from_input(validate_country_input(ask_car_origin()))
    )

def total_cost_with_taxes(car):
    return SimpleCarTaxStrategy(taxes_dictionary()).total_cost_with_taxes(car)

def final_message(total_cost):
    return f'The total cost for your car is {total_cost}'

def main():
    print(final_message(total_cost_with_taxes(create_car())))

try:
    main()
except Exception as exception:
    print(exception)