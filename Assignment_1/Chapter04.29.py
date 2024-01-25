x1,y1,r1=eval(input("Enter circle1's center x-, y-coordinates, and radius:"))
x2,y2,r2=eval(input("Enter circle2's center x-, y-coordinates, and radius:"))
distance_between_centers = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

if distance_between_centers<=(r1-r2):
    print("circle2 is inside circle1")
elif distance_between_centers>(r1-r2) and distance_between_centers<(r1+r2):
    print("circle2 overlaps circle1")
else:
    print("circle2 is outside circle1")