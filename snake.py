
from turtle import Turtle


POSITIONS = [(0,0),(-20,0), (-40,0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()

    def createSnake(self):
        for i in POSITIONS:
            self.addSegment(i)

    def addSegment(self, position):
        newSegment = Turtle(shape="square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)

    def move(self):
        for segNum in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segNum-1].xcor()
            new_y= self.segments[segNum-1].ycor()
            self.segments[segNum].goto(new_x,new_y)
        self.segments[0].forward(20)

    def up(self):
        if not self.segments[0].heading()==270:
            self.segments[0].setheading(90)
    def down(self):
        if not self.segments[0].heading()==90:
            self.segments[0].setheading(270)

    def left(self):
        if not self.segments[0].heading()==0:
            self.segments[0].setheading(180)

    def right(self):
        if not self.segments[0].heading()==180:
            self.segments[0].setheading(0)

    def check(self):
        if(self.segments[0].xcor()>285 or self.segments[0].xcor()<-285
        or self.segments[0].ycor()>285 or self.segments[0].ycor()<-285 ):
            return False
        else:
            return True
    def head(self):
        return self.segments[0]
    
    def extend(self):
        self.addSegment(self.segments[-1].position())

    
