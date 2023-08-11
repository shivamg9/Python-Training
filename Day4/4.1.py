# Polymorphism -EXAMPLE 1

"""
Create a program that represents different shapes (circle, square, and triangle) using classes.
Implement a method called calculate_area() in each shape class to calculate and return the area of the respective shape.
Use polymorphism to call the calculate_area() method on different shape objects and display their areas.
"""

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "circle"

    def calculate_area(self):
        return round(math.pi * self.radius**2.,2)


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return "square"

    def calculate_area(self):
        return round(self.side**2,2)


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def __str__(self):
        return "triangle"

    def calculate_area(self):
        return round(0.5 * self.base * self.height,2)


shapes = [Circle(2.4), Square(3.9), Triangle(4, 6)]

for shape in shapes:
    print(f"Area of {shape}: {shape.calculate_area()}")
