# -*- coding: utf-8 -*-
"""
Define and Call Function
Scope and Lifetime of variables

"""
name_prefix = "Sir"#Scope and Lifetime of variables
def info(name, age, fav_color):
    print("Your Name Is {}.".format(name))
    print("Your Age Is {}.".format(age))
    print("Your Favourite Colour Is {}.".format(fav_color))
    #print("Hello, " + name + ".Good Morning!")
    return name_prefix + " " + name

    
print(info("Redzuan","19", "Black"))

