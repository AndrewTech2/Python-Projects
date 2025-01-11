from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    stage = 1
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
    def write_stage(self):
        self.write(f"Stage {self.stage}", align='center', font=FONT)
    def game_over(self):
        self.home()
        self.write("Game over!", align='center', font=FONT)
