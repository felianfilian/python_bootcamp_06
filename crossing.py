from turtle import Screen
from crossing_player import Player
from crossing_cars import Cars
import time

def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = Cars()

    screen.listen()
    screen.onkey(player.move_up, "w")

    game_active = True
    while game_active:
        time.sleep(0.1)
        screen.update()
        car_manager.create_cars()
        car_manager.move_cars()

        # car collision detection
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_active = False


