from turtle import *
from random import *


class MyTurtle(Turtle):
    def glow(self,x,y):
        global random
        r = random()
        g = random()
        b = random()
        x = randint(-200,200)
        y = randint(-200,200)
        self.fillcolor(r,g,b)
        self.goto(x,y)

turtle = MyTurtle()
turtle.shape("turtle")
turtle.onclick(turtle.glow)

