import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
player = Player()
cars = CarManager()
screen.listen()
screen.onkey(fun=player.move, key='w')
screen.onkey(fun=player.move, key='Up')
car_counter = 1
score = Scoreboard()
score.write_stage()

while True:
    time.sleep(0.1)
    screen.update()
    if player.is_touching_car(cars.cars_list):
        score.game_over()
        break
    if player.is_at_finish():
        score.clear()
        score.stage += 1
        score.write_stage()
        player.goto(0, -280)
        cars.speed += 10
    if car_counter % 3 == 0:
        cars.generate_car()
        car_counter += 1
    else:
        car_counter += 1
    cars.move()

screen.exitonclick()