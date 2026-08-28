# -*- coding: utf-8 -*-
"""
Getter and Setter
Property and Instance

"""

class Car:
    def __init__(self, make, model, price, inventory):
        self.__make =make
        self.__model =model
        self.__price =price
        self.__inventory =inventory
        
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_price(self):
        return self.__price
    def get_inventory(self):
        return self.__inventory
    
    def set_make(self, make):
        self.__make = make
    def set_model(self, model):
        self.__model = model
    def set_price(self, price):
        self.price = price
    def set_inventory(self,inventory):
        self.__inventory = inventory
        
    make = property(get_make,set_make)
    model = property(get_model,set_model)
    price = property(get_price, set_price)
    inventory = property(get_inventory,set_inventory)
    
car1= Car("Chevy","Volt",15000.00, 10)

print("Car 1 Details : ")
print("Make : ", car1.make)
print("Model : ", car1.model)
print("Price : ", car1.price)
print("Inventory : ", car1.inventory)
    
    
    