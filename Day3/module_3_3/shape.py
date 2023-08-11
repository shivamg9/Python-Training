class shape:
    """A class representing shape"""

    def __init__(self, name, sides):
        """Initializing a shape object with attributes name and sides"""
        self.name = name
        self.sides = sides

    def __repr__(self):
        """Representation of shape object"""
        return f"name={self.name}, sides={self.sides}"

    def __eq__(self, other):
        """Comparing if two shapes are same"""
        if isinstance(other, shape):
            return self.sides == other.sides
        raise NotImplementedError("Objects of different types.")

    def __gt__(self, other):
        """Comparing if shape object has more sides than other shape"""
        if isinstance(other, shape):
            return self.sides > other.sides
        raise NotImplementedError("Objects of different types.")

    def __lt__(self, other):
        """Comparing if shape object has less sides than other shape"""
        if isinstance(other, shape):
            return self.sides < other.sides
        raise NotImplementedError("Objects of different types.")
