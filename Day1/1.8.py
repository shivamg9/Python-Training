# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).  
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

s=input("Enter the string: ")

last3_char=s[len(s)-3]+s[len(s)-2]+s[len(s)-1]
if len(s)>=3 :
    if last3_char=="ing":
        print(s+"ly")
    else:
        print(s+"ing")
else:
    print(s)