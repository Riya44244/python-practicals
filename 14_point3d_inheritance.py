import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print("Point is (", self.x, ",", self.y, ")")


class Point3D(Point2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print("Point is (", self.x, ",", self.y, ",", self.z, ")")

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


p = Point3D(1, 2, 2)
p.display()
print("Distance from origin:", p.distance_from_origin())
