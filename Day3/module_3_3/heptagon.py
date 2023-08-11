from module_3_3.shape import shape
import math

    
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

