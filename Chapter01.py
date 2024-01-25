import turtle
turtle.begin_fill()
turtle.color("red")
turtle.circle(100)
turtle.end_fill()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(50)
turtle.end_fill()
#turtle.circle(100, steps=4)
#turtle.circle(100, 180)
'''
x1, y1 =eval(input("Enter x1 and y1 : "))
x2, y2 =eval(input("Enter x2 and y2 : "))
d = ((x2-x1)**2 + (y2-y1)**2)**0.5
xm = (x1+x2)/2
ym = (y1+y2)/2
turtle.showturtle()
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.penup()
turtle.goto(xm,ym)
turtle.write(d)
'''
turtle.done()