# Create a program to take student information as input. 
# Student will have First Name, Last Name, Roll No. 
# Write a function to sort the list based on given input parameter.  

# Input Parameters can be: ‘By First Name’ or ‘Last Name’ or ‘Roll No’. 

class student:
    def __init__(self, first_name, last_name, roll_no):
        self.first_name= first_name
        self.last_name= last_name
        self.roll_no= int(roll_no)
            

def sort(argum):
    if argum == "first name":
        sorted_list = sorted(lists, key=lambda x: x.first_name.lower())
    elif argum == "last name":
        sorted_list = sorted(lists, key=lambda x: x.last_name.lower())
    elif argum == "roll no":
        sorted_list = sorted(lists, key=lambda x: x.roll_no)
    else:
        print("Invalid input.")

    for student in sorted_list:
        print(f"{student.first_name} {student.last_name} {student.roll_no}")


n=int(input("enter no. of students: "))

lists=[]
print("enter student first name, last name and roll no. for e.g. Mohan Singh 23")
for i in range(n):
    l1 = input().split()
    s1 = student(*l1)
    lists.append(s1)

argum=input("sort by 'first name’ or ‘last name’ or ‘roll no': ")

sort(argum)





    