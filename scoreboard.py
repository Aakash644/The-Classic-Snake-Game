from distutils.file_util import write_file
from tkinter import CENTER
from turtle import Turtle 
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()  
        self.score=0  
        self.highscore=0
        self.showscore()
    def showscore(self):
        self.clear() 
        
        with open("hs.txt","r") as data:
             self.highscore=int(data.read())
        


        self.color("white") 
        self.penup()
        self.goto(x=-20,y=280) 
        self.write(arg=f"Score:{self.score} High score:{self.highscore}",align=CENTER,font="Arial,24,Normal") 
        self.hideturtle()
    def refreshscore(self): 
        self.score+=1  
        if(self.score >= self.highscore):
            self.highscore=self.score 
            file=open("hs.txt","w")
            file.write(f"{self.highscore}")
            file.close()

        self.showscore() 
    def gameover(self):
        self.color("white") 
        self.penup()
        self.goto(x=-20,y=0) 
        self.write(arg=f"Game Over",align=CENTER,font="Arial 24 ") 
        self.hideturtle()