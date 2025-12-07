# Prompt the user to enter three numbers separated by spaces
x, y, z = map(int, input("Enter three numbers separated by spaces: ").split())

# Display the values before swapping
print(f"Before swapping: x = {x}, y = {y}, z = {z}")

# Swap y and z using tuple unpacking in one line
y, z = z, y

# Display the values after swapping
print(f"After swapping: x = {x}, y = {y}, z = {z}")