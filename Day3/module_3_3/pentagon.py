from module_3_3.shape import shape
import math

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
