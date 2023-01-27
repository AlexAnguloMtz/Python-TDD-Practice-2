import string

class Student:

    _MALE_FLAG = 'M'
    _FEMALE_FLAG = 'F'

    def __init__(self, name, gender):
        if (not isinstance(name, str)):
            raise ValueError(f'Expected string as a name for this student, was: {type(name).__name__}')
        if (not name):
            raise ValueError('Cannot create student without a name')
        self._name = name
        self._gender = gender
    
    @staticmethod
    def male(name):
        return Student(name, Student._MALE_FLAG)

    @staticmethod
    def female(name):
        return Student(name, Student. _FEMALE_FLAG)

    def is_male(self):
        return self._gender == Student._MALE_FLAG

    def is_female(self):
        return self._gender == Student._FEMALE_FLAG

    @property
    def name(self):
        return string.capwords(self._name)