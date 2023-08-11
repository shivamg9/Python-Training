# Write a program that takes Student's name and their marks in 3 subjects as input. 
# Print each student's total marks as output.

class student:
    def __init__(self, name, marks1,marks2,marks3):
        self.name = name
        self.marks1=int(marks1)
        self.marks2=int(marks2)
        self.marks3=int(marks3)
        
    def total_marks(self):
        total=self.marks1+self.marks2+self.marks3
        # print(f"{self.name}:{total}")
        return {self.name: total}

n=int(input("enter no. of students: "))

Result={}
print("enter student name and their marks out of 100 for e.g. Abc 87 69 54")
for i in range(n):
    l1 = input().split()
    s1 = student(*l1)
    Result.update(s1.total_marks())

print(f"dictionary of name with their total marks : {Result}")
