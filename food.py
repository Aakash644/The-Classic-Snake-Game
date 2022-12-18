from turtle import Turtle, width 
import random
class food(Turtle):
    def __init__(self) :
        super().__init__() 
        self.speed(f"fastest")
        self.shape("circle")
        self.penup() 
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue") 
        self.refresh()
        
    def refresh(self):
        randomx=random.randint(-260,260)
        randomy=random.randint(-260,260) 
        self.goto(x=randomx,y=randomy) 