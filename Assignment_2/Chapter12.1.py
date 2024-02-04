import math
class GeometricObject:
    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return f"color: {self.__color}, filled: {self.__filled}"

class Triangle(GeometricObject):
    def __init__(self, s1=1.0, s2=1.0, s3=1.0, color="green", filled=True):
        super().__init__(color, filled)
        self.__s1 = s1
        self.__s2 = s2
        self.__s3 = s3

    def getSide1(self):
        return self.__s1

    def getSide2(self):
        return self.__s2

    def getSide3(self):
        return self.__s3

    def getArea(self):
        s = (self.__s1 + self.__s2 + self.__s3) / 2
        area = math.sqrt(s * (s - self.__s1) * (s - self.__s2) * (s - self.__s3))
        return area

    def getPerimeter(self):
        return self.__s1 + self.__s2 + self.__s3

    def __str__(self):
        return f"Triangle: side1 = {self.__s1}, side2 = {self.__s2}, side3 = {self.__s3}, {super().__str__()}"

s1 = float(input("Enter side1: "))
s2 = float(input("Enter side2: "))
s3 = float(input("Enter side3: "))
color = input("Enter color: ")
filled = bool(int(input("Enter 1 for filled, 0 for not filled: ")))

triangle = Triangle(s1, s2, s3, color, filled)

print("\nTriangle Information:")
print("Area:", triangle.getArea())
print("Perimeter:", triangle.getPerimeter())
print("Color:", triangle.getColor())
print("Filled:", triangle.getFilled())
