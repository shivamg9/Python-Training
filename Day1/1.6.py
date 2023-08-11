# Write a python function which counts the frequency of given character in a given string.
# Inputs - A String A Character whose frequency needs to be determined 

def freq(s,c):
    count=0
    for i in range(len(s)):
        if c==s[i]:
            count+=1
    return count





stri =input("enter a string: ")
charac=input("enter a character whose frequency need to be determined:")

print(f"frequency of character {charac} in string {stri} is {freq(stri,charac)}")