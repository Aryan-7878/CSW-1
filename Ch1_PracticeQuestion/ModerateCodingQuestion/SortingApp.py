number = []
while True:
    num = input("Enter a Number or 'done' to exit: ")
    if num.lower() == "done":
        break
    else:
        number.append(int(num))

number.sort()
print(number)

