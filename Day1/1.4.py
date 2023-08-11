# Write a program to take two numbers as input parameter and then ask for the arithmetic parameter to be performed.  
# 	>>> “Enter Two numbers” 
# 	10 45  
# 	>>>“Operations to perform “  
# 	+  
# 	>>> 55 

print("Enter two numbers: ")
a=int(input("a: "))
b=int(input("b: "))

print("Operation to perform")
operation=input()

result=eval(f'{a} {operation} {b}')

print(result)



