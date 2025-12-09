dict = {}
str = input("Enter a String: ")
for i in str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)