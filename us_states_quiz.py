import turtle
import pandas

def start():
    print("Guess the US States")
    screen = turtle.Screen()
    screen.title("US States Quiz")
    image = "./us_states/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    answer_state = screen.textinput(title="Guess the state", prompt="Type a states name: ")
    print(answer_state)
    turtle.mainloop()