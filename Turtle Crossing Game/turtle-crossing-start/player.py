from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])
        self.speed("fastest")
        self.left(90)
    def move(self):
        self.forward(MOVE_DISTANCE)
    def is_touching_car(self, cars_list):
        for x in cars_list:
            if self.distance(x) < 25:
                return True
        return False
    def is_at_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False