import turtle
turtl=turtle.showturtle()

for i in range(8):

    for j in range(8):
        turtle.pencolor("black")
        turtle.goto(i*25,j*25)
        turtle.pendown()

        if (i+j)%2==0:
            turtle.begin_fill()
            turtle.color('black')
        else:
            pass
        for k in range(4):
            turtle.pendown()
            turtle.forward(25)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()