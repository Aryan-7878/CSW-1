
poem = [
    "Roses are red,",
    "Violets are blue,",
    "Python is fun,",
    "And so are you."
]
with open("poem.txt", "w") as file:
    for line in poem:
        file.write(line + "\n")

print("Poem written to file successfully.")

# Read the poem from the file
print("Reading back from poem.txt:")
with open("poem.txt", "r") as file:
    for line in file:
        print(line.strip())