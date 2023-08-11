"""
Write a program that takes a number from user. If negative number is provided then raises an exception. (Exception handling) 

======================================= 

Input: 

       Enter a positive integer: -5 

output : 

      That is a negative number!  
3.Write a program that takes two inputs from user and perform division of input1 by input2. (Exception handling)  

        - Handle invalid integers 

        - Handle divide by zero exception.  (Use Nested exception, else and finally)      

        ========================================= 

        Input: 

                Enter Input1: 10 

                Enter Input2: 0 

        Output: 

                Divide by Zero exception...!!! 

                Hi, I'm from finally...!!! 

        ========================================== 

        Input: 

                Enter Input1: 10 

                Enter Input2: abc 

        Output: 

	Invalid inputs, expected integers...!!! 

                Hi, I'm from finally...!!! 

"""


def perform_division():
    try:
        input1 = int(input("Enter Input1: "))
        input2 = int(input("Enter Input2: "))

        try:
            result = input1 / input2
        except ZeroDivisionError:
            print("Divided by Zero exception...!!!")
        else:
            print("Result:", result)
        finally:
            print("Hi, I'm from finally...!!!")

    except ValueError:
        print("Invalid inputs, expected integers...!!!")
        print("Hi, I'm from finally...!!!")


perform_division()
