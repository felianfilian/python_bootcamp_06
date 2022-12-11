from turtle import Turtle

FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.write(f"Level: {self.level}", align="left", font=FONT)
