import os
from datetime import date

# Ask user for diary note
note = input("Enter your diary note: ")

# Check if file already exists
if os.path.exists("diary.txt"):
    print("File already exists. Diary entry was not overwritten.")
else:
    with open("diary.txt", "w") as file:
        today = date.today()
        file.write(f"Date: {today}\n")
        file.write(note + "\n")
    print("Diary entry saved successfully.")