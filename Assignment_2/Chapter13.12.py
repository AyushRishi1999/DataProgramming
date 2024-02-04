class TriangleError(RuntimeError):
    def __init__(self, s1, s2, s3):
        super().__init__("Invalid sides. The sum of any two sides must be greater than the third side.")
        self.__s1 = s1
        self.__s2 = s2
        self.__s3 = s3

    def getSide1(self):
        return self.__s1

    def getSide2(self):
        return self.__2

    def getSide3(self):
        return self.__s3

class Triangle:
    def __init__(self, s1=1.0, s2=1.0, s3=1.0):
        if not self.isValid(s1, s2, s3):
            raise TriangleError(s1, s2, s3)

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
        area = (s * (s - self.__s1) * (s - self.__s2) * (s - self.__s3)) ** 0.5
        return area

    def getPerimeter(self):
        return self.__s1 + self.__s2 + self.__s3

    def isValid(self, s1, s2, s3):
        return (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1)

# Example usage
try:
    triangle = Triangle(1, 2, 5)
except TriangleError as e:
    print(f"Error: {e}")
    print(f"Sides: {e.getSide1()}, {e.getSide2()}, {e.getSide3()}")
