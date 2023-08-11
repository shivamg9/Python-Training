from module_3_3.shape import shape
import math


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
