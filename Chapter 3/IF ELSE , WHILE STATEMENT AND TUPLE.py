# -*- coding: utf-8 -*-
"""
IF ELSE , WHILE STAEMENT AND TUPLE
"""
def uppercase_tuple_strings(tuple_strings):
    
    upper_strings = tuple(s.upper() for s in tuple_strings)
    return upper_strings

while True:
    
    user_input = input("Enter a tuple of strings (comma-separated), or type 'Exit' to quit: ")
    
    if user_input.lower() == "exit" :
        print("Exiting...")
        break
    
    tuple_strings = tuple (user_input.split(","))
    
    uppercase_tuple = uppercase_tuple_strings(tuple_strings)
    
    print(f"The original tuple of strings : {tuple_strings}")
    print(f"The new of uppercase strings : {uppercase_tuple}")