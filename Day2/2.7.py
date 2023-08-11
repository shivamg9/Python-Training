# Write a Python program to input a list of non-empty tuples, 
# sort it in increasing order by the last element in each tuple. 

# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 

def sort_last_element(tuples):
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    return sorted_tuples

sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
sorted_tuples = sort_last_element(sample)
print(sorted_tuples)
