class LinearEquation:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3
        self.__x4 = x4
        self.__y4 = y4

    def getX1(self):
        return self.__x1

    def setX1(self, x1):
        self.__x1 = x1

    def getY1(self):
        return self.__y1

    def setY1(self, y1):
        self.__y1 = y1

    def getX2(self):
        return self.__x2

    def setX2(self, x2):
        self.__x2 = x2

    def getY2(self):
        return self.__y2

    def setY2(self, y2):
        self.__y2 = y2

    def getX3(self):
        return self.__x3

    def setX3(self, x3):
        self.__x3 = x3

    def getY3(self):
        return self.__y3

    def setY3(self, y3):
        self.__y3 = y3

    def getX4(self):
        return self.__x4

    def setX4(self, x4):
        self.__x4 = x4

    def getY4(self):
        return self.__y4

    def setY4(self, y4):
        self.__y4 = y4

    def isSolvable(self):
        a = self.__y1 - self.__y2
        b = self.__x2 - self.__x1
        c = self.__y3 - self.__y4
        d = self.__x4 - self.__x3
        if (a * d - b * c) == 0:
            return False
        else:
            return True

    def intersectingPoint(self):
        a = self.__y1 - self.__y2
        b = self.__x2 - self.__x1
        c = self.__y3 - self.__y4
        d = self.__x4 - self.__x3
        e = ((self.__y1 - self.__y2) * self.__x1 -
             (self.__x1 - self.__x2) * self.__y1)
        f = ((self.__y3 - self.__y4) * self.__x3 -
             (self.__x3 - self.__x4) * self.__y3)
        if LinearEquation.isSolvable(self):
            x = (e * d - b * f) / (a * d - b * c)
            y = (a * f - e * c) / (a * d - b * c)
            return x, y
        else:
            return "The equation has no solution"


x1, y1, x2, y2 = eval(input("Enter the endpoints of the first line segment: "))
x3, y3, x4, y4 = eval(input("Enter the endpoints of the second line segment: "))

eq = LinearEquation(x1, y1, x2, y2, x3, y3, x4, y4)
intersectingPoint = eq.intersectingPoint()

print(f"The intersecting point is: ", intersectingPoint)
