from turtle import Screen, Turtle
import random, time

def move_up1():
    x = paddle1.xcor()
    y = paddle1.ycor()
    if y >= 240:
        pass
    else:
        paddle1.goto(x, y + 20)

def move_down1():
    x = paddle1.xcor()
    y = paddle1.ycor()
    if y <= -220:
        pass
    else:
        paddle1.goto(x, y-20)

def move_up2():
    x = paddle2.xcor()
    y = paddle2.ycor()
    if y >= 240:
        pass
    else:
        paddle2.goto(x, y + 20)

def move_down2():
    x = paddle2.xcor()
    y = paddle2.ycor()
    if y <= -220:
        pass
    else:
        paddle2.goto(x, y-20)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.onkey(move_up1, "Up")
screen.onkey(move_down1, 'Down')
screen.onkey(move_up2, "w")
screen.onkey(move_down2, 's')

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=3)
        self.penup()
        self.speed('fastest')

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.speed('fastest')
    def bounce(self):
        current = self.heading()
        self.setheading(360-current)

class Scoreboard(Turtle):
    score1 = 0
    score2 = 0
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(y=250, x=0)
        self.write(arg="0\t\t\t0", align='center', font=("Courier", 24, 'normal'))
    def update(self):
        if ball.xcor() >= 280:
            self.score2 += 1
        else:
            self.score1 += 1
        self.clear()
        self.write(arg=f"{self.score2}\t\t\t{self.score1}", align='center', font=("Courier", 24, 'normal'))
paddle1 = Paddle()
paddle1.goto(x=350, y=0)
paddle2 = Paddle()
paddle2.goto(x=-350, y=0)
ball = Ball()
ball.setheading(random.randint(0, 360))
score = Scoreboard()

while True:
    time.sleep(0.1)
    if ball.ycor() >= 279 or ball.ycor() <= -270:
        ball.bounce()
    if ball.xcor() >= 380 or ball.xcor() <= -380:
        score.update()
        ball.home()
        ball.setheading(random.randint(0, 360))
    if ball.distance(paddle1) <= 40:
        ball.right(360-ball.heading())
    if ball.distance(paddle2) <= 40:
        ball.right(360-ball.heading())
    ball.forward(20)

screen.exitonclick()