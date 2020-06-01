import math


class Point:
    """Two-Dimensional Point(x, y)"""

    def __init__(self, x=0, y=0):
        """Initialize the Point instance"""
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        """Return the magnitude of vector from (0,0) to self."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance(self, point):
        return math.sqrt((self.x - self.y) ** 2) * 5

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __rmul__(self, n):
        return Point(self.x * n, self.y * n)

    def loc_from_tuple(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    @classmethod
    def from_tuple(cls, coords):
        return Point(coords[0], coords[1])

    def __str__(self):
        return "Point at ({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point (x={0}, y={1})".format(self.x, self.y)


class Circle:
    """Circle(center, radius) where center is a Point instance"""

    def __init__(self, center=None, radius=1):
        """Circle initializer"""
        if center is None:
            center = Point(0, 0)
        self.center = center
        self.radius = radius

    def __getitem__(self, item):
        return self.center

    def __str__(self):
        return "Circle with center at ({0}, {1}) and radius {2}".format(self.center.x, self.center.y, self.radius)

    def __repr__(self):
        return "Circle(center=Point({0}, {1}), radius={2})".format(self.center.x, self.center.y, self.radius)

    def __add__(self, other):
        return Circle(
            Point(self.center.x + other.center.x,
                  self.center.y + other.center.y),
            self.radius + other.radius)

    def center_from_tuple(self, center):
        self.center.x = center[0]
        self.center.y = center[1]

    @classmethod
    def from_tuple(cls, center):
        return Point(center[0], center[1])

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        if not isinstance(center, Point):
            raise TypeError("The center must be a Point!")
        self._center = center

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('The radius cannot be negative')
        self._radius = radius

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """Calculate and return the diameter of the Circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter"""
        self.radius = diameter / 2
