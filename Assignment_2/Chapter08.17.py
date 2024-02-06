import math


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distance(self, p):
        return math.sqrt((self.__x - p.get_x()) ** 2 + (self.__y - p.get_y()) ** 2)

    def is_nearby(self, p1):
        return self.distance(p1) < 5

    def __str__(self):
        return f'({self.__x}, {self.__y})'


# Test program
def main():
    x1, y1 = map(float, input("Enter coordinates of point 1 (x y): ").split())
    x2, y2 = map(float, input("Enter coordinates of point 2 (x y): ").split())

    point1 = Point(x1, y1)
    point2 = Point(x2, y2)

    print(f"Distance between {point1} and {point2}: {point1.distance(point2):.2f}")
    if point1.is_nearby(point2):
        print("The points are nearby.")
    else:
        print("The points are not nearby.")


if __name__ == "__main__":
    main()
