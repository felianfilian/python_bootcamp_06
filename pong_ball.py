from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.dir_x = 10
        self.dir_y = 10

    def move(self):
        new_x = self.xcor() + self.dir_x
        new_y = self.ycor() + self.dir_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dir_y *= -1
    def bounce_x(self):
        self.dir_x *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
