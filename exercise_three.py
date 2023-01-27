'''
The students in a class were divided in 2 groups: group A and B, 
according to their gender and name. 

Group A is for women with a name that starts with "M" or a previous
letter, and for men with a name that starts with "N" or a following letter. 

Group B is fot the rest of them.

Write a program that asks the user their name and gender, and print
on console which group should they join.
'''
from models import SimpleGroupingStrategy, Student

def male_gender():
    return '1'

def female_gender():
    return '2'

def genders():
    return [male_gender(), female_gender()]

def student_factories():
    return {
        male_gender(): Student.male,
        female_gender(): Student.female
    }

def ask_student_name():
    return input('Enter your name: ')

def ask_student_gender():
    return input(f'Enter your gender. {male_gender()} for male, {female_gender()} for female: ')
    
def validate_gender(gender):
    if (not gender in genders()):
        raise ValueError('Invalid gender option. Run the program again')

def create_student(name, gender):
    validate_gender(gender)
    return student_factories()[gender](name)

def final_message(student):
    return f'Your group is {SimpleGroupingStrategy().group_for(student)}'

def main():
    print(final_message(create_student(ask_student_name(), ask_student_gender())))

try:
    main()
except Exception as exception:
    print(exception)