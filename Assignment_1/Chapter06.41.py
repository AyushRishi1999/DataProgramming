import math
import turtle
import random

def draw_rectangle():
    turtle.penup()
    turtle.goto(-125,50)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

def draw_circle():
    turtle.penup()
    turtle.goto(50,-50)
    turtle.pendown()
    turtle.circle(50)

def generate_points_in_rectangle():
    points = []
    for _ in range(10):
        x = random.uniform(-125, -25)
        y = random.uniform(-50, 50)
        points.append((x, y))
    return points
def generate_points_in_circle():
    points = []
    for _ in range(10):
        angle = random.uniform(0,2*3.14)
        radius = random.uniform(0,50)
        x = 50 + radius * round(math.cos(angle), 2)
        y = radius * round(math.sin(angle), 2)
        points.append((x, y))
    return points

turtle.speed(2)
draw_rectangle()
draw_circle()
rectangle_points = generate_points_in_rectangle()
for point in rectangle_points:
    turtle.penup()
    turtle.goto(point)
    turtle.dot(5)
circle_points = generate_points_in_circle()
for point in circle_points:
    turtle.penup()
    turtle.goto(point)
    turtle.dot(5)

turtle.hideturtle()
turtle.done()