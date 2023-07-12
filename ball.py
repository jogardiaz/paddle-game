from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.up = True
        self.right = False

    def move_up(self):
        y = self.ycor() + 15
        self.goto(self.xcor(), y)
    def move_down(self):
        y = self.ycor() - 15
        self.goto(self.xcor(), y)
    def move_right(self):
        x = self.xcor() + 15
        self.goto(x, self.ycor())
    def move_left(self):
        x = self.xcor() - 15
        self.goto(x, self.ycor())

    def move(self):
        if self.ycor() == 300:
            self.up = False
        elif self.ycor() == -300:
            self.up = True
        if self.up:
            self.move_up()
        else:
            self.move_down()




