from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.goto(position)
        self.add_score()
        
    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score - 1}", align=ALIGNMENT, font=FONT)
