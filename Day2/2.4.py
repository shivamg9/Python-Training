# Write a program that takes the input from the user (i.e., N). 
# Create the generator function that takes this input as an argument and returns numbers from 1 to N.  

def generate_n(n):
    for i in range(1,n+1):
        yield(i)


n=int(input("enter number N:"))

val = generate_n(n)
for i in range(n):
    print(next(val))