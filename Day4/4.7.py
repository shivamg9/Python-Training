# Overloading- Example 1


class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


math = MathOperations()

result1 = math.add(2, 3)
print(result1)  # Output: TypeError: MathOperations.add() missing 1 required positional argument: 'c'

result2 = math.add(2, 3, 4)
print(result2)  # Output: 9
