# Q2: Simple Hangman game

import random

words = ["python", "shadow", "internship", "coding", "developer"]
word = random.choice(words)

guessed = []
tries = 6

print("Welcome to Hangman!")

while tries > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)

if tries == 0:
    print("You lost! Word was:", word)
