from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detectar colisão top and botton walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detectar colisão com o r_paddle e l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detectar colisão com a r_paddle
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    #detectar colisão com a l_paddle
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
