import turtle as t
from random import choice, randint

colour_list = [(203, 172, 108), (220, 227, 234), (237, 245, 242), (153, 180, 195), (152, 186, 174), (193, 161, 176), (214, 203, 113), (208, 179, 195), (174, 188, 213), (161, 213, 187), (161, 203, 215), (114, 123, 186), (177, 160, 71), (213, 182, 181), (198, 207, 46), (105, 114, 142), (164, 121, 51)]

pen = t.Turtle()
screen = t.Screen()
t.colormode(255)

def draw_dots(width, height):
    pen.penup()
    pen.goto(-200, -200)
    for i in range(height):
        for j in range(width):
            pen.dot(20, choice(colour_list))
            pen.goto(pen.xcor()+50, pen.ycor())
        pen.goto(-200, pen.ycor()+50)

draw_dots(10, 10)

screen.exitonclick()