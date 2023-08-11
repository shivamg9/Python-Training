from module_3_3.shape import shape
import math

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
