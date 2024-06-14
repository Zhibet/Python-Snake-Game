from turtle import Turtle
from weapons import Weapons


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('red')
        self.goto(0, -245)
        self.setheading(90)

