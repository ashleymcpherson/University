import math

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%r, %r)" % (self.x, self.y)

    def delta_x(self, dx):
        return Point(self.x + dx, self.y)

    def delta_y(self, dy):
        return Point(self.x, self.y + dy)

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)


class Circle:

    def __init__(self, center = Point(), radius = 0):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"Circle({repr(self.center)}, {self.radius})"

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def translate(self, dx, dy):
        new_center = self.center.translate(dx, dy)
        return Circle(center = new_center, radius = self.radius)


class Rectangle:

    def __init__(self, lower_left=Point(), upper_right=Point()):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def __repr__(self):
        lower_left_repr = repr(self.lower_left)
        upper_right_repr = repr(self.upper_right)
        return f"Rectangle({lower_left_repr}, {upper_right_repr})"

    def area(self):
        length = self.upper_right.x - self.lower_left.x
        width = self.upper_right.y - self.lower_left.y
        return abs(length * width)

    def perimeter(self):
        length = self.upper_right.x - self.lower_left.x
        width = self.upper_right.y - self.lower_left.y
        return 2 * (abs(length) + abs(width))

    def translate(self, dx, dy):
        new_upper_right = self.upper_right.translate(dx, dy)
        new_lower_left = self.lower_left.translate(dx, dy)
        return Rectangle(upper_right = new_upper_right, lower_left = new_lower_left)

