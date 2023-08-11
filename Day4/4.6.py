# Data Abstraction Example 2

"""
Implement a Python code example illustrating Data Abstraction in object-oriented programming. 
Define an abstract class 'Shape' with an abstract method 'area()', and a derived class 'Rectangle' 
that extends 'Shape' and implements 'area()'. Create an instance of 'Rectangle' with specific dimensions, 
calculate and display the area using the 'area()' method.

"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(2, 3)
print(rectangle.area())
