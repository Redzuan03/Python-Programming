# -*- coding: utf-8 -*-
"""
Tpic 3.5
Magic Method
"""

'''print(dir(str))#cara nak tunjuk attributes

num = 10
a = num + 5

print(a)

b = num.__add__(5) # sma fungsi cuma beza dri simbol dan ayat
print(b)'''

class Employee : 
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)  
        
        return inst
           
    def __init__(self):
        print("__init__ magic method is called")
        self.name = 'Satya'
        
e1=Employee()


