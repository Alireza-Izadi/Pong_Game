from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
l_score = Scoreboard((-40, 260))
r_score = Scoreboard((40, 260))

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update() 
    time.sleep(ball.move_speed)
    ball.move()
    
    #detect collision with paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 340 or ball.distance(l_paddle) < 30 and ball.xcor() < -340:
        ball.x_velocity *= -1
        ball.move_speed *= 0.9
    
    #detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        l_score.add_score()
        
    #detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        r_score.add_score()
        
screen.exitonclick()