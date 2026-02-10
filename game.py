"""
NAME:Justin Muriithi N
REG NO: BSCIT-05-0071/2024
GUESSING GAME
"""

import random

winning_number = random.randint(1, 10) #generates number between 1 and 10
guess = 3

while guess != winning_number:
    guess = int(input("Guess the number (1–10): "))

    if guess < winning_number:
        print("Too low")
    elif guess > winning_number:
        print("Too high")
    else:
        print("YOU WIN !!!!")
