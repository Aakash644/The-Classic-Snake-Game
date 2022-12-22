
from turtle import Turtle as t,Screen as s

dis=[20,0,-20] 
class snake():  
    
    def __init__(self) : 
       self.timparts=[] 
       self.createsnake()
       
    
          
    def createsnake(self):
        for i in dis: 
          tim=t(shape="square")  
          tim.setheading(0) 
          tim.penup()
          tim.color("white")
          tim.goto(x=i,y=0) 
          self.timparts.append(tim)  
    def extend(self): 
        tim=t(shape="square")  
        tim.setheading(self.timparts[-1].heading()) 
        tim.penup()
        tim.color("white")
        tim.goto( x=self.timparts[-1].xcor(),y=self.timparts[-1].ycor() )
        self.timparts.append(tim)    
    
    def move(self):
        for i in range(len(self.timparts)-1,0,-1): 
           newx=self.timparts[i-1].xcor()
           newy=self.timparts[i-1].ycor()
           self.timparts[i].goto(x=newx,y=newy)
        self.timparts[0].forward(20) 
    
    def Up(self): 
        if(self.timparts[0].heading()!=270):
           self.timparts[0].setheading(90)
    def Down(self): 
        if(self.timparts[0].heading()!=90):
           self.timparts[0].setheading(270)
    def Left(self):
        if(self.timparts[0].heading()!=0):
           self.timparts[0].setheading(180)
    def Right(self): 
        if(self.timparts[0].heading()!=180):
           self.timparts[0].setheading(0)