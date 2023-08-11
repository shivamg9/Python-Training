"""
Write a program that takes a number from user. If negative number is provided then raises an exception. (Exception handling) 

======================================= 

Input: 

       Enter a positive integer: -5 

output : 

      That is a negative number!  

"""


def check_positive_integer():
    try:
        number = int(input("Enter a positive integer: "))
        if number < 0:
            raise ValueError("That is a negative number!")
        else:
            print("Valid input.")
    except ValueError as vE:
        print(str(vE))


check_positive_integer()
