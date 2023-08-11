    # Write a program to take size of the list as input. 
    # Then read the integer values and store these details into list.  

    # Output: 
    # - The list entered by the user.

sizeList=int(input("size of list : "))
list=[]
for i in range(sizeList):
    list.append(i+1)

print(list)


  
