# -*- coding: utf-8 -*-
"""
Operator Overloading

"""
class MyClass:
    def __init__(self,x):
        self.x = x
    
    def __add__(self, othe):
        return MyClass(self.x + othe.x)
    
obj1 = MyClass('a')
obj2 = MyClass('b')
obj3 =obj1 + obj2

print(obj3.x)
