from replit import clear
from day9_art import logo

def find_highest_bid(bidders):
    top_bidder = ""
    top_bid = 0
    for bidder in bidders:
        if top_bid < bidders[bidder]:
            top_bidder = bidder
            top_bid = bidders[bidder]
    print(f"The winner is {top_bidder} with a bid of ${top_bid}.")

def get_bids(bidders):
    more_bidders = True
    while more_bidders:
        name = input("What is your name? ")
        bid = int(input("What's your bid? $"))
        bidders[name] = bid
        more = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if more == "yes":
            clear()
        elif more == "no":
            more_bidders = False
            clear()
            find_highest_bid(bidders)

bidders = {}
print(logo)
print("Welcome to the secret auction program")
get_bids(bidders)