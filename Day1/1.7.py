# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.  
# If the string length is less than 2, return "Empty String" 


s=input("Enter the string: ")

if len(s)<2 :
    print("Empty String")
else:
    print(s[0]+s[1]+s[len(s)-2]+s[len(s)-1])