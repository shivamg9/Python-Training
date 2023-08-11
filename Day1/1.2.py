# Write python script to take one integer argument and then print as follows: 
#     	- If Value >0 and Value < 10 — Small 

#     	- If Value > 10 and Value <100 — Medium 

#     	- If Value <1000 — Large 

#     	- If Value > 1000 — Invalid


a=int(input("Type one integer argument: "))

if a>0 and a<=10:
    print("Small Argument")
elif a>10 and a<=100:
    print("Medium Argument")
elif a>100 and a<=1000:
    print("Large Argument")
else:
    print("Invalid Argument")