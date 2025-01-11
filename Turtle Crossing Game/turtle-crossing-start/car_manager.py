from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:
    speed = 5
    cars_list = []
    def __init__(self):
        for x in range(30):
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(random.randint(-280, 280), random.randint(-200, 280))
            car.setheading(180)
            self.cars_list.append(car)
    def generate_car(self):
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(random.randint(300, 1000), random.randint(-200, 280))
            car.setheading(180)
            self.cars_list.append(car)
    def move(self):
        for x in self.cars_list:
            x.forward(self.speed)