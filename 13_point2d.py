# Practical 13: Class for 2D point
# (Python class names cannot start with a digit, so it is named Point2D)
import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


p1 = Point2D(1, 2)
p2 = Point2D(4, 6)

print("Point 1:", p1)
print("Point 2:", p2)
print("Distance between the points:", p1.distance(p2))
