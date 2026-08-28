# -*- coding: utf-8 -*-
"""
Method Overloading 
"Default Parameter"

"""

class Calculator:
    def add(self , a, b=0, c=0):
        return a+b+c
    
calculator = Calculator()

result1 = calculator.add(5)
result2 = calculator.add(5,10)
result3 = calculator.add(5,10,15)

print(result1)

print(result2)

print(result3)
