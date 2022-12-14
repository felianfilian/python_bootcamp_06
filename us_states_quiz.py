import turtle
import pandas

def start():
    print("Guess the US States")
    screen = turtle.Screen()
    screen.title("US States Quiz")
    image = "./us_states/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    

    screen.exitonclick()