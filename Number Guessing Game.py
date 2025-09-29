import random
from datetime import datetime

print("Welcome to the Number Guessing Game!" )
print("I'm thinking of a number between 1 and 100.")

while True:
    #-----Game starts-----
    number = random.randint(1, 100) # New Number for every game
    start_time = datetime.now() # Timer starts here

    print("Please Select Difficulty")
    print("1. Easy (10 Chances)")
    print("2. Medium (5 Chances)")
    print("3. Hard (3 Chances)")

    Difficulty = int(input("Enter your choice: "))

    if Difficulty == 1:
        Attempts = 10
    elif Difficulty == 2:
        Attempts = 5
    elif Difficulty == 3:
        Attempts = 3
    else:
        Attempts = 10
        print("Invalid Difficulty. Defaulting to easy")

    print("Great! You have " + str(Attempts) + " Attempts to guess the number correctly.")

    for i in range(1, Attempts+1):
        Guess = int(input("Enter your Guess: "))
        if Guess == number:
            elapsed = datetime.now() - start_time
            print("Congratulations! You guessed correctly after " + str(i) + " guesses!")
            print("Time taken: " + str(elapsed))
            break
        elif Guess < number:
            print("Incorrect! The number is greater than " + str(Guess))
        elif Guess > number:
            print("Incorrect! The number is less than " + str(Guess))
    else:
        elapsed = datetime.now() - start_time
        print("You're out of Attempts! The correct number was " + str(number))
        print("Time taken: " + str(elapsed))

    #-----Asking whether you want to go again-----
    again = input("Do you want to play again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for playing!")
        break