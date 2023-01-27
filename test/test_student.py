import unittest
from models import Student

class TestStudent(unittest.TestCase):

    def test_can_create_male_student(self):
        student = Student.male('Richard')
        self.assertTrue(student.is_male())

    def test_can_create_female_student(self):
        student = Student.female('Tiffany')
        self.assertTrue(student.is_female())

    def test_males_are_not_females(self):
        student = Student.male('Richard')
        self.assertFalse(student.is_female())

    def test_females_are_not_males(self):
        student = Student.female('Tiffany')
        self.assertFalse(student.is_male())

    def test_should_always_return_capitalized_name(self):
        student = Student.female('tiFfaNy jOhNsOn')
        self.assertEqual('Tiffany Johnson', student.name)
  
    def test_cannot_create_student_with_empty_name(self):
        self.assertRaises(ValueError, lambda: Student.male(''))
        self.assertRaises(ValueError, lambda: Student.female(''))