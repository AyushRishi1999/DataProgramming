import math
class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    def getN(self):
        return self.__n
    def setN(self,n):
        self.__n=n
    def getSize(self):
        return self.__n
    def setSize(self, size):
        self.__size = size
    def getX(self):
        return self.__x
    def setX(self, x):
        self.__x = x
    def getY(self):
        return self.__n
    def setY(self, y):
        self.__y = y
    def getPerimeter(self):
        return self.__n*self.__side
    def getArea(self):
        n=self.__n
        s=self.__side
        area=(n*(s**2))/(4*math.tan(3.14/n))
        return area

polygon1=RegularPolygon()
polygon2=RegularPolygon(6,4)
polygon3=RegularPolygon(10,4,5.6,7.8)

print("Polygon 1 -Perimeter:",polygon1.getPerimeter(),"Area:",polygon1.getArea())
print("Polygon 2 -Perimeter:",polygon2.getPerimeter(),"Area:",polygon2.getArea())
print("Polygon 3 -Perimeter:",polygon3.getPerimeter(),"Area:",polygon3.getArea())