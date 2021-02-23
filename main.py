from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
left_paddle = Paddle(-380, 0)
right_paddle = Paddle(380, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if (ball.distance(right_paddle) <= 30 and ball.xcor() >= 350) or\
            (ball.distance(left_paddle) <= 30 and ball.xcor() <= -350):
        ball.bounce_off_paddle()
    if ball.xcor() > 380:
        scoreboard.calculate_score("Left")
        ball.reset_position()
    elif ball.xcor() < -380:
        scoreboard.calculate_score("Right")
        ball.reset_position()
screen.exitonclick()
