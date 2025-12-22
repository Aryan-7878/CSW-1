try:
    with open("diary.txt", "r") as file:
        print("Contents of diary.txt:")
        print(file.read())

except FileNotFoundError:
    print("File not found. Please check the name.")