x1,y1,r1=eval(input("Enter circle1's center x-, y-coordinates, and radius:"))
x2,y2,r2=eval(input("Enter circle2's center x-, y-coordinates, and radius:"))
distance_between_centers = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
import turtle
turtle.penup()
turtle.goto(x1,y1-r1)
turtle.pendown()
turtle.circle(r1)
turtle.penup()
turtle.pendown()
turtle.goto(x2,y2-r2)
turtle.circle(r2)
turtle.penup()
if distance_between_centers<=(r1-r2):
    turtle.write("circle2 is inside circle1")
elif distance_between_centers>(r1-r2) and distance_between_centers<(r1+r2):
    turtle.write("circle2 overlaps circle1")
else:
    turtle.write("circle2 is outside circle1")

turtle.done()