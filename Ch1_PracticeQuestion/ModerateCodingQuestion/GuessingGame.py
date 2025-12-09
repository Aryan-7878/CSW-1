import random

comp_guess = random.randint(0,9)
while True:
    user_guess = int(input("Guess the Number: "))
    if user_guess == comp_guess:
        print("You Won !!!!!")
        break
    else:
        print("Oops! Try Again")