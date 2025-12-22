
text = "Python"

fixed_length = text.ljust(20)

variable_length = text

with open("strings.txt", "w") as file:
    file.write(fixed_length + "\n")
    file.write(variable_length + "\n")


with open("strings.txt", "r") as file:
    fixed_read = file.readline().strip("\n")
    variable_read = file.readline().strip("\n")

print(f"Fixed length storage: '{fixed_read}' ({len(fixed_read.encode())} bytes)")
print(f"Variable length storage: '{variable_read}' ({len(variable_read.encode())} bytes)")