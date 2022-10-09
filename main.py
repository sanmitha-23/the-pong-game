from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# creating screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

# creating paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# creating ball
ball = Ball()

# creating scoreboard
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce the ball
        ball.bounce_y()

    # detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # if r paddle misses the ball
    if ball.xcor() > 380:
        ball.restart()
        score.l_score_update()

    # if l paddle misses the ball
    if ball.xcor() < -380:
        ball.restart()
        score.r_score_update()


screen.exitonclick()
