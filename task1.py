#!python3
import math


class quadratic:
    a = 0
    b = 0
    c = 0
    roots = []

    def discriminant(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the dis which is calculated as
        # b^2 - 4ac
        # return value should be a float type decimal
        return float((self.b ** 2) - (4 * self.a * self.c))

    def hasRealRoots(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine if the quadratic has real roots
        # defined when the dis is non-negative
        # return value should be True or False
        return self.discriminant() >= 0

    def isFactorable(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine if the quadratic can be factored
        # quadratic can be factored if the dis is a perfect square
        # return value is True or False
        d = self.discriminant()
        return d >= 0 and math.isqrt(int(d)) ** 2 == int(d)

    def calcRoots(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the roots of the quadratic if
        # the quadratic has real roots
        # should make use of the class methods:
        # self.hasRealRoots()
        # self.dis
        # method does not have a return value
        # but should store the values of the roots in the 
        # list self.roots
        # list should be sorted in ascending order
        # roots should be rounded to 2 decimal places
        if not self.hasRealRoots():
            self.roots = []
            return
        d = self.discriminant()
        sqrt_d = math.sqrt(d)

        r1 = round((-self.b + sqrt_d) / (2 * self.a), 2)
        r2 = round((-self.b - sqrt_d) / (2 * self.a), 2)
        self.roots = sorted([r1, r2])

    def axisOfSymmetry(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the x value that is for the equation
        # of the axis of symmetry
        # should return the x value for the axis of symmetry
        return round(-self.b / (2 * self.a), 2)

    def vertex(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the x,y value of the vertex
        # should return a list with the x and y coordinates of the vertex
        x = self.axisOfSymmetry()
        y = self.a * x ** 2 + self.b * x + self.c
        return [round(x, 2), round(y, 2)]

    def __init__(self, a, b, c):
        # this should require 3 positional arguments and assign the values
        # to self.a, self.b and self.c
        self.a = a
        self.b = b
        self.c = c
        self.roots = []
        self.calcRoots()


if __name__ == "__main__":
    q1 = quadratic(1, 4, 4)
    assert q1.isFactorable() == True
    assert q1.hasRealRoots() == True
    assert q1.discriminant() == 0
    assert q1.roots == [-2, -2]
    assert q1.axisOfSymmetry() == -2
    assert q1.vertex() == [-2, 0]

    q2 = quadratic(1, 1, -6)
    assert q2.isFactorable() == True
    assert q2.hasRealRoots() == True
    assert q2.discriminant() == 25
    assert q2.roots == [-3, 2]
    assert q2.axisOfSymmetry() == -0.5
    assert q2.vertex() == [-0.5, -6.25]

    q3 = quadratic(1, 1, 10)
    assert q3.isFactorable() == False
    assert q3.hasRealRoots() == False
    assert q3.discriminant() == -39
    assert q3.roots == []
    assert q3.axisOfSymmetry() == -0.5

    q4 = quadratic(1, 10, 1)
    assert q4.isFactorable() == False
    assert q4.hasRealRoots() == True
    assert q4.discriminant() == 96
    assert q4.roots == [-9.90, -0.10]
    assert q4.axisOfSymmetry() == -5
