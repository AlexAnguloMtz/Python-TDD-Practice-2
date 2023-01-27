from models import Student, GroupingStrategy

class SimpleGroupingStrategy(GroupingStrategy):

    _FIRST_GROUP = 'A'
    _SECOND_GROUP = 'B'
    
    def group_for(self, student):
        if (not isinstance(student, Student)):
            raise TypeError(f'Expected Student, was: {type(student).__name__}')
        
        return self._group_for_female(student) \
            if student.is_female() \
            else self._group_for_male(student)

    def _group_for_female(self, student):
        return SimpleGroupingStrategy._FIRST_GROUP \
            if student.name[0] <= 'M' \
            else SimpleGroupingStrategy._SECOND_GROUP

    def _group_for_male(self, student):
        return SimpleGroupingStrategy._FIRST_GROUP \
            if student.name[0] >= 'N' \
            else SimpleGroupingStrategy._SECOND_GROUP

