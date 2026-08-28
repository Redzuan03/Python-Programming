# -*- coding: utf-8 -*-
"""
Method Overloading
"""
from multipledispatch import dispatch

'''
def multiply(x,y):
    mul = x * y
    print(mul)
    
def multiply(x,y,z):
    mul = x * y * z
    print(mul)
    
multiply(4,5,6)
multiply(6,7,8)
'''
class MyClass :
    @dispatch(int)
    def my_method(self, x):
        print("One argument method: ", x)
        
    @dispatch(int,int)
    def my_method(self, x , y):
        print("Two argument method: ",x,y)
        
obj = MyClass()
obj.my_method(1)
obj.my_method(2, 3)