# -*- coding: utf-8 -*-
"""
@author: Muhammad Redzuan

Name : Muhammad Redzuan Bin Parsikun
Matric Number : 03DDT21F1005
Class : DDT4A
Title : Laboratory Exercise 4

"""

import tkinter as tk #creating gui like button,label and entry
from tkinter import messagebox #like message box
from PIL import ImageTk , Image #like image


def on_button_click(): #create method for button
    
    Username = Username_entry.get() #create object 
    Email = Email_entry.get() #create object 
    FullName = FullName_entry.get() #create object 
    ContactNo = ContactNo_entry.get() #create object 
    IC_Passport = IC_Passport_entry.get() #create object 
    Password = Password_entry.get() #create object 
    Confirm_Password = Confirm_Password_entry.get() #create object 
    
    #create if else when user click the button after they input the information
    #if for user not insert the information 
    if  Username_entry.get() == "   Username (Required)"  or Email_entry.get() == "   Email (Required)"  or FullName_entry.get(
        ) == "   Full Name (Required)"  or ContactNo_entry.get() == "   Contact No (Required)"  or  IC_Passport_entry.get(
        ) == "  IC / Passport (Required)" or Password_entry.get() == "  Password (Required)" or Confirm_Password_entry.get(
        ) == "  Confirm Password (Required)" :
        
        messagebox.showinfo("Register", "Please fill in Registration.")#will display the message box
        
        window.destroy()#after click "ok" the message bos, the gui of window will close
    
    #else if user insert the information
    elif Username == Username_entry.get() or Email == Email_entry.get() or FullName == FullName_entry.get(
         ) or ContactNo == ContactNo_entry.get() or  IC_Passport == IC_Passport_entry.get(
         ) or Password == Password_entry.get() or Confirm_Password == Confirm_Password_entry.get():
                 
         messagebox.showinfo("Register", "Register Succcessfully.")#will display the message box

         window.destroy()#after click "ok" the message bos, the gui of window will close
         
def on_entry_click(event):#create method / event handling function
    #if else for each type of register when user click at the text
    if Username_entry.get() == "   Username (Required)" :#when user click it and to put info
       Username_entry.delete(0, tk.END)# the text will delete the grey sentences
       Username_entry.configure(foreground="black")#give the user to write an input with black color
        
    elif Email_entry.get() == "   Email (Required)" :#when user click it and to put info
         Email_entry.delete(0, tk.END)# the text it will delete the grey sentences
         Email_entry.configure(foreground="black")#give the user to write an input with black color
         
    elif FullName_entry.get() == "   Full Name (Required)" :#when user click it and to put info
         FullName_entry.delete(0, tk.END)# the text it will delete the grey sentences
         FullName_entry.configure(foreground="black")#give the user to write an input with black color
              
    elif ContactNo_entry.get() == "   Contact No (Required)" :#when user click it and to put info
         ContactNo_entry.delete(0, tk.END)# the text it will delete the grey sentences
         ContactNo_entry.configure(foreground="black")#give the user to write an input with black color
                   
    elif IC_Passport_entry.get() == "  IC / Passport (Required)" :#when user click it and to put info
         IC_Passport_entry.delete(0, tk.END)# the text it will delete the grey sentences
         IC_Passport_entry.configure(foreground="black")#give the user to write an input with black color
                        
    elif Password_entry.get() == "  Password (Required)" :#when user click it and to put info
         Password_entry.delete(0, tk.END)# the text it will delete the grey sentences
         #give the user to write an input with black color and encrypt password
         Password_entry.configure(foreground="black", show="*")
                                                               
    elif Confirm_Password_entry.get() == "  Confirm Password (Required)" :
         Confirm_Password_entry.delete(0, tk.END)#when user click the text it will delete the grey sentences
         #give the user to write an input with black color and encrypt password
         Confirm_Password_entry.configure(foreground="black", show="*")


