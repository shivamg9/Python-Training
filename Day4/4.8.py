# Overriding- Example 1

"""
How does method overriding facilitate the implementation of polymorphism 
and dynamic behavior in object-oriented programming?

"""

class Animal:
    def make_sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def make_sound(self):
        print("Dog barks.")


dog = Dog()
dog.make_sound()  # Output: Dog barks.
