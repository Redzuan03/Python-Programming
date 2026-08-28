# -*- coding: utf-8 -*-
"""
Function Arguments

"""
#Required Arguments
def printme( str,num ):
    print (str)
    print(num)
    return;
    
printme("Hello dunia",2)
print()

#Keyword arguments
def printme1( str,num ):
    print ("Name : ", str)
    print("Age : ", num)
    return;
    
printme1(num = 19,str="Redzuan")
print()

#Default arguments
def printme2( str,num = 0 ):
    print ("Name : ", str)
    print("Age : ", num)
    return;
    
printme2(num = 19,str="Redzuan")
printme2(str="Mahmud")
print()

#Variable-length arguments
def cetaksaya(args, *varbuah):
    print("Output is : ")
    print(args)
    for var in varbuah:
        print (var)
    return;
    
cetaksaya("Langsat")
cetaksaya("Durian", "Delima","Jambu")
