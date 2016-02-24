# -*- coding: utf-8 -*-
from decimal import Decimal
class Point(tuple):
    """ Represents a 2D point. Inherits built-in tuple """

    def __new__(cls, num, x, y):
        return tuple.__new__(cls,(num, float(x), float(y)))

    def __init__(self, num, x, y):
        super(Point, self).__init__(num, x, y)
        self.id = num
        self.x = float(x)
        self.y = float(y)
        self.color = 0

    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

    def get_pos(self):
        return (self.x, self.y)

# Testing class
if __name__ == "__main__":

    point = Point(0, 3, 8)

    print point
    print "id = %s" % point.id
    print "x = %s" % point.x
    print "y = %s" % point.y

    for i in point:
        print i
