from studentprog.Student import Student

students = []
number = 1

while True:
    name = input("please enter student name ")
    mark = int(input("please enter a number in range of 1 to 100"))
    student = Student(number, name, mark)
    students.append(student)
    decision = input("would you like to continue or quit {y or  n }").lower()
    if not decision == "y":
        break
    else:
        number+=1

print("Student summary")
for student in students:
    print(student)
print(f"student total = {Student.class_total(students)} ")

