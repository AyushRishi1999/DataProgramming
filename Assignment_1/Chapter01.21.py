import turtle

turtle.width(3)
turtle.forward(125)
turtle.back(225)
turtle.width(5)
turtle.goto(0,0)
turtle.width(1)
turtle.goto(0,125)
turtle.penup()
turtle.goto(0,-150)
turtle.pendown()
turtle.circle(150)
turtle.write("6")
turtle.penup()
turtle.goto(140,-5)
turtle.write("3")
turtle.goto(0,130)
turtle.write("12")
turtle.goto(-140,-5)
turtle.write("9")
turtle.goto(0,-200)
turtle.write("9:15:00")

turtle.done()