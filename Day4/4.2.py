# Polymorphism -EXAMPLE-2 

"""
Implement a Python code example that demonstrates polymorphism using student 
roll numbers, subjects, and marks. Define a base class 'Student' with a 'display_result' method, 
and two derived classes 'ScienceStudent' and 'ArtsStudent' that override the method to display subject-specific marks. 
Finally, create instances of both derived classes, call 'display_result' for each student, 
and observe the polymorphic behavior."
"""

class Student:
    def __init__(self, roll_no, subject):
        self.roll_no = roll_no
        self.subject = subject
    
    def display_result(self):
        pass


class ScienceStudent(Student):
    def __init__(self, roll_no, subject, physics_marks, chemistry_marks):
        super().__init__(roll_no, subject)
        self.physics_marks = physics_marks
        self.chemistry_marks = chemistry_marks
    
    def display_result(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Subject: {self.subject}")
        print(f"Physics Marks: {self.physics_marks}")
        print(f"Chemistry Marks: {self.chemistry_marks}")


class ArtsStudent(Student):
    def __init__(self, roll_no, subject, history_marks, literature_marks):
        super().__init__(roll_no, subject)
        self.history_marks = history_marks
        self.literature_marks = literature_marks
    
    def display_result(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Subject: {self.subject}")
        print(f"History Marks: {self.history_marks}")
        print(f"Literature Marks: {self.literature_marks}")

science_student = ScienceStudent(1, "Science", 80, 85)
arts_student = ArtsStudent(2, "Arts", 75, 90)

students = [science_student, arts_student]

for student in students:
    student.display_result()
    print() 
