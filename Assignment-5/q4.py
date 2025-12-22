
line_count = 0
word_count = 0
char_count = 0


with open("input.txt", "r") as file:
    for line in file:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line.strip())

print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Number of characters:", char_count)