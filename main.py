from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


is_game_on = True

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=600, canvheight=600)

screen.tracer(0)

left_paddle = Paddle(xcor=-350, ycor=0)
right_paddle = Paddle(xcor=350, ycor=0)
scoreboard = ScoreBoard()

ball = Ball()
screen.title("PONG")
screen.listen()
screen.onkeypress(fun=left_paddle.go_up, key="w")
screen.onkeypress(fun=left_paddle.go_down, key="s")
screen.onkeypress(fun=right_paddle.go_up, key="Up")
screen.onkeypress(fun=right_paddle.go_down, key="Down")

while is_game_on:

    screen.update()
    ball.penup()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 or ball.xcor() > 340:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 or ball.xcor() > 340:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.lscore()

    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.rscore()













screen.exitonclick()