from module_3_3.hexagon import hexagon
from module_3_3.octagon import octagon
from module_3_3.pentagon import pentagon
from module_3_3.rectangle import rectangle
from module_3_3.square import square
from module_3_3.triangle import triangle
from module_3_3.shape import shape
from module_3_3.circle import circle
import math


def compare_shapes(shape1, shape2, property):
    if property not in ["perimeter", "area"]:
        raise ValueError("Invalid property. Must be 'perimeter' or 'area'.")

    value1 = getattr(shape1, f"{property}")()
    value2 = getattr(shape2, f"{property}")()

    if value1 > value2:
        return f"The {shape1.name} has a larger {property} than the {shape2.name}."
    elif value1 < value2:
        return f"The {shape2.name} has a larger {property} than the {shape1.name}."
    else:   
        return f"The {shape1.name} and the {shape2.name} have the same {property}."


crcl = circle(5)
rtngle = rectangle(4, 6)
trngle = triangle(3)

compare = input("Enter the property to compare (perimeter or area): ")

while compare not in ["perimeter", "area"]:
    print("Invalid property. Must be 'perimeter' or 'area'.")
    compare = input("Enter the property to compare (perimeter or area): ")

result = compare_shapes(crcl, rtngle, compare)
print(result)
