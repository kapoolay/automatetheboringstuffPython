# This is a guess the number game.

# need to come up with a random number. Use the random module for that
import random

print('Hello. What is your name?')
name = input().title()

print(f"Well, {name}, I am a thinking of a number between 1 and 20.")

## Generate a random number between 1-20 using the 'random.randint(a, b)' function
secretNumber = random.randint(1, 20)

## Debug Code to test the for loop results
# print(f"DEBUG: Secret number is {secretNumber}")

# For loop for number of guesses taken
for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low!")
    elif guess > secretNumber:
        print("Your guess is too high!")
    else:
        break   # This condition is for the correct guess

if guess == secretNumber:
    if guessesTaken > 1:
        print(f"Good job, {name}! You guessed my number in {str(guessesTaken)} guesses!")
    else:
        print((f"Good job, {name}! You guessed my number on the first try!"))
else:
    print(f"Nope. The number I was thinking of was {str(secretNumber)}.")