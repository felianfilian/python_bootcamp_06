from turtle import Screen
from pong_paddle import Paddle
from pong_ball import Ball
import time

def start():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    game_active = True
    while game_active:
        time.sleep(0.08)
        screen.update()
        ball.move()
        # collision
        if ball.ycor() > 275 or ball.ycor() < -275:
            ball.bounce()

    screen.exitonclick()

