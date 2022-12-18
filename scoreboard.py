from tkinter import CENTER
from turtle import Turtle 
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()  
        self.score=-1
        
    def refreshscore(self):  
        self.clear()
        self.score+=1
        self.color("white") 
        self.penup()
        self.goto(x=-20,y=280) 
        self.write(arg=f"Score:{self.score}",align=CENTER,font="Arial,24,Normal") 
        self.hideturtle()
    def gameover(self):
        self.color("white") 
        self.penup()
        self.goto(x=-20,y=0) 
        self.write(arg=f"Game Over",align=CENTER,font="Arial,24,Normal") 
        self.hideturtle()