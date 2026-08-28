# -*- coding: utf-8 -*-
"""
Function code with if else statement
"""
#{} for called back the thing we make in the function
#mean f hide from {} at output
def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd")
        
even_or_odd(7)
even_or_odd(12)

print()

def check_sign(num):
    if num > 0:
        print("Positive number entered")
    elif num == 0:
        print("Zero entered")
    else:
        print("Negative number entered")
        
user_input = int(input("Enter the number : "))
check_sign(user_input)

print()

def is_leap_year(year):  
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
       print(f"{year} is a leap year")
    else:
       print(f"{year} is a not leap year")
    
user_input1 = int(input("Enter a year : "))
is_leap_year(user_input1)

print()

def  is_palindrome(input_str):
   
    input_str = input_str.lower().replace(" ", "")
    
    if input_str == input_str[::-1]:
        print(f"{input_str} is a palindrome.")
    else:
        print(f"{input_str} is not a palindrome.")
    
print()

def contains_substring(input_str, substring):
    if substring in input_str:
        print(f"'{input_str}'contains the substring '{substring}'.")
    else:
        print(f"'{input_str}' does not contains the substring '{substring}'.")
        
user_input3 = input("Enter the string : ")
substring = input("Enter a substring to search for : ")
contains_substring(user_input, substring)