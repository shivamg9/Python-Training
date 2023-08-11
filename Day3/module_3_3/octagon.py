
from module_3_3.shape import shape
import math

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
