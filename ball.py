from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.y_velocity = 10
        self.x_velocity = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.move_speed = 0.1
    def move(self):
        self.setx(self.xcor() + self.x_velocity)
        self.sety(self.ycor() + self.y_velocity)
        
        #bounce effect
        if self.ycor() >560 / 2 or self.ycor() < -560 / 2:
            self.y_velocity *= -1
            
    def reset_position(self):
        self.goto(0, 0)
        self.x_velocity *= -1
        self.move_speed = 0.1