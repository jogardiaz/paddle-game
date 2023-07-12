from turtle import Turtle

ALIGN = 'center'
FONT = ('courier', 30, 'normal')


class Score(Turtle):

    def __init__(self, x):
        super().__init__()
        self.score = -1
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x, 270)
        self.up_score()

    def up_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, align=ALIGN, font=FONT)

    def winner(self):
        self.goto(0, 0)
        self.write("YOU WIN", False, align=ALIGN, font=FONT)

    def loser(self):
        self.goto(0, 0)
        self.write("YOU LOSE", False, align=ALIGN, font=FONT)

