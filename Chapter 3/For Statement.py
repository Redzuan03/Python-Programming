# -*- coding: utf-8 -*-
"""
FOR STATEMENT 

"""

def count_vowels(input_str):
    
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in input_str:
        if char in vowels:
            count += 1
            
    print(f"There are {count} vowels in {input_str}")
    
user_Input = input("Enter a string : ")
count_vowels(user_Input)

#nak kira berapa huruf yang user mainkkan di ouput



