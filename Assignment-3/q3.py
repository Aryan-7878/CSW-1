# Advanced Tuple Assignment and Unpacking Demonstration

# Step 1: Prompt the user for a list of integers
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

# Step 2: Unpack the first two numbers and the rest using starred expression
first, second, *remaining = numbers

# Step 3: Display the unpacked values
print(f"First number: {first}")
print(f"Second number: {second}")
print(f"Remaining numbers: {remaining}")

# Step 4: Swap the first two numbers using tuple assignment
first, second = second, first
print(f"After swapping: First: {first}, Second: {second}")

# Step 5: Compute and display the sum of remaining numbers
sum_remaining = sum(remaining)
print(f"Sum of remaining numbers: {sum_remaining}")

# Step 6: Demonstrate unpacking where the starred variable appears in the middle
first, *middle, last = numbers
print("Unpacking Example:")
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")