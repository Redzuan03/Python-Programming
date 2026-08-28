# -*- coding: utf-8 -*-
"""
Super class and Sub Class

"""

class Person:
    def __init__(self,name):
        self.name = name
  
        
class Student(Person):
    def __init__(self, name ,student_id):
        super(Student, self).__init__(name)
        self.student_id = student_id

student = Student("Muhammad Redzuan", "F1005")
print(student.name)
print(student.student_id)


