import turtle
import pandas

def start():
    guessed_states = []
    data = pandas.read_csv("./us_states/50_states.csv")

    all_states = data.state.to_list()

    print("Guess the US States")
    screen = turtle.Screen()
    screen.title("US States Quiz")
    image = "./us_states/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)


    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="Type a states name: ").title()
        print(answer_state)

        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state_data = data[data.state == answer_state]
            print(state_data.x)
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
        elif answer_state == "Exit":
            missed_states = [state for state in all_states if state not in guessed_states]
            # missed_states = []
            # for state in all_states:
            #     if state not in guessed_states:
            #         missed_states.append(state)
            new_data = pandas.DataFrame(missed_states)
            new_data.to_csv("./us_states/missed_states.csv")
            break

    # states to learn

