nlist = []
while True:
    name = input("Enter Name or 'done' to exit: ")
    if name.lower() == "done":
        break
    else:
        nlist.append(name)

nlist.sort()
print(nlist)