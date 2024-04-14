import random
from replit import clear
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guessed_letters = []

display = []
for i in chosen_word:
    display.append("_")

print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if len(guess) == 1:
        if guess in guessed_letters:
            print(f"You've already guessed {guess}.")
        else:
            for i in range(word_length):
                letter = chosen_word[i]
                if guess == letter:
                    display[i] = letter

            if guess not in display:
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                lives -= 1
            else:
                print(f"You guessed {guess}, that's in the word.")
    else: 
        print("You have to type a single letter!")

    guessed_letters.append(guess)
    print(f"{' '.join(display)}")
    print(stages[lives])

    if lives == 0:
        end_of_game = True
        print(f"You lose... The word was {chosen_word}")
    if not "_" in display:
        end_of_game = True
        print("You guessed the word! You win!")
