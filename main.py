from turtle import Turtle, Screen
from  board import Board
from character import Characterxx

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('purple')
screen.listen()
# classes
board = Board()
soldier = Character()







game_on = True

while game_on:
    screen.update()

screen.exitonclick()