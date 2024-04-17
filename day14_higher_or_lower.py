from day14_game_data import data
from day14_art import logo, vs
from random import choice
from replit import clear


#Start by creating two instances
def start():
    a = choice(data)
    b = choice(data)
    b = make_unique(a, b)
    return [a, b]

c = 3

#Makes sure the options are unique
def make_unique(a, b):
    while a == b:
        b = choice(data)
    return b


#Check if you guessed the highest follower count
def check_highest(score, answer, game_data):
    a_followers = game_data[0]["follower_count"]
    b_followers = game_data[1]["follower_count"]
    if answer == 'a' and b_followers < a_followers:
        return score + 1
    elif answer == 'b' and a_followers < b_followers:
        return score + 1
    else:
        return score


#Updates A = B and B = new instance
def update_game_data(game_data):
    game_data[0] = game_data[1]
    game_data[1] = make_unique(game_data[0], game_data[1])
    return game_data


#Prints game over screen
def game_end(score):
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


#Prints each r
def new_round(game_data, score):
    print(logo)
    if 0 < score:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {game_data[0]["name"]}, a {game_data[0]["description"]}, from {game_data[0]["country"]}.")
    print(vs)
    print(f"Against B: {game_data[1]["name"]}, a {game_data[1]["description"]}, from {game_data[1]["country"]}.")
    return input("Who has more followers? Type 'A' or 'B': ").lower()


#The game itself with all methods implemented
def new_game():
    game_data = start()
    score = 0
    game_over = False
    answer = new_round(game_data, score)
    while not game_over:
        old_score = score
        score = check_highest(score, answer, game_data)
        if old_score == score:
            game_over = True
        else:
            game_data = update_game_data(game_data)
            answer = new_round(game_data, score)
    game_end(score)


new_game()
