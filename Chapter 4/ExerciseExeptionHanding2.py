# -*- coding: utf-8 -*-
"""
Exercise EXECPTION HANDLING 2
"""
# Soalan 1 1
'''
def divide(FNumber,SNumber):   
    try:
         print(f'{FNumber}/{SNumber} is {FNumber / SNumber}')
    except ZeroDivisionError :
        print("You put the zero(0) Number")

divide(10,0)'''
   
#Soalan 2
'''try:
     file = open("myletter.txt","r")
     print(file.read(10))
except FileNotFoundError:
    print("Cannot found the File.")'''
   
#Soalan 3
'''def sum():
   
    try:
        
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        add = a + b
        print(add)
    except ValueError:
    # Handle the exception
        print("Invalid input. Please enter a valid integer.")
     
sum()'''
#Soalan 4
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
    
#Soalan 5
'''class InvalidNumber(Exception):
    pass
try:
    number=int(input('Enter the number between 1 to 10:'))
    if number > 10 :
        raise InvalidNumber
    else:
        print("Done you put ",number)
       
except ValueError :
        print("Invalid Value : The value must in integer not string")
        
except InvalidNumber :
        print("Invalid Number : The terms of number is between 1 to 10")'''
        
     
      