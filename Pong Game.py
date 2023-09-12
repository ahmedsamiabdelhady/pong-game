from turtle import Turtle, Screen
from Padle import Padle
from ball import Ball
from score import ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)


r_padle = Padle((380, 0))
l_padle = Padle((-380, 0))
ball = Ball()
r_scoreboard = ScoreBoard((70, 160))
l_scoreboard = ScoreBoard((-130, 160))





screen.listen()
screen.onkeypress(r_padle.move_up, "Up")
screen.onkeypress(r_padle.move_down, "Down")
screen.onkeypress(l_padle.move_up, "w")
screen.onkeypress(l_padle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()
    elif ball.xcor() == 360 and r_padle.distance(ball) < 100 or ball.xcor() == -360 and l_padle.distance(ball) < 100:
        ball.bounce_x()
    elif ball.xcor() > 410:
        ball.reset_position()
        l_scoreboard.point((-130, 160))
    elif ball.xcor() < -410:
        ball.reset_position()
        r_scoreboard.point((70, 160))

        
























screen.exitonclick()