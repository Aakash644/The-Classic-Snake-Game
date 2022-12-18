from turtle import Turtle as t, Screen as s
import time
from scoreboard import scoreboard
from food import food
from snakeclass import snake
import snakeclass
screen = s()

#main screen setup 
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game") 
#initializing the snake class
snake = snake() 
#initializing the food class
food = food() 
#initializing the game score
score = scoreboard()
score.refreshscore() 
#used to turn turtle animation on or off and set a delay for update drawings
screen.tracer(0)
#setting the game to true
gameison = True
while gameison:
    screen.update() # used to update the screen
    time.sleep(0.15)#used to create a time delay
    snake.move() 
    #Detect collision with the wall
    if(snake.timparts[0].xcor()>=280 or snake.timparts[0].xcor()<=-280 or snake.timparts[0].ycor()>=280 or snake.timparts[0].ycor()<=-280):
      gameison=False 
      score.gameover()
    #Detect collision with food and extend the length of snake and score of the game
    if (snake.timparts[0].distance(food) < 15):
        food.refresh() 
        snake.extend()
        score.refreshscore() 
    #Detect collision of snake's head with it's tail or body parts
    for segment in snake.timparts: 
      if(snake.timparts[0]==segment):
        continue
    
      if(snake.timparts[0].distance(segment)<10): 
        gameison=False
        score.gameover()
    #Control keys

    screen.listen()
    screen.onkey(snake.Up, key="w")
    screen.onkey(snake.Down, key="s")
    screen.onkey(snake.Left, key="a")
    screen.onkey(snake.Right, key="d")


screen.exitonclick()
