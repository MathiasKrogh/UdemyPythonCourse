from turtle import Turtle
SPEED = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = SPEED
        self.y_move = SPEED
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def increase_speed(self):
        if self.x_move < 0:
            self.x_move -= 2
        elif self.x_move > 0:
            self.x_move += 2

    def reset_speed(self):
        if self.x_move < 0:
            self.x_move = -SPEED
        elif self.x_move > 0:
            self.x_move = SPEED

    def out_of_bounds(self):
        self.bounce_x()
        self.reset_speed()
        self.goto(0,0)
