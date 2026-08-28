# -*- coding: utf-8 -*-
"""
Super class and Sub class
"""

class Car :
    def __init__(self,make,model,price,inventory):
        self.make = make 
        self.model = model
        self.price = price
        self.inventory = inventory
    def display(self):
        print('{0} {1}'.format(self.make,self.model))
        
class Sedan(Car):
    def __init__(self , make , model ,price , inventory, doors , seats):
        super(Sedan , self).__init__(make,model,price,inventory)
        self.doors = doors
        self.seats = seats    
        
class Van(Car):
    def __init__(self , make , model ,price , inventory, doors , seats):
        super(Van , self).__init__(make,model,price,inventory)
        self.doors = doors
        self.seats = seats            
        
# create a car object and display its make and model
my_car = Car("Toyota","Corolla", 15000, 10)
my_car.display()

# create a Sedan object and display its make, model, doors and seats
my_sedan = Sedan ('Toyota','Civic',20000,6, 4, 5)
my_sedan.display()
print(f"Number of doors : {my_sedan.doors}")
print(f"Number of seats : {my_sedan.seats}")
print(f"Number of inventory : {my_sedan.inventory}")

my_van = Sedan ('Toyota','Zack',30000, 6, 6, 8)
my_van.display()
print(f"Number of doors : {my_van.doors}")
print(f"Number of seats : {my_van.seats}")
print(f"Number of inventory : {my_van.inventory}")
        
        