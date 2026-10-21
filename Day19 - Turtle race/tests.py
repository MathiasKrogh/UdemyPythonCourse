from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()

def move_forward():
    bob.forward(5)

screen.listen()
screen.onkeypress(key="space", fun=move_forward)
screen.exitonclick()