from module_3_3.shape import shape
import math

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

