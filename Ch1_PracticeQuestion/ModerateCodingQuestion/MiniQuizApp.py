score = 0

print("Welcome to the Mini Quiz App!")
print("Answer the following 3 questions:\n")

# Question 1
q1 = input("1) What is the capital of India? ")
if q1.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is New Delhi.")

# Question 2
q2 = input("2) Who developed Python programming language? ")
if q2.lower() == "guido van rossum":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Guido van Rossum.")

# Question 3
q3 = input("3) What is 5 * 6? ")
if q3 == "30":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 30.")

print("\nYour final score is:", score, "/ 3")