def on_focus_out(event):#create method / event handling function
    #if else for each type of register when user click the text and cancel do not want to input the info
    if  Username_entry.get() == "":#when user click it and cancel not put info
        Username_entry.insert(0, "  Username (Required)")#became this text as before
        Username_entry.configure(foreground="gray")#with color gray
        
    elif Email_entry.get() == "":#when user click it and cancel not put info
         Email_entry.insert(0, "  Email (Required)")#became this text as before
         Email_entry.configure(foreground="gray")#with color gray
         
    elif FullName_entry.get() == "":#when user click it and cancel not put info
         FullName_entry.insert(0, "  Full Name (Required)")#became this text as before
         FullName_entry.configure(foreground="gray")#with color gray

    elif ContactNo_entry.get() == "":#when user click it and cancel not put info
         ContactNo_entry.insert(0, "  Contact No (Required)")#became this text as before
         ContactNo_entry.configure(foreground="gray")#with color gray
      
      
    elif IC_Passport_entry.get() == "":#when user click it and cancel not put info
         IC_Passport_entry.insert(0, "  IC / Passport (Required)")#became this text as before
         IC_Passport_entry.configure(foreground="gray")#with color gray
          
    elif Password_entry.get() == "":#when user click it and cancel not put info
         Password_entry.insert(0, " Password (Required)")#became this text as before
         Password_entry.configure(foreground="gray")#with color gray
                
    elif Confirm_Password_entry.get() == "":#when user click it and cancel not put info
         Confirm_Password_entry.insert(0, "  Confirm Password (Required)")#became this text as before
         Confirm_Password_entry.configure(foreground="gray")#with color gray


window = tk.Tk() # Main Window
window.title("Register")# Title in window of gui


'''Image'''        
image = Image.open("Perpustakaan Negara Malaysia.jpg")#import image from folder
new_image = image.resize((100, 100))#rezise the image
new_image.save('Perpustakaan Negara Malaysia_new.jpg')#make new image and new rename

image_label = tk.Label(window) #create the object for display at gui
image_label.place(x=18, y=10)  # Set the desired x and y coordinates
image_label.pack(anchor="w",padx=18, pady=(15,40))#layout manager from image

# Replace "path_to_image.png" with the actual image file path with load back the new image
image = ImageTk.PhotoImage(Image.open("Perpustakaan Negara Malaysia_new.jpg"))  
image_label.config(image=image)#declare  that iamge before this same this new image


'''Label'''
#create the object with text(label) for dislay at gui
text_label = tk.Label(window, text="User Registration \n Perpustakaan Negara \n Malaysia"
            , font=("Times New Roman",15,"bold"))
text_label.place(x=150,y=30)#layout manager for geometry manager to arrange the text widgets


'''Username'''
Username_label = tk.Label(window, text="Username")#create the object with text(label) for dislay at gui
Username_label.pack(anchor="w",padx=18, pady=0)#layout manager for text

text_user= "   Username (Required)"# Create a text entry field

Username_entry = tk.Entry(window, fg="gray",width=50)#create the object with text,color,width for dislay at gui

Username_entry.insert(0,text_user)#calling back the text entry field in text
Username_entry.bind("<FocusIn>", on_entry_click)#calling back the method when click the text
Username_entry.bind("<FocusOut>", on_focus_out)#calling back the method when click the text
Username_entry.pack(anchor="w",padx=20, pady=0, ipadx=3, ipady=3)#layout manager for Username text entry


''''Email'''
Email_label = tk.Label(window, text="Email")#create the object with text(label) for dislay at gui
Email_label.pack(anchor="w",padx=18, pady=0)#layout manager for text

text_user1= "   Email (Required)"# Create a text entry field

Email_entry = tk.Entry(window, fg="gray", width=50)#create the object with text,color,width for dislay at gui

Email_entry.insert(0,text_user1)#calling back the text entry field in text
Email_entry.bind("<FocusIn>", on_entry_click)#calling back the method when click the text
Email_entry.bind("<FocusOut>", on_focus_out)#calling back the method when click the text
Email_entry.pack(anchor="w",padx=20, pady=0, ipadx=3, ipady=3)#layout manager for Username text entry

''''Full Name'''
FullName_label = tk.Label(window, text="Full Name")#create the object with text(label) for dislay at gui
FullName_label.pack(anchor="w",padx=18, pady=0)#layout manager for text

