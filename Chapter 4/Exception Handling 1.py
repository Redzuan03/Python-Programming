# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 15:26:48 2023

@author: P340
"""

def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except (ZeroDivisionError, TypeError, ValueError) as e:
        print(e)
