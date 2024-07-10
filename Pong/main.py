from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    # to make the ball move slower
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # detect ball hitting wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect ball hitting right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() > -330):
        ball.bounce_x()

    # detect ball going out of bounds
    if ball.xcor() > 400:
        ball.center()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.center()
        scoreboard.r_point()

screen.exitonclick()
