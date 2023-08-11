"""
Write a program check_inputs.py that gets two inputs and checks that the first represents a valid int number and that the second represents a valid float number. (Exception handling) 
===================================== 

Input: 

       Enter Input1: 10 

Enter Input2: Hello!! 

Output: 

        "Hello!" is not a valid second input, expected a float value  
"""


def check_inputs():
    try:
        input1 = int(input("Enter Input1 (valid int number): "))
    except ValueError:
        print("Invalid first input, expected an integer value")
        return

    try:
        input2 = float(input("Enter Input2 (valid float number): "))
    except ValueError:
        print("Invalid second input, expected a float value")
        return

    print("Both inputs are valid.")


check_inputs()


# jidbewbihq
