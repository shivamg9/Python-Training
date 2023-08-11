"""
Write a program to convert a string value to integer and raise a custom exception. (Hint: Use raise) 

Input:  

                Enter value: “test” 

 Output: 

                Entered value can’t be converted to integer!! 

"""


class conversion_error(Exception):
    pass


def convert_to_integer(value):
    try:
        integer_value = int(value)
        return integer_value
    except ValueError:
        raise conversion_error("Entered value can't be converted to an integer!!")


# Example usage
try:
    value = input("Enter value: ")
    result = convert_to_integer(value)
    print("Converted integer value:", result)
except conversion_error as err:
    print(str(err))
