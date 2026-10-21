import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.move_cars()
    car_manager.remove_cars()

    #At finish line
    if player.at_finish_line():
        player.reset_position()
        scoreboard.update_scoreboard()
        car_manager.increase_speed()

    #Detect collision
    for car in car_manager.cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()