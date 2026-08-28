# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
str1 = "Politeknik Sultan Abdul Halim Mu'adzam Shah"


c = str1[3]
print("char 3", c)

r = str1 [0:10]
print("Char 0 - 10:", r)

rn = str1 [-11:-1]
print("String negatif:", rn)

length = len(str1)
print("Jumlah aksara :", length)

strlower = str1.lower()
print(strlower)

strupper = str1.upper()
print(strupper)

strrep = str1.replace("Politeknik", "Kolej")
print(strrep)

perkataan = str1.split(" ")
print(perkataan[0])
print(perkataan[1])
print(perkataan[2])
print(perkataan[3])
print(perkataan[4])
print(perkataan[5])
print(perkataan)

check = "Poli" in str1
if check:
    print("Ada")
    
else:
    print("Tiada")
    
str2 = ", Kedah"
print(str1 + str2)

firstname = "John"
lastname = "Malibu"
age = 35

info = "{} {} is {} years old"

print(info.format(firstname, lastname, age))

name = "Mike" #String declare
print ("Nickname : ", name)
fname, lname = "Mike", "Gilmore"
print("Full name is: ", fname, lname)#concatinate 2 string 
