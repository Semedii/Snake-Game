import time
from turtle import Screen, Turtle, color
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

myScreen = Screen()
myScreen.bgcolor("black")
myScreen.setup(600,600)
myScreen.title("Snake Game")
myScreen.tracer(0)
timm = Turtle()


snake = Snake()
food = Food()
score = ScoreBoard()

myScreen.listen()
myScreen.onkey(snake.up, "Up")
myScreen.onkey(snake.down, "Down")
myScreen.onkey(snake.left, "Left")
myScreen.onkey(snake.right, "Right")

myScreen.update()
gameOn=True
while gameOn and snake.check():
    myScreen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head().distance(food)<15:
        food.refresh()
        score.update_score()
        snake.extend()

    for i in snake.segments[1:]:
       if snake.head().distance(i)<5:
            gameOn=False

score.gameOver()
    
  
myScreen.exitonclick()
