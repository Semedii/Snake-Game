from turtle import Turtle
class ScoreBoard(Turtle):
 
    def __init__(self):
        super().__init__()
        self.score = 0
        self.start()
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.start()
 
    def start(self):
        self.penup()
        self.color("#303030")
        self.goto(0, 270)
        self.hideturtle()
        self.speed(0)
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))
    
    def gameOver(self):
        self.goto(0,0)
        self.write(arg=f"Game Over", align="center", font=("Arial", 50, "bold"))
        self.goto(0,-100)
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 50, "bold"))