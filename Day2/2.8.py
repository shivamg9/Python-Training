# Write a program to make a new string from a given string in which the 
# xth character should be replaced with yth character, where x,y and string should be taken as input from user. 
# (x,y should be less than length of string) 

# Input String: Helper 
# x= 2 
# y= 4 
# Output: Hpleer

str=input("Enter String : ")
x=int(input("Enter x : "))-1
y=int(input("Enter y : "))-1
l=len(str)
temp=""

if x>y:
    t=x
    x=y
    y=t


if x<l and y<l:
    temp+=str[0:x]+str[y]+str[x+1:y]+str[x]+str[y+1:l]
    print(temp)
else:
    print("invalid x and y")
