
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll Number: {self.roll}")

students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for student {i + 1}:")
    name = input("Enter name: ")
    roll = input("Enter roll number: ")

    students.append(Student(name, roll))

print("\nStudent Details:")
for student in students:
    student.display()