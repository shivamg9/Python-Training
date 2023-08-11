"""
Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.(Regex)

"""

import re


def convert_date(input_date):
    regex = r"^(\d{4})-(\d{2})-(\d{2})$"
    match = re.match(regex, input_date)

    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        converted_date = f"{day}-{month}-{year}"
        return converted_date
    else:
        raise ValueError("Invalid date format. Expected format: yyyy-mm-dd")


try:
    input_date = input("Enter a date in yyyy-mm-dd format: ")
    converted_date = convert_date(input_date)
    print("Converted date:", converted_date)
except ValueError as err:
    print(str(err))
