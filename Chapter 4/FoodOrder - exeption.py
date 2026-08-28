# -*- coding: utf-8 -*-
"""
Food Order - exception.py
"""

import os

import datetime

import re

food_price = 0.00
beverage_price = 0.00
total_price = 0.00
delivery_charge = 4.00
payment = 0.00
total_overall = 0.00
inputNumberIC = False
inputNumberPhone = False
inputNumberPostCode = False
inputEmailAddress = False

print("++--------------------------------------++")
print("+                 WELCOME                +")
print("++--------------------------------------++")

now = datetime.datetime.now()
print("Current date : ",now.strftime("%Y-%m-%d"))
print("Current time:",now.strftime("%H:%M:%S"))
print("Today is : ",now.strftime("%A"))
print()

orderTime = str("******Order Time******")
inputDate = now.strftime("%Y-%m-%d")
inputTime= now.strftime("%H:%M:%S")
inputDay = now.strftime("%A")

print("-------------------------------------------")
print("***      Please Insert Your Info       ***")
print("-------------------------------------------")
line1= str ("\n*****CUSTOMER DETAIL*****")


inputName = str(input("Name   :  "))
while not input: 
    print("Your name is empty. Please insert your name again")
    inputName = str(input("Name  : "))
    continue
while True:
    break


while not inputNumberIC:
    inputIC = str(input("IC    :"))
    if len(inputIC) == 12:
        inputNumberIC = True
    elif len(inputIC) == 0:
        print("Your IC is empty. Please insert your IC again")
        inputNumberIC = False
    else:
        print("Invalid IC Number")
    break
        
print()
print("Please fill up your adrress")

inputStreet = str(input("Street  : "))
while not inputStreet :
    print("Your steer is empty. Please insert your street again")
    inputStreet = str(input("Street  : "))
while True:
    break


while not inputNumberPostCode:
    inputPostCode = str(input("Postcode   : "))
    if len(inputPostCode) == 5:
        inputNumberPostCode = True
    elif len(inputPostCode) == 0:
        print("Your Postcode is empty. Please insert your city again")
        inputNumberPostCode = False
    else :
        print("Invalid Postcode Number")
    break
        
inputCity = str(input("City   : "))
while not inputCity:
    print("Your city is empty. Please insert yout city again")
    inputCity = str(input("City   :  "))
    continue 
while True:
    break
        

inputState= str(input("State  : "))
while not inputState:
    print("Your state is empty. Please insert your state again")
    inputState = str(input("State   : "))
    continue
while True:
    break

inputAddress = (inputStreet + "," + inputPostCode + ","+inputCity + ","+ inputState)

print()
while not inputNumberPhone: 
    inputPhone = str(input("Phone num:  "))
    if len (inputPhone) == 10:
        inputNumberPhone = True
    elif len (inputPhone) == 11:
        inputNumberPhone = True
    elif len (inputPhone) == 0:
        print("Your phone number is empty. Please insert your phone number again")
        inputNumberPhone = False
      
    else: 
        print("Invalid phone number")
    break
    
while(True):
   inputEmail = str(input("Email  : "))
   if re.match(r"[^@]+@[^@]+\.[^@]+",inputEmail):
      break
   elif len(inputEmail) == 0:
       print("Your email is empty. Please insert your email again")
       inputEmailAddress = False
   else:
       print("Email is not valid")
       break
   
def input_info():
    
    with open('Order.txt','w+') as out:
         out.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'
                  . format(orderTime, "Date : "+inputDate,"Time : "+inputTime,"Day : "+inputDay,
                   line1,"Name : "+inputName,"IC  : "+inputIC, "Address : "+inputAddress,
                   "PhonNum : "+inputPhone, "Email : "+inputEmail))
         
input_info()

print()
print("Please select your food and beverage")
print()

data1 = str("++----------------FOOD MENU------------------++")
data2 = str("+ CODE   MENU                    PRICE +")
data3 = str("+ 1.   Burger Set                 (RM 11.00) +")
data4 = str("+ 2.   Pizza Set                  (RM 11.00) +")
data5 = str("+ 3.   Spaghetti Bolognese Set    (RM 12.00) +")
data6 = str("+ 4.   Spaghetti Aglio Set        (RM 13.00) +")
data7 = str(" ")
data8 = str("++----------------BEVERAGE MENU------------------++")
data9 = str("+ CODE   MENU                    PRICE +")
data10 = str("+ 1.    Coca Cola                  *  +")
data11 = str("+ 2.    Pepsi                      *  +")
data12 = str("+ 3.    Fanta Strawberry           *  +")
data13 = str("+ 4.    Fanta Orange               *  +")
data14 = str("+ *Included in the Food Set           +")
data15 = str("++-----------------------------------++")

