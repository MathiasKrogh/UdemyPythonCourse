import turtle as t
from random import choice, randint

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("DarkSeaGreen")
t.colormode(255)

def random_colour():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r, g, b)


# CHALLENGE 1
# Square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# CHALLENGE 2
# For black and white
# for i in range(20):
#     timmy.color("black")
#     timmy.forward(10)
#     timmy.color("white")
#     timmy.forward(10)
#
# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# CHALLENGE 3
# colours = ["Red", "Yellow", "Green", "DarkSeaGreen", "Blue", "SeaGreen", "Purple"]
#
# def draw_shape(sides):
#     angle = 360/sides
#     for i in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for i in range(3, 11):
#     timmy.color(choice(colours))
#     draw_shape(i)

# CHALLENGE 4
# angles = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed(0)

# for i in range(500):
#     timmy.color(random_colour())
#     timmy.setheading(choice(angles))
#     timmy.forward(20)

# CHALLENGE 5
def circles(amount):
    angle = 360/amount
    for i in range(amount):
        timmy.color(random_colour())
        timmy.circle(100)
        timmy.left(angle)
timmy.speed(0)
circles(200)


screen = t.Screen()
screen.exitonclick()