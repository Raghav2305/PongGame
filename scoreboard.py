from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.Lscore = 0
        self.Rscore = 0

        self.update_score()



    def update_score(self):
        self.goto(-100, 200)
        self.write(self.Lscore, False, align="center", font=('courier', 80, "normal"))
        self.goto(100, 200)
        self.write(self.Rscore, False, align="center", font=('courier', 80, "normal"))



    def lscore(self):
        self.Lscore += 1
        self.clear()
        self.update_score()

    def rscore(self):
        self.Rscore += 1
        self.clear()
        self.update_score()
