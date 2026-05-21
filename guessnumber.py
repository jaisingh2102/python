# A simple number guessing game where the user has to guess a randomly generated number between 1 and 1000.
import random

# Use a different name for the secret number to avoid overwriting the 'random' module
secret_number = random.randint(1, 1000)
attempts = 0

print("Welcome to the Guessing Game!")

while True:
    try:
        guess = int(input("Guess a number between 1 and 1000: "))
        attempts += 1 # Increment attempts for every valid number entered

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print(f"Correct! It took you {attempts} attempts.")
            break # Exit the loop when they win
            
    except ValueError:
        # This catches non-integers without crashing the program
        print("Invalid input! Please enter a whole number.")