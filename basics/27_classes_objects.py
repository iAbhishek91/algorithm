# classes helps to structure your projects
# as normal class which have some properties and methods attached


class Student:
    def __init__(self, name, major, grade, is_on_probation):
        self.name = name
        self.major = major
        self.grade = grade
        self.is_on_probation = is_on_probation

    def is_scholership(self):
        if self.grade == 'A':
            return True
        return False


abhishek = Student('abhishek', 'CS', 'B', False)
su = Student('Sutapa', 'CS', 'A', True)

print(abhishek.name)
print(abhishek.major)
print(su.grade)
print(su.is_on_probation)
print(su.is_scholership())
print(abhishek.is_scholership())
