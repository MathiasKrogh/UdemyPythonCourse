from turtle import Turtle
DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)

    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + DISTANCE)

    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - DISTANCE)