import turtle
import math


turtle.pendown()
turtle.goto(0,100)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0, -100)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(-100, -0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(100, 0)
turtle.penup()
turtle.goto(0,0)
turtle.penup()
for x in range(-100, 101):
    y = x ** 2 /100

    turtle.goto(x, y)
    turtle.pendown()
turtle.done()