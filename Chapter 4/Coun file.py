# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 23:16:19 2023

@author: user
"""

try:
    
    filename = input("Enter the filename: ")
    word = input("Enter the word to search for: ")

    file = open(filename, 'r') 
    text = file.read()

    count = text.count(word)
    print(f"The word '{word}' appears {count} times in the file '{filename}'.")

except FileNotFoundError:
    print(f"Error: file '{filename}' not found.")
    
except IOError:
    print(f"Error: unable to read file '{filename}'.")