# Basic Command-Line Calculator

while True:
    # Prompt user for input
    user_input = input("Enter operation (add/sub/mul/div) or 'exit' to quit:\n").strip()

    # Check for exit command
    if user_input == "exit":
        print("Program terminated.")
        break

    # Split the input into parts
    parts = user_input.split()

    # Validate input format
    if len(parts) != 3:
        print("Error: Invalid input format. Use: {operation num1 num2}")
        continue

    operation, num1_str, num2_str = parts

    # Try to convert numbers to float
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("Error: Both operands must be numbers.")
        continue

    # Perform the selected operation
    if operation == "add":
        result = num1 + num2
        print(f"Result: {result}")
    elif operation == "sub":
        result = num1 - num2
        print(f"Result: {result}")
    elif operation == "mul":
        result = num1 * num2
        print(f"Result: {result}")
    elif operation == "div":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {result}")
    else:
        print("Error: Unknown operation. Use add, sub, mul, or div.")