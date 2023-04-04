from turtle import Turtle

FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-270, 260)
        self.score_up()

    def score_up(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL : {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=FONT)
