requirements = {
    "random number generation": "random module to generate a random number between 1 and 100",
    "user input handling": ["input() to get user input", "Convert it to integer", "handle invalid inputs gracefully"],
    "loops": "repeat actions until the user's guess matches the randomly selected number",
    "conditional statements": "if, elif, and else statements to provide feedback on the user's guesses",
    "end the game" : ["congratulate the user", "display the number of attempts taken"]
}

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100")

    while not guessed:
        user_input = input("Enter your guess: ")
        
        try:
            user_guess = int(user_input)
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        attempts += 1

        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")


number_guessing_game()