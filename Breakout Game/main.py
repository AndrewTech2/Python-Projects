import random
from turtle import Turtle, Screen

ball = Turtle('circle')
ball.color("white")
ball.penup()
ball.setheading(random.randint(181, 359))
screen = Screen()
print(screen.screensize())
screen.bgcolor("black")
blocks = []

for _ in range(-400, 401, 100):
        block = Turtle()
        block.speed("fastest")
        block.shape("square")
        block.color("red")
        block.turtlesize(2, 4)
        block.penup()
        block.goto(_, 275)
        blocks.append(block)

paddle = Turtle("square")
paddle.color("white")
paddle.turtlesize(1, 16)
paddle.penup()
paddle.goto(0, -350)

def go_right():
    paddle.goto(paddle.xcor() + 30, paddle.ycor())

def go_left():
    paddle.goto(paddle.xcor() - 30, paddle.ycor())

screen.onkey(go_right, 'd')
screen.onkey(go_left, 'a')
screen.listen()

while True:
    if ball.ycor() <= -380:
        screen.clear()
        screen.bgcolor('black')
        writer = Turtle()
        writer.speed('fastest')
        writer.pencolor("white")
        writer.hideturtle()
        writer.write('GAME OVER', align='center', font=('Arial', 20, 'normal'))
        break
    if ball.xcor() <= -480:
        ball.setheading(180-ball.heading())
    if ball.xcor() >= 480:
        ball.setheading(180-ball.heading())
    if ball.ycor() >= 380:
        ball.setheading(360-ball.heading())
    if abs(ball.xcor() - paddle.xcor()) <= 160 and abs(ball.ycor() - paddle.ycor()) <= 20:
        ball.setheading(360-ball.heading())
    for block in blocks:
        if abs(block.xcor()-ball.xcor()) <= 40 or abs(block.ycor()-ball.ycor()) <= 40:
            blocks.remove(block)
            block.hideturtle()
            ball.setheading(360-ball.heading())
    ball.forward(5)

screen.mainloop()