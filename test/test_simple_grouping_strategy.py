import unittest
from models import Income, SimpleGroupingStrategy, Student

class TestSimpleGroupingStrategy(unittest.TestCase):

    def test_females_with_names_starting_with_M_or_previous_letter_belong_to_group_A(self):
        grouping_strategy = SimpleGroupingStrategy()
        student = Student.female('Mandy')
        self.assertEqual(grouping_strategy.group_for(student), 'A')

    def test_females_with_names_starting_with_N_or_following_letter_belong_to_group_B(self):
        grouping_strategy = SimpleGroupingStrategy()
        student = Student.female('Nancy')
        self.assertEqual(grouping_strategy.group_for(student), 'B')

    def test_males_with_names_starting_with_N_or_following_letter_belong_to_group_A(self):
        grouping_strategy = SimpleGroupingStrategy()
        student = Student.male('Norman')
        self.assertEqual(grouping_strategy.group_for(student), 'A')

    def test_males_with_names_starting_with_M_or_previous_letter_belong_to_group_B(self):
        grouping_strategy = SimpleGroupingStrategy()
        student = Student.male('Mike')
        self.assertEqual(grouping_strategy.group_for(student), 'B')