from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()  # Hide the turtle itself
        self.color('green')
        self.penup()
        self.goto(0, 240)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def hide_scoreboard(self):
        self.clear()