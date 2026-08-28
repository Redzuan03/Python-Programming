# -*- coding: utf-8 -*-
"""
IF ELSE STATEMENTS AND TUPLE
"""
def uppercase_tuple_strings(tuple_strings):
    
    upper_strings = tuple(s.upper() for s in tuple_strings)
    return upper_strings

tuple_strings = ("hello","world","python")
uppercase_tuple = uppercase_tuple_strings(tuple_strings)
print(f"The original tuple of strings : {tuple_strings}")
print(f"The new tuple of uppercase strings : {uppercase_tuple}")


