import turtle

colors = ["orange", "purple", "yellow", "red", "green", "pink", "blue"]
t= turtle.Turtle("turtle")

turtle. bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length < 390:
    t.pencolor(colors[length%7])
    t.circle(length,90)
    length += 5
