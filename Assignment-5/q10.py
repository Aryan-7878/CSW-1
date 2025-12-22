import pickle


students = {
    "Alice": (20, "A"),
    "Bob": (19, "B"),
    "Charlie": (21, "A")
}


with open("students.pkl", "wb") as file:
    pickle.dump(students, file)

print("Pickled data saved successfully.")


with open("students.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print("Unpickled data:", loaded_data)