def show_item():
    
    with open('Menu.txt','w+') as out:
         out.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'
                   . format(data1,data2,data3,data4,data5,data6,data7,
                           data8,data9,data10,data11,data12,data13,data14,
                           data15))
         
    file = open('Menu.txt','r')
    print(file.read())
    
show_item()

print("Please choose your favourite food and beverage")

def food_input_menu(a):
    pass

while True:
    
    food = int(input("Food code: "))
    if food == 1:
        food = "Burger Set"
        food_price = 11.00
        food_code =1
        break
    elif food == 2:
        food = "Burger Set"
        food_price = 11.00
        food_code = 2
        break
    elif food == 3:
        food = "Spaghetti Bolognese Set"
        food_price = 12.00
        food_code = 3
        break
    elif food == 4:
        food = "Spaghetti Aglio Set"
        food_price = 13.00
        food_code = 4
        break
    
print()

    
def beverage_input_menu(a):
    pass

while True:
    
     beverage = int(input("Food code: "))
     if beverage == 1:
         beverage = "Coca Cola"
         beverage_price = 0.00
         break
     if beverage == 2:
         beverage = "Pepsi"
         beverage_price = 0.00
         break
     if beverage == 3:
         beverage = "Fanta Strawberry"
         beverage_price = 0.00
         break
     if beverage == 4:
         beverage = "Fanta Orange"
         beverage_price = 0.00
         break
     
print("Invalid input. Please try again")
print()
print("Food code: ", food_code)

total_price = food_price + beverage_price
total_overall= total_price + delivery_charge

print("--------------------------------------")
print("Dear ", inputName, ",")
print("Your order is ", food, "RM", food_price)
print("Your order is",beverage,"RM",beverage_price)

print("--------------------------------------")
print()

print("Food price       =RM" , format(food_price,'.2f'))
print("Beverage price   =RM" , format(beverage_price,'.2f'))
print("Total price      =RM" , format(total_price,'.2f'))
print("Delivery price   =RM" , format(delivery_charge,'.2f'))
print("___________________________________________________")
print("Total            =RM",format(total_overall))

def payment_balance(a):
    pass

while True:
    
    payment = int(input("Cash payment   = RM "))
    if payment > total_price:
        balance = payment - total_overall
        print("Balance     = RM ",format(balance,'.2f'))
        break
    elif payment < total_price:
        print("Your amount is not enough")
        print()
        continue
    
print()

print()
print("Your order will arrive with in 30 minutes")
print()

foodPrice= str(food_price)
beveragePrice = str(beverage_price)
totalPrice = str (total_price)
deliveryCharge = str(delivery_charge)
totalOverall = str(total_overall)
Payment = str(payment)
Balance = str(balance)

append = open("Order.txt","a")

append.write("\n*****ORDER INFORMATION*****")
append.write("\nFood       : " +food + "(RM" + foodPrice +")")
append.write("\Beverage    : " +beverage + "(RM" + beveragePrice +")")
append.write("\n")
append.write("\n*****PAYMENT INFORMATION*****")
append.write("\nTotal Price : RM"+ totalPrice)
append.write("\nDelivery Charge : RM"+ deliveryCharge)
append.write("\nTotal  : RM"+ totalOverall)
append.write("\nPayment  : RM"+ Payment)
append.write("\nBalance  : RM"+ Balance)

append.close()

def yes_or_no():
    print("Do you want to view your receipt order?")
    print("[y]=Yes / [n]=No")
    YesNo = input("View Receipt? : ")
    print()
    
    YesNo = YesNo.lower()
    
    if(YesNo == "y"):
       return 1
    elif(YesNo == "n"):
       return 0
    else:
       print("Invalid Input")
       return -1
   
while(True):
    inp = yes_or_no()
    if(inp == -1):
        continue
    elif(inp == 1):
        file = open('Order.txt','r')
        print(file.read())
    elif(inp == 0):
        print("++-----------------------------------++")
        print("+              THANK YOU              +")
        print("++-----------------------------------++")
        break
    break