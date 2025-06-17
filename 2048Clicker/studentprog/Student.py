class Student:
    def __init__(self,number,name,mark):
        self.number = number
        self.name = name
        self.mark = mark

    def __str__(self):
        return f"number = {self.number} : name = {self.name} : mark = {self.mark}"

    def class_total(self, students):
        return sum(student.mark for student in students)




