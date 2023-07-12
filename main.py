from turtle import Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time

screen = Screen()
screen.screensize(400, 400)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

score_left = Score(-100)
score_right = Score(100)

paddle_player = Paddle(-350)
paddle = Paddle(350)

ball = Ball()

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)

    ball.move()
    paddle.move()

    screen.onkeypress(paddle_player.move_up, 'w')
    screen.onkeypress(paddle_player.move_down, 's')

    #CHECK IF SCORE A GOAL
    if ball.xcor() == 360:
        ball.right = False
        ball.goto(0, ball.ycor())
        score_left.up_score()
    elif ball.xcor() == -360:
        ball.right = True
        ball.goto(0, ball.ycor())
        score_right.up_score()
        print(f'{score_left.score}')
    if ball.right:
        ball.move_right()
    else:
        ball.move_left()

    #CHECK IF BOUNCE IN PADDLE
    if ball.distance(paddle_player) < 30:
        ball.right = True
        ball.move_right()
    elif ball.distance(paddle) < 30:
        ball.right = False
        ball.move_left()

    if score_right.score == 5:
        score_right.loser()
        game_on = False
    elif score_left.score == 5:
        score_left.winner()
        game_on = False

screen.exitonclick()