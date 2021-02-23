from turtle import Turtle
FONT = ("Arial", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 220)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_l}          {self.score_r}", align="center", font=FONT)

    def calculate_score(self, player):
        if player == "Left":
            self.score_l += 1
            self.clear()
            self.update_scoreboard()
        elif player == "Right":
            self.score_r += 1
            self.clear()
            self.update_scoreboard()
