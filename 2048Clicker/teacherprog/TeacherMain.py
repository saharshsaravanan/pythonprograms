from Teacher import Teacher
from openpyxl import Workbook
teacherlist = []
choice = True
while choice:
    name = input("Enter teacher's name")
    salary = input(f"Enter {name}'s salary")
    gender = input(f"Enter {name}'s  gender")
    teacher = Teacher(name , salary, gender)
    teacherlist.append(teacher)
    choice = input("DO you want to continue? (yes/no)")
    if not choice == "yes":
        choice = False




def write_excel(teacherlist):
    wb = Workbook()
    ws = wb.create_sheet()
    ws.append(["Name", "Salary", "Gender"])
    for teacher in teacherlist:
        ws.append([teacher.name, teacher.salary, teacher.gender])
    wb.save("C:/Users/email/pythonoutput/teacher.xlsx")

write_excel(teacherlist)










