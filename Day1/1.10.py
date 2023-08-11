# Write a Python function to insert a string in the middle of a string. 
# For odd length of string, remove the middle character and replace with given string. 

def insert_mid(s,ins):
    ans=""
    l=len(s)
    a=int(l//2)
    if l%2==0:
        for i in range(0,a):
            ans+=s[i]
        ans=ans+ins
        for i in range(a,l):
            ans+=s[i]
        print(ans)
    else:
        for i in range(0,a):
            ans+=s[i]
        ans=ans+ins
        for i in range(a+1,l):
            ans+=s[i]
        print(ans)

s=input("enter a string: ")
ins=input("enter a string to add in middle: ")
insert_mid(s,ins)

        


