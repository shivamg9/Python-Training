# Write a Python function to remove the characters which have odd index values of a given string. 

def remove_odd_index(s):
    newstr=""
    for i in range(len(s)):
        if i%2==0:
            newstr+=s[i]
    print(newstr)

s=input("Enter the string: ")
remove_odd_index(s)



