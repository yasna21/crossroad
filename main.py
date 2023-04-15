import time

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
playyer = Player()

carmanager = CarManager()
scorborad = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=playyer.move_turtle)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_car()
    for car in carmanager.cars:
        if car.distance(playyer) < 20:
            game_is_on = False
            scorborad.game_over()

    if playyer.is_playyer_at_finish_line():
        playyer.go_to_start()
        carmanager.level_up()
        scorborad.increase_level()



screen.exitonclick()