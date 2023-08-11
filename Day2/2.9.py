# Write a program to input 2 strings, and merge the reversed strings separated with $. 
# Sample strings : abcd wxyz 
# Output string: dcba$zyxw 

x, y = input("Enter two strings: ").split()

ans=x[::-1]+"$"+y[::-1]
print(ans)