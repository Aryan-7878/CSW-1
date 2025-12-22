
with open("sample.txt", "w") as file:
    file.write("Hello Python World!")

with open("sample.txt", "r") as file:
    first_part = file.read(10)
    print("First 10 characters:", first_part)
    file.seek(0)

    # Read the full file
    full_content = file.read()
    print("Full file contents after seek():", full_content)