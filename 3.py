# Welcome to the day 3 of my project in python. Today we'll build a Number Guessing game 

import random

secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("Guessed right!")
        break
    else:
        attempts -= 1
        print("Wrong guess. Attempts left:", attempts)

if attempts == 0:
    print("You lost! The number was:", secret_number)
