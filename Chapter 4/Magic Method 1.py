# -*- coding: utf-8 -*-
"""
Magic Methods
Comparison Methods
"""

class Cloth:
    def __init__(self,type,price,inventory):
        self.type = type
        self.price = price
        self.inventory = inventory
        
    def __gt__(self,other):
        if(self.price > other.price):
            return True
    
    def __lt__(self,other):
        if(self.price < other.price):
            return True
        
    def __eq__(self,other):
        if(self.price == other.price):
             return True
         
cloth1 = Cloth("BlouseLady",49.00,14)
cloth2 = Cloth("BlouseFlorist", 59.00, 17)

if(cloth1 > cloth2):
    print("The {0} is more expensive than the {1}". format(cloth1.type,cloth2.type))
else:
    print("The {0} is cheaper than the {1}". format(cloth1.type,cloth2.type))
    

