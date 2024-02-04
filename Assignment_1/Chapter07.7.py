class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def setA(self, a):
        self.__a = a

    def getB(self):
        return self.__b

    def setB(self, b):
        self.__b = b

    def getC(self):
        return self.__c

    def setC(self, c):
        self.__c = c

    def getD(self):
        return self.__d

    def setD(self, d):
        self.__d = d

    def getE(self):
        return self.__e

    def setE(self, e):
        self.__e = e

    def getF(self):
        return self.__f

    def setF(self, f):
        self.__f = f

    def isSolvable(self):
        a = self.__a
        b = self.__b
        c = self.__c
        d = self.__d
        if (a * d - b * c) == 0:
            return False
        else:
            return True

    def getX(self):
        a = self.__a
        b = self.__b
        c = self.__c
        d = self.__d
        e = self.__e
        f = self.__f
        if LinearEquation.isSolvable(self):
            x = (e * d - b * f) / (a * d - b * c)
            return x
        else:
            return "The equation has no X \n"

    def getY(self):
        a = self.__a
        b = self.__b
        c = self.__c
        d = self.__d
        e = self.__e
        f = self.__f
        if LinearEquation.isSolvable(self):
            y = (a * f - e * c) / (a * d - b * c)
            return y
        else:
            return "The equation has no Y"


linearEquation1 = LinearEquation(9.0, 4.0, 3.0, -5.0, -6.0, -21.0)
linearEquation2 = LinearEquation(1.0, 2.0, 2.0, 4.0, 4.0, 5.0)
print(linearEquation1.getX(), linearEquation1.getY())
print(linearEquation2.getX(), linearEquation2.getY())
