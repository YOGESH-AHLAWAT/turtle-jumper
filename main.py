import time
from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(fun=player.move, key='Up')
car = CarManager()
scoreboard=Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    # detect collision with car
    for cars in car.all_car:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect at finish line
    if player.is_at_finish_line():
        player.goto_starting_pos()
        car.level_up()
        scoreboard.score_up()

screen.exitonclick()
