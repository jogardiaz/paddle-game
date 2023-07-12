from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos_x):
        super().__init__()
        self.pos_x = pos_x
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()
        self.goto(self.pos_x, 0)
        self.speed(0)
        self.up = True

    def move_up(self):
        if self.ycor() > 260:
            pass
        else:
            self.forward(20)

    def move_down(self):
        if self.ycor() < -260:
            pass
        else:
            self.backward(20)

    def move(self):
        if self.ycor() == 280:
            self.up = False
        elif self.ycor() == -280:
            self.up = True
        if self.up:
            self.move_up()
        else:
            self.move_down()