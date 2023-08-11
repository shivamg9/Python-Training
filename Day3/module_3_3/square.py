from module_3_3.shape import shape
import math

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


