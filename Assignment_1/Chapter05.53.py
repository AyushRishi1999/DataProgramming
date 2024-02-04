import turtle
import math


turtle.pendown()
turtle.goto(0,540)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0, -540)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(-540, -0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(540, 0)
turtle.penup()
turtle.goto(0,0)
turtle.penup()
turtle.goto(-540, 0)

turtle.pencolor("red")
for x in range(-540, 541):
    y = math.sin(math.radians(x))
    turtle.goto(x, y * 100)
    turtle.pendown()

turtle.penup()
turtle.goto(-540, 0)

#
turtle.pencolor("blue")
for x in range(-540, 541):
    y = math.cos(math.radians(x))
    turtle.goto(x, y * 100)
    turtle.pendown()

turtle.done()