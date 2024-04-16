from day12_art import logo
from random import randint

chosen_number = randint(1, 100)

def set_difficulty(difficulty):
    if difficulty == "easy":
        game(10)
    elif difficulty == "hard":
        game(5)

def check_guess(guess):
    if guess < chosen_number:
        print("Too low.")
        print("Guess again.")
        return False
    elif chosen_number < guess:
        print("Too high")
        print("Guess again.")
        return False
    else:
        print(f"You got it! The answer was {chosen_number}.")
        return True

def game(turns):
    has_won = False
    while 0 < turns and not has_won:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        has_won = check_guess(guess)
        turns -= 1
    if not has_won:
        print(f"You've run out of guesses, you lose.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
set_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))