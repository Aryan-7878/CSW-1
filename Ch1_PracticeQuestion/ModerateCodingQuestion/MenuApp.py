while True:
    print("\n===== MENU APP =====")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Result:", x + y)

    elif choice == "2":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Result:", x - y)

    elif choice == "3":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Result:", x * y)

    elif choice == "4":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        if y == 0:
            print("Error! Division by zero.")
        else:
            print("Result:", x / y)

    elif choice == "5":
        print("Exiting Menu App. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

