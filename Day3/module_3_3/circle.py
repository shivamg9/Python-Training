from module_3_3.shape import shape
import math

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

