# Separate the classes made in task 2 into different files.
# Implement __init__.py, __version__.py
# which prints applicable details of the contents of this module.

from module_3_3.hexagon import hexagon
from module_3_3.octagon import octagon
from module_3_3.pentagon import pentagon
from module_3_3.rectangle import rectangle
from module_3_3.square import square
from module_3_3.triangle import triangle

"""# from module_4_3 import *
"""

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
