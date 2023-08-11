# Implement a destructor of the objects which voids the object of the Class 
    
class Shape:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def __repr__(self):
        return f"name={self.name}, sides={self.sides}"

    def __del__(self):
        print(f"Destroying {self.name} object...")
        # Additional cleanup actions can be performed here


""" Create a Shape class hexagon"""
regular_hex = Shape("Hexagon", 6)

"""delete the hexagon object"""
del regular_hex
