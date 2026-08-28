"""Name : Muhammad Redzuan Bin Parsikun
   Class: DDT4A
   Title: Laboratory Exercise 1
   Date: 21/2/2023"""

#Question 1
print("Hello World")
print("My Name is Muhammad Redzuan \n")


#Question 2
print("========COURSE REGISTRATION========\n")#To display at the output
Name = str(input("Enter your name : "))#Can put the value at the output
while True:#The loop with infinity
      
      
    print("========SELECT OPERATION========\n")#To display at the output
    print("1.  COURSE REGISTRATION")#To display at the output
    print("2.  DISPLAY REGISTRATION")#To display at the output
    print("3.  EXIT")#To display at the output
      
    NumberSelection = int(input("Selection : "))#Can put the value at the output
    
    #Can choose the NumberSelection which number is 1,2 or 3 with invented if else
    if NumberSelection == 1:
       
     print("\n========COURSE REGISTRATION========")#To display at the output
     Course = str(input("Enter 1st course : "))#Can put the value at the output
     Hour = int(input("Enter 1st credit hour : "))#Can put the value at the output
     Course1 = str(input("Enter 2nd course : "))#Can put the value at the output
     Hour1 = int(input("Enter 2nd credit hour : "))#Can put the value at the output
     Course2 = str(input("Enter 3rd course : "))#Can put the value at the output
     Hour2 = int(input("Enter 3rd credit hour : "))#Can put the value at the output
     
    elif NumberSelection==2:
     
     print("\n========Display REGISTRATION========")#To display at the output
     print("Name : ",Name)#To display at the output with called the object
     print("Course 1 : ", Course,  "\t", Hour,"Credit Hours")#To display at the output with called the object
     print("Course 2 : ", Course1, "\t", Hour1, "Credit Hours")#To display at the output with called the object
     print("Course 3 : ", Course2, "\t", Hour2, "Credit Hours")#To display at the output with called the object
     
     TotalCredit = Hour + Hour1 + Hour2#make some calculation
     print("Total credit hours is : ",TotalCredit)#To display at the output with called the object
    
    elif NumberSelection == 3:
        print("System Exited")#To display at the output
        print("Thank you :) , Have a nice day") #To display at the output
        break#To stop the infinte loop
  
      
            
        
    
        
        
   

     
     

