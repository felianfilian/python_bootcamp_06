from turtle import Screen
from crossing_player import Player
import time

def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    screen.listen()
    screen.onkey(player.move_up, "w")

    game_active = True
    while game_active:
        time.sleep(0.1)
        screen.update()