# Write a program to take two integers as input. 
# Print those two integers as output and then call a function to swap those two integers. 
# - Write function for each possible way to swap two integers 

def swap(a,b):
    temp=b
    b=a
    a=temp
    print(f"after swapping a:{a}")
    print(f"after swapping b:{b}")

print("Enter two numbers: ")
a=int(input("a="))
b=int(input("b="))

swap(a,b)


