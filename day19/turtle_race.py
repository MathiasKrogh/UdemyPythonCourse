from turtle import Turtle, Screen
from random import randint

colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]

def create_turtles():
    turtles = []
    i = 0
    for colour in colours:
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colour)
        new_turtle.goto(x=-230, y=-90+i)
        turtles.append(new_turtle)
        i += 30
    return turtles

def move_turtles(turtles):
    for turtle in turtles:
        turtle.forward(randint(0, 10))

def is_race_on(turtles):
    state = True
    for turtle in turtles:
        if 230 <= turtle.xcor():
            state = False
    return state

def find_winner(turtles):
    for turtle in turtles:
        if 230 <= turtle.xcor():
            winner = turtle.pencolor().lower()
            if winner == user_bet.lower():
                print(f"The {winner} turtle won, you guessed correctly!")
            else:
                print(f"The {winner} turtle won, you were wrong...")

screen = Screen()
screen.setup(width=500, height=400)
racing = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
if user_bet:
    racing = True
turtles = create_turtles()
while racing:
    move_turtles(turtles)
    racing = is_race_on(turtles)
turtle = find_winner(turtles)

screen.exitonclick()