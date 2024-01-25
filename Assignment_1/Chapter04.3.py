a,b,c,d,e,f = eval(input("Enter values of a, b, c, d, e, f : "))

if (a*d-b*c) == 0:
    print("The equation has no solution.")
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x is " + str(x) + " and y is " + str(y))
