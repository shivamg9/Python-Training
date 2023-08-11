"""
Write a program that takes integer age from the user if age is under 18, raise custom exception UnderAgeError and if age is over 40, raise custom exception OverAgeError. (Exception handling) 

        ========================== 

        Input:  

                Enter age: 10 

        Output: 

                You are UnderAge by 8 years..!! 

        ========================== 

        Input:  

                Enter age: 45 

        Output: 

                You are OverAge by 5 years..!! 
"""


class under_age_error(Exception):
    pass


class over_age_error(Exception):
    pass


def check_age():
    try:
        age = int(input("Enter age: "))
        if age < 18:
            raise under_age_error(f"You are underage by {18 - age} years..!!")
        elif age > 40:
            raise over_age_error(f"You are overage by {age - 40} years..!!")
        else:
            print("Valid age.")
    except ValueError:
        print("Invalid input, expected an integer for age.")
    except under_age_error as err:
        print(str(err))
    except over_age_error as err:
        print(str(err))


check_age()
