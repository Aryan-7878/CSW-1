
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

with open("students.txt", "w") as file:
    for name in students:
        file.write(name + "\n")

print("File 'students.txt' created successfully.")

print("Contents of the file:")
with open("students.txt", "r") as file:
    contents = file.read()
    print(contents)