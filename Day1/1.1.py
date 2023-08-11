# Write python script to take no of arguments as input from the user. 
# Then read the arguments from the standard input. 
# Print read arguments on output.

a=int(input("No. of Arguments:"))
b=[]

for i in range(0,a):
    b.append(input(f"enter argument {i+1}:"))

print(f"list of arguments are: {b}")
