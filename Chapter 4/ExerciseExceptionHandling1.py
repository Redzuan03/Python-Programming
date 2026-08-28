# -*- coding: utf-8 -*-
"""
Exercise Exception Handling 1
"""


'''try:
    print(x)
except:
    print("An exception ocurred")'''
    
'''def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except ZeroDivisionError as e:
           print(e)
           
divide(10,10)
divide(10,4)
divide(10,0)'''

'''def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except (ZeroDivisionError, TypeError, ValueError, NameError) as a:
        print(a)
        
divide(5,0)
divide(2,5)'''

'''try :
    x=float(input("Enter The Number:"))
    result = 100/x
    print(result)
except Exception as e:
    print ("exception occured:" ,e)
else:
    print("else block is executing")'''
    
'''x = 10
y = 0

try : 
    print("outer try block")
    try:
        print("nested try block")
        print(x/y)
    except TypeError as te:
        print("nested except block")
        print(te)
except ZeroDivisionError as ze:
    print("outer execept block")
    print(ze)'''
    
'''def divide(x, y):    
    try:
        print( f'{x}/{y} is {x / y}' )
    except ZeroDivisionError as e:
        print(e)
    else:
        print("Divide() function worked fine.")
    finally:
        print("Close all the resources here")
        print()
        
divide(10,"cD")'''

'''try:
    num= int(input('Enter The Number : '))
    num1= int(input('Enter divisible number : '))
    re=num/num1
except ValueError:
    print("Value is not type")
except ZeroDivisionError as e:
    print("Don't use error",e) 
else:
    print("result is ",round(re,3))'''
  
'''class ValidationError(Exception):
    pass

def divide(x, y):    
    try:
        if type(x) is not int:
           raise TypeError("Unsupported type")
        if type(y) is not int:
           raise TypeError("Unsupported type")
    except TypeError as e:
        print(e)
        raise ValidationError("Invalid type of arguments")

    if y == 0:
        raise ValidationError("We can't didivde by 0")
        
try:
    divide(10,"5")
except ValidationError as ve:
    print(ve)'''
    
class InvalidRange(Exception):
    pass

try:
    marks=input('Enter a marks:')
    marks=int(marks)
    if (marks<0 or marks>100):
        raise InvalidRange
           
except ValueError :
        print("Invalid Input")
        
except InvalidRange:
    print("Input value out of range")