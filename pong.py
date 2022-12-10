from turtle import Screen
from pong_paddle import Paddle
from pong_ball import Ball
from pong_ui import PongUI
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
    ui = PongUI()

    screen.listen()
    screen.onkeypress(r_paddle.go_up, "Up")
    screen.onkeypress(r_paddle.go_down, "Down")
    screen.onkeypress(l_paddle.go_up, "w")
    screen.onkeypress(l_paddle.go_down, "s")

    game_active = True
    while game_active:
        time.sleep(0.08)
        screen.update()
        ball.move()
        # collision
        if ball.ycor() > 275 or ball.ycor() < -275:
            ball.bounce_y()
        # paddle collision
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
        if ball.xcor() > 380:
            ui.change_score(0)
            ball.reset_position()
        if ball.xcor() < -380:
            ui.change_score(1)
            ball.reset_position()


    screen.exitonclick()

