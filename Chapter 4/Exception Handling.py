# -*- coding: utf-8 -*-
"""
Exception Hndling
"""

def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
        Ex = ValueError()
        Ex.strterror="Value must be within 1 and 10"
        raise Ex
    except ZeroDivisionError as e:
           print(e)
    except TypeError as e:
           print("Wrong type of number")
    except ValueError as e:
           
           print("Yout put  wrong value",e.strerror)

divide(12,2)#output 6
divide(13,0)#Zero Division Error
divide("b",5)
divide(2,-55)

