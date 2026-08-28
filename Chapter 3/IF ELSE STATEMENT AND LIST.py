# -*- coding: utf-8 -*-
"""
IF ELSE STATEMENT AND LIST
"""

def sum_even_numbers(numbers):
    
    sum = 0
    for num in numbers : 
        if num % 2 == 0:
            sum += num
    return sum

numbers = [1,2,3,4,5,6,7,8,9,10]
even_sum = sum_even_numbers(numbers)
print(f"The sum of all the even in {numbers} is {even_sum}.")