text_user2= "   Full Name (Required)"# Create a text entry field

FullName_entry = tk.Entry(window, fg="gray", width=50)#create the object with text,color,width for dislay at gui

FullName_entry.insert(0,text_user2)#calling back the text entry field in text
FullName_entry.bind("<FocusIn>", on_entry_click)#calling back the method when click the text
FullName_entry.bind("<FocusOut>", on_focus_out)#calling back the method when click the text
FullName_entry.pack(anchor="w",padx=20, pady=0, ipadx=3, ipady=3)#layout manager for Username text entry

''''Contact No'''
ContactNo_label = tk.Label(window, text="Contact No")#create the object with text(label) for dislay at gui
ContactNo_label.pack(anchor="w",padx=18, pady=0)#layout manager for text

text_user3= "   Contact No (Required)"# Create a text entry field

ContactNo_entry = tk.Entry(window, fg="gray", width=50)#create the object with text,color,width for dislay at gui

ContactNo_entry.insert(0,text_user3)#calling back the text entry field in text
ContactNo_entry.bind("<FocusIn>", on_entry_click)#calling back the method when click the text
ContactNo_entry.bind("<FocusOut>", on_focus_out)#calling back the method when click the text
ContactNo_entry.pack(anchor="w",padx=20, pady=0, ipadx=3, ipady=3)#layout manager for Username text entry

''''IC / Passport'''
IC_Passport_label = tk.Label(window, text="IC / Passport")#create the object with text(label) for dislay at gui
IC_Passport_label.pack(anchor="w",padx=18, pady=0)#layout manager for text

text_user4= "  IC / Passport (Required)"# Create a text entry field

IC_Passport_entry = tk.Entry(window, fg="gray", width=50)#create the object with text,color,width for dislay at gui

IC_Passport_entry.insert(0,text_user4)#calling back the text entry field in text
IC_Passport_entry.bind("<FocusIn>", on_entry_click)#calling back the method when click the text
IC_Passport_entry.bind("<FocusOut>", on_focus_out)#calling back the method when click the text
IC_Passport_entry.pack(anchor="w",padx=20, pady=0, ipadx=3, ipady=3)#layout manager for Username text entry

''''Password'''
Password_label = tk.Label(window, text="Password")#create the object with text(label) for dislay at gui
Password_label.pack(anchor="w",padx=18, pady=0)#layout manager for text

text_user5= "  Password (Required)"# Create a text entry field

Password_entry = tk.Entry(window, fg="gray", width=50)#create the object with text,color,width for dislay at gui

Password_entry.insert(0,text_user5)#calling back the text entry field in text
Password_entry.bind("<FocusIn>", on_entry_click)#calling back the method when click the text
Password_entry.bind("<FocusOut>", on_focus_out)#calling back the method when click the text
Password_entry.pack(anchor="w",padx=20, pady=0, ipadx=3, ipady=3)#layout manager for Username text entry

''''Confirm Password'''
Confirm_Password_label = tk.Label(window, text="Confirm Password")#create the object with text(label) for dislay at gui
Confirm_Password_label.pack(anchor="w",padx=18, pady=0)#layout manager for text

text_user6= "  Confirm Password (Required)"# Create a text entry field

Confirm_Password_entry = tk.Entry(window, fg="gray", width=50)#create the object with text,color,width for dislay at gui

Confirm_Password_entry.insert(0,text_user6)#calling back the text entry field in text
Confirm_Password_entry.bind("<FocusIn>", on_entry_click)#calling back the method when click the text
Confirm_Password_entry.bind("<FocusOut>", on_focus_out)#calling back the method when click the text
Confirm_Password_entry.pack(anchor="w",padx=20, pady=0, ipadx=3, ipady=3)#layout manager for Username text entry

#create the object with button for dislay at gui
button = tk.Button(window, text="REGISTER NOW", command=on_button_click, bg="green", fg="white")
button.pack(anchor = "w", padx=110, pady=20, ipadx = 10, ipady = 10)#layout manager for button

window.mainloop()# Start the main event loop / calling back the window