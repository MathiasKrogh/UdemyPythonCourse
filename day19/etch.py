from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

def turn_clockwise():
    pen.right(5)

def turn_counterclockwise():
    pen.left(5)

def move_forward():
    pen.forward(5)

def move_backward():
    pen.backward(5)

def clear():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()
    
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()