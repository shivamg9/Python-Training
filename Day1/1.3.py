# Write a function to find larger of three numbers.  
# 	- Functions for each possible way we can find larger of three numbers. 

def large_3(a,b,c):
    c1=max(a,b)
    ans=max(c1,c)
    return ans

a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

print(f"maximum number is {large_3(a,b,c)}")




