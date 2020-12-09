from collections import OrderedDict
class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade in self.students:
            for i in range(len(self.students[grade])):
                if self.students[grade][i] >= name:
                    self.students[grade][i:i] = [name]
                    break
                elif i == len(self.students[grade])-1:
                    self.students[grade].append(name)
        else:
            self.students[grade] = [name]

    def roster(self):
        all_students = []
        for i in OrderedDict(sorted(self.students.items())):
            all_students += self.students[i]
        return all_students

    def grade(self, grade_number):
        return self.students[grade_number] if grade_number in self.students else []
