from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        if randint(0, 10) > 7:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(choice(COLORS))
            car.goto(300, randint(-260, 260))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - self.current_speed, car.ycor())

    def remove_cars(self):
        for car in self.cars[-1::-1]:
            if car.xcor() < -320:
                self.cars.remove(car)

    def increase_speed(self):
        self.current_speed += MOVE_INCREMENT