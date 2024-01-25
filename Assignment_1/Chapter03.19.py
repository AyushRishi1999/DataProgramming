import turtle
x1, y1, x2, y2 = eval(input("Enter co-ordinates of the two points : "))
turtle.penup()
turtle.goto(x1,y1)
turtle.write("("+str(x1)+", "+str(y1)+")")
turtle.pendown()
turtle.goto(x2,y2)
turtle.write("("+str(x2)+", "+str(y2)+")")
turtle.done()