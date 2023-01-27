'''
Suppose that to pay a specific tax to the government
you must be over 18 years old and have a monthly income
of 15,000 mexican pesos. Write a program that asks the user
their age and their monthly income, and print on the console
if the user should pay this special tax or not
'''
from models import Age, Income, SimpleTaxStrategy

def ask_age():
    return Age(int(input('Enter your age: ')))

def ask_income():
    return Income(float(input('Enter your monthly income in mexican pesos: ')))

def final_message(age, monthly_income):
    return 'You should pay your taxes!' \
        if SimpleTaxStrategy.should_pay_taxes(age, monthly_income) \
        else 'You don''t need to pay taxes yet'

def main():
    print(final_message(ask_age(), monthly_income))

try:
    main()
except Exception as exception:
    print(exception)