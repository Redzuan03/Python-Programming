# -*- coding: utf-8 -*-
"""
Raise Exception
"""
x = int(input("Enter a number:"))

if x < 0:
    raise Exception("Sorry, no numbers below zero dude")
else:
    print("It positive number")