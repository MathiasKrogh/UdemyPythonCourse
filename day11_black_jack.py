############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from day11_art import logo
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sum_of_hand(player_hand):
    score = 0
    for card_value in player_hand:
        score += card_value
    if 21 < score and 11 in player_hand:
        player_hand[player_hand.index(11)] = 1
        score -= 10
    return score

def computer_end(computer_hand):
    forced_hit = True
    while forced_hit:
        sum = sum_of_hand(computer_hand)
        if sum == 21:
            forced_hit = False
        elif sum <= 16:
            computer_hand.append(get_extra_card())
        elif 17 <= sum and 11 in computer_hand and sum < 22:
            forced_hit = False
        else:
            forced_hit = False
    return computer_hand

def game_state(current_hands):
    human_score = sum_of_hand(current_hands["human"])
    print(f"Your cards: {current_hands["human"]}, current score: {human_score}")
    print(f"Computer's first card: {current_hands["computer"][0]}")

def start(start_hand):
    human_start = [get_extra_card(), get_extra_card()]
    computer_start = [get_extra_card(), get_extra_card()]
    start_hand["human"] = human_start
    start_hand["computer"] = computer_start
    return start_hand

def get_extra_card():
    new_card = random.choice(cards)
    return new_card

def get_winner(hands, computer_sum, human_sum):
    print(f"Your hand at the end was {hands["human"]}")
    print(f"The computers hand at the end was {hands["computer"]}")
    print(f"The computer had a sum of {computer_sum}")
    print(f"You had a sum of {human_sum}")
    if 21 < computer_sum:
        print("The computer overdrew. You win!")
    elif computer_sum == human_sum:
        print("The match drew...")
    elif human_sum < computer_sum:
        print("You lose...")
    else:
        print("You win!")

        

def new_game():
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_game == "y":
        clear()
        game()
    else:
        print("Goodbye")
        exit()

def game():
    print(logo)
    hands = {}
    hands = start(hands)
    game_state(hands)
    hit = True
    while sum_of_hand(hands["human"]) < 21 and hit:
        extra_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if extra_card == 'y':
            hands["human"].append(get_extra_card())
        else:
            hit = False
        game_state(hands)
    human_sum = sum_of_hand(hands["human"])
    if human_sum < 22:
        hands["computer"] = computer_end(hands["computer"])
        computer_sum = sum_of_hand(hands["computer"])
        get_winner(hands, computer_sum, human_sum)
    else:
        print("You overdrew. You lose...")
    new_game()

new_game()