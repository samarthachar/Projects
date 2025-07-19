import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

cars = []
car = CarManager()
cars.append(car)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # Creates car
    if randint(1,6) == 1:
        car = CarManager()
        cars.append(car)

    # Check for next level
    if player.is_at_finish_line():
        player.restart()
        scoreboard.next_level()
        CarManager.next_level()
    # Make cars appear
    for car in cars:
        car.move()
        # Delete used cars
        if car.xcor() < -350:
            cars.remove(car)

        # Detect game over
        if car.distance(player) < 20:
            scoreboard.end_game()
            game_is_on = False
    screen.update()

screen.exitonclick()

