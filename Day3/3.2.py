# Create classes: Circle, Square, Rectangle, Triangle, Pentagon, Hexagon, Heptagon, Octagon as child classes of Shape.
# These classes should have functions to calculate perimeter, area, description about the shape and comparison with
# another shape based on area or perimeter.
# For eg:
# there is an object of Circle with x area and object of Heptagon with y area,
# a function should tell which object has a larger area.

import math


class shape:
    """A class representing shape"""

    def __init__(self, name, sides):
        """Initializing a shape object with attributes name and sides"""
        self.name = name
        self.sides = sides

    def __repr__(self):
        """Representation of shape object"""
        return f"name={self.name}, sides={self.sides}"

    def __eq__(self, other):
        """Comparing if two shapes are same"""
        if isinstance(other, shape):
            return self.sides == other.sides
        raise NotImplementedError("Objects of different types.")

    def __gt__(self, other):
        """Comparing if shape object has more sides than other shape"""
        if isinstance(other, shape):
            return self.sides > other.sides
        raise NotImplementedError("Objects of different types.")

    def __lt__(self, other):
        """Comparing if shape object has less sides than other shape"""
        if isinstance(other, shape):
            return self.sides < other.sides
        raise NotImplementedError("Objects of different types.")


class circle(shape):
    """Initialising circle object"""

    def __init__(self, radius):
        super().__init__("circle", 0)
        self.radius = radius

    def perimeter(self):
        """Perimeter of circle"""
        return 2 * math.pi * self.radius

    def area(self):
        """Area of circle"""
        return math.pi * (self.radius**2)


class square(shape):
    """Initialising square object"""

    def __init__(self, length):
        super().__init__("square", sides=4)
        self.length = length

    def perimeter(self):
        """Perimeter of square"""
        return 4 * self.length

    def area(self):
        """Area of square"""
        return self.length**2


class rectangle(shape):
    """Initialising rectangle object"""

    def __init__(self, length, width):
        super().__init__("rectangle", 4)
        self.length = length
        self.width = width

    def perimeter(self):
        """Perimeter of rectangle"""
        return 2 * (self.length + self.width)

    def area(self):
        """Area of rectangle"""
        return self.length * self.width


class triangle(shape):
    """Initialising triangle object"""

    def __init__(self, length):
        super().__init__("triangle", 3)
        self.length = length

    def perimeter(self):
        """Perimeter of equilateral triangle"""
        return 3 * self.length

    def area(self):
        """Area of equilateral traingle"""
        return round(math.sqrt(3) * (self.length**2) / 4, 2)


class pentagon(shape):
    """Initialising regular pentagon object"""

    def __init__(self, length):
        super().__init__("pentagon", 5)
        self.length = length

    def perimeter(self):
        """Perimeter of regular pentagon"""
        return 5 * self.length

    def area(self):
        """Area of regular pentagon"""
        return round(1.7204774 * (self.length**2), 2)


class hexagon(shape):
    """Initialising regular hexagon object"""

    def __init__(self, length):
        super().__init__("hexagon", 6)
        self.length = length

    def perimeter(self):
        """Perimeter of regular hexagon"""
        return 6 * self.length

    def area(self):
        """Area of regular hexagon"""
        return round(3 * math.sqrt(3) * (self.length**2) / 2, 2)


class heptagon(shape):
    """Initialising regular heptagon object"""

    def __init__(self, length):
        super().__init__("heptagon", 7)
        self.length = length

    def perimeter(self):
        """Perimeter of regular heptagon"""
        return 7 * self.length

    def area(self):
        """Area of regular heptagon"""
        return round(3.63391 * (self.length**2), 2)


class octagon(shape):
    """Initialising regular octagon object"""

    def __init__(self, length):
        super().__init__("octagon", 8)
        self.length = length

    def perimeter(self):
        """Perimeter of regular octagon"""
        return 8 * self.length

    def area(self):
        """Area of regular octagon"""
        return round(4.82843 * (self.length**2), 2)


def compare_area(shape1, shape2):
    """Compare two shapes based on their areas."""
    area1 = shape1.area()
    area2 = shape2.area()

    if area1 > area2:
        return f"{shape1.name} has a larger area than {shape2.name}."
    elif area1 < area2:
        return f"{shape2.name} has a larger area than {shape1.name}."
    else:
        return f"The areas of {shape1.name} and {shape2.name} are equal."


def compare_perimeter(shape1, shape2):
    """Compare two shapes based on their perimeters."""
    perimeter1 = shape1.perimeter()
    perimeter2 = shape2.perimeter()

    if perimeter1 > perimeter2:
        return f"{shape1.name} has a larger perimeter than {shape2.name}."
    elif perimeter1 < perimeter2:
        return f"{shape2.name} has a larger perimeter than {shape1.name}."
    else:
        return f"The perimeters of {shape1.name} and {shape2.name} are equal."


sqr = square(5)
pent = pentagon(3.9)
rect = rectangle(2, 0.5)
hex = hexagon(1)
tri = triangle(3)
oct = octagon(2.5)

print(pent.area())
print(compare_area(hex, tri))
print(compare_perimeter(oct, sqr))
print(compare_area(sqr, rect))
