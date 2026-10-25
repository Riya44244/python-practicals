import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print("Point is (", self.x, ",", self.y, ")")

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


p1 = Point2D(3, 4)
p2 = Point2D(6, 8)

p1.display()
p2.display()
print("Distance of p1 from origin:", p1.distance_from_origin())
print("Distance between p1 and p2:", p1.distance_to(p2))
