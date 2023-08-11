# Encapsulation EXAMPLE-1


"""
Provide a Python code snippet that demonstrates encapsulation through student roll numbers, subjects, and marks. 
Define a class 'Student' with private attributes and getter/setter methods to access 
and modify the attributes, ensuring controlled access and maintaining data privacy.

"""


class Student:
    def __init__(self, roll_no, subject, marks):
        self.__roll_no = roll_no
        self.__subject = subject
        self.__marks = marks
    
    def get_roll_no(self):
        return self.__roll_no
    
    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no
    
    def display_result(self):
        print(f"Roll No: {self.__roll_no}")
        print(f"Subject: {self.__subject}")
        print(f"Marks: {self.__marks}")


student = Student(1, "Science", 90)
student.display_result()
student.set_roll_no(2)
print(student.get_roll_no()) 
student.display_result()
