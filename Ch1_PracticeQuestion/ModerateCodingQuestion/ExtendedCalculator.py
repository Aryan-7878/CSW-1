x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
op = input("Enter the Operation (+, -, *, /, //, %, **): ")

if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    if y == 0:
        print("Error! Division by zero Error")
        result = None
    else:
        result = x / y
elif op == "//":
    if y == 0:
        print("Error! Division by zero Error")
        result = None
    else:
        result = x // y
elif op == "%":
    if y == 0:
        print("Error! Division by zero Error")
        result = None
    else:
        result = x % y
elif op == "**":
    result = x ** y
else:
    print("Invalid Choice. Try Again")

print("Result:", result)
