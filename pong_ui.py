from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class PongUI(Turtle):
    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"{self.score[0]} | {self.score[1]}", align=ALIGNMENT, font=FONT)

    def change_score(self, player):
        self.score[player] += 1
        self.clear()
        self.update_score()